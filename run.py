# run.py
import pytest
import sys

def main():

	'''
	This allows the tester to input positional arguments when calling both run.py and test_fizzbuzzpluzz.py
	'''

	pytest.main([sys.argv[1]])

if __name__ == '__main__':
	main()
