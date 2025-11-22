import generator, os.path, sys
edgeprob=0.8
nodeamt=10
fileamt=1 #one less than u actually need
matrix=[]
fr, to, wt = generator.main(edgeprob, nodeamt)
def main_m():
    matrix = [[0 for x in range(nodeamt)] for y in range(nodeamt)]
    i=0
    j=0
    while i!=len(fr):
        a=fr[i]
        b=to[i]
        c=wt[i]
        matrix[a][b]=c
        i+=1
    return(matrix)



i=0
while i <= fileamt:
    matrix=main_m()
    directory=os.path.dirname(os.path.abspath(sys.argv[0]))
    name = f"matrix({i}).txt"
    name=os.path.join(directory, name)

    with open(name, 'w') as f:
        for row in matrix:
            text=",".join(map(str,row))
            f.write(text+"\n") 
    i+=1

i=0
j=0
k=0
zipd= list(zip(to,wt))
tempname=[]

def main_l():
    i=0
    j=0
    k=0
    tempname=[]
    output=""
    while i!=nodeamt:
        while j!=fr.count(i):
            tempname.append(zipd[k])
            j+=1
            k+=1

        rowa = ", ".join(map(str,tempname))
        output= f"{output}{i}:{{{rowa}}}\n"
            #    output= str(output,i,":{",rowa,"}", sep="")
        i+=1
        j=0
        tempname=[]
    return(output)

i=0
while i <= fileamt:
    result=main_l()
    directory=os.path.dirname(os.path.abspath(sys.argv[0]))
    name = f"list({i}).txt"
    name=os.path.join(directory, name)

    with open(name, 'w') as f:
        f.write(result)
    i+=1