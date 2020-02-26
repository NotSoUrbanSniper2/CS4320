import pytest
import Professor
import System
import json


def test_drop_student2(grading_system,professor):
	
	course = 'databases'
	name = 'akend3'
	
	
	professor.drop_student(name,course)
	
	with open('Data/users.json') as f:
		data = json.load(f)
		
	assert course in data[name]
	# course should not be dropped due to this professor not having access to the course
	# it is dropped though so the test fails
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
@pytest.fixture
def professor():
	with open('Data/users.json') as f:
		data = json.load(f)
	prof = Professor.Professor('saab',data,data['saab']['courses'])
	return prof