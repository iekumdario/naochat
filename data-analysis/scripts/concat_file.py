dates=[3,5,8,9,10,11,12,15,16,17,19]

file_out=open('total.log','a')
for x in range(0,len(dates)):
	filename=str(dates[x])+' de Junio.log'
	f=open(filename,'r')
	for line in f:
		file_out.write(line)
	f.close()
	file_out.write('\n')
file_out.close()