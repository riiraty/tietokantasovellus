from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignUpForm

# sisäänkirjautuminen
@app.route("/auth/login/", methods = ["GET", "POST"])
def auth_login():
  if request.method == "GET":
    return render_template("auth/loginform.html",
      form = LoginForm()
    )

  form = LoginForm(request.form)
    
  if not form.validate():
    return render_template("auth/loginform.html",
      form = LoginForm(),
      error = 'There must be a typo, please try again'
    )

  user = User.query.filter_by(username=form.username.data,
    password=form.password.data).first()
  if not user:
    return render_template("auth/loginform.html",
      form = form,
      error = "Invalid username or password"
    )

  print("User '" + user.username + "' identified")
  login_user(user)
  return redirect(url_for("posts_index"))

# uloskirjautuminen
@app.route("/auth/logout/")
def auth_logout():
  logout_user()
  flash("Succesfully logged out!")
  return redirect(url_for("index"))

# uusi käyttäjä
@app.route("/auth/signup/", methods = ["GET", "POST"])
def auth_signup():
  if request.method == "GET":
    return render_template("auth/signupform.html",
      form = SignUpForm()
    )
  
  form = SignUpForm(request.form)
  
  if not form.validate():
    return render_template("auth/signupform.html",
      form = form
    )

  wantedUsername = form.username.data

  existingUser = User.query.filter_by(username=wantedUsername).first()

  # jos käyttäjänimi ei ole jo käytössä
  if not existingUser:
    newUser = User(form.username.data, form.password.data)

    db.session().add(newUser)
    db.session.commit()

    # uusi käyttäjä tallennettiin tietokantaan ja kirjataan sisään
    login_user(newUser)
    flash(f"Welcome to the Forum, {current_user.username}! You are ready to start posting.")
    return redirect(url_for("posts_index"))
  else:
    flash("Wanted username already taken, choose another")
    return render_template("auth/signupform.html", form = form)


