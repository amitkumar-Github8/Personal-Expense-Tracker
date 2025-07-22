from flask import Flask, request, jsonify
from config import Config
from models import db, User, Expense
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Authentication endpoints
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    if not data.get("username") or not data.get("password"):
        return jsonify({"message": "Missing username or password"}), 400
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "User already exists"}), 409
    hashed_pw = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registered"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Login successful", "user_id": user.id}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Expense CRUD endpoints
@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    try:
        expense = Expense(
            amount=data["amount"],
            category=data["category"],
            date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
            description=data.get("description", ""),
            user_id=data["user_id"]
        )
        db.session.add(expense)
        db.session.commit()
        return jsonify({"message": "Expense added"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/expenses/<int:user_id>", methods=["GET"])
def list_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": e.id,
            "amount": e.amount,
            "category": e.category,
            "date": str(e.date),
            "description": e.description
        } for e in expenses
    ])

@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message": "Expense deleted"})

if __name__ == "__main__":
    app.run(debug=True)
