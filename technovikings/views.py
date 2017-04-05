from flask import Blueprint, render_template

mod = Blueprint('index', __name__)

@mod.route('/')
def index():
    return render_template('index.html')

@mod.route('/konva')
def konva():
	return render_template('konva.html')