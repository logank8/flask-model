from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort 

from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def home():
    return render_template('home/index.html')

