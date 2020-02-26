import pytest
import System
import json
import Student


def test_Student_Change_Grade(grading_system,student):
	username = 'akend3'
	course = 'databases'
	assignment = 'assignment1'
	grade =  '99'
	
	student.change_grade(username,course,assignment,grade)
	
	with open('Data/Users.json') as f:
		data = json.load(f)
		
	assert data[username][course][assignment]['grade'] == grade
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