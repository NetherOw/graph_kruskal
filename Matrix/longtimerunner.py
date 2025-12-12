import matrix_algorithm, os, sys

i=5
longi=i # ахпхахпахпха я думав я хоч трішки навчився програмувати за цей весь час, але чого я це зробив саме так :sob:
j=0

nodes=[190,200]  # сюди можна вписати всі значення кількості вершин для перевірки
dens=[0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1]  # а сюди - значення ваги
testvaluesvert=[]
testvaluesdens=[]
k=0
while k!=len(nodes):
    h=0
    while h!=len(dens):
        testvaluesvert.append(nodes[k])  # і воно зробить комбінацію всіх значень (декартовий добуток, Я ЗНАЮ НАЩО Я ВЧУ ДИСКРЕТКУ, ЩОБ ТУТ Я МІГ СКАЗАТИ ЩО ЦЕ - ДЕКАРТОВИЙ ДОБУТОК!!!)
        testvaluesdens.append(dens[h])  # *кхм кхм* жартую
        h+=1
    k+=1
print(testvaluesvert)
print(testvaluesdens)

while j!=len(testvaluesvert):  # цикл який працює на всі значення декартового добутку
    t=0
    i=longi
    while i!=0:

        directory=os.path.dirname(os.path.abspath(sys.argv[0])) # mandatory ші mention
        name = "data.py"
        name=os.path.join(directory, name) # і тут теж ші

        with open(name, 'w') as f:
            text=str(testvaluesvert[j])+' '+str(testvaluesdens[j])
            f.write(text)  # чи я його зробив дуже криво? так. чи воно працює? теж так. тому так.
        i-=1



        t=matrix_algorithm.res()+t  # додаю час
        print(i)
    time=t/longi  # і розділяю його на кількість повторів ще й тут
    print(testvaluesvert[j],testvaluesdens[j],time,sep=', ')  # це щоб бачить шо воно реально працює в реальному часі
    directory=os.path.dirname(os.path.abspath(sys.argv[0])) # ши
    name = "output.csv"
    name=os.path.join(directory, name) # ші

    with open(name, 'a') as o: # ну тут наче все ясно, я краще поясню чому я зберігаю текст в .py. річ в тім, що я таким чином можу легко відсортувати за типами файлів, і видалити всі виводи, які зберігаються в .txt
        text=str(str(testvaluesvert[j])+', '+str(testvaluesdens[j])+', '+str(time)+'\n')
        o.write(text)
    i-=1
    j+=1