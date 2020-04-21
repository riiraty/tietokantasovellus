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

  # kaikki käyttäjän aloittamat langat
  threads = Thread.query.filter_by(owner_id=user.id).all()

  # 8 viimeisintä lankaa
  sub = db.session.query(func.max(Post.id)).filter_by(account_id=user.id).group_by(Post.thread_id).subquery()
  thread_posts = db.session.query(Post).filter(Post.id.in_(sub)).order_by(Post.post_time.desc()).limit(8).all()


  return render_template("users/user.html",
    user = user,
    threads = threads,
    thread_posts = thread_posts,
    curren_user = current_user
  )