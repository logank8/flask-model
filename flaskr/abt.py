import functools

## A Blueprint organizes a group of related views and other code
## this is a Blueprint for authentication functions
### will have views to register new users and to log in and out

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for 
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

## creates Blueprint named 'abt'
bp = Blueprint('abt', __name__, url_prefix='/abt')

## associates url /login with the login function
@bp.route('/abt', methods=('GET', 'POST'))
def about():
    return render_template('abt/about.html')


