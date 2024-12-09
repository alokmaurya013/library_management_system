from flask import jsonify, request
from .models import db, Book, Member
from .auth import token_required, create_token
from werkzeug.security import generate_password_hash, check_password_hash

def configure_routes(app):
    # Signup Route
    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Email and password are required."}), 400

        existing_user = Member.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "Email already in use."}), 400

        hashed_password = generate_password_hash(password)
        new_member = Member(email=email, password=hashed_password)

        db.session.add(new_member)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201

    # Login Route
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = Member.query.filter_by(email=email).first()
        if not user:
            return jsonify({"message": "User not found."}), 404

        if not check_password_hash(user.password, password):
            return jsonify({"message": "Invalid credentials"}), 401

        # Generate token
        token = create_token(user.id)

        print("Generated Token: ", token)  # Check the generated token
        return jsonify({"message": "Login successful", "token": token}), 200

    # CRUD Routes for Books
    @app.route('/books', methods=['POST'])
    @token_required
    def add_book(current_user):
        data = request.get_json()
        new_book = Book(
            title=data['title'],
            author=data['author'],
            published_year=data.get('published_year')
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added successfully!"}), 201

    @app.route('/books', methods=['GET'])
    @token_required
    def get_books(current_user):
        books = Book.query.all()
        return jsonify([
            {"title": book.title, "author": book.author, "published_year": book.published_year}
            for book in books
        ])

    @app.route('/books/<int:id>', methods=['PUT'])
    @token_required
    def update_book(current_user, id):
        data = request.get_json()
        book = Book.query.get(id)
        if not book:
            return jsonify({"message": "Book not found"}), 404

        book.title = data['title']
        book.author = data['author']
        book.published_year = data.get('published_year')
        db.session.commit()
        return jsonify({"message": "Book updated successfully!"})

    @app.route('/books/<int:id>', methods=['DELETE'])
    @token_required
    def delete_book(current_user, id):
        book = Book.query.get(id)
        if not book:
            return jsonify({"message": "Book not found"}), 404

        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully!"})

    # CRUD Routes for Members
    @app.route('/members', methods=['POST'])
    @token_required
    def add_member(current_user):  # current_user is passed by token_required
        data = request.get_json()
        email = data.get('email')

        if not email:
            return jsonify({"message": "Email is required."}), 400

        existing_member = Member.query.filter_by(email=email).first()
        if existing_member:
            return jsonify({"message": "A member with this email already exists."}), 400

        # Use a default password or the provided one
        hashed_password = generate_password_hash(data.get('password', 'defaultpassword'))
        new_member = Member(email=email, password=hashed_password)

        db.session.add(new_member)
        db.session.commit()

        return jsonify({"message": "Member added successfully!"}), 201
    
    @app.route('/members', methods=['GET'])
    @token_required
    def get_members(current_user):
        members = Member.query.all()
        return jsonify([{"email": member.email} for member in members])

    @app.route('/members/<int:id>', methods=['PUT'])
    @token_required
    def update_member(current_user, id):
        data = request.get_json()

        # Check if email and password are provided
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Email and password are required."}), 400

        member = Member.query.get(id)
        if not member:
            return jsonify({"message": "Member not found"}), 404

        # Update member fields
        member.email = email
        member.password = generate_password_hash(password)
        db.session.commit()

        return jsonify({"message": "Member updated successfully!"}), 200

    @app.route('/members/<int:id>', methods=['DELETE'])
    @token_required
    def delete_member(current_user, id):
        member = Member.query.get(id)

        if not member:
            return jsonify({"message": "Member not found"}), 404

        db.session.delete(member)
        db.session.commit()
        return jsonify({"message": "Member deleted successfully!"}), 200
