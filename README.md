# Personal Expense Tracker (Flask/AWS)

Welcome! This project is a cloud-deployable backend API for tracking personal expenses, built with Flask (Python) and designed for scalable, secure operation on AWS using EC2, RDS, and CloudWatch.

---

## 🚀 Project Overview
- **Backend:** Python Flask REST API
- **Cloud:** AWS (EC2, RDS, CloudWatch)
- **Database:** PostgreSQL (recommended) or MySQL via Amazon RDS
- **Monitoring:** CloudWatch for alerts and resource monitoring

---

## ✨ Features
- User registration and login (secure credential storage)
- Add, view, and delete personal expenses
- Persistent storage in a managed SQL database
- Easily integrable with any frontend (web, mobile) or API tool
- Cloud monitoring and alert capabilities

---

## 🛠️ Architecture
| Component         | Purpose                        |
|------------------|--------------------------------|
| Flask app (EC2)  | Exposes REST API, business logic|
| RDS (PostgreSQL) | Stores users and expenses       |
| CloudWatch       | Monitors server health, alerts  |
| API Client       | Frontend, mobile, or Postman/cURL |

**Interaction flow:**
Client → Flask API (EC2) → RDS
AWS CloudWatch monitors EC2 and RDS for alerts and logs

---

## 📂 Project Structure
```
expense-tracker/
├── app.py            # Main Flask app and routes
├── models.py         # SQLAlchemy models (User, Expense)
├── config.py         # Central app config and DB URI
├── requirements.txt  # Python package dependencies
├── .env              # Environment/work secrets (never commit)
├── helpers.py        # (Optional) Utility functions
└── README.md         # Project instructions (this file)
```

---

## 🌐 API Reference
| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| POST   | /register               | Register a new user          |
| POST   | /login                  | Authenticate user, get user ID|
| POST   | /expenses               | Add new expense (JSON)       |
| GET    | /expenses/<user_id>     | Get all expenses for user    |
| DELETE | /expenses/<expense_id>  | Delete an expense by ID      |

All endpoints use JSON and respond in JSON format.
Authentication is basic (user ID in API calls); you can add token or session auth as an enhancement.

---

## ⚡ Quickstart (Local Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/amitkumar-Github8/Personal-Expense-Tracker.git
   cd expense-tracker
   ```
2. **Set up Python and dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Configure .env**
   ```
   SECRET_KEY=your-strong-secret
   DATABASE_URI=sqlite:///expense-tracker.db
   ```
4. **Initialize the database**
   ```bash
   python -m flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```
5. **Run the app**
   ```bash
   python -m flask run
   ```
   Access at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ☁️ Deploying to AWS

- **Provision EC2 Instance**
  - Select Ubuntu or Amazon Linux 2.
  - Allow HTTP/HTTPS and your chosen app port (usually 5000).
- **Create Amazon RDS Instance**
  - Choose PostgreSQL or MySQL.
  - Note the endpoint, username, password.
- **Configure Security Groups**
  - RDS: Only allow database port from EC2.
  - EC2: Allow HTTP from internet, lock other ports.
- **Set .env with your production secrets**
   ```
   SECRET_KEY=your-strong-prod-key
   DATABASE_URI=postgresql://user:password@rds-endpoint:5432/dbname
   ```
- **Install, initialize, and run**
   ```bash
   pip install -r requirements.txt
   python -m flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   python -m flask run --host=0.0.0.0
   ```
   (Use nginx+gunicorn for production).
- **Set up CloudWatch**
  - Enable log streaming and resource alarms for EC2 and RDS.

---

## 🧑‍💻 Example API Usage

**Register a user**
```bash
curl -X POST http://<host>/register \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "pw123"}'
```

**Login**
```bash
curl -X POST http://<host>/login \
  -H "Content-Type: application/json" \
  -d '{"username": "alice", "password": "pw123"}'
```

**Add an expense**
```bash
curl -X POST http://<host>/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 55.5, "category": "Food", "date": "2025-07-22", "user_id": 1}'
```

**List expenses**
```bash
curl http://<host>/expenses/1
```

**Delete an expense**
```bash
curl -X DELETE http://<host>/expenses/1
```

---

## 🔒 Security & Best Practices
- Never commit sensitive data (.env, credentials) to version control.
- Use AWS Secrets Manager/Parameter Store for production secrets.
- Fine-tune your Security Groups; never expose databases to the world.
- Set up regular backups and enable multi-zone availability for RDS if required.

---

## ⚙️ Technologies Used
- Python 3.x, Flask, SQLAlchemy
- AWS: EC2, RDS, CloudWatch
- pip for Python packages
- dotenv for configuration
