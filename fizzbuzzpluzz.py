#fizzbuzzpluzz.py
import sys
import json
import pytest

#setting MasterList equal to an empty list to use later for testing
MasterList =[]

# storing positional args
Frange = sys.argv
ArgRange = len(Frange)

# This ensures that the positional args are type 'int',
# as we only expect integers to be input for the positional args

arg1 = int(Frange[2])
arg2 = int(Frange[3])

#In order to make fizzbuzzpuzz "inclusive" with respect to the range given,
# we must create inclusiveArg2

inclusiveArg2 = (arg2 + 1)


# Used to get JSON file:
with open('./fbp-config.json') as G:
	data = json.load(G)

MatchList1 = data["MatchOne"]
MatchList2 = data["MatchTwo"]


def Convert(lst): 
	"""
	This function converts the list we get from the JSON file,
	and converts it into a dictionary to be used later in the script.
	"""

	res_dct = {lst[x]: lst[x + 1] for x in range(0, len(lst), 2)} 
	return res_dct 


# this is where match1 and match2 get converted
Match1 = (Convert(MatchList1))
Match2 = (Convert(MatchList2))

# boil down match1 and match2 to be able to use their the values for their respective key pairs

def Match1KV():
	"""
	This function takes the dictionary information from MatchOne and
	allows us to use the information in the key or the value without
	having call a reference to the dictionary.
	
	"""

	for key, value in Match1.items():
		Match1KV.M1key = key
		Match1KV.M1Val = value


def Match2KV():

	"""
	This function takes the dictionary information from MatchTwo and
	allows us to use the information in the key or the value without
	having call a reference to the dictionary.
	
	"""

	for key, value in Match2.items():
		Match2KV.M2key = key
		Match2KV.M2Val = value
		
# this run the above functions to be able to use the boiled down values from the config JSON files
Match1KV()
Match2KV()

#assigning variables to be used in fizzbuzzpluzz logic
M1_Key = Match1KV.M1key
M1_Val = Match1KV.M1Val
M2_Key = Match2KV.M2key
M2_Val = Match2KV.M2Val

# logic for printing out fizz, buzz, or any other name listed in the config file,
# along with its associated value

def fizzbuzzpluzz(k):

	"""
	This function uses the information accessed in the JSON config to determine
	when one of the numbers selected in the JSON congif is called as well as what word to
	output as specified by the JSON config

	This function also handles the condition when a number in the range meets both conditions.

	"""

	if k % M1_Val == 0 and k % M2_Val == 0 :
		return M1_Key + M2_Key
	elif k % M1_Val == 0:
		return M1_Key
	elif k % M2_Val == 0:
		return M2_Key
	else:
		return str(k)


#prints the range of values, inputting fizz, buzz, or any other name listed in the config file
print("\n".join(fizzbuzzpluzz(k) for k in range(arg1, inclusiveArg2) ))
