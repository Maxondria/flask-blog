from flask import Flask, render_template, url_for

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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
