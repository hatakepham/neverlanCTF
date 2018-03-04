f = open("file_sum.txt","r")
f1 = open("temp_sum.txt","w")

import re
for line in f:
	line2 = re.sub(r'\s','\n',line)
	a=",qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
	for char in a:
		line2 = line2.replace(char,"")
	f1.write(line2)	

f.close()
f1.close() 