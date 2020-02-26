import pytest
import System

#login fails due to missing information

def test_login(grading_system):
	username = ''
	password =  ''
	grading_system.login(username,password)
	

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
