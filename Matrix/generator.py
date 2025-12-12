import random # цей файл є remnant of the past, тут раніше був код на 90 рядків, бо я пайтон тоді ще взагалі не знав. зараз тут все охайно переписано
def main(edgeprob, nodeamt): 
    edgeweightmax = 20 # максимальна вага ребра, можна змінювати
    matrix = [[0 for x in range(nodeamt)] for y in range(nodeamt)]
    i=0
    j=0

    while i!=nodeamt: # робимо повний граф
        j=0
        while j!=i:
            if random.random() < edgeprob: # додаємо шанс на недодання ребра в граф
                matrix[j][i]=random.randint(1,edgeweightmax) # якщо ребро додане, то даємо йому рандомну вагу
                matrix[i][j]=matrix[j][i] # симетрично відображаємо
            j+=1
        i+=1
    return(matrix)


