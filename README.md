# StockFlow — Inventory Management MVP

A simple inventory management backend built with FastAPI and PostgreSQL. This project is being developed phase by phase as part of an assignment, with the goal of building a basic inventory application that allows users to manage products and track stock.

## Project Overview

StockFlow is a small inventory management application designed to keep track of products, quantities and pricing. The MVP focuses on the core functionality required for inventory management without adding unnecessary complexity.

## Tech Stack

- **Python** — Programming language
- **FastAPI** — Backend API framework
- **PostgreSQL** — Database
- **SQLAlchemy** — ORM for database operations
- **Uvicorn** — ASGI server

## Current Progress

### Phase 1 — Project Setup and Database

- [x] FastAPI project setup
- [x] PostgreSQL connection
- [x] SQLAlchemy configuration
- [x] Organization model
- [x] User model
- [x] Product model
- [x] Initial database table creation
- [x] Basic API endpoint

### Planned Phases

- [ ] Phase 2 — Authentication and Organization
- [ ] Phase 3 — Product CRUD operations
- [ ] Phase 4 — Inventory and Dashboard
- [ ] Phase 5 — Testing and final improvements

## Project Structure

stockflow/
├── app/
│   ├── core/
│   │   └── database.py
│   ├── models/
│   │   ├── organization.py
│   │   ├── user.py
│   │   └── product.py
│   ├── routes/
│   ├── repositories/
│   ├── services/
│   ├── schemas/
│   └── main.py
├── .env
├── .gitignore
└── requirements.txt

## Setup and Installation

### 1. Clone the repository

bash
git clone <your-repository-url>
cd stockflow


### 2. Create a virtual environment

bash
python -m venv venv


Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

Create a database named:

```sql
CREATE DATABASE stockflow_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/stockflow_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, access the interactive Swagger documentation:

- **API:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Current Endpoint

| Method | Endpoint | Description                       |
| ------ | -------- | --------------------------------- |
| GET    | `/`      | Checks whether the API is running |

## Current Database Models

- **Organization:** Stores organization information.
- **User:** Stores user information and links users to organizations.
- **Product:** Stores product details, pricing, quantity and stock threshold.

## Development Approach

The project is developed incrementally. Each phase focuses on a specific part of the application, and changes are committed to Git after completing and testing the phase.

## Note

This is an MVP project currently under development. Features will be added gradually as the project progresses.

