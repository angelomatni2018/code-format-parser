import re
import sys
import os

# f.read(num_bytes = 1)
# f.seek(num_bytes, from_what = 0) 
# from_what flag is: 0 -> from beginning, 1 -> from current pos, 2 -> from end

def detect_pattern(filepath, patterns):
	pattern = ""
	
	f = open(filepath,'r')
	for line in f.readlines():
		for p in patterns:
			match = re.search(p, line)
			if match:
				print ("Line: " + line + "Match: " + match.group(0))

	return pattern

filename = sys.argv[1]
dir = os.path.dirname(__file__)
pattern = detect_pattern(os.path.join(dir,filename), ['\t', ' '])
print(pattern)

