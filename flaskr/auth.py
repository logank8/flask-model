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

## associates url /register with the register view function
@bp.route('/register', methods=(GET, POST))
def register():
    ## if user submitted the form - start validating the input
    if request.method == 'POST':
        ## requesting user and pass from dict mapping
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        ## validate that username and password are not empty
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                ## takes a sql query with ? placeholders and a tuple to replace the placeholders with
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    ## password is securely hashed and stored
                    (username, generate_password_hash(password)),
                )
                db.commit()
            ## occurs if the username already exists
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                ## redirect to login page
                return redirect(url_for('auth_login'))
        ## show error message
        flash(error)
    ## renders template for html page with registration form
    return render_template('auth/register.html')
            

## associates url /login with the login function
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        ## finds username in db
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone() ## returns one row from the query

        if user is None:
            error = "Incorrect username."
        ## elif password doesnt match given username
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            ## log in
            ### session is a dict that stores data across requests - when validation succeeds, user id is stored in new session
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)
    return render_template('auth/login.html')

## checks if user id is stored in session already and gets user data from db
#### runs before the view function regardless of requested URL
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

##logout url
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


## login required decorator that wraps original view
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        
        return view(**kwargs)
    
    return wrapped_view
