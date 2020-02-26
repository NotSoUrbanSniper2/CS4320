import pytest
import Student
import System
import json
from datetime import datetime

def test_check_ontime(grading_system,student):
	
	
	assignmentToCheck = 'assignment1'
	course = 'cloud_computing'
	
	
	with open('Data/users.json') as f:
		data1 = json.load(f)
	with open('Data/courses.json') as f:
		data2 = json.load(f)
		
	date1 = data1[student.name]['courses'][course][assignmentToCheck]['submission_date']
	date2= data2[course]['assignments'][assignmentToCheck]['due_date']
	test = student.check_ontime(data1[student.name]['courses'][course][assignmentToCheck]['submission_date'],data2[course]['assignments'][assignmentToCheck]['due_date'])
	date1A = datetime.strptime(date1, '%m/%d/%y')
	date2A = datetime.strptime(date2, '%m/%d/%y')
	if (date1A <= date2A):
		assert test == True
	else :
		assert test == False
		
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
	
@pytest.fixture
def student():
	with open('Data/users.json') as f:
		data = json.load(f)
	stu = Student.Student('hdjsr7',data,data['akend3']['courses'])
	return stu