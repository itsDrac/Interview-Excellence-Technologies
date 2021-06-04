from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
db = SQLAlchemy(app)


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tests = db.relationship('TestScore', backref='candidate', lazy=True)

class TestScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    candidate_id = db.Column('candidate_id', db.Integer, db.ForeignKey('candidate.id'))
    

@app.post('/add_candidate')
def add_candidate():
    candidate = request.get_json()
    if Candidate.query.filter_by(email=candidate['email']).first():
        return jsonify({'Message': 'Candidate with this email already exist'}), 401
    can = Candidate(name=candidate['name'], email=candidate['email']) 
    db.session.add(can)
    db.session.commit()
    return jsonify({'Message':'User Added', "id": can.id})

@app.get('/candidate')
def get_candidate():
    email = request.args.get('email')
    can = Candidate.query.filter_by(email=email).first_or_404()
    result = {'id': can.id, 'name': can.name, 'email': can.email}
    return jsonify(result)

@app.post('/add_score')
def add_score():
    data = request.get_json()
    candidate = Candidate.query.get_or_404(int(data['candidate_id']))
    test1 = TestScore(name=data['tests']['test_1']['name'],
                      score=data['tests']['test_1']['score'])
    test2 = TestScore(name=data['tests']['test_2']['name'],
                      score=data['tests']['test_2']['score'])
    test3 = TestScore(name=data['tests']['test_3']['name'],
                      score=data['tests']['test_3']['score'])
    tests = [test1, test2, test3]
    candidate.tests = tests
    db.session.add_all(tests)
    db.session.commit()
    return jsonify({'Message': f'tests added for {candidate.name}'})

@app.get('/highest_score')
def highest_score():
    candidates = Candidate.query.all()
    marks = {}
    for can in candidates:
        marks[can.id] = [ can.tests[0].score, can.tests[1].score, can.tests[2].score]

    can_id, high = highest(marks)
    can = Candidate.query.get(can_id)
    return jsonify({'Candidate id':can_id,'Candidate name':can.name,'marks':high})

def highest(marks):
    high = 0
    can_id = 0
    for id, mark in marks.items():
        if sum(mark)>high:
            high = sum(mark)
            can_id = id
    return can_id, high

@app.get('/average')
def find_average():
    candidates = Candidate.query.all()
    result = {}
    for can in candidates:
        result[can.name] = sum([ can.tests[0].score, can.tests[1].score, can.tests[2].score])/3

    return jsonify(result)


if __name__ == "__main__":
    app.run()

