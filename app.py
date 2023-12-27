from flask import Flask, redirect, Blueprint, render_template, request, url_for
from Db import db
from Db.models import users
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)