import pytest
import Staff
import System
import json


def test_change_grade(grading_system,staff):
	username = 'akend3'
	course = 'databases'
	assignment = 'assignment1'
	grade =  '99'
	
	staff.change_grade(username,course,assignment,grade)
	
	with open('Data/Users.json') as f:
		data = json.load(f)
		
	assert data[username][course][assignment]['grade'] == grade
		
	
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
@pytest.fixture
def staff():
	staff = Staff.Staff()
	return staff