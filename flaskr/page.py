from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.exceptions import abort 

from flaskr.db import get_db
from flaskr.pred import Predictor, Prediction

p = Predictor()
bp = Blueprint('page', __name__)

class NamerForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    submit = SubmitField('Submit')

@bp.route('/', methods=('GET', 'POST'))
def home():
    pred = None
    form = NamerForm()
    db = get_db()
    if form.validate_on_submit():
        pred = p.predict(search=form.name.data)
        title = pred.song.name + "(" + pred.song.artists[0].name + ")"
        db.execute(
            "INSERT INTO prediction (song, pred, realnum) VALUES (?, ?, ?)",
            (title, pred.pred[0], pred.real)
        )
        db.commit()
        form.name.data = ''
    prev = db.execute(
        'SELECT * FROM prediction'
        ' ORDER BY created DESC'
    ).fetchall()
    
    return render_template('home/index.html', pred = pred, form = form, previous=prev)
    

