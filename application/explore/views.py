from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user

from sqlalchemy import desc, func

from application import app, db
from application.auth.models import User
from application.posts.models import Post
from application.threads.models import Thread

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
  user = User.query.filter_by(username=username).first()

  if user:
    # 5 viimeisintä lankaa
    sub = db.session.query(func.max(Post.id)).filter_by(account_id=user.id).group_by(Post.thread_id).subquery()
    thread_posts = db.session.query(Post).filter(Post.id.in_(sub)).order_by(Post.post_time.desc()).limit(5).all()

    # kaikki käyttäjän aloittamat langat sivutettuna
    page = request.args.get("page", default=1, type=int)
    per_page = 2

    threads = Thread.query.filter_by(owner_id=user.id).order_by(Thread.creation_time.desc()).paginate(page,per_page,error_out=False)

    return render_template("explore/user.html",
      user = user,
      thread_posts = thread_posts,
      threads = threads,
      curren_user = current_user
    )
  else:
    flash(f"There is no {username} on the Forum. If you entered the URL manually please check your spelling and try the search tool. ", "alert alert-warning")
    return redirect(url_for("posts_index"))

@app.route("/search/", methods=["POST"])
def search():
  wanted = request.form.get("seek")
  formatted_wanted = "%" + wanted + "%"

  users = User.query.filter(User.username.like(formatted_wanted)).all()
  posts = Post.query.filter(Post.content.like(formatted_wanted)).all()
  threads = Thread.query.filter(Thread.title.like(formatted_wanted)).all()

  return render_template("explore/search_results.html",
    users = users,
    posts = posts,
    threads = threads,
    wanted = wanted
  )