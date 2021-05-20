import json, re
import os

def remove_comment(path,returnType='str',returnFilePath='./'):
	if os.path.isfile(path):
		result = ''
		with open(,'r') as dr:
			for line in dr:
				#result += re.sub('//.*','',line,flags=re.MULTILINE)
				result += re.sub('//.*','',line,flags=re.MULTILINE)
		print(result)
		if str(returnType).lower()=='str':
			return result
		# TBD add return to file 	
	else:
		print(f'ERR : Wrong file path : {path}')
		return -1
		
	### TBD make this module to function
	###     add option for python comment('#') and etcs...
