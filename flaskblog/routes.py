from flask import flash, redirect, render_template, url_for

from flaskblog import app, bcrypt
from flaskblog.forms import LoginForm, RegistrationForm
from flaskblog.models import Post, User

posts = [
    {
        "author": "Lars Vondracek",
        "title": "Trance",
        "content": "nulla nisl nunc nisl duis bibendum felis sed t",
        "date_posted": "2019-09-08"
    },
    {
        "author": "Portia Stennard",
        "title": "Quiet Flows the Don (Tikhiy Don)",
        "content": "luctus ultricies eu nibh quisque id justo sit amet sapien ",
        "date_posted": "2020-01-08"
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')

        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)

        user.save()

        flash('Your account has been created, please login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Authentication Failed', 'danger')
    return render_template('login.html', title='LogIn', form=form)
