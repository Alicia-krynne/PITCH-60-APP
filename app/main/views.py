from flask import render_template, redirect, url_for
from . import main
from ..models import User
from .. import db

@main.route('/')
def index():
    pitches = Pitch.query.all()
    bonvoyage= Pitch.query.filter_by(category = 'Bonvoyage').all() 
    concert = Pitch.query.filter_by(category = 'Concert').all()
    Run = Pitch.query.filter_by(category = 'Run').all()
    return render_template('index.html', bonvoyage = bonvoyage,concert = concert, pitches = pitches,run= run)

