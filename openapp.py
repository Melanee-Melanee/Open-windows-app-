import pyttsx3
import os

engine = pyttsx3.init()
pyttsx3.speak('Enter number to open application')
while True:
    print('Enter number to open application\n')
    print('\n1.MICROSIFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT  EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER \t 6.ADOBE ILLUSTARTOR \n\t 7.ADOBE PHOTOSHOP \t 8.MICROSIFT EDGE \n\t 9.NOTEPAD \t 10.TELEGRAM \n\n\t\t 0.FOR EXIT')
  
    p=input()
    p=p.upper()
    print(p)
    if ('DONT' in p) or ("DON'T" in p) or ('NOT' in p):
        pyttsx3.speak('Type Again')
        print(" . ")
        print(" . ")
        continue

    elif ('1' in p ):
        os.system('start winword')

    elif ('2' in p ):
        os.system('start powerpiont') 

    elif ('3' in p ):
        os.system('start excel')       

    elif ('4' in p ):
        os.system('start chrome')

    elif ('5' in p ):
        os.system('start vlc')  

    elif ('6' in p ):
        os.system('start illustrator')

    elif ('7' in p ):
        os.system('start photoshop')          

    elif ('8' in p ):
        os.system('start msedge')  

    elif ('9' in p ):
        os.system('start notepad')

    elif ('10' in p ):
        os.system('start telegram')

    
    elif ('0' in p ):
        pyttsx3.speak('Exiting')
        break

    else:
        pyttsx3.speak(p)
        print('Is invalid, please try again')
        pyttsx3.speak('Is invalid, please try again')














