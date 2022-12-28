from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort 

from flaskr.db import get_db
from flaskr.pred import prediction

bp = Blueprint('page', __name__)

@bp.route('/', methods=('GET', 'POST'))
def home():
    render_template('home/index.html')

