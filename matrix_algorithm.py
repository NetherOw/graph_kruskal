import os, sys, math, time, outputter
def main(input):
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0])) #ai generated
    fname=f"matrix({input}).txt"
    full_path = os.path.join(script_directory, fname) #ai generated
    with open(full_path, 'r') as f: # імпорт даних з файліку
        matrix = f.read()

    matrixl= matrix.replace('\n', ',').split(',') #все в один рядочок, а після цього - в один список

    testmatr = []

    matrixla = [
        int(item.strip())  # Converts to integer after removing external spaces
        for item in matrixl #this piece is ai generated
        if item.strip()    # Filters out empty strings and strings with only spaces
    ]
    vertices = int(math.sqrt(len(matrixla))) # імпортувати цілу бібліотеку чисто для того щоб дуже неоптимізовано підрахуват кількість вершин

    j=0
    h=0
    o=0
    testmatr = [[0 for x in range(vertices)] for y in range(vertices)]
    treematr = [[0 for x in range(vertices)] for y in range(vertices)]

    while j!=(vertices):
        a=j
        while h!=(vertices): #...а потім це все ще менш оптимізовано перетворити в список з списків (себто матрицю)
            b=h
            o=a*vertices + b
            testmatr[a][b]=matrixla[o]
        
            h+=1
        h=0
        j+=1
    matrixla = [x for x in matrixla if x != 0] # а це мій список з усіх значень, але в рядочок, з нього я прибраю нулі, аби потім знайти мінімум. Чи можна було це зробити через set()? еммм, нуууу

    j=0
    h=0

    i=0
    while i!=vertices:
        while j!=vertices:
            if testmatr[i][j] ==0: # тут мабуть пора розповісти про самі матриці. testmatr (ім'я, яке після вдалих тестів я ніколи не змінював) - це початкова матриця всіх значень. В ній я буду змінювати ребра, які додав, на "а", щоб потім, вирівнявши в рядочок, легко було шукати мінімум
                testmatr[i][j]='a' # знову ж таки, чи можна було б це все зробити оптимізованіше? абсолютно. Але у мене 3 дедлайна по проєктах на цьому тижні :sob:
            j+=1
        j=0
        i+=1
    i=0
    j=0

    lsets=[]
    while i != vertices: # о а це до речі цікаво. перший тиждень я вбив на те щоб реалізувати алгоритм, перевіряючи списки один з одни. другий тиждень - намагався зробити типу dfs
        lsets.append({i}) # а потім Назар сказав мені як це має бути, і я його зробив за майже рівно 2 години. навчіть мене вчитися і проводити ресьорч перед тим як шось робити :sob::sob:
        i+=1

    i=0 
    while i!=vertices-1: # дорогий мій цикл. скільки я тут просидів... Більше половини часу, витраченого на цей проєкт, вбив я саме тут.
        if len(matrixla)==0:
            break # failsafe #1, я не знаю чи він працює навіть чи ні, але я знаю що всі failsafeи разом, на диво, таки працюють
        minar=min(matrixla)  # тут ми шукаємо значення ваги тієї грані, яку нам треба додати, себто мінімум
        j=0
        h=0
        l=0
        while j!=vertices:
            while h!=vertices:
                if minar ==testmatr[j][h]: # для першого елементу в матриці, який дорівню нашому мінімуму:
                    l=0
                    while l != len(lsets): # перевіряємо множини
                        if j in lsets[l]:
                            jj=lsets[l]
                        if h in lsets[l]: # задаємо тимчасові змінні для перевірки на цикл
                            hh=lsets[l]
                        l+=1
                    if len(hh|jj)==len(hh)+len(jj): # якщо сума потужності утвореної множини (об'єднання графів) є сумою потужностей графів до об'єднання, то: 
                        k=0
                        while k!=len(lsets):
                            if j in lsets[k] or h in lsets[k]:
                                lsets[k]=jj|hh #...власне об'єднуємо ці множини
                            k+=1
                        k=0
                        while k!=len(lsets): # тут я думаю варто пояснити як це все працює. ми створюємо 2 копії об'єднаної множини, а далі ще раз перевіряємо всі множини, щоб знайти першу, яка є тією множиною, яку ми створли
                            if h in lsets[k]:
                                lsets.remove(lsets[k])  # ...а далі прибираємо її
                                break # failsafe #2
                            elif j in lsets[k]:
                                lsets.remove(lsets[k])
                                break # failsafe #2
                            k+=1
                        treematr[j][h]=testmatr[j][h]  # treematr це якраз матриця нашого дерева, те, що треба
                        treematr[h][j]=testmatr[j][h]  # ну і власне якщо ми довели, що ребро додати можна, то додаємо його
                    testmatr[j][h]='a'  # замінюємо в оригінальній матриці значення, щоб не враховувати їх до мінімуму
                    testmatr[h][j]='a'
                    j=vertices-1  # fun fact: я не знаю чому я скидую лічильники до цього значення, а не до нуля. я робочий цикл був написав ще на самому початку, кілька тижнів тому, а далі... а далі було те, що я описував вище
                    h=vertices-1  
                h+=1
            h=j # стоп а де четвертий failsafe, їх ж тут було більше
            j+=1
        matrixla.remove(minar)  # при... -бираємо значення мінімум в списку... стоп, а нащо-... як працює мій код :sob::sob::sob:
        matrixla.remove(minar)
        i+=1
    return(treematr)








def res():
    timelapsd = 0
    i=0
    totaltime=0   
    outputter.gen()  # генеруємо значення
    while i!=20: # я на кожну пару значеннь (вершини, щільність) роблю 20 по 20 тестів. Чому саме так? Чому 400, якщо сказано 100? Чому ви все ще шукаєте логіку в моїх діях? :sob:

        timea = time.perf_counter() #засікаємо час
        matrixe=main(i)  # робимо алгоритм
        timeb = time.perf_counter()
        timelapsd=timelapsd-timea+timeb # рахуємо час
        directory=os.path.dirname(os.path.abspath(sys.argv[0])) # ші
        name = f"matrix_tre({i}).txt" # це, до речі, я сам писав, я памєнтаю
        name=os.path.join(directory, name) # ші
        with open(name, 'w') as w: # виводимо саме дерево в інший файл - до речі так можна легко впевнитися що це саме дерево, просто вставивши його в сайтик
            for r in matrixe:
                text=",".join(map(str,r))
                w.write(text+"\n") 
        i+=1
    timelapsd=timelapsd/i  # ділимо сумарне значення часу на кількість виконань
    return(timelapsd)
    







