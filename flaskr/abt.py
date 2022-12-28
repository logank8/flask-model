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
    return render_template('abt/about.html')


