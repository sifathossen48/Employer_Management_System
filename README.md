# 🛠 Employer Management System API

A simple RESTful API for managing employers, built using **Django** and **Django REST Framework** with **Simple JWT** authentication.







## 🚀 Features
- Custom user model (email-based authentication)
- JWT-based login & logout
- Employer CRUD (Create, Read, Update, Delete)
- User-specific employer access
- Clean architecture using class-based views


## 📦 Requirements
- asgiref==3.8.1
- Django==5.2
- djangorestframework==3.16.0
- djangorestframework_simplejwt==5.5.0
- PyJWT==2.9.0
- sqlparse==0.5.3
- tzdata==2025.2


## Setup Instructions

### Clone the repository:
```bash
git clone https://github.com/sifathossen48/Employer_Management_System.git

cd Employer_Management_System
```
### Create a virtual environment:
```bash
pipenv install  #install pipenv
```
```bash
pipenv shell   #create venv
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### Apply migrations:
```bash
pip install -r requirements.txt
```
### Run the development server:
```bash
pip install -r requirements.txt
```

## API Endpoints
### Auth
- `POST /api/auth/signup/` – Register
- `POST /api/auth/login/` – Login (get JWT)
- `POST /api/auth/logout/` – Logout
- `GET /api/auth/profile/` – Get current user

### Employers (JWT required)
- `POST /api/employers/` – Create employer
- `GET /api/employers/` – List employers
- `GET /api/employers/<id>/` – Get one employer
- `PUT /api/employers/<id>/` – Update employer
- `DELETE /api/employers/<id>/` – Delete employer


# 📝 Notes

- Run `pipenv shell` to activate the virtual environment.

- JWT authentication is used; include Bearer <access_token> in the Authorization header.

- Only authenticated users can access employer routes.

- Each user can only view and modify their own employers.

- Run `python manage.py migrate` before starting the server.

- Use Postman or any API client to test endpoints.

