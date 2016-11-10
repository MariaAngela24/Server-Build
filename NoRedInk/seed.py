"""Utility file to seed database from sample data in seed_data"""

from sqlalchemy import func

from model import Student, Question, StudentQuestion, Strand, Standard

from server import app



def load_questions():
    for i, row in enumerate(open("seed_data/u.question.tsv")):
        row = row.rstrip()
        question_id, difficulty = row.split("\t")
        question = Question(question_id=question_id,
                            difficulty=difficulty)
                                              
        db.session.add(question)
        db.session.commit()



def load_students():
    """Load students from u.student into database."""

    print "Students"

    for i, row in enumerate(open("seed_data/u.student.tsv")):
        row = row.rstrip()
        student_id, difficulty = row.split("\t")
        student = Student(student_id=student_id)
                                              
        db.session.add(student)
        db.session.commit()

#Am running out of time and want to work on server file so am not
#going to finish loading the the rest of the seed data.




if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_questions()
    load_students()
    
