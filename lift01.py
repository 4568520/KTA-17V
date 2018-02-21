class Cabine:
    stage=1 # номер этажа
    direction=0 # 1 - вверх, -1 - вниз, 0 - стоп
    status="free" # free - свободен, order - заказан

class CabineButton:
    status=False # нажата или нет кнопка
    stage=1 # номер этажа, который обозначает данная кнопка

class StageButton:
    status=False # нажата или нет кнопка
    stage=1 # номер этажа, который обозначает данная кнопка
    direction=0 # 1 - вверх, -1 - вниз, 0 - не активная

theCabine=Cabine() # создали объект класса Cabine
'''print(theCabine.stage)
theCabine.stage=5
print(theCabine.stage)'''
N=78 # количество этажей
CabineButtons=[]
StageButtons=[]
i=1
while i<=N: # Создаем кнопки в лифте и на этажах
    newButton=CabineButton() # создаем новый объект кдасса CabineButton
    newButton.stage=i # Меняем свойство stage на номер этажа
    CabineButtons.append(newButton) # Добавляем новый объект в массив
    #print(CabineButtons[i-1].stage)
    if i>1: # добавляем кнопку вниз
        newButton=StageButton()
        newButton.stage=i
        newButton.direction=-1
        StageButtons.append(newButton)
    if i<N: # добавляем кнопку вверх
        newButton=StageButton()
        newButton.stage=i
        newButton.direction=1
        StageButtons.append(newButton)
    i+=1

def Call(place,stage,direction=0):
    # place=c||s cabine or stage
    # stage - номер этажа
    # 1 - вверх, -1 - вниз, 0 - при вызове в кабине лифта
    if place=="c": # Нажали кнопку в кабине
        # изменение состояния соответвующей кнопки в массиве CabineButtons
        print("нажали в лифте на этаж"+str(stage))
        for oneButton in CabineButtons: # цикл обхода всех элементов массива
            if oneButton.stage==stage:
                oneButton.status=True
    if place=="s": # Нажали кнопку на этаже
        # изменение состояния соответвующей кнопки в массиве StageButtons
        if direction==1:
            dirText="Верх"
        if direction==-1:
            dirText="Вниз"
        print("нажали в на этаже "+str(stage)+" кнопку "+dirText)
        for oneButton in StageButtons:
            if oneButton.stage==stage and oneButton.direction==direction:
                oneButton.status=True

        
    MoveIt()
        


def MoveIt():
    # функция принятия решения куда должен передвинуться лифт
    # и где остановиться

    # Программа определяет место положения лифта, его статус и направление
    # theCabine.stage  theCabine.status   theCabine.direction
    print("Кабина лифта на этаже "+str(theCabine.stage))
    print("Состояние лифта "+str(theCabine.status))
    print("Направление движения лифта "+str(theCabine.direction))

    # Программа производит обзор состояния кнопок в лифте
    # Только те кнопки лифта, которые "по-пути" для движения лифта,
    # если лифт движется. Если не движется, то все.

    # Программа производит обзор состояния кнопок на этажах
    # Только те кнопки лифта, которые "по-пути" для движения лифта
    # по номеру и направлению, если лифт движется.
    # Если не движется, то все.

    # Программа принимает решение о том, на какой этаж переместиться 

    # Программа меняет состояние соответствующих кнопок на False 

    # Если остаются кнопки с состоянием True,
    # то программа вызывает саму себя (рекурсия) 


Call("c",3)
#Call("s",5,-1)
