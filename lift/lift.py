

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
upButtons = []
downButtons = []
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
        upButtons.append(newButton)
    if i>1:
        newButton.stage = i
        newButton.direction = -1
        downButtons.append(newButton)
    i+=1
