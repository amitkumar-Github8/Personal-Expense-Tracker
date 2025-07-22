# Personal Expense Tracker Backend (AWS Cloud)

## Overview
This project is a cloud-ready personal expense tracker backend built using Flask (Python), designed for secure, scalable deployment on AWS. It delivers a RESTful API for expense management and demonstrates real-world infrastructure skills including managed databases, cloud virtual servers, and proactive monitoring.

## Features
- RESTful API for user authentication and expense management
- Cloud deployment ready (AWS EC2, RDS, CloudWatch)
- Persistent storage using managed PostgreSQL/MySQL on Amazon RDS
- API endpoints for registering, logging in, adding, viewing, and deleting expenses
- Cloud monitoring setup using CloudWatch

## Architecture
| Component         | Role                        |
|------------------|-----------------------------|
| Flask App (EC2)  | Hosts backend API           |
| Amazon RDS       | Stores user and expense data|
| Amazon CloudWatch| Monitors health, sets alerts|
| API Consumer     | Any frontend/mobile app or API tool |

- User/API Client → Flask API (on EC2) → RDS (database)
- CloudWatch monitors EC2, RDS, and app logs/metrics

## Project Structure
```
expense-tracker/
├── app.py            # Main Flask app, API routes
├── models.py         # SQLAlchemy models (User, Expense)
├── config.py         # Centralized app config
├── requirements.txt  # Python dependencies
├── .env              # Secrets and environment variables (not tracked by git)
├── helpers.py        # (Optional) Utility functions
└── README.md         # Project information & setup
```

## API Endpoints
| Method | Endpoint                | Description                      |
|--------|-------------------------|----------------------------------|
| POST   | /register               | Register new user                |
| POST   | /login                  | Authenticate user                |
| POST   | /expenses               | Add new expense (with user_id)   |
| GET    | /expenses/<user_id>     | Get all expenses for a user      |
| DELETE | /expenses/<expense_id>  | Delete a specific expense        |

## Quick Start (Local)

### 1. Clone the repository
```bash
git clone https://github.com/amitkumar-Github8/Personal-Expense-Tracker.git
cd expense-tracker
```

### 2. Setup Python environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file (do not commit!) with:
```
SECRET_KEY=your-strong-key
DATABASE_URI=sqlite:///expense-tracker.db
```

### 4. Initialize the database
```bash
python create_db.py
```

### 5. Run the app locally
```bash
python -m flask run
```
The server listens at http://127.0.0.1:5000

## Deploying to AWS (Cloud)

### 1. Provision EC2 Instance
- Choose Ubuntu or Amazon Linux 2.
- Open HTTP (80), HTTPS (443), and Flask port (5000).
- Install Python 3, pip, git.

### 2. Set Up Database with Amazon RDS
- Create a PostgreSQL/MySQL instance via AWS console.
- Note the endpoint, database name, user, and password.
- Update `.env` with `DATABASE_URI` in the form:
  - `postgresql://user:password@rds-endpoint:5432/dbname`

### 3. Clone, Configure, and Run
```bash
git clone https://github.com/amitkumar-Github8/Personal-Expense-Tracker.git
cd expense-tracker
pip install -r requirements.txt
# Update .env for production
python -m flask run --host=0.0.0.0
```
Or use gunicorn and proxy with nginx for production.

### 4. Initialize Remote Database
```bash
python -m flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 5. Configure Security Groups
- RDS: Allow inbound DB port from EC2 only.
- EC2: Allow HTTP/HTTPS from public, but restrict sensitive ports.

### 6. Enable CloudWatch Monitoring
- Set up log streaming from EC2.
- Create alarms for CPU, memory, and application errors.

## Sample API Calls

**Register:**
```bash
curl -X POST http://<host>/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "pw123"}'
```

**Login:**
```bash
curl -X POST http://<host>/login \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "pw123"}'
```

**Add Expense:**
```bash
curl -X POST http://<host>/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount":99.99, "category":"Food", "date":"2025-07-22", "user_id":1}'
```

**List Expenses:**
```bash
curl http://<host>/expenses/1
```

**Delete Expense:**
```bash
curl -X DELETE http://<host>/expenses/1
```

## Cloud & Security Considerations
- **Secrets:** Never commit sensitive info; use AWS Secrets Manager if possible.
- **Network:** Isolate RDS and EC2 in a private VPC; restrict security groups.
- **Scaling:** Leverage auto-scaling for EC2 and RDS as app grows.
- **Monitoring:** Rely on CloudWatch for logs, alarms, and insight into resource use.

## Technologies Used
- Python 3.x, Flask, SQLAlchemy
- AWS EC2, RDS (PostgreSQL/MySQL), CloudWatch
- pip, gunicorn, nginx (for production)
- dotenv for config
- curl / Postman for API testing

---
This backend offers a complete, scalable API for expense tracking, built for cloud and ready for integration with frontends or mobile apps.
