# Based on 5 questions, python will decide whether you gmi or ngmi

question1 = int(input('What year did you start your crypto journey? '))
question2 = input('What was your first crypto coin? ').lower()
question3 = input('Are you still holding that coin? ').lower()
question4 = input('Did you ever sell a bottom? ').lower()
question5 = input('Safemoon investor? ').lower()

def outputThrower():
    ct = 0
    if question1 <= 2019:
        ct + 1
    if question2 == 'xvg':
        ct + 1
    if question3 == 'yes':
        ct + 1   
    if question4 == 'yes':
        ct + 1 
    if question5 == 'no':
        ct + 1           
    if ct >= 3:
        print('Congrats ser, you GMI')
        return
    print('Unforunately ser, you NGMI')

outputThrower()        