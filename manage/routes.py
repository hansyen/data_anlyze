
from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user, login_required

from models import Role, User
from __init__ import db

ohyamanage = Blueprint('ohyamanage', __name__)

# @manage.context_processor  # 將class丟到前端
# def inject_role():
#     return dict(Role=Role)


@ohyamanage.route("/manage", methods=['GET', 'POST'])
def manage():
    result = User.query.all()
    
    if current_user.is_authenticated:
        if current_user.role != 9:
            flash('You are not allow into manage!', 'warning')
            return redirect(url_for('main.home'))
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('manage.html', result=result)

@ohyamanage.route("/manage/<int:id>", methods=['GET', 'POST'])
def manage_delete(id):
    result = User.query.get(id)  # photo path
    
    if result.role != 9:
        db.session.delete(result)
        db.session.commit()
        flash('Delete account successful!', 'success')
        return  redirect(url_for('ohyamanage.manage'))
    elif result.role == 9:
        flash('You can\'t delete me!', 'warning')
        return  redirect(url_for('ohyamanage.manage'))
