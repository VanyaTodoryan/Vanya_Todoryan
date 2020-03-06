# імпоруєм необхідні бібліотеки
import random
print("Вітаю в грі хрестики нолики!")
# створюжм список який буде складатися з клітинок ігрового поля
nomerCell=[1,2,3,
           4,5,6,
           7,8,9]
# просим вибрати користувача ігровий режим
gamemode=input("Виберіть з ким хочете грати 1-два гравця 2-бот: ")
# перевіряєм правильність ведення ігрового режиму
if gamemode not in "12":
    while True:
        print("Ви ввели неправельне значення, спробуйте щераз!")
        gamemode=input("Виберіть з ким хочете грати 1-два гравця 2-бот: ")
        if gamemode in "12":
            break
# перетворюєм в цілочисельний
gamemode=int(gamemode)
# перевіряєм ігровий режим та просим користувача вести фігур якою буде грати з ботом
if gamemode==2:
    fig=input("Виберіть чим будете грати 1-хрестик 2-нолик: ")
    if fig not in "12":
        while True:
            print("Ви ввели неправельне значення, спробуйте щераз!")
            fig=input("Виберіть чим будете грати 1-хрестик 2-нолик: ")
            if fig in "12":
                break
else:
    fig=0
# перетворюєм в цілочисельне значення
fig=int(fig)
def prostofunc(c,x,o,i):
    while True:
        a = random.randint(0, 8)
        if c[a] !=o and c[a]!=x :
            c[a]=x
            # print("Хід номер ",i)
            # Visual(c)
            return "X"
            if winner(c,"X") ==1:
                return 1
            break
# створюєм функію яка буде містити в собі "І.І."
def clv(c,cell,x,o,i):
    if c[0]==o and c[1]==o:
        if cell[2] !=o and cell[2]!=x :
            return 2
        else:
            prostofunc(cell,x,o,i)
    elif c[0]==o and c[2]==o:
        if cell[1] !=o and cell[1]!=x :
            return 1
        else:
            prostofunc(cell,x,o,i)
    elif c[1]==o and c[2]==o:
        if cell[0] !=o and cell[0]!=x :
            return 0
        else:
            prostofunc(cell,x,o,i)

    elif c[3]==o and c[4]==o:
        if cell[5] !=o and cell[5]!=x :
            return 5
        else:
            prostofunc(cell,x,o,i)
    elif c[3]==o and c[5]==o:
        if cell[4] !=o and cell[4]!=x :
            return 4
        else:
            prostofunc(cell,x,o,i)
    elif c[4]==o and c[5]==o:
        if cell[3] !=o and cell[3]!=x :
            return 3
        else:
            prostofunc(cell,x,o,i)

    elif c[6]==o and c[7]==o:
        if cell[8] !=o and cell[8]!=x :
            return 8
        else:
            prostofunc(cell,x,o,i)
    elif c[6]==o and c[8]==o:
        if cell[7] !=o and cell[7]!=x :
            return 7
        else:
            prostofunc(cell,x,o,i)
    elif c[7]==o and c[8]==o:
        if cell[6] !=o and cell[6]!=x :
            return 6
        else:
            prostofunc(cell,x,o,i)

    elif c[0]==o and c[3]==x:
        if cell[6] !=o and cell[6]!=x :
            return 6
        else:
            prostofunc(cell,x,o,i)
    elif c[3]==o and c[6]==o:
        if cell[0] !=o and cell[0]!=x :
            return 0
        else:
            prostofunc(cell,x,o,i)
    elif c[6]==o and c[0]==o:
        if cell[3] !=o and cell[3]!=x :
            return 3
        else:
            prostofunc(cell,x,o,i)

    elif c[1]==o and c[4]==o:
        if cell[7] !=o and cell[7]!=x :
            return 7
        else:
            prostofunc(cell,x,o,i)

    elif c[4]==o and c[7]==o:
        if cell[1] !=o and cell[1]!=x :
            return 1
        else:
            prostofunc(cell,x,o,i)
    elif c[1]==o and c[7]==o:
        if cell[4] !=o and cell[4]!=x :
            return 4
        else:
            prostofunc(cell,x,o,i)

    elif c[2]==o and c[5]==o:
        if cell[8] !=o and cell[8]!=x :
            return 8
        else:
            prostofunc(cell,x,o,i)
    elif c[2]==o and c[8]==o:
        if cell[5] !=o and cell[5]!=x :
            return 5
        else:
            prostofunc(cell,x,o,i)
    elif c[5]==o and c[8]==o:
        if cell[2] !=o and cell[2]!=x :
            return 2
        else:
            prostofunc(cell,x,o,i)

    elif c[4]==o and c[8]==o:
        if cell[0] !=o and cell[0]!=x :
            return 0
        else:
            prostofunc(cell,x,o,i)
    elif c[0]==o and c[4]==o:
        if cell[8] !=o and cell[8]!=x :
            return 8
        else:
            prostofunc(cell,x,o,i)
    elif c[0]==o and c[8]==o:
        if cell[4] !=o and cell[4]!=x :
            return 4
        else:
            prostofunc(cell,x,o,i)

    elif c[2]==o and c[4]==o:
        if cell[6] !=o and cell[6]!=x :
            return 6
        else:
            prostofunc(cell,x,o,i)
    elif c[2]==o and c[6]==o:
        if cell[4] !=o and cell[4]!=x :
            return 4
        else:
            prostofunc(cell,x,o,i)
    elif c[4]==o and c[6]==o:
        if cell[2] !=o and cell[2]!=x :
            return 2
        else:
            prostofunc(cell,x,o,i)
    else:
        while True:
            a = random.randint(0, 8)
            if c[a] !=o and c[a]!=x :
                c[a]=x
                print("Хід номер ",i)
                Visual(c)
                return x
                if winner(c,"X") ==1:
                    return 1
                break

# створюєм функію яка буде перевіряти перемогу
def winner(cell,a):
    if cell[0] == a and cell[1] == a and cell[2] == a or \
    cell[3] == a and cell[4] == a and cell[5] == a or \
    cell[6] == a and cell[7] == a and cell[8] == a or \
    cell[0] == a and cell[3] == a and cell[6] == a or \
    cell[1] == a and cell[4] == a and cell[7] == a or \
    cell[2] == a and cell[5] == a and cell[8] == a or \
    cell[0] == a and cell[4] == a and cell[8] == a or \
    cell[2] == a and cell[4] == a and cell[6] == a:
        if a=="X":
            return 1
        elif a=="O":
            return 2
        else:
            return 0
# створюєм функцію яка буде виводи "дизайн"
def Visual(cell):
    for i in range(3):
        print("+",end="")
        for i1 in range(3):
            print(" - - - - - +",end="")
        print()
        if i==1:
            i=3
        elif i==2:
            i=6
        print("|           |           |           |")
        print("|    ",cell[i],"    |    ",cell[i+1],"    |    ",cell[i+2],"    |")
        print("|           |           |           |")
    print("+",end="")
    for i1 in range(3):
         print(" - - - - - +",end="")
    print()

# створюєм функцю яка буде тримати в собі код гри з ботом
def PlayWithComputer(cell,f):
    b="123456789"
    Visual(cell)

    if f==2:
        print("Хід номер 1")
        cell[4]="X"
        Visual(cell)
        for i in range(2,10):
            if i%2!=0:
                while True:
                    a = random.randint(0, 8)
                    if cell[a] !="O" and cell[a]!="X" :
                        cell[a]="X"
                        print("Хід номер ",i)
                        Visual(cell)
                        if winner(cell,"X") ==1:
                            return 1
                        break
            else:
                while True:
                    a=int(input("Ведіть номер клітинки: "))
                    if cell[a-1] !="O" and cell[a-1]!="X" :
                        cell[a-1]="O"
                        print("Хід номер ", i)
                        Visual(cell)
                        if winner(cell,"O") == 2:
                            return 2
                        break
                    else:
                        print("Клітнка зайнята, пробуйте іншу!")
    else:
        for i in range(1,10):
            if i%2==0:
                while True:
                    a = random.randint(0, 8)
                    if cell[a] !="O" and cell[a]!="X" :
                        cell[a]="O"
                        print("Хід номер ",i)
                        Visual(cell)
                        if winner(cell,"O") == 2:
                            return 1
                        break
            else:
                while True:
                    a=int(input("Ведіть номер клітинки: "))
                    if cell[a-1] !="O" and cell[a-1]!="X" :
                        cell[a-1]="X"
                        print("Хід номер ", i)
                        Visual(cell)
                        if winner(cell,"X") == 1:
                            return 2
                        break
                    else:
                        print("Клітнка зайнята, пробуйте іншу!")
# створєм функцю яка буде тримати в собі код гри двох гравців
def TwoPlayerGame(cell,f):
    Visual(cell)
    for i in range(1,10):
        if i%2==0:
            while True:
                a=int(input("Хід гравця номер 2 (О) ,ведіть номер клітинки: "))
                if cell[a-1] !="O" and cell[a-1]!="X" :
                    cell[a-1]="O"
                    print("Хід номер ", i)
                    Visual(cell)
                    if winner(cell,"O") == 2:
                        return 2
                    break
                else:
                    print("Клітнка зайнята, пробуйте іншу!")
        else:
            while True:
                a=int(input("Хід гравця номер 1 (Х) ,введіть номер клітинки: "))
                if cell[a-1] !="O" and cell[a-1]!="X" :
                    cell[a-1]="X"
                    print("Хід номер ", i)
                    Visual(cell)
                    if winner(cell,"X") == 1:
                        return 1
                    break
                else:
                    print("Клітнка зайнята, пробуйте іншу!")
# перевіряєм режим гри та викликаєм функцію
if gamemode==2:
    a=PlayWithComputer(nomerCell,fig)
    if a==1:
        print("Ви програли!")
    elif a==2:
        print("Ви виграли!")
    else:
        print("Нічія!")
else:
    a=TwoPlayerGame(nomerCell,fig)
    if a==1:
        print("Переміг гравець номер 1!")
    elif a==2:
        print("Переміг граіець номер 2!")
    else:
        print("Нічія!")
input()
