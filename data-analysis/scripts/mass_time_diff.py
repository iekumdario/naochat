from datetime import datetime
from inspect import currentframe, getframeinfo
import time
import re

def time_diff(start, end):
    start_dt = datetime.strptime(start, '%H:%M:%S.%f')
    end_dt = datetime.strptime(end, '%H:%M:%S.%f')
    diff = (end_dt - start_dt)
    return diff.total_seconds()

dates=[3,5,8,9,10,11,12,15,16,17,19]
filenames=[]
ext_in='.log'
ext_out='.csv'
for date in dates:
	filenames.append(str(date)+' de Junio')
filenames.append('total')

for filename in filenames:
	f=open(filename+ext_in,'r')
	file_out=open('results '+filename+ext_out,'a')
	count=0
	timere=re.compile(r'([0-9]:*|(?:\d*\.)?\d+)')
	for line in f:
		m=timere.findall(line)

		if not m:
			count=0
			continue

		sline=line.split(',')

		if count==0:
			a=sline[0]
			pname=sline[1].rstrip()
			count+=1
		else:
			b=sline[0]
			result=str(time_diff(a,b))
			file_out.write(pname+','+result+"\n")
			a=b
			pname=sline[1].rstrip()

	f.close()
	file_out.close()