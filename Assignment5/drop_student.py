import pytest
import Professor
import System
import json


def test_drop_student(grading_system,professor):
	
	course = 'databases'
	name = 'akend3'
	
	
	professor.drop_student(name,course)
	
	with open('Data/users.json') as f:
		data = json.load(f)
		
	assert course not in data[name]
		
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