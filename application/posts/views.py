from application import app, db
from flask import render_template, request, redirect, url_for
from application.posts.models import Post

@app.route("/posts/", methods=["GET"])
def posts_index():
    return render_template("posts/list.html", posts = Post.query.all())

@app.route("/posts/new/")
def posts_form():
    return render_template("posts/new.html")

@app.route("/posts/", methods=["POST"])
def posts_create():
    posted = Post(request.form.get("content"))

    db.session().add(posted)
    db.session().commit()
  
    return redirect(url_for("posts_index"))