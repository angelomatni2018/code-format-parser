class MatchEntry:
	# match object
	match_obj = None

	# line of string match
	line_num = -1

	# number of repetitions in matched string
	num_reps = 0

	def __init__(self, m_obj, line, reps):
		self.match_obj = m_obj
		self.line_num = line
		self.num_reps = reps

class PatternMatch:
	# regex pattern
	pattern = ""

	# list of MatchEntry for each match found
	matches = None

	def __init__(self, p):
		self.matches = []
		self.pattern = p

	def log_match(self, match_obj, line_num):
		span = match_obj.span()
		num_reps = span[1] - span[0]
		self.matches.append(MatchEntry(match_obj, line_num, num_reps))
		print(len(self.matches))
