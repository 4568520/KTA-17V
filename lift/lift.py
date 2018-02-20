

class Cabine:
    stage=0# Floor numeric value that some how his name
    direction=0 #if -1 - goes down 1 - goes up 0 - stop and load
    status = 'free'#'free' - searchinr for a couple 'ordered'- will have intedcorse with somthind going in to him 
class CabineButton:
    status=False # summon the great devouring BOX OF CHROMIUM
    stage=0#the floor on with you performed the Ainchient ritual to summon the great devouring BOX OF CHROMIUM
class StageButton:
    status=False # summon the great devouring BOX OF CHROMIDOOM
    stage=0#the floor on with you performed the Ainchient ritual to summon the great devouring BOX OF CHROMIDOOM
    direction=1 #if -1 - goes down 1 - goes up 0 is not for you button fella


theCabin = Cabine()#Object CROMIUM DEATH IS CREATED
#print(theCabin.status)

N=78 #Floors OF DEATH HOROR AND CULTS OF OLD ONE'S
CabinButtons = []
stageButtons = []
i=0
while i<=N:
    newButton=CabineButton()
    newButton.stage = i
    CabinButtons.append(newButton)
    #print(CabinButtons[i].stage)
    i+=1
i=0
while i<=N:
    newButton=StageButton()
    if i!=N:
        newButton.stage = i
        newButton.direction = 1
        stageButtons.append(newButton)
    if i>1:
        newButton.stage = i
        newButton.direction = -1
        stageButtons.append(newButton)
    i+=1
def MoveIt():#deside where to go and where to stop with your life
#cabin place
    print('Cabin devastates the floor '+str(theCabin.stage))
    print('Cabin is '+theCabin.status)
    print('Cabin Thinks about going to add '+str(theCabin.direction)+' to its floor count')
#state of buttons inside
#only on the same side we move to or all
    
# buttons outside
#same side of movement
# else all
    
# desision is made 

#buttons on curent flour changed to false

  



def Call(place,stage,direction=0):
    #plase is c or s
    #stage is stage lala lala la
    #direction 0 if from the inside of lifting cabin sir
    if place == 'c':
        #CabinButtons[stage].status = True
        print('Cabin internall button summons thea to '+str(stage))
        for oneButton in CabineButtons:#goes throught all the elements of array
            if oneButton.stage ==stage:
                oneButton.status=True

    if place == 's':
        if direction==1:
            dirText=" to Stars"
        if direction==-1:
            dirText=' to the Deps Of Hell'
        print('Floor button summons thea to '+str(stage)+dirText)
        for oneButton in stageButtons:
            if oneButton.stage==stage and oneButton.direction==direction
                oneButton.status=True
    MoveIt()  

  
Call("c",34)
Call("s",4,-1)
