# 📄 CollabDocs API

A collaborative document management backend built using Django REST Framework and PostgreSQL.

## 🚀 Features

- User Management
- Workspace Management
- Workspace Members
- Document CRUD
- Document Versioning
- Comments
- Tags
- Audit Logs
- Search & Filtering
- UUID Primary Keys
- Signals
- Middleware
- PostgreSQL

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL

## 📦 Installation

```bash
git clone <repository-url>

cd collabdocs-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Configure Environment

Create `.env`

```env
DB_NAME=collabdocs
DB_USER=postgres
DB_PASSWORD=Shree1710
DB_HOST=localhost
DB_PORT=5432

SECRET_KEY=your-secret-key
DEBUG=True

DATABASE_URL=postgresql://collabuser:vVtaK8hs2QFH7a1D2K9oNHrkfJDHutfV@dpg-d94tg2cvikkc73cvl2ag-a.singapore-postgres.render.com/collabdocs_3e0z

```

## Run

```bash
python manage.py migrate

python manage.py runserver
```

## Run Tests

```bash
python manage.py test
```

## API Endpoints

- `/api/users/`
- `/api/workspaces/`
- `/api/documents/`
- `/api/comments/`
- `/api/tags/`
- `/api/auditlogs/`

## Project Structure

```
users/
workspaces/
documents/
comments/
tags/
auditlogs/
core/
config/
```
