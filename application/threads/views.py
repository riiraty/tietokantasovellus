from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from sqlalchemy import desc, func

from application import app, db
from application.posts.models import Post
from application.auth.models import User
from application.threads.models import Thread

from application.threads.forms import ThreadForm

# listausnäkymä
@app.route("/posts/", methods=["GET"])
def posts_index():
  # haetaan 25 viimeksi päivitettyä ketjua
  threads = db.session.query(Thread.id, Thread.title, User.username, Thread.modification_time).join(User, User.id == Thread.owner_id).order_by(Thread.modification_time.desc()).limit(25).all()

  return render_template("threads/list.html",
    threads = threads,
    user = current_user,
    now = db.func.current_timestamp()
  )

# lomake uudelle langalle
@app.route("/posts/threads/new/")
@login_required
def threads_form():
  return render_template("threads/new_thread.html",
    form = ThreadForm()
  )

# uuden langan tallennus
@app.route("/posts/threads/", methods=["POST"])
@login_required
def threads_create():
  form = ThreadForm(request.form)

  if not form.validate():
    return render_template("threads/new_thread.html",
      form = form
    )

  # luodaan uusi lanka ja luodaan ID tallentamalla
  thread = Thread(form.title.data)
  thread.owner_id = current_user.id
  db.session.add(thread)
  db.session.commit()

  # luodaan uusi postaus
  posted = Post(form.content.data)
  posted.account_id = current_user.id
  posted.thread_id = thread.id
  db.session().add(posted)
  db.session().commit()
  
  flash("Your new post was saved", "alert alert-info")
  return redirect(url_for("posts_index"))

# yksittäisen langan näkymä
@app.route("/posts/threads/<thread_id>", methods=["GET"])
def posts_thread(thread_id):
  thread = Thread.query.get_or_404(thread_id)

  return render_template("threads/thread.html",
    thread = thread,
    user = current_user
  )

# langan poistaminen
@app.route("/posts/threads/delete/<thread_id>", methods=["GET", "POST"])
@login_required
def threads_delete(thread_id):
  thread = Thread.query.get_or_404(thread_id)

  # kirjautuneen oltava langan omistaja
  if thread.owner_id == current_user.id:
    db.session.delete(thread)
    Thread.delete_thread_posts(thread_id)
    db.session.commit()

    flash("Your post and all the comments were deleted", "alert alert-info")
    return redirect(url_for("posts_index"))
  else:
    flash("You are not authorized", "alert alert-danger")
    return redirect(url_for("posts_index"))
