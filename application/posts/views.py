from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.posts.models import Post
from application.posts.forms import PostForm

@app.route("/posts/", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/new/")
@login_required
def posts_form():
    return render_template("posts/new.html", form = PostForm())

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