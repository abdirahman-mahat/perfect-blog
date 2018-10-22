from flask import Flask
from . import main
from datetime import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Blogpost, Comment
from .forms import UpdateProfile, BlogForm , CommentForm
from .. import db, photos
@main.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', posts=posts)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/about')
def about():
    return render_template('about.html')
@main.route('/subscribe')
def subscribe():
    return render_template('subscribe.html')

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
    subscribers=Subscriber.query.all()

    for subscriber in subscribers:
        mail_message("New Blog Post","email/new_post",subscriber.email,post=new_post)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('main.index'))
@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content,post_id=id)

        db.session.add(comment)
        db.session.commit()

    comment = Comment.query.filter_by(post_id=id).all()
      
    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
    del_post = Blogpost.query.filter_by(id=id).first()
    db.session.delete(del_post)
    db.session.commit()

    return redirect(url_for('main.index'))
@main.route('/delet/<int:id>',methods=['GET','POST'])
@login_required
def delete_comment(id):
    delete_comment = Comment.query.filter_by(id=id).first()
    db.session.delete(delete_comment)
    db.session.commit()

    return redirect(url_for('main.index'))