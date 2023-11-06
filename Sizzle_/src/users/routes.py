from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import db, User

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle user registration here
        # Validate and store user data in the database
        flash('Registration successful!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle user login here
        # Authenticate user and create a session
        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html')

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import db, User

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)

        # You should add validation and error handling here
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html')

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # You should add authentication logic here
        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            flash('Login successful!', 'success')
            # Create a session or token for the user
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager()

@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

@users.route('/menu_item/<int:item_id>/add_review', methods=['POST'])
@login_required  # Requires user authentication
def add_review(item_id):
    rating = int(request.form['rating'])
    comment = request.form['comment']

    # Validate and save the review to the database
    review = Review(user_id=current_user.id, item_id=item_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()

    flash('Review added successfully!', 'success')
    return redirect(url_for('menu.show_item', item_id=item_id))

from datetime import datetime, timedelta

# Define the maximum number of reviews allowed per user per day
MAX_REVIEWS_PER_DAY = 3

@users.route('/menu_item/<int:item_id>/add_review', methods=['POST'])
@login_required
def add_review(item_id):
    # Check the user's recent reviews
    user_reviews = Review.query.filter_by(user_id=current_user.id).filter(
        Review.timestamp > (datetime.utcnow() - timedelta(days=1))
    ).all()

    if len(user_reviews) >= MAX_REVIEWS_PER_DAY:
        flash(f'You have reached the maximum number of reviews allowed per day ({MAX_REVIEWS_PER_DAY}).', 'danger')
        return redirect(url_for('menu.show_item', item_id=item_id))

    # Proceed with review submission
    rating = int(request.form['rating'])
    comment = request.form['comment']

    # Validate and save the review to the database
    review = Review(user_id=current_user.id, item_id=item_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()

    flash('Review added successfully!', 'success')
    return redirect(url_for('menu.show_item', item_id=item_id))

import requests

RECAPTCHA_SECRET_KEY = 'YOUR_SECRET_KEY'

@users.route('/menu_item/<int:item_id>/add_review', methods=['POST'])
@login_required
def add_review(item_id):
    # Check the reCAPTCHA response
    recaptcha_response = request.form.get('g-recaptcha-response')
    if not recaptcha_response:
        flash('Please complete the reCAPTCHA to submit a review.', 'danger')
        return redirect(url_for('menu.show_item', item_id=item_id))

    # Verify the reCAPTCHA response
    response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={'secret': RECAPTCHA_SECRET_KEY, 'response': recaptcha_response}
    )
    result = response.json()
    if not result['success']:
        flash('reCAPTCHA verification failed. Please try again.', 'danger')
        return redirect(url_for('menu.show_item', item_id=item_id))

    # Proceed with review submission
    rating = int(request.form['rating'])
    comment = request.form['comment']

    # Validate and save the review to the database
    review = Review(user_id=current_user.id, item_id=item_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()

    flash('Review added successfully!', 'success')
    return redirect(url_for('menu.show_item', item_id=item_id))

@app.route('/promotions')
def list_promotions():
    promotions = Promotion.query.filter(Promotion.end_date >= datetime.now()).all()
    return render_template('promotions.html', promotions=promotions)

from datetime import datetime

def deactivate_expired_promotions():
    expired_promotions = Promotion.query.filter(Promotion.end_date < datetime.now()).all()
    for promotion in expired_promotions:
        # Update the promotion status in the database
        promotion.active = False
    db.session.commit()

#admin user roles
from flask_principal import Principal, Permission, RoleNeed

principal = Principal(app)

admin_permission = Permission(RoleNeed('admin'))

@app.route('/admin/promotions', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def admin_promotions():
    # Admin promotions management page
    # Only users with the 'admin' role can access this route

#admin routes
@app.route('/admin/promotions/new', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def create_promotion():
    # Create a new promotion
    if request.method == 'POST':
        # Handle form data to create a new promotion
        # ...

@app.route('/admin/promotions/<int:id>/edit', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def edit_promotion(id):
    # Edit an existing promotion
    promotion = Promotion.query.get(id)
    if promotion:
        if request.method == 'POST':
            # Handle form data to edit the promotion
            # ...
    else:
        flash('Promotion not found.', 'danger')
        return redirect(url_for('admin_promotions'))
