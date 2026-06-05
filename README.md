# Veterinary Clinic Management System

![Tests](https://github.com/JohnDLothbrock/vet_clinic/actions/workflows/tests.yml/badge.svg)

A full-stack veterinary clinic management system built with FastAPI, SQL Server, React, and Python.

---

## Overview

This application allows veterinary clinics to manage:

- Owners
- Pets
- Appointments
- Dashboard statistics

The project follows a layered architecture using:

- Controllers
- Services
- Repositories
- Validators
- Models
- REST API Endpoints

---

## Tech Stack

### Backend

- Python
- FastAPI
- SQL Server
- PyODBC
- Pydantic
- Pytest

### Frontend

- React
- Vite
- JavaScript
- CSS

### DevOps

- Docker
- GitHub Actions

---

## Project Structure

```text
vet_clinic/
│
├── api/
│   ├── handlers/
│   ├── routes/
│   └── schemas/
│
├── app/
│   ├── bootstrap.py
│   └── dependencies.py
│
├── config/
├── controllers/
├── database/
├── exceptions/
├── models/
│
├── repositories/
│   ├── base_repository.py
│   ├── owner_repository.py
│   ├── pet_repository.py
│   └── appointment_repository.py
│
├── services/
│   ├── owner_service.py
│   ├── pet_service.py
│   ├── appointment_service.py
│   └── dashboard_service.py
│
├── validators/
├── views/
├── tests/
│
├── frontend/
│   ├── public/
│   └── src/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── Dockerfile
├── requirements.txt
├── main.py
├── main_api.py
└── README.md
```

---

## Features

### Owner Management

- Create owner
- Update owner
- Delete owner
- Search owners
- View owner details

### Pet Management

- Create pet
- Update pet
- Delete pet
- Search pets
- View pets with owner information

### Appointment Management

- Create appointments
- Update appointments
- Delete appointments
- Search appointments
- View appointments with pet information

### Dashboard

- Total owners
- Total pets
- Total appointments
- Recent appointments

---

## Testing

Current test suite:

```bash
39 tests passing
```

Run tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

Current coverage:

```text
76%
```

---

## Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs tests
- Validates pull requests

Workflow location:

```text
.github/workflows/tests.yml
```

---

## Run Backend

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main_api:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

---

## Docker

Build image:

```bash
docker build -t vet-clinic .
```

Run container:

```bash
docker run -p 8000:8000 vet-clinic
```

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Owners

![Owners](screenshots/owners.png)

### Pets

![Pets](screenshots/pets.png)

### Appointments

![Appointments](screenshots/appointments.png)

---

## Future Improvements

- Authentication and Authorization
- Medical History Management
- Email Appointment Reminders
- Docker Compose Setup
- Deployment to Cloud Platform

---

## Author

**Juan Andrey Ureña Chaves**

Costa Rica