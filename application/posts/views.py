from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from sqlalchemy import desc, func

from application import app, db
from application.posts.models import Post
from application.auth.models import User
from application.threads.models import Thread
from application.posts.forms import PostForm

# lomake uudelle kommentille
@app.route("/posts/<thread_id>/new/")
@login_required
def posts_form(thread_id):
  thread = Thread.query.get_or_404(thread_id)
  
  return render_template("posts/new.html",
    form = PostForm(),
    thread_id = thread_id,
    title = thread.title
  )

# uuden tallennus
@app.route("/posts/<thread_id>", methods=["POST"])
@login_required
def posts_create(thread_id):
  thread = Thread.query.get_or_404(thread_id)

  form = PostForm(request.form)

  if not form.validate():
    return render_template("posts/new.html",
      form = form,
      thread_id = thread_id,
      title = thread.title
    )

  thread.modification_time = db.func.current_timestamp()

  posted = Post(form.content.data)
  posted.account_id = current_user.id
  posted.thread_id = thread_id

  db.session().add(posted)
  db.session().commit()
  
  flash("Your comment was posted", "alert alert-info")
  return redirect(url_for("posts_thread", thread_id=thread_id))

# vanhan (oman) postauksen muokkauslomake
@app.route("/posts/<thread_id>/<post_id>", methods=["GET"])
@login_required
def edit_form(thread_id, post_id):
  post = Post.query.get_or_404(post_id)

  # kirjautuneen käyttäjän oltava alkuperäinen postaaja
  if post.account_id == current_user.id:
    return render_template("posts/edit_post.html",
      form = PostForm(), post = post
    )
  else:
    flash("You are not authorized", "alert alert-danger")
    return redirect(url_for("posts_index"))

# muokkauksen tallennus
@app.route("/posts/<thread_id>/<post_id>", methods=["POST"])
@login_required
def posts_edit(thread_id, post_id):
  post = Post.query.get_or_404(post_id)

  if post.account_id == current_user.id:
    form = PostForm(request.form)

    if not form.validate():
      return render_template("posts/edit_post.html",
        form = form, post = post
      )

    newContent = form.content.data
    post.content = newContent

    db.session().commit()

    flash("Your post was edited", "alert alert-info")
  else:
    flash("You are not authorized", "alert alert-danger")
    
  return redirect(url_for("posts_thread", thread_id=thread_id))

# oman postauksen poistaminen
@app.route("/posts/<thread_id>/delete/<post_id>", methods=["GET", "POST"])
@login_required
def posts_delete(thread_id, post_id):
  post = Post.query.get(post_id)

  if post.account_id == current_user.id:
    db.session.delete(post)
    db.session.commit()
    flash("Your post was deleted", "alert alert-info")
  else:
    flash("You are not authorized", "alert alert-danger")

  return redirect(url_for("posts_thread", thread_id=thread_id))

