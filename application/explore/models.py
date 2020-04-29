from application import db

class Archive(db.Model):

  id = db.Column(db.Integer, primary_key=True)

  account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
  thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

  def __init__(self, account_id, thread_id):
    self.account_id = account_id
    self.thread_id = thread_id