from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required

from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)


@posts.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        post.save()
        flash('Your post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Create Post', form=form, legend='Create Post')


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.find_one(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.find_one(post_id)

    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.save()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post_id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.find_one(post_id)

    if post.author != current_user:
        abort(403)
    post.delete()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
