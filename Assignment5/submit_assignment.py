import pytest
import Student
import System
import json


def test_submit_assignment(grading_system,student):
	
	course = 'databases'
	assignment_name = 'AssignmentX'
	submission = 'raet dna pir'
	submission_date = '3/20/2020'
	
	student.submit_assignment(course,assignment_name,submission,submission_date)
	
	with open('Data/users.json') as f:
		data = json.load(f)
		
	assert assignment_name in data[name][course]
	assert submission_date == data[name][course][assignment_name]['submission_date']
		
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
@pytest.fixture
def student():
	with open('Data/users.json') as f:
		data = json.load(f)
	stu = Student.Student('akend3',data,data['akend3']['courses'])
	return stu