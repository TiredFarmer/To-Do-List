from todoapp import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    assignments = db.relationship('Assignment', backref='author', lazy=True)

    def __repr__(self):
        return f"User(\"{self.username}\")"


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(60), nullable=False)
    due_date = db.Column(db.String(60), nullable=False)
    due_time = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Assignment(\"{self.name}\", \"{self.course}\", \"{self.due_date}\", \"{self.due_time}\")"


def add_user(username: str, password: str) -> bool:
    for user in User.query.all():
        if user.username == username:
            return False
        elif password == "":
            return False

    db.session.add(User(username=username, password=password))
    db.session.commit()
    return True


def auth_user(username: str, password: str) -> bool:
    for user in User.query.all():
        if user.username == username:
            if user.password == password:
                return True

    return False
