from Tkinter import *
from chat import *
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


    for i in range(len(messageText)):
        if(messageText[i]=='.' and messageText[i+1]=='-' and messageText[i+2]==' '):
            if(messageText[i-1]==' ' or i==0):
                pomoc+='a'

        if (messageText[i] == '-' and messageText[i+1] == ' '):
            if (messageText[i - 1] == ' ' or i == 0):
                pomoc += 't'


    messageText = pomoc
    s.send(messageText) #send over socket

    displayLocalMessage(chatBox, messageText) #display local
    chatBox.yview(END) #auto-scroll
    textBox.delete("0.0",END) #clear the input box

def onClick2():
    messageText = messageFilter(textBox.get("0.0",END)) #filter

    tmp = messageFilter(textBox2.get("0.0",END))

    tmp2=tmp+messageText
    pomoc=''
    messageText=tmp2
    for i in range(len(messageText)):
        if(messageText[i]=='a' or messageText[i]=='A'):
            pomoc+='.- '

        if (messageText[i] == 't' or messageText[i] == 'T'):
            pomoc += '- '









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
            mixer.music.load('f:/Sounds/A_morse_code.mp3')
            mixer.music.play()
            time.sleep(1)


        if(data[i]=='t' or data[i]=='T'):
            mixer.init()
            mixer.music.load('f:/Sounds/T_morse_code.mp3')
            mixer.music.play()
            time.sleep(1)

def Remove(widget):
    widget.destroy()
def ChangeToImage(data,base):
    image = Button(base, font="Helvetica", bg="grey")
    image.place(x=440, y=305, height=100, width=100)
    image.config(state=DISABLED)
    for i in range(len(data)):
        if data[i]=='a' or data[i]=='A':
            image.configure(bg="yellow")
            time.sleep(0.75)
            image.configure(bg="red")
            time.sleep(2.25)
            image.configure(bg="grey")
            time.sleep(0.25)

        if data[i]=='t' or data[i]=='T':
            image.configure(bg="red")
            time.sleep(2.25)
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
Radiobutton(base,text='Tekst',value=0,variable=var).place(x=440, y=170)
Radiobutton(base,text='Dekodowanie',value=1,variable=var).place(x=440, y=195)
Radiobutton(base,text='Kodowanie',value=2,variable=var).place(x=440, y=220)
Radiobutton(base,text='Sygnały dzwiekowe',value=3,variable=var).place(x=440, y=245)
Radiobutton(base,text='Sygnały graficzne',value=4,variable=var).place(x=440, y=270)


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
#sendButton = Button(base, font="Helvetica", text="Wyślij", width="50", height=5,
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