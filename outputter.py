import generator, os.path, sys
edgeprob=0.5
nodeamt=20
fileamt=19 #one less than u actually need
matrix=[]

def gen():
    i=0
    while i <= fileamt:
        script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) #ai generated
        fname="data.py" # з'єднання файлів і маршруту до них - це робив ші, я тільки змінював назви (маленький гвинтік)
        full_path = os.path.join(script_directory, fname) #ai generated
        with open(full_path, 'r') as d: # загалом я дуже класний пограміст, і я не знаю як це можна було охайно зробити, тому я просто експортую необхідні значення кількості вершин і щільності в інший файл, а тут їх імпортую
            data = d.read() # прикольно шо воно автоматом імпортує його як список
        nodeamt=int(data.split()[0]) # і я можу одразу дістати те шо мені треба)
        edgeprob=float(data.split()[1])


        matrix=generator.main(edgeprob, nodeamt) # вконується генеатор матриці
        directory=os.path.dirname(os.path.abspath(sys.argv[0])) #ші
        name = f"matrix({i}).txt"
        name=os.path.join(directory, name) #ші

        with open(name, 'w') as f:
            for row in matrix: # виводжу матриці в окремий файл шоб красіво було і шоб можна було в будь який момент їх відкрити, перевірити, і впевнитися, що там все добре
                text=",".join(map(str,row))
                f.write(text+"\n") 
        i+=1
        
# а до речі причина існування цього файлу це той факт, що тут раніше був вивід і в списки суміжності, але через 5 днів після того як я це був зробив і йому скинув, Назар мені написав шо сам все переробив :)


def fileamty(): # не знаю чи воно ще десь використовується, але if it is not broken, don't touch it
    return(fileamt)