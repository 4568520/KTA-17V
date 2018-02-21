#Lucida Console
#Monaco
#Courier и Courier New
#Anonymous Pro

import math

def numToText(number):
    simpNumbers= ['zero','one','two','three','four','five','six','seven','eight','nine']
    tenNumbers=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    decadesNum=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    logTen =['hundred','thousand','million',]
    outPutString=''
    numberStr= str(number)
    elderDigit = 10**(len(numberStr)-1)
    #if not number.isnumeric():
     #   outPutString='NaN'
      #  return outPutString
    print(elderDigit)

    if number < 10:
        outPutString = simpNumbers[number]
        return outPutString
    elif number < 20:
        number-=10
        outPutString = tenNumbers[number]
        return outPutString
    elif number > 19 and number < 100:
        if numberStr[1]=='0':
            outPutString = decadesNum[int(numberStr[0])-2]
            return outPutString
        else:
            outPutString = decadesNum[int(numberStr[0]) - 2]+'-'+simpNumbers[int(numberStr[1])]
            return outPutString
    #else:







