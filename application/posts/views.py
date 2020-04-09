from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.auth.models import User
from application.posts.forms import PostForm, EditForm

# listausnäkymä
@app.route("/posts/", methods=["GET"])
def posts_index():
  return render_template("posts/list.html",
    posts = Post.query.all(),
    user = current_user
  )

# lomake uudelle postaukselle
@app.route("/posts/new/")
@login_required
def posts_form():
  return render_template("posts/new.html", form = PostForm())

# uuden tallennus
@app.route("/posts/", methods=["POST"])
@login_required
def posts_create():
  # posted = Post(request.form.get("content"))
  form = PostForm(request.form)

  if not form.validate():
    return render_template("posts/new.html", form = form)

  posted = Post(form.content.data)
  posted.account_id = current_user.id

  db.session().add(posted)
  db.session().commit()
  
  return redirect(url_for("posts_index"))

# vanhan (oman) postauksen muokkauslomake
@app.route("/posts/<post_id>", methods=["GET"])
@login_required
def edit_form(post_id):
  post = Post.query.get(post_id)

  if post.account_id == current_user.id:
    return render_template("posts/edit_post.html",
      form = EditForm(), post = post
    )
  else:
    return redirect(url_for("posts_index"))

# muokkauksen tallennus
@app.route("/posts/<post_id>", methods=["POST"])
@login_required
def posts_edit(post_id):
  post = Post.query.get(post_id)

  if post.account_id == current_user.id:
    form = EditForm(request.form)

    if not form.validate():
      return render_template("posts/edit_post.html",
        form = form, post = post
      )

    newContent = form.content.data

    post = Post.query.get(post_id)
    post.content = newContent
    db.session().commit()

    return redirect(url_for("posts_index"))
  else:
    return redirect(url_for("posts_index"))

