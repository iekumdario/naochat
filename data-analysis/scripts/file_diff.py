dates=[3,5,8,9,10,11,12,15,16,17,19]

for x in range(0,len(dates)-1):
	filename1=str(dates[x])+' de Junio.log'
	filename2=str(dates[x+1])+' de Junio.log'
	filenamer='results '+filename2
	f1=open(filename1,'r')
	f2=open(filename2,'r')
	file_out=open(filenamer,'a')
	for line2 in f2:
		line1=f1.readline()
		if not line1 or line1!=line2:
			file_out.write(line2)