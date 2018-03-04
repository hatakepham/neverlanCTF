f = open('file-20171020T1500','r')
import json
import operator

dc = {}
dc_n = {}

for l in f:
	j =json.loads(l) 
	# lay du lieu json
	scans = j["scans"]
	#lay du lieu scans
	# print scans,"\n"
	for i in scans:
		if scans[i]["detected"] == True:
			if i in dc.keys():
				dc[i] += 1
			else:
				dc[i] = 1
		elif scans[i]["detected"] == False:
			if i in dc_n.keys():
				dc_n[i] += 1
			else:
				dc_n[i] = 1	
d2 = {}
for i in dc.keys():
	d2[i] = float(dc[i]) / (dc[i] + dc_n[i])
d2 = sorted(d2.items(), key=operator.itemgetter(1))

for a,b in d2:
	print a,b