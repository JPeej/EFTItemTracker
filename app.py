from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('EFT_SECRET')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash(f'You have been logged in.', 'success')
            return redirect((url_for('tracker')))
        else:
            flash(f'Log in failed. Check email and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.', 'success')
        return redirect(url_for('tracker'))
    return render_template('register.html', form=form)


@app.route('/tracker')
def tracker():
    return render_template('tracker.html')


if __name__ == '__main__':
    app.run(debug=True)
