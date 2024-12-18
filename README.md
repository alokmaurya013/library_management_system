# Library Management System

A RESTful web application built using Flask for managing library members and their accounts. This system allows admins to add, update, delete, and view library members, with secure authentication implemented using JWT.

## Features

- **User Authentication:**
  - Secure login system using JWT tokens.
  - Token-based authorization for accessing restricted routes.
  
- **Member Management:**
  - Add new members to the library.
  - Update existing member details.
  - Delete members from the system.
  - View a list of all members.

- **Database Integration:**
  - Uses SQLAlchemy for database management.
  - Supports SQLite by default (can be configured for other databases).

---

## Technologies Used

- **Backend:** Flask, Flask-SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** SQLite (default)
- **Deployed on:** Render

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alokmaurya013/library-management-system.git
   cd library-management-system
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**
   Create a `.env` file in the root directory and configure the following:
   ```env
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///library.db
   ```

5. **Initialize the Database:**
   ```bash
   python run.py
   ```

6. **Run the Application:**
   ```bash
   python run.py
   ```
   The application will run at `http://127.0.0.1:5000`.

---

## API Endpoints

### **Authentication**

- **Login**
  - `POST /login`
  - **Body:**
    ```json
    {
      "email": "user@example.com",
      "password": "password123"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Login successful",
      "token": "JWT_TOKEN"
    }
    ```

### **Member Management**

- **Add Member**
  - `POST /members`
  - **Headers:**
    ```json
    {
      "Authorization": "Bearer JWT_TOKEN"
    }
    ```
  - **Body:**
    ```json
    {
      "email": "newmember@example.com",
      "password": "password123"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Member added successfully!"
    }
    ```

- **Update Member**
  - `PUT /members/<id>`
  - **Headers:**
    ```json
    {
      "Authorization": "Bearer JWT_TOKEN"
    }
    ```
  - **Body:**
    ```json
    {
      "email": "updatedemail@example.com",
      "password": "newpassword123"
    }
    ```

- **Delete Member**
  - `DELETE /members/<id>`
  - **Headers:**
    ```json
    {
      "Authorization": "Bearer JWT_TOKEN"
    }
    ```
  - **Response:**
    ```json
    {
      "message": "Member deleted successfully!"
    }
    ```

- **Get All Members**
  - `GET /members`
  - **Headers:**
    ```json
    {
      "Authorization": "Bearer JWT_TOKEN"
    }
    ```
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "email": "user1@example.com"
      },
      {
        "id": 2,
        "email": "user2@example.com"
      }
    ]
    ```

---

## Deployment

This project is deployed on [[Render](https://render.com) The deployment can be accessed at:

```
https://library-management-system-yy7w.onrender.com
```

Ensure the `PORT` environment variable is set in Render for proper functioning.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
