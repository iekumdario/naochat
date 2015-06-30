filename=raw_input()
f=open(filename,'r')
p=["Inicio del Ciclo","Grabando","Grabacion finalizada","Conversion a flac","API Request","API Response","Brain Request","Brain Response","Ejecutando TTS"]
o=[0]*len(p)
for line in f:
	s=line.split(',')
	o[p.index(s[0])]+=1

for i in range(0,len(p)):
	print p[i]+' - '+str(o[i])