from Tkinter import *
from chat import *
import os
from PIL import *
import thread
import tkMessageBox
from tkFileDialog import askopenfilename
from pygame import mixer
import time




#HOST = '25.53.53.24'
HOST = gethostname()

PORT = 9003
s = socket(AF_INET, SOCK_STREAM)
global nick
nick

def onClick():
    messageText = messageFilter(textBox.get("0.0",END)) #filter

    tmp = messageFilter2(textBox2.get("0.0",END))
    tmp = tmp.upper()

    tmp2=tmp+messageText
    messageText=tmp2

    s.send(messageText) #send over socket

    displayLocalMessage(chatBox, messageText) #display local
    chatBox.yview(END) #auto-scroll
    textBox.delete("0.0",END) #clear the input box

def onClick1():
    messageText = messageFilter(textBox.get("0.0",END)) #filter

    tmp = messageFilter2(textBox2.get("0.0",END))
    tmp = tmp.upper()

    tmp2=tmp+messageText
    messageText=tmp2
    pomoc=''
    i = 0
    for i in range(len(messageText)):
        if(messageText[i]=='.' and messageText[i+1]=='-' and messageText[i+2]==' '):
            if(messageText[i-1]==' ' or i==0):
                pomoc+='a'

        if (messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]=='.' and messageText[i+3]=='.' and messageText[i+4]==' '):
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'b'

        if ( messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]=='-' and messageText[i+3]=='.' and messageText[i+4]==' ' ):
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'c'

        if messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]=='.' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'd'

        if (messageText[i] == '.' and messageText[i+1] == ' '):
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'e'

        if messageText[i] == '.' and messageText[i+1] == '.' and messageText[i+2]=='-' and messageText[i+3]=='.'and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'f'


        if messageText[i] == '-' and messageText[i+1] == '-' and messageText[i+2]=='.' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'g'

        if messageText[i] == '.' and messageText[i+1] == '.' and messageText[i+2]=='.' and messageText[i+3]=='.' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'h'

        if messageText[i] == '.' and messageText[i+1] == '.' and messageText[i+2]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'i'

        if messageText[i] == '.' and messageText[i+1] == '-' and messageText[i+2]=='-' and messageText[i+3]=='-' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'j'

        if messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]=='-' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'k'

        if messageText[i] == '.' and messageText[i+1] == '-' and messageText[i+2]=='.' and messageText[i+3]=='.' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'l'

        if messageText[i] == '-' and messageText[i+1] == '-' and messageText[i+2]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'm'

        if messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'n'

        if messageText[i] == '-' and messageText[i+1] == '-' and messageText[i+2]=='-' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'o'

        if messageText[i] == '.' and messageText[i+1] == '-' and messageText[i+2]=='-' and messageText[i+3]=='.' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'p'

        if messageText[i] == '-' and messageText[i+1] == '-' and messageText[i+2]=='.' and messageText[i+3]=='-' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'q'

        if messageText[i] == '.' and messageText[i+1] == '-' and messageText[i+2]=='.' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'r'

        if messageText[i] == '.' and messageText[i+1] == '.' and messageText[i+2]=='.' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 's'

        if messageText[i] == '-' and messageText[i+1] == ' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 't'

        if messageText[i] == '.' and messageText[i+1] == '.' and messageText[i+2]=='-' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'u'

        if messageText[i] == '.' and messageText[i+1] == '.' and messageText[i+2]=='.' and messageText[i+3]=='.' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'v'

        if messageText[i] == '.' and messageText[i+1] == '-' and messageText[i+2]=='-' and messageText[i+3]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'w'

        if messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]=='.' and messageText[i+3]=='-' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'x'

        if messageText[i] == '-' and messageText[i+1] == '.' and messageText[i+2]=='-' and messageText[i+3]=='-' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'y'

        if messageText[i] == '-' and messageText[i+1] == '-' and messageText[i+2]=='.' and messageText[i+3]=='.' and messageText[i+4]==' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 'z'

        if messageText[i] == ' ' and messageText[i+1] == ' ':
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += ' '




    messageText = pomoc

    tmp = messageFilter(textBox2.get("0.0", END))
    tmp2 = tmp + messageText
    messageText = tmp2

    s.send(messageText) #send over socket

    displayLocalMessage(chatBox, messageText) #display local
    chatBox.yview(END) #auto-scroll
    textBox.delete("0.0",END) #clear the input box

def onClick2():
    messageText = messageFilter(textBox.get("0.0",END)) #filter

    pomoc=''
    for i in range(len(messageText)):
        if(messageText[i]=='a' or messageText[i]=='A'):
            pomoc+='.- '
        if (messageText[i] == 'b' or messageText[i] == 'B'):
            pomoc += '-... '
        if (messageText[i] == 'c' or messageText[i] == 'C'):
            pomoc += '-.-. '
        if (messageText[i] == 'd' or messageText[i] == 'D'):
            pomoc += '-.. '
        if (messageText[i] == 'e' or messageText[i] == 'E'):
            pomoc += '. '
        if (messageText[i] == 'f' or messageText[i] == 'F'):
            pomoc += '..-. '
        if (messageText[i] == 'g' or messageText[i] == 'G'):
            pomoc += '--. '
        if (messageText[i] == 'h' or messageText[i] == 'H'):
            pomoc += '.... '
        if (messageText[i] == 'i' or messageText[i] == 'I'):
            pomoc += '.. '
        if (messageText[i] == 'j' or messageText[i] == 'J'):
            pomoc += '.--- '
        if (messageText[i] == 'k' or messageText[i] == 'K'):
            pomoc += '-.- '
        if (messageText[i] == 'l' or messageText[i] == 'L'):
            pomoc += '.-.. '
        if (messageText[i] == 'm' or messageText[i] == 'M'):
            pomoc += '-- '
        if (messageText[i] == 'n' or messageText[i] == 'N'):
            pomoc += '-. '
        if (messageText[i] == 'o' or messageText[i] == 'O'):
            pomoc += '--- '
        if (messageText[i] == 'p' or messageText[i] == 'P'):
            pomoc += '.--. '
        if (messageText[i] == 'q' or messageText[i] == 'Q'):
            pomoc += '--.- '
        if (messageText[i] == 'r' or messageText[i] == 'R'):
            pomoc += '.-. '
        if (messageText[i] == 's' or messageText[i] == 'S'):
            pomoc += '... '
        if (messageText[i] == 't' or messageText[i] == 'T'):
            pomoc += '- '
        if (messageText[i] == 'u' or messageText[i] == 'U'):
            pomoc += '..- '
        if (messageText[i] == 'v' or messageText[i] == 'V'):
            pomoc += '...- '
        if (messageText[i] == 'w' or messageText[i] == 'W'):
            pomoc += '.-- '
        if (messageText[i] == 'x' or messageText[i] == 'X'):
            pomoc += '-..- '
        if (messageText[i] == 'y' or messageText[i] == 'Y'):
            pomoc += '-.-- '
        if (messageText[i] == 'z' or messageText[i] == 'Z'):
            pomoc += '--.. '
        if (messageText[i] == ' ' and messageText[i+1] == ' '):
            pomoc += ' '


    messageText=pomoc

    tmp = messageFilter(textBox2.get("0.0",END))

    tmp2=tmp+messageText
    messageText=tmp2


    s.send(messageText) #send over socket

    displayLocalMessage(chatBox, messageText) #display local
    chatBox.yview(END) #auto-scroll
    textBox.delete("0.0",END) #clear the input box

def onEnterButtonPressed(event):
    textBox.config(state=NORMAL)

    if var.get()==0:
        onClick()
    if var.get()==1:
        onClick1()
    if var.get()==2:
        onClick2()







def removeKeyboardFocus(event):
	textBox.config(state=DISABLED)



#base2 = Tk()

#base2.title("Ustaw Nick")
#base2.geometry("200x50")
#base2.resizable(width=FALSE, height=FALSE)

#def Close(event):
    #base2.destroy()



def ChangeToSound(data):
    for i in range(len(data)):
        if(data[i]=='a' or data[i]=='A'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/A_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'b' or data[i] == 'B'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/B_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)

        if (data[i] == 'c' or data[i] == 'C'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/C_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'd' or data[i] == 'D'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/D_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'e' or data[i] == 'E'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/E_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'f' or data[i] == 'F'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/F_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'g' or data[i] == 'G'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/G_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'h' or data[i] == 'H'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/H_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'i' or data[i] == 'I'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/I_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'j' or data[i] == 'J'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/J_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'k' or data[i] == 'K'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/K_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'm' or data[i] == 'M'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/M_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'n' or data[i] == 'N'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/N_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'o' or data[i] == 'O'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/O_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)

        if (data[i] == 'p' or data[i] == 'P'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/P_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'r' or data[i] == 'R'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/R_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 's' or data[i] == 'S'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/S_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 't' or data[i] == 'T'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/T_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'u' or data[i] == 'U'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/U_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'v' or data[i] == 'V'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/V_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'w' or data[i] == 'W'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/W_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'x' or data[i] == 'X'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/X_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'y' or data[i] == 'Y'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/Y_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)
        if (data[i] == 'z' or data[i] == 'Z'):
            mixer.init()
            soundPath = os.path.abspath('Sounds/Z_morse_code.mp3')
            mixer.music.load(soundPath)
            mixer.music.play()
            time.sleep(1)

def Remove(widget):
    widget.destroy()
def ChangeToImage(data,base):
    image = Button(base, font="Helvetica", bg="grey")
    image.place(x=440, y=305, height=100, width=100)
    image.config(state=DISABLED)
    for i in range(len(data)):
        if data[i] == 'a' or data[i] == 'A':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 't' or data[i] == 'T':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'b' or data[i] == 'B':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'c' or data[i] == 'C':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)

        if data[i] == 'd' or data[i] == 'D':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)

        if data[i] == 'e' or data[i] == 'E':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'f' or data[i] == 'F':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'g' or data[i] == 'G':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'h' or data[i] == 'H':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'i' or data[i] == 'I':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'j' or data[i] == 'J':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'k' or data[i] == 'K':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'l' or data[i] == 'L':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'm' or data[i] == 'M':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'n' or data[i] == 'M':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'o' or data[i] == 'O':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'p' or data[i] == 'P':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'q' or data[i] == 'Q':
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'r' or data[i] == 'R':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'r' or data[i] == 'R':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 's' or data[i] == 'S':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'u' or data[i] == 'U':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'v' or data[i] == 'V':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'w' or data[i] == 'W':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'x' or data[i] == 'X':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i] == 'z' or data[i] == 'Z':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="grey")
            time.sleep(0.25)









def ReceiveData():
    try:
        s.connect((HOST, PORT))
        getConnectionInfo(chatBox, '[ Connected! ]\n-------------------------------------')
    except:
        getConnectionInfo(chatBox, '[ Cannot connect ]')
        return

    while 1:
        try:
            data = s.recv(1024)
        except:
            getConnectionInfo(chatBox, '\n [ Your partner left.] \n')
            break
        if data != '':
            if var.get()<3:
                displayRemoteMessage(chatBox, data) #Tutaj jest wysylanie wiadomosci
            elif var.get()==3:
                ChangeToSound(data)
            elif var.get() == 4:
                ChangeToImage(data,base)

        #if data != '' and var.get()==3:
            #ChangeToSound(data)


        else:
            getConnectionInfo(chatBox, '\n [ Your partner left. ] \n')
            break
    s.close()

#NickNameWindow




#Base Window
base = Tk()
base.title("Pychat Client")
base.geometry("600x450")
base.resizable(width=FALSE, height=FALSE)
base.configure(bg="#716664")

#thread.start_new_thread(openConnection,())

  #TUTAJ



textBox2 = Text(base, bd=0, bg="#FFFFFF", width="30", height="10", font="Helvetica")
textBox2.focus_force()

textBox2.bind("<Return>", removeKeyboardFocus)

textBox2.bind("<KeyRelease-Return>", onEnterButtonPressed)

w=Label(base,text="Ustaw Nick")

w.place(x=460, y=25)


y=Label(base,text="Wybierz kodowanie")

y.place(x=441, y=140)


textBox2.place(x=400, y=50, height=35, width=180)
base.focus_force()

def block():
    textBox2.config(state=DISABLED)





saveNickButton=Button(base,font="Helvetica",text="Zapisz",bg="#33CC00",command=block)

#Radiobutthon
var=IntVar()
tapy=170
var.set(0)
Radiobutton(base,text='Tekst',value=0,variable=var).place(x=440, y=180)
Radiobutton(base,text='Dekodowanie',value=1,variable=var).place(x=440, y=205)
Radiobutton(base,text='Kodowanie',value=2,variable=var).place(x=440, y=230)
Radiobutton(base,text='Sygnaly dzwiekowe',value=3,variable=var).place(x=440, y=255)
Radiobutton(base,text='Sygnaly graficzne',value=4,variable=var).place(x=440, y=280)


nickButton = Button(base,font="Helvetica",text="Wybierz Kodowanie",bg="#33CC00")
nickButton.pack()

saveNickButton=Button(base,font="Helvetica",text="Zapisz",bg="#33CC00",command=block)




#Chat
chatBox = Text(base, bd=0, bg="#99FFFF", height="8", width="20", font="Helvetica",)
chatBox.insert(END, "Waiting for your partner to connect..\n")
chatBox.config(state=DISABLED)
sb = Scrollbar(base, command=chatBox.yview, bg = "#34495e")
chatBox['yscrollcommand'] = sb.set

#Send Button
#sendButton = Button(base, font="Helvetica", text="Wyslij", width="50", height=5,
 #                   bd=0, bg="#33CC00", activebackground="#339900", justify="center",
  #                  command=onClick)

#Text Input
textBox = Text(base, bd=0, bg="#FFFFFF",width="29", height="5", font="Helvetica")
textBox.bind("<Return>", removeKeyboardFocus)
textBox.bind("<KeyRelease-Return>", onEnterButtonPressed)

#Put everything on the window
sb.place(x=370,y=5, height=350)
chatBox.place(x=15,y=5, height=350, width=355)
#sendButton.place(x=255, y=360, height=80, width=130)
textBox.place(x=15, y=360, height=80, width=370)



nickButton.place(x=390, y=140, height=40, width=205)

saveNickButton.place(x=440, y=90, height=40, width=100)
thread.start_new_thread(ReceiveData,())
base.mainloop()