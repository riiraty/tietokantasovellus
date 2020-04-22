from flask import render_template, request, redirect, url_for, flash

from application import app, db
from application.posts.models import Post
from application.auth.models import User
from application.threads.models import Thread

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/search/", methods=["POST"])
def search():
  wanted = request.form.get("seek")
  formatted_wanted = "%" + wanted + "%"

  users = User.query.filter(User.username.like(formatted_wanted)).all()
  posts = Post.query.filter(Post.content.like(formatted_wanted)).all()
  threads = Thread.query.filter(Thread.title.like(formatted_wanted)).all()

  return render_template("search_results.html",
    users = users,
    posts = posts,
    threads = threads,
    wanted = wanted
  )