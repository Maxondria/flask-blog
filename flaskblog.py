from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

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

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee9ce57217cad182c77c88b36f62e79c'


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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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


if __name__ == "__main__":
    app.run(debug=True)
