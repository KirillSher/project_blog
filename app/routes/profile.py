from flask import request, redirect, url_for, render_template
from flask_login import login_required

from app import app
from app.models.users import User, db


@app.route('/profile/<int:user_id>/', methods=['GET'])
@login_required
def profile(user_id):
    user = User.query.get(user_id)
    if user is None:
        return "User not found", 404
    return render_template('profile/profile.html', user=user, avatar=user.avatar)


@app.route('/profile/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_profile(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('profile', user_id=user.id))
    return render_template("profile/edit_profile.html", user=user)
