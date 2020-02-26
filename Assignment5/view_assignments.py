import pytest
import Student
import System
import json


def test_view_assignments(grading_system,student):
	
	course = 'databases'
	
	
	
	assignments1 = student.view_assignments(course)
	
	with open('Data/users.json') as f:
		data = json.load(f)
		
	course = student.all_courses[course]['assignments']
	assignments2 = []
	for key in course:
		assignments2.append([key,course[key]['due_date']])
		
	assert assignments1 == assignments2
		
		
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