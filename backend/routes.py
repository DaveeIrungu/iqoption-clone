from flask import render_template, flash, redirect

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpform()
    if form.validate_on_submit():
        flash('Sign up requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('SignUp.html', title='Sign Up', form=form)

def login():
    form = LogInform()
    if form.validate_on_submit():
        flash('Log in requested for user {}, remember me={}'.format(
            form.username.data, form login.data))
        return redirect('/index')
    return render_template('Login.html', title = 'Log In', form = form)