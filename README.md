# Flask App with JWT Authentication and CRUD Operations

## Overview
A Flask application with user management, JWT authentication, and CRUD operations for an additional model.

## Features
- **User Management**: Registration, login, profile updates, password changes, and account deletion.
- **JWT Authentication**: Protects sensitive routes.
- **Item Model**: Full CRUD operations for items with fields  `id`, `name`, `description`, `price`.

## Key Endpoints
1. **Authentication**:
   - `POST /register`: User registration.
   - `POST /login`: User login with JWT token issuance.
   - `POST /logout`: Logout and token invalidation.
2. **User Management**:
   - `GET /current_user`: Fetch logged-in user details.
   - `PUT /user/update`: Update user profile.
   - `PUT /user/updatepassword`: Change password.
   - `DELETE /user/delete_account`: Delete own account.

3. **Items**:
   - `POST /item`: Create an item.
   - `GET /item`: Retrieve all items.
   - `GET /item/<id>`: Retrieve a specific item.
   - `PUT /item/<id>`: Update an item.
   - `DELETE /item/<id>`: Delete an item.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure `.env`:
   ```
   SECRET_KEY=your_secret_key
   JWT_SECRET_KEY=your_jwt_secret_key
   SQLALCHEMY_DATABASE_URI=sqlite:///app.db
   ```
3. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. Run the app:
   ```bash
   flask run
   ```

## Testing
Use Postman to test endpoints with proper JWT tokens.

