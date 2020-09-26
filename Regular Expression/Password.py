import re 
password = input()
s = True
while s: 
	if (len(password)<6): 
	    break
	elif not re.search("[a-z]", password): 
	    break
	elif not re.search("[A-Z]", password): 
	    break
	elif not re.search("[0-9]", password): 
	    break
	elif not re.search("[!@$#&]", password): 
	    break
	else:
		s=0
		print("password is valid")
		break
if s:
	print("password is invalid")
