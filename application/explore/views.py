from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from sqlalchemy import desc, func

from application import app, db
from application.auth.models import User
from application.posts.models import Post
from application.threads.models import Thread
from application.explore.models import Archive

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

@app.route("/user/archive/<thread_id>", methods=["GET","POST"])
@login_required
def archive(thread_id):
  thread = Thread.query.get_or_404(thread_id)
  try:
    existing = Archive.query.filter_by(account_id=current_user.id, thread_id=thread.id).first()

    if not existing:
      record = Archive(current_user.id, thread.id)
      db.session().add(record)
      db.session().commit()
      flash("Discussion thread archived", "alert alert-info")
    else:
      flash("Already in archive", "alert alert-warning")
  except:
    db.session.rollback()
    flash("Error occurred", "alert alert-danger")

  return redirect(url_for("posts_thread", thread_id=thread_id))

@app.route("/user/<username>/archive/", methods=["GET"])
@login_required
def get_archive(username):
  if current_user.username == username:
    try:
      sub = db.session.query(Archive.thread_id).filter_by(account_id=current_user.id).subquery()
      threads = db.session.query(Thread.id, Thread.title, User.username, Thread.modification_time).join(User, User.id==Thread.owner_id).filter(Thread.id.in_(sub)).all()
      return render_template("explore/archive.html",
        user = current_user,
        threads = threads
      )
    except:
      flash("Error occurred", "alert alert-danger")
  else:
    flash("You are not authorized", "alert alert-danger")
  return redirect(url_for("posts_index"))

@app.route("/user/<username>/archive/delete/<thread_id>", methods=["GET","POST"])
@login_required
def remove_archived_thread(username, thread_id):
  # remove from db:
  # write code here

  return redirect(url_for("posts_index"))