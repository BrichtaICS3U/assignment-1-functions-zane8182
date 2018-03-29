# Assignment 1
# ICS3U
# Nathan Ilunga elelellel
# March 28 2018




def CtoF(C):
    """ Convert the temperature written in celsisus to fahrenheit"""
    F = 1.8 * C + 32
    return F

def FtoC(F):
     """ Convert the temperature in fahrenheit to celsius"""
     c = (0.55556) * (F-32)
     return C

print('enter 1 to convert a temperature to celsius and enter 2 to convert a temperature to fahrenheit: ')
x = int(input())
temp = int(input())
if x == 1 and temp >= -273.15:
   print(CtoF(temp))

elif x == 2 and temp >= -459.67:
    print(FtoC(temp))
else:
    print('Enter 1 for celsius and 2 for fahrenheit.')
    
