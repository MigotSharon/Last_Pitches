from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, RadioField,SelectField
from wtforms.validators import Required

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post Comment')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category_id = SelectField('Select Pitch Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'), ('4', 'Life'), ('5', 'Product')])
    pitch = TextAreaField('Create A Pitch', validators=[Required()])
    submit = SubmitField('Submit Pitch') 

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')

class DownvoteForm(FlaskForm):
    '''
    Class to create a wtf form for downvoting a pitch
    '''
    submit = SubmitField('Downvote')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')