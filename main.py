import re
from Place import Place
from Transaction import Transaction

places = [Place] * 20  
transactions = [Transaction] * 20
trans_count = 0
places_count = 0

def countobj(obj):
    count = 0
    for i in range(len(obj)):
        if obj[i].name != "":
            count += 1
    return count

def createplaces(line):
    if re.search(r'[0-9]', line):
            index = re.findall(r'[0-9]', line)
            for i in range(int(index[0])):
                places[i] = Place("L"+str(i+1))

def createtransactions(line):
    if re.search(r'[0-9]', line):
            index = re.findall(r'[0-9]', line)
            for i in range(int(index[0])):
                transactions[i] = Transaction("T"+str(i+1))

def addplacestotransactions(line):
    parts = re.split('(^.*)?\?', line)
    parts = re.split('(^.*)?\?', parts[2])
    plaace_numbers = re.findall(r'[0-9]', parts[0])
    for i in range(len(plaace_numbers)):
        plaace_numbers[i] = "L"+str(plaace_numbers[i])
    for i in range(countobj(transactions)):
        if line.find(transactions[i].name) != -1:
            for j in range(countobj(places)):
                for k in range(len(plaace_numbers)):
                    if places[j].name == plaace_numbers[k]:
                        transactions[i].addlocation(places[j])

def addmarks(line):
    marks = re.split('(^.*)?\?', line)
    place = re.findall(r'[0-9]', marks[1])
    place = "L"+place[0]
    marks = re.split('(^.*)?\?', marks[2])
    marks = int(marks[0])
    for i in range(countobj(places)):
        if places[i].name == place:
            places[i].addmark(marks)

def addsize(line):
    marks = re.split('(^.*)?\?', line)
    index = re.findall(r'[0-9]', marks[1])
    place = "L"+index[0]
    transaction = "T"+index[1]
    size = int(marks[2])
    print(size)
    for i in range(countobj(places)):
        if places[i].name == place:
            trans = places[i].gettransactions()
            for j in range(countobj(trans)):
                if trans[j].name == transaction:
                    trans[j].setsize(size)

def buildobjects(line):
    if line.find("A") != -1:
        createplaces(line)
    elif line.find("B") != -1:
        createtransactions(line)
    elif line.find("C") != -1:
        addplacestotransactions(line)
    elif line.find("D") != -1:
        addmarks(line)
    elif line.find("E") != -1:
        addsize(line)


#A Quantos lugares: 3
#B Quantas transicoes: 2
#C Quais são os lugares de entrada de T1? 1, 3
#C Quais são os lugares de entrada de T2? 2, 3
#D Quantas marcas em L1 ? 10
#D Quantas marcas em L2 ? 4
#D Quantas marcas em L3 ? 0
#E Qual o peso do arco de L1 para T1 ? 1
#E Qual o peso do arco de L3 para T1 ? 2




def readFile():
    with open("file.txt", 'r') as f:
        for line in f:
            buildobjects(line)

#    str = file.readlines(1)
#    print(str)

#    for i in range(3):
#        a = Place(4)
#        places[i] = a
#        places[i].printPlace()



#def getData():
    #receber dados do usuário

userinput = input("Digite 1 para buscar os dados do arquivo ou 2 para inserir manulamente: ")  

if userinput == "1":
    readFile()
elif userinput == "2":
    print("dois")
else:
    print("tres")
