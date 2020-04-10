from application import db

class Thread(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  creation_time = db.Column(db.DateTime, default=db.func.current_timestamp())
  modification_time = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

  title = db.Column(db.String(64), nullable=False)

  posts = db.relationship("Post", backref='thread', lazy=True)

  def __init__(self, title):
    self.title = title