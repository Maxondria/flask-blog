from datetime import datetime

from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flaskblog import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(
        db.String(20),
        nullable=False,
        default='default.jpg')
    password = db.Column(db.String(60),  nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first_or_404()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first_or_404()

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config.get('SECRET_KEY'), expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @classmethod
    def verify_reset_token(cls, token):
        s = Serializer(app.config.get('SECRET_KEY'))
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return cls.query.get(user_id)

    def __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls, page):
        return cls.query.order_by(cls.date_posted.desc()).paginate(per_page=5, page=page)

    @classmethod
    def find_posts_by_user(cls, user, page):
        return cls.query.filter_by(author=user)\
            .order_by(cls.date_posted.desc())\
            .paginate(per_page=5, page=page)

    @classmethod
    def find_one(cls, post_id):
        return cls.query.get_or_404(post_id)

    def __repr__(self):
        return f'Post("{self.title}", "{self.date_posted}")'
