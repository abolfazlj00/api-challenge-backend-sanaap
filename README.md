# api-challenge-backend-sanaap

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Setup](#setup)
* [Running the Project](#running-the-project)
* [API Endpoints](#api-endpoints)
* [Admin User](#admin-user)
* [File Uploads](#file-uploads)

---

## Features

* Django REST API with Token Authentication
* Role-Based Access Control (RBAC)

  * **Admin**: full access, manage users
  * **Editor**: can create/edit own documents
  * **Viewer**: read-only access
* File storage using **MinIO (S3 compatible)**
* PostgreSQL database with Docker
* Default admin user and role setup via `setup_roles`

---

## Requirements

* Docker >= 20.10
* Docker Compose >= 2.0

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/abolfazlj00/api-challenge-backend-sanaap.git
cd api-challenge-backend-sanaap
```

2. Create a `.env` file:

```env
SECRET_KEY=django-insecure-key
DEBUG=True
DJANGO_ALLOWED_HOSTS=*

# PostgreSQL
DB_NAME=django_db
DB_USER=django
DB_PASSWORD=django
DB_HOST=db
DB_PORT=5432

# MinIO
MINIO_ENDPOINT=http://minio:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET_NAME=documents
MINIO_REGION=us-east-1
```

---

## Running the Project

Build and start all services:

```bash
docker-compose up --build
```

This will:

1. Start **PostgreSQL**, **MinIO**, and Django server
2. Run migrations
3. Run `setup_roles` to create roles and a default admin user
4. Start the Django development server at `http://localhost:8000`

---

## Admin User

* Default admin user created by `setup_roles`:

```
username: admin
password: admin123
```

---

## API Endpoints

| Endpoint          | Method         | Description                                 |
| ----------------- | -------------- | ------------------------------------------- |
| `/users/login/`     | POST           | Login with username/password, returns token |
| `/users/`     | GET/POST/PATCH | Admin-only user management                  |
| `/api/v1/documents/` | CRUD           | Document API with RBAC                      |

> Use the token from login for authenticated requests.

---

## File Uploads

* Files are uploaded to **MinIO** (S3 compatible).

* The URL of uploaded files is available in the document API.

* MinIO console: [http://localhost:9001](http://localhost:9001)

  * Access Key: `minioadmin`
  * Secret Key: `minioadmin`

---

## Notes

* RBAC roles: Admin, Editor, Viewer
* Permissions for document CRUD are automatically enforced
