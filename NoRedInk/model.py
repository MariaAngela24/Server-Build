from flask_sqlalchemy import SQLAlchemy

db = NoRedInk()



##############################################################################
# Model definitions

class Student(db.Model):
    """Student users"""

    __tablename__ = "students"

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #Fields below are examples of other data that may be recorded in this table
    #email = db.Column(db.String(64), nullable=True)
    #password = db.Column(db.String(64), nullable=True)
    #age = db.Column(db.Integer, nullable=True)
    #zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Student student_id=%s>" % (self.student_id)



class Question(db.Model):
    """Quiz questions"""

    __tablename__ = "questions"

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #Fields below are examples of other data that may be recorded in this table
    #prompt = db.Column(db.String(64), nullable=True)
    #correct_answer = db.Column(db.String(64), nullable=True)
    #type = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Question question_id=%s>" % (self.question_id)



class Student(db.Model):
    """Quiz questions"""

    __tablename__ = "questions"

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #Fields below are examples of other data that may be recorded in this table
    #prompt = db.Column(db.String(64), nullable=True)
    #correct_answer = db.Column(db.String(64), nullable=True)
    #type = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Question question_id=%s>" % (self.question_id)



class StudentQuestion(db.Model):
    """Association table for students and classes."""
    #Data from usage.csv file is in this table

    __tablename__ = "students_questions"

    student_question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.student_id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<StudentQuestion student_question_id=%s student_id=%s question_id=%s" % (self.student_question_id, self.student_id, self.question_id)

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    db.app = app
    db.init_app(app)

#TO DO: Posibly remove this
if __name__ == "__main__":
   

    from server import app
    connect_to_db(app)
    print "Connected to DB."
