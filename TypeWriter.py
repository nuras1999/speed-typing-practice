'''
TYPEWRITER ~by  https://github.com/nuras1999
Stop worrying about your typing speed and start practising.
This contails more than 370k english dictionary words for practice.
It is highly recommended to convert this python file into exe file for ease of use.
Wordlist and images are taken from various sources.
'''

from tkinter.ttk import *                                   #For creating GUI windows and elements
from tkinter import *
from PIL import Image, ImageTk                              #For image operations
import os                                                   #For file operations
import random                                               #For random number generation
from tkinter import messagebox                              #Message box for showing alert when closing


def splashScreen():
    window=Tk()
    window.title("")
    window.geometry("600x400")
    window.resizable(0,0)
    window.configure(background = '#C6F1F1')

    width = 600
    height = 400
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    label_1=Label(window,text="TYPEWRITER", font=("Stencil",45),foreground="#232323",width="18",background="#DAF1F1")
    label_1.place(x=-29, y=220)

    label_3=Label(window,text="  Typing practise made simpler..!!", font=("Segoe Print",17),foreground="#232323",background="#DAF1F1",width="40")
    label_3.place(x=0, y=320)
    
    load = Image.open("images/logo.png")                            #opening logo
    load = load.resize((170, 170))                                  #resize logo
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render,border=FALSE)
    img.image = render
    img.place(x=220, y=30)                                          #placing logo
    
    window.wm_attributes('-topmost',True)                           #top of all applications
    window.overrideredirect(True)                                   #no titlebar

    windowWidth=600
    Style=ttk.Style()
    window.after(1000, window.destroy)                              #splashscreen for 5 sec
    window.mainloop()



def practicePage():

    window=Tk()
    window.title("TypeWriter")
    window.geometry("630x400")
    window.resizable(0,0)
    window.configure(background = '#C6F1F1')

    width = 630
    height = 400
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def tutorialImgOpen():
        try:
            img=Image.open("images/practice_sheet.jpg")                 #open practice sheet image
            img.show()                                                  #show practise sheet
        except IOError:                                                 #if image not found
            print("Error opening image")

    style=ttk.Style()
    style.configure("TButton",font=("ITC Franklin Gothic",10))
        
    learnButton=ttk.Button(window,text="?",style="TButton", command=tutorialImgOpen)    #button for practise sheet
    learnButton.place(x=580,y=350)
    learnButton.place(width="30",height="30")

        
    label_end=Label(window,text="Note : Type END to stop practising", font=("Arial",8),foreground="#A9A9A9",width="75",background="#DAF1F1")
    label_end.place(x=0, y=345)

    label_tip=Label(window,text="Tip : Take your time when typing to avoid mistakes. The speed will pick up as you progress", font=("Arial",8),foreground="#A9A9A9",width="75",background="#DAF1F1")
    label_tip.place(x=0, y=362)

    def mainFunc():
        if os.path.exists("wordlist.txt"):                          #check wordlist file exists
            while True:
                f=open("wordlist.txt","rt")                         #open wordlist
                lines = f.readlines()                               #read all lines
                length=len(lines)                                   #finding number of lines
                ran=random.randint(0,length-1)                      #generating a random line number
                global desired_lines
                desired_lines = lines[ran]                          #pickup a fixed line
                x=len(desired_lines)
                desired_lines=desired_lines[:x-2]                   #to remove \n at the end of each line
            
                label_1=Label(window,text=" ", font=("Stencil",45),foreground="#232323",width="18",background="#DAF1F1")
                label_1.place(x=-28, y=55)

                label_1["text"]=desired_lines                       #dynamically show the randomly picked word

                inputVal=StringVar()
                                
                entry_1 = ttk.Entry(window, textvariable = inputVal, justify = CENTER, font=("Fixedsys 27"))
                entry_1.place(height=40,width=400) 
                entry_1.place(x=110, y=198)
                entry_1.focus_force()                               #make it focus by default

                def caps(event):
                    inputVal.set(entry_1.get().upper())             #get input.. change it to uppercase.. update

                def thankyouMsg():
                    messagebox.showinfo("Thankyou","Thanks for using TypeWriter. Keep practising :)")       #messageBox
                    window.destroy()                                #close the GUI window
                    sys.exit()                                      #close the whole program

                def endFunc():
                    MsgBox=messagebox.askquestion("Exit Application","Are you sure you want to exit the application?",icon="warning")
                    if MsgBox=="yes":
                        thankyouMsg()
                    elif MsgBox=="no":
                        inputVal.set("")
                        pass

                def checkVal():
                    inputVal=entry_1.get()
                    inputVal=inputVal.lower()               #change all uppercase and lowercase to lowercase
                
                    if desired_lines == (inputVal):         #if inputted value equals random word
                        mainFunc()
                       
                    elif (inputVal=="end"):                 #inorder to end practise
                        endFunc()

                def enterPressed(event):                    
                    checkVal()

                window.bind('<Return>',enterPressed)        #when ENTER button is pressed check validity
                window.bind('<KeyPress>',caps)              #when any key is pressed convert to uppercase
                window.protocol("WM_DELETE_WINDOW", endFunc)        #when trying to close the GUI window

                input()                                     #for just holding screen. Avoid the error when executing.

                f.close()

        else:
            print("The file does not exist")                #if wordlist is not found

    mainFunc()

    windowWidth=630
    Style=ttk.Style()
    window.mainloop()


splashScreen()
practicePage()