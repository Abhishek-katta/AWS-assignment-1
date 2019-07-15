from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/student', methods=['POST'])
def insert_student():
    new_student = request.get_json()
    return 'Insert Student data: %s' % new_student['name']

@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    return 'Get Student data with ID: %s' % student_id

@app.route('/student', methods=['PUT'])
def update_student():
    updated_student = request.get_json()
    return 'Update Student data: %s' % updated_student['name']

@app.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    return 'Delete Student data with ID: %s' % student_id
