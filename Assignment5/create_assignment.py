import pytest
import Staff
import System
import json


def test_create_assignment(grading_system,staff):
	duedate = '1/1/2021'
	course = 'databases'
	assignment = 'assignmentX'
	
	
	staff.create_assignment(assignment,duedate,course)
	
	with open('Data/courses.json') as f:
		data = json.load(f)
		
	assert data[course]['assignment'] == assignment
		
	assert data[course][assignment]['due_date'] == duedate
		
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
@pytest.fixture
def staff():
	staff = Staff.Staff()
	return staff