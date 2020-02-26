import pytest
import System
import json


def test_check_password(grading_system):
	username = 'akend3'
	password =  '123454321'
	grading_system.check_password(username,password)
	
	with open('Data/Users.json') as f:
		data = json.load(f)
		
	if(password == data[username]['password']):
		assert grading_system.check_password(username,password) == True
	elif(password != data[username]['password']):
		assert grading_system.check_password(username,password) == False
	password = '132454321'
	if(password == data[username]['password']):
		assert grading_system.check_password(username,password) == True
	elif(password != data[username]['password']):
		assert grading_system.check_password(username,password) == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
