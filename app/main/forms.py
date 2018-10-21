from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class BlogForm(FlaskForm):

    title = StringField('title')
    subtitle= StringField('subtitle')
    content = TextAreaField('blog content...')
    author= StringField('author')
    submit = SubmitField('Post')


class CommentForm(FlaskForm):

    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you...')
    submit = SubmitField('Submit')