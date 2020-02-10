import os
import secrets

from flask import current_app, url_for
from flask_mail import Message
from PIL import Image

from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    file_name = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', file_name)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return file_name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(subject='Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: 
{url_for('users.reset_password', token=token, _external=True)}
    
    If you did not make this request, please ignore this email and no changes will be made.
    '''
    mail.send(msg)