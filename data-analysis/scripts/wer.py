#!/usr/bin/env python

def wer(r, h):
    """
        Calculation of WER with Levenshtein distance.
        Works only for iterables up to 254 elements (uint8).
        O(nm) time ans space complexity.

        >>> wer("who is there".split(), "is there".split()) 
        1
        >>> wer("who is there".split(), "".split()) 
        3
        >>> wer("".split(), "who is there".split()) 
        3
    """
    # initialisation
    import numpy
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8)
    d = d.reshape((len(r)+1, len(h)+1))
    for i in range(len(r)+1):
        for j in range(len(h)+1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(r)+1):
        for j in range(1, len(h)+1):
            if r[i-1] == h[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                substitution = d[i-1][j-1] + 1
                insertion    = d[i][j-1] + 1
                deletion     = d[i-1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    return d[len(r)][len(h)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# r es la referencia transcrita manualmente del audio grabado
# h es la pregunta capturada por el stt y entrada del chatbot
# w es el word error rate
# c es el confidence
# a es la respuesta del bot
# cer es el concept error rate

output_file_overall=open('results overall.tsv','a')
for x in range(1,33):
    output_file_subject=open('results sujeto '+str(x)+'.tsv','a')
    for y in range(1,3):
        output_file_test=open('results prueba '+str(y)+'.tsv','a')
        input_file_name='sujeto '+str(x)+' - prueba '+str(y)
        input_file=open(input_file_name,'r')
        output_file_name='results '+input_file_name+'.tsv'
        output_file=open(output_file_name,'a')
        count=0
        for line in input_file:
            try:
                parts=line.split("\t")
                current=parts[0]
                if current == 'r':
                    r=parts[1].rstrip()
                elif current == 'h':
                    c=parts[1]
                    h=parts[2].rstrip()
                elif current == 'a':
                    a=parts[1].rstrip()
                elif current == 'c':
                    cer=parts[1].rstrip()
                    count+=1
                    if r and h and c and str(cer):
                        if h=="ERROR":
                            h=''
                        w=wer(r,h)
                        result=str(count)+'\t'+r+'\t'+h+'\t'+str(w)+'\t'+str(c)+'\t'+a+'\t'+str(cer)
                        result+="\n"
                        output_file.write(result)
                        output_file_subject.write(result)
                        output_file_test.write(result)
                        output_file_overall.write(result)
            except ValueError:
                print "hubo un error con el archivo "+input_file_name
        input_file.close()
        output_file.close()
        output_file_test.close()
    output_file_subject.close()
output_file_overall.close()