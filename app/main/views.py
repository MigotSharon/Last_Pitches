from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import User
from ..models import User
from . import main
from .. import db,photos
from .forms import UpdateProfile
import markdown2


@main.route('/')
def index():
    '''
    View root page function that returns index page 
    '''
    message= "Hello"
    title = 'Welcome To One Minute Pitch'
    return render_template('index.html', message=message,title=title)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        # user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
