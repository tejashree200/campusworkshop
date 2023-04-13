"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq0tpmbg5e4khq14lg-a",
        database="todo_yku9",
        user="root",
        password="YiwMtgb5mTZfK6oy7bLx2nFEqKbTudJQ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
