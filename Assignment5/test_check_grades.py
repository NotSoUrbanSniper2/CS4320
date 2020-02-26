import pytest
import Student
import System
import json


def test_check_grades(grading_system,student):
	
	course = 'databases'
	
	
	
	grades = student.check_grades(course)
	
	with open('Data/users.json') as f:
		data = json.load(f)
	assignments = student.users[student.name]['courses'][course]
	for i in grades:
		for key in assignments:
			assert ([key, assignments[key]['grade']] in grades)
		
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