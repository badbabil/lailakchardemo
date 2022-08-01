from flask import render_template, session, url_for,flash,redirect
from requests import request
from main import app
from main import auth
from main.forms import RegistrationForm, LoginForm, Forgetpassword
from flask_login import login_user


posts = [
    {
        'author':'babil',
        'title':'the first post',
        'content':'flask',
        'date_posted':'20-06-2022'
    },
   {
        'author':'ritam',
        'title':'the second post',
        'content':'flask',
        'date_posted':'19-06-2022'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',post=posts,title='home')


@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/logout")
def logout():
    pass


@app.route("/Signup", methods = ['GET','POST'])
def Signup():
    
    userreg = RegistrationForm()

    if userreg.validate_on_submit():
        try:
            regemail = userreg.email.data
            regpassword = userreg.password.data
            new_user = auth.create_user_with_email_and_password(regemail,regpassword)
            auth.send_email_verification(new_user['idToken'])
            flash(f'Account created for {new_user.username.data}!, verification mail has been sent to your email. Please verify and login','success')
            return redirect(url_for('login'))
        except:
             flash('Email already exists','danger')

    return render_template('signuppage.html',title='Sign up',form = userreg)

@app.route("/Login",methods = ['POST','GET'])
def login():
    userinfo = LoginForm()

    if userinfo.validate_on_submit(): 
        email = userinfo.email.data
        password = userinfo.password.data
        print(email,password)
        try:
            user = auth.sign_in_with_email_and_password(email,password)
            user_account_info = auth.get_account_info(user['idToken'])
            if user_account_info['users'][0]['emailVerified']==False:
                flash(f'Email not verified, Please verify (check for verification mail) and login','danger')
                return redirect(url_for('login'))
            else:
                # login_user(user,remember=userinfo.remember.data)
                flash(f'successfully logged in {email}!','success')
                return redirect (url_for('home'))
                # session['user'] = email
                # return render_template('loginpage.html',title='Log in',form = user)
        except:
            flash(f'unsuccessful ,please check your email or password !','danger')
            return redirect(url_for('login'))

    return render_template('index.html',title='Log in',form = userinfo)

@app.route("/ForgetPassword")
def forgetpassword():
    user_fp = Forgetpassword()

    if user_fp.validate_on_submit(): 
        try:
            auth.send_password_reset_email(user_fp.email.data)
            flash(f'An password reset mail has been sent to {user_fp.email.data}!. Please check and login','success')
            return redirect(url_for('login'))
        except:
            flash(f'email not exist!')
    return render_template('forgetpassword.html',title='Forget Password',form = user_fp)