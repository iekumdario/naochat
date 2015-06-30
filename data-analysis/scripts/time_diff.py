from datetime import datetime
from inspect import currentframe, getframeinfo
import time
import re

def time_diff(start, end):
    start_dt = datetime.strptime(start, '%H:%M:%S.%f')
    end_dt = datetime.strptime(end, '%H:%M:%S.%f')
    diff = (end_dt - start_dt)
    return diff.total_seconds()

f=open('exelog','r')
f2=open('results','a')
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
		print pname+','+result
		f2.write(pname+','+result+"\n")
		a=b
		pname=sline[1].rstrip()

f.close()
f2.close()