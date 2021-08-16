def status_method(password):
	score = 0
	if (len(password) > 8):
		score += 1
	if (password.lower() != password):
		score += 1
	if (not password.isalpha()):
		score += 1
	if (score == 3):
		return "Strong"
	elif (score == 2):
		return "Medium"
	else:
		return "Weak"