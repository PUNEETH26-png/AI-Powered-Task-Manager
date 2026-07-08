# AI Task Manager

An AI-powered full-stack Task Management application built using **FastAPI**, **Streamlit**, **SQLAlchemy**, **SQLite**, and **Google Gemini AI**.

The application allows users to securely manage their daily tasks and also generate tasks automatically using AI from natural language descriptions.

---

#  Features

##  User Authentication
- User Registration (Signup)
- User Login
- Password hashing using bcrypt
- Duplicate email validation

##  Task Management
- Create Tasks
- View All Tasks
- Update Existing Tasks
- Delete Tasks

##  AI Task Generation
Generate structured tasks from natural language using Google Gemini.

Example:

**Input**

```
I have to prepare for my machine learning interview tomorrow.
```

**AI Output**

```
Title:
Prepare Machine Learning Interview

Description:
Revise machine learning fundamentals, CNNs, Transformers,
SQL, and PyTorch before the interview.

Priority:
High
```

The generated fields are automatically populated into the task creation form.

---

#  Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Passlib (bcrypt)
- Python-dotenv

## Frontend

- Streamlit
- Requests

## AI

- Google Gemini API

---

#  Project Structure

```
Task_Manager_App/
│
├── app/
│   ├── ai/
│   │   ├── router.py
│   │   ├── schema.py
│   │   └── service.py
│   │
│   ├── auth/
│   │   ├── router.py
│   │   ├── schema.py
│   │   └── service.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── models.py
│   │
│   ├── tasks/
│   │   ├── router.py
│   │   ├── schema.py
│   │   └── service.py
│   │
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── .env
├── requirements.txt
├── README.md
└── task_manager.db
```

---

#  Installation

## 1. Clone the repository

```bash
git clone <your-github-repository>
cd Task_Manager_App
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a `.env` file

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 5. Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 6. Start the Streamlit frontend

```bash
streamlit run frontend/app.py
```

Frontend runs at

```
http://localhost:8501
```

---

#  API Endpoints

## Authentication

| Method | Endpoint | Description |
|----------|-------------|----------------|
| POST | `/signup` | Register a new user |
| POST | `/login` | Login |

---

## Tasks

| Method | Endpoint | Description |
|----------|-------------|----------------|
| POST | `/tasks` | Create task |
| GET | `/tasks` | Get all tasks |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

---

## AI

| Method | Endpoint | Description |
|----------|-------------|----------------|
| POST | `/ai/suggest` | Generate task using Gemini AI |

---

#  Why Gemini AI?

Instead of manually filling task details, users can simply describe their work in natural language.

The AI automatically generates:

- Task Title
- Description
- Priority

which significantly improves usability.

---

#  Security

- Passwords are securely hashed using bcrypt.
- Gemini API Key is stored in a `.env` file.
- Sensitive files are excluded using `.gitignore`.

---

#  Why These Technologies?

### FastAPI

Chosen for its excellent performance, automatic OpenAPI documentation, and strong support for type-safe API development.

### SQLAlchemy

Provides ORM capabilities, making database interactions cleaner and easier to maintain.

### Streamlit

Enabled rapid development of an interactive frontend entirely in Python.

### Google Gemini

Integrated to provide AI-powered task generation from natural language prompts.

---

#  What I Learned

During this project I learned:

- Building REST APIs using FastAPI
- SQLAlchemy ORM
- Pydantic validation
- Authentication and password hashing
- CRUD operations
- API integration with Google Gemini
- Building Python-based frontends using Streamlit
- Managing project architecture using routers, services, schemas, and models
- Secure handling of API keys using environment variables

---

#  Future Improvements

Given more time, I would like to add:

- JWT Authentication
- User-specific task management
- PostgreSQL support
- Docker containerization
- Task filtering and searching
- Due date reminders
- Task categories and labels
- Cloud deployment
- Responsive frontend UI

---

#  Screenshots

(Add screenshots here)

- Login Page
- Signup Page
- Dashboard
- AI Task Generation
- Task CRUD Operations

---



#  Author

**Puneeth Raj**


