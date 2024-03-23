"""Blogly application."""

from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import text
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def list_users(): 
    """ Shows list of all pets in db"""
    with app.app_context():
        users = User.query.all()

    return render_template('list_users.html', users = users)

@app.route('/new')
def show_add_user():

    return render_template('new_user.html')

@app.route('/new', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    with app.app_context():
        new_user = User(first_name = first_name, last_name = last_name, image_url = image_url)
        db.session.add(new_user)
        db.session.commit()
        return redirect (f"/{new_user.id}")
    
@app.route('/<int:user_id>')
def show_user(user_id):
    """Show details about a single pet"""
    with app.app_context():
        user = User.query.get_or_404(user_id)

    return render_template("user_details.html",user=user)

@app.route('/<int:user_id>/edit')
def show_edit_user(user_id):

    with app.app_context():
        user = User.query.get_or_404(user_id)

    return render_template("edit_user.html", user=user)

@app.route('/<int:user_id>/edit', methods=["POST"])
def edit_user(user_id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    with app.app_context():
        user = User.query.get(user_id)
        user.first_name = f'{first_name}'
        user.last_name= f'{last_name}'
        user.image_url= f'{image_url}'
        db.session.add(user)
        db.session.commit()
        return redirect (f"/{user.id}")
    
@app.route('/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect("/")