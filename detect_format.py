import re
import sys
import os
from pattern_match import *

# f.read(num_bytes = 1)
# f.seek(num_bytes, from_what = 0) 
# from_what flag is: 0 -> from beginning, 1 -> from current pos, 2 -> from end

def detect_pattern(filepath, patterns):
	f = open(filepath,'r')
	
	for p in patterns:
		print (p.pattern + "<<<")
		pat = p.pattern

		f.seek(0,0)
		line_num = 0
		for line in f.readlines():
			match = re.search(pat, line)
			if match:
				p.log_match(match, line_num)
				# print ("Line:" + line + "Match:" + match.group(0) + "<<<")
			line_num += 1


filename = sys.argv[1]
dir = os.path.dirname(__file__)

patterns = [PatternMatch("^\t+"), PatternMatch("^ +")]
detect_pattern(os.path.join(dir,filename), patterns)

for p in patterns:
	print ("Pattern: " + p.pattern)
	for m in p.matches:
		print("Match: " + str(m.line_num))
