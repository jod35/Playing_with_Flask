from App import db

class Text(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(255),nullable=False)
    comment=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '{}'.format(self.text)
        