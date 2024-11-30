from flask import Blueprint, render_template, request, jsonify
from app.database import test_connection, delete_all_products, insert_products_ldm, insert_products_sp
import time

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/test_connection/<db_type>')
def connection_status(db_type):
    status = test_connection(db_type)
    return jsonify({"status": status})

@bp.route('/delete/<db_type>', methods=['DELETE'])
def delete_records(db_type):
    success = delete_all_products(db_type)
    return jsonify({"success": success})

@bp.route('/insert_ldm/<db_type>', methods=['POST'])
def insert_ldm(db_type):
    data = request.form.to_dict()
    count = insert_products_ldm(db_type, data)
    return jsonify({"count": count})

@bp.route('/insert_sp/<db_type>', methods=['POST'])
def insert_sp(db_type):
    data = request.form.to_dict()
    count = insert_products_sp(db_type, data)
    return jsonify({"count": count})
