import pytest
import Professor
import System
import json


def test_add_student(grading_system,professor):
	
	course = 'databases'
	name = 'StudentX'
	
	
	professor.add_student(name,course)
	
	with open('Data/users.json') as f:
		data = json.load(f)
		
	assert data[name] != NULL
		
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
@pytest.fixture
def professor():
	with open('Data/users.json') as f:
		data = json.load(f)
	prof = Professor.Professor('goggins',data,data['goggins']['courses'])
	return prof