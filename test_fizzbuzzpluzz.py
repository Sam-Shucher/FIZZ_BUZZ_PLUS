#test_fizzbuzzpluzz.py
import pytest
import fizzbuzzpluzz as FUZZ


# this test verifies that only positive numbers ( including zero) are valid for a defined range
def test_definingValidNumbers():
	if FUZZ.arg1 < 0:
		assert False

	if FUZZ.arg2 < 0:
		assert False

#TThis test verifies that the user inputs the beginning and end of the number range, defining it from a lower value to higher value
def test_CorrectArgPositions():
	if FUZZ.arg1 > FUZZ.arg2:
		assert False

#This test verifies that the user only provides 4 positional arguments ( arg0 through arg 3 )
def test_checkNumberOfArgs():
	if FUZZ.ArgRange != 4:
		assert False

#This test verifies that fizzbuzzpluzz.py is able to convert the data from the config JSON into data type 'dict'
def test_MatchTypeIsDict():
	if type(FUZZ.Match1) != dict:
		assert False

	if type(FUZZ.Match2) != dict:
		assert False

#This test verifies that match cases integer values are expected data type 'int'
def test_fizzbuzzpluzzInputValues():
	if type(FUZZ.M1_Val) != int:
		assert False
	if type(FUZZ.M2_Val) != int:
		assert False

#This test verifies that match cases keys are expected data type "str"
#this test will likely fail if you run the test with python 2

def test_fizzbuzzpluzzInputKeys():
	if type(FUZZ.M1_Key) != str:
		assert False

	if type(FUZZ.M2_Key) != str:
		assert False

