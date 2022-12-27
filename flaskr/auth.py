import functools

## A Blueprint organizes a group of related views and other code
## this is a Blueprint for authentication functions
### will have views to register new users and to log in and out

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for 
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

## creates Blueprint named 'auth'
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=(GET, POST))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for('auth_login'))
        flash(error)
    return render_template('auth/register.html')
            
