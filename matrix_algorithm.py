import os, sys, math

script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) #ai generated

def main():
    i=0
    fname="matrix(0).txt"
    full_path = os.path.join(script_directory, fname) #ai generated
    with open(full_path, 'r') as f:
        matrix = f.read()
    
    matrixl= matrix.replace('\n', ',').split(',')



    matrixla = [
            int(item.strip())  # Converts to integer after removing external spaces
            for item in matrixl #this piece is ai generated
            if item.strip()    # Filters out empty strings and strings with only spaces
        ]

    vertices = int(math.sqrt(len(matrixla)))
    testmatr = []
    j=0
    h=0
    o=0
    testmatr = [[0 for x in range(vertices)] for y in range(vertices)]
    treematr = [[0 for x in range(vertices)] for y in range(vertices)]
    while j!=(vertices):
        a=j
        while h!=(vertices):
            b=h
            o=a*5+b
            testmatr[a][b]=matrixla[o]
        
            h+=1
        h=0
        j+=1
    matrixla = [x for x in matrixla if x != 0]

    j=0
    h=0
    result = []
    # while i != (vertices):
    #     minar=min(matrixla)
    #     print(minar)
    #     matrixla.remove(minar)
    #     matrixla.remove(minar)
    #     if j!=1:
    #         while h!=vertices:
    #             if minar!=testmatr[i][h]:
    #                 i+=1
                

    #             h+=1
    #     i+=1
    i=0
    while i!=vertices:
        while j!=vertices:
            if testmatr[i][j] ==0:
                testmatr[i][j]='a'
            j+=1
        j=0
        i+=1
    i=0
    j=0
    nodearray=[]
    while i!=vertices:
        minar=min(matrixla)


        j=0
        h=0
        while j!=vertices:
            while h!=vertices:
                if minar ==testmatr[j][h]:
                    if nodearray.count(j) ==0 or nodearray.count(h)==0:
                        i+=1
                        
                        treematr[j][h]=testmatr[j][h]
                        treematr[h][j]=testmatr[j][h]
                    testmatr[j][h]='a'
                    testmatr[h][j]='a'
                    print(i,j,h,minar,treematr[j][h],treematr)
                    j=vertices-1
                    h=vertices-1
                h+=1
            h=0
            j+=1
        matrixla.remove(minar)
        matrixla.remove(minar)
    print(treematr)






    

main()