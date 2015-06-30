dates=[3,5,8,9,10,11,12,15,16,17,19]
filenames=[]
ext='.csv'
for date in dates:
	filenames.append('results '+str(date)+' de Junio')
filenames.append('results '+'total')

for filename in filenames:

	f=open(filename+ext,'r')
	p=["Inicio del Ciclo","Grabando","Grabacion finalizada","Conversion a flac","API Request","API Response","Brain Request","Brain Response","Ejecutando TTS"]
	c1=[]
	c2=[]
	c3=[]
	c4=[]
	c5=[]
	c6=[]
	c7=[]
	c8=[]
	c9=[]

	for line in f:
		s=line.split(',')
		if s[0]==p[0]:
			c1.append(s[1].rstrip())
		elif s[0]==p[1]:
			c2.append(s[1].rstrip())
		elif s[0]==p[2]:
			c3.append(s[1].rstrip())
		elif s[0]==p[3]:
			c4.append(s[1].rstrip())
		elif s[0]==p[4]:
			c5.append(s[1].rstrip())
		elif s[0]==p[5]:
			c6.append(s[1].rstrip())
		elif s[0]==p[6]:
			c7.append(s[1].rstrip())
		elif s[0]==p[7]:
			c8.append(s[1].rstrip())
		elif s[0]==p[8]:
			c9.append(s[1].rstrip())

	fo=open(filename+' transposed'+ext,'a')
	sl=''
	for x in p:
		sl+=x+','
	else:
		sl+='\n'

	fo.write(sl)

	count=1
	i=0

	while True:
		if count > 925:
			break
		line=''
		if count <= len(c1):
			line+=c1[i]+','
		else:
			line+=','
		if count <= len(c2):
			line+=c2[i]+','
		else:
			line+=','
		if count <= len(c3):
			line+=c3[i]+','
		else:
			line+=','
		if count <= len(c4):
			line+=c4[i]+','
		else:
			line+=','
		if count <= len(c5):
			line+=c5[i]+','
		else:
			line+=','
		if count <= len(c6):
			line+=c6[i]+','
		else:
			line+=','
		if count <= len(c7):
			line+=c7[i]+','
		else:
			line+=','
		if count <= len(c8):
			line+=c8[i]+','
		else:
			line+=','
		if count <= len(c9):
			line+=c9[i]+','

		line+='\n'
		i+=1
		count+=1
		fo.write(line)
