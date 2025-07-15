from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.db import mysql

expense_bp = Blueprint('expense', __name__)

@expense_bp.route('/add', methods=['POST'])
@jwt_required()
def add_expense():
    user_id = get_jwt_identity()
    data = request.json
    amount = data['amount']
    category = data['category']
    date = data['date']
    description = data['description']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO expenses (user_id, amount, category, date, description) VALUES (%s, %s, %s, %s, %s)",
                   (user_id, amount, category, date, description))
    mysql.connection.commit()
    return jsonify(message="Expense added"), 201

@expense_bp.route('/list', methods=['GET'])
@jwt_required()
def list_expenses():
    user_id = get_jwt_identity()
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM expenses WHERE user_id=%s", (user_id,))
    expenses = cursor.fetchall()
    result = []
    for e in expenses:
        result.append({
            'id': e[0],
            'amount': float(e[2]),
            'category': e[3],
            'date': str(e[4]),
            'description': e[5]
        })
    return jsonify(expenses=result)
