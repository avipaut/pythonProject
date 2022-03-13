import sqlite3 as sq


def arrangement():
	global type_
	while True:
		try:
			type_ = int(input())
			if type_ not in (1, 2, 3):
				raise ValueError
		except:
			print()
			continue
		break
	if type_ == 1:
		arrangement = 1
	elif type_ == 2:
		arrangement = 2
	elif type_ == 3:
		arrangement = 3
	return type_
