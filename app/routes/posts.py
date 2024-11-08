from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from app import app
from app.models import db, Post


@app.route('/posts/')
@login_required
def posts():
    posts = Post.query.filter_by(author_id=current_user.id).all()
    if posts:
        return render_template('posts/posts.html', posts=posts)
    else:
        return render_template('posts/empty_post.html')


@app.route('/posts/create/', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template('posts/create_post.html')


@app.route('/posts/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user != post.author:
        return "У вас нет доступа к редактированию этого поста"

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template('posts/edit_post.html', post=post)
