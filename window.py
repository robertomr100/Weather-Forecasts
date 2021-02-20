import tkinter as tk
from tkinter import *
from location import location
from weather_forecast import weatherForecast
from LUIS import *

locationObj = location()
weather_forecast = weatherForecast()
y = LUIS("9d556518bc2b49489a61ddbdc98884a3")


class window(tk.Frame):
    def __init__(self, parent):

        self.dialog=0
        null = ""
        self.location = null
        self.time = null
        self.timex = null
        self.repeat = 0
        parent.bind('<Return>', self.press_enter)
        tk.Frame.__init__(self, parent)
        self.messages = []
        self.tag=[]
        # we need to set parent as a class attribute for later use
        self.parent = parent
        self.parent.geometry('800x600')
        self.entryText = StringVar(self.parent)
        self.parent.config(bg="#202020")
        self.make_widgets()
        self.inputcount = 1
        self.row = 1


        #text labels for user
        self.usrlbl1
        self.usrlbl2
        self.usrlbl3
        self.usrlbl4
        self.usrlbl5
        self.usrlbl6
        self.usrlbl7
        self.usrlbl8

        #text labels for ai
        self.ailbl1
        self.ailbl2
        self.ailbl3
        self.ailbl4
        self.ailbl5
        self.ailbl6
        self.ailbl7
        self.ailbl8

        #text variables for user
        self.usr1
        self.usr2
        self.usr3
        self.usr4
        self.usr5
        self.usr6
        self.usr7
        self.usr8

        #text variables for ai
        self.ai1
        self.ai2
        self.ai3
        self.ai4
        self.ai5
        self.ai6
        self.ai7
        self.ai8

        # self.input_val


    def make_widgets(self):
        self.winfo_toplevel().title("Weather Bot")

        #configure all the rows for window
        self.parent.grid_rowconfigure(0, weight=10)
        self.parent.grid_rowconfigure(1, weight=10)
        self.parent.grid_rowconfigure(2, weight=10)
        self.parent.grid_rowconfigure(3, weight=10)
        self.parent.grid_rowconfigure(4, weight=10)
        self.parent.grid_rowconfigure(5, weight=10)
        self.parent.grid_rowconfigure(6, weight=10)
        self.parent.grid_rowconfigure(7, weight=10)
        self.parent.grid_rowconfigure(8, weight=10)
        self.parent.grid_rowconfigure(9, weight=10)

        #configure all the columns for window
        self.parent.grid_columnconfigure(0,weight=10)
        self.parent.grid_columnconfigure(1,weight=10)
        self.parent.grid_columnconfigure(2,weight=10)
        self.parent.grid_columnconfigure(3,weight=10)

        Toplbl=Label(self.parent, text="Type 'exit' to leave the program",bg="#202020",fg="white")
        Toplbl.grid(row=0,column=0, columnspan=4, sticky= NSEW)

        #text entries for user
        self.usr1= StringVar()
        self.usr2 = StringVar()
        self.usr3 = StringVar()
        self.usr4 = StringVar()
        self.usr5 = StringVar()
        self.usr6 = StringVar()
        self.usr7 = StringVar()
        self.usr8 = StringVar()

        self.usrlbl1 = Label(self.parent, textvariable=self.usr1, bg="#66B2FF",fg="black")
        self.usrlbl1.grid(row=1, column=2, columnspan=2, sticky=E)
        self.usrlbl2 = Label(self.parent, textvariable=self.usr2, bg="#66B2FF",fg="black")
        self.usrlbl2.grid(row=2, column=2, columnspan=2, sticky=E)
        self.usrlbl3 = Label(self.parent, textvariable=self.usr3, bg="#66B2FF",fg="black")
        self.usrlbl3.grid(row=3, column=2, columnspan=2, sticky=E)
        self.usrlbl4 = Label(self.parent, textvariable=self.usr4, bg="#66B2FF",fg="black")
        self.usrlbl4.grid(row=4, column=2, columnspan=2, sticky=E)
        self.usrlbl5 = Label(self.parent, textvariable=self.usr5, bg="#66B2FF",fg="black")
        self.usrlbl5.grid(row=5, column=2, columnspan=2, sticky=E)
        self.usrlbl6 = Label(self.parent, textvariable=self.usr6, bg="#66B2FF",fg="black")
        self.usrlbl6.grid(row=6, column=2, columnspan=2, sticky=E)
        self.usrlbl7 = Label(self.parent, textvariable=self.usr7, bg="#66B2FF",fg="black")
        self.usrlbl7.grid(row=7, column=2, columnspan=2, sticky=E)
        self.usrlbl8 = Label(self.parent, textvariable=self.usr8, bg="#66B2FF",fg="black")
        self.usrlbl8.grid(row=8, column=2, columnspan=2, sticky=E)

        #text entries for AI
        self.ai1=StringVar()
        self.ai2 = StringVar()
        self.ai3 = StringVar()
        self.ai4 = StringVar()
        self.ai5 = StringVar()
        self.ai6 = StringVar()
        self.ai7 = StringVar()
        self.ai8 = StringVar()

        self.ailbl1 = Label(self.parent, textvariable=self.ai1, bg="#FF9933",fg="black")
        self.ailbl1.grid(row=1, column=0, columnspan=2, sticky=W)
        self.ailbl2 = Label(self.parent, textvariable=self.ai2,bg="#FF9933",fg="black")
        self.ailbl2.grid(row=2, column=0, columnspan=2, sticky=W)
        self.ailbl3 = Label(self.parent, textvariable=self.ai3, bg="#FF9933",fg="black")
        self.ailbl3.grid(row=3, column=0, columnspan=2, sticky=W)
        self.ailbl4 = Label(self.parent, textvariable=self.ai4,bg="#FF9933",fg="black")
        self.ailbl4.grid(row=4, column=0, columnspan=2, sticky=W)
        self.ailbl5 = Label(self.parent, textvariable=self.ai5, bg="#FF9933",fg="black")
        self.ailbl5.grid(row=5, column=0, columnspan=2, sticky=W)
        self.ailbl6 = Label(self.parent, textvariable=self.ai6, bg="#FF9933",fg="black")
        self.ailbl6.grid(row=6, column=0, columnspan=2, sticky=W)
        self.ailbl7 = Label(self.parent, textvariable=self.ai7, bg="#FF9933",fg="black")
        self.ailbl7.grid(row=7, column=0, columnspan=2, sticky=W)
        self.ailbl8 = Label(self.parent, textvariable=self.ai8, bg="#FF9933",fg="black")
        self.ailbl8.grid(row=8, column=0, columnspan=2, sticky=W)

        #last row for entry text and submit button
        input = Entry(self.parent, width=102, textvariable=self.entryText)
        input.grid(row=9,column=0,columnspan=3,sticky=W)

        submitbtn=Button(self.parent, text="Submit", width=24, command=self.submit_press)
        submitbtn.grid(row=9,column=3, sticky=E)

    def press_enter(self, event):
        self.submit_press()

    def msgAI(self, message):
        #ailbl = Label(self.parent, text=message, bg="#66B2FF", fg="black")
        #ailbl.grid(row=self.row, column=2, columnspan=2, sticky=E)

        if self.row <= 8:
            if (self.row==1):
                self.ai1.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 2):
                self.ai2.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 3):
                self.ai3.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 4):
                self.ai4.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 5):
                self.ai5.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 6):
                self.ai6.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 7):
                self.ai7.set(message)
                self.messages.append(message)
                self.tag.append(0)
            elif (self.row == 8):
                self.ai8.set(message)
                self.messages.append(message)
                self.tag.append(0)
        else:                        #if we are at the end
            self.messages.append(message)
            self.tag.append(0)
            self.moveUp()
        self.row += 1


    def msgHuman(self, message):
        #usrlbl = Label(self.parent, text=message, bg="#66B2FF", fg="black")
        #usrlbl.grid(row=self.row, column=2, columnspan=2, sticky=E)
        if self.row <= 8:
            if (self.row==1):
                self.usr1.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 2):
                self.usr2.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 3):
                self.usr3.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 4):
                self.usr4.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 5):
                self.usr5.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 6):
                self.usr6.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 7):
                self.usr7.set(message)
                self.messages.append(message)
                self.tag.append(1)
            elif (self.row == 8):
                self.usr8.set(message)
                self.messages.append(message)
                self.tag.append(1)
        else:               # if we are at the end
            self.messages.append(message)
            self.tag.append(1)
            self.moveUp()
        self.row += 1


    def moveUp(self):
        self.messages=self.messages[1:]
        self.tag=self.tag[1:]
        self.usr1.set("")
        self.usr2.set("")
        self.usr3.set("")
        self.usr4.set("")
        self.usr5.set("")
        self.usr6.set("")
        self.usr7.set("")
        self.usr8.set("")
        self.ai1.set("")
        self.ai2.set("")
        self.ai3.set("")
        self.ai4.set("")
        self.ai5.set("")
        self.ai6.set("")
        self.ai7.set("")
        self.ai8.set("")

        for x in range(0,8):
            if self.tag[x] == 1: # if ai
                if x == 0:
                    self.usr1.set(self.messages[x])
                elif x == 1:
                    self.usr2.set(self.messages[x])
                elif x == 2:
                    self.usr3.set(self.messages[x])
                elif x == 3:
                    self.usr4.set(self.messages[x])
                elif x == 4:
                    self.usr5.set(self.messages[x])
                elif x == 5:
                    self.usr6.set(self.messages[x])
                elif x == 6:
                    self.usr7.set(self.messages[x])
                elif x == 7:
                    self.usr8.set(self.messages[x])

            else:
                if x == 0:
                    self.ai1.set(self.messages[x])
                elif x == 1:
                    self.ai2.set(self.messages[x])
                elif x == 2:
                    self.ai3.set(self.messages[x])
                elif x == 3:
                    self.ai4.set(self.messages[x])
                elif x == 4:
                    self.ai5.set(self.messages[x])
                elif x == 5:
                    self.ai6.set(self.messages[x])
                elif x == 6:
                    self.ai7.set(self.messages[x])
                elif x == 7:
                    self.ai8.set(self.messages[x])



    def submit_press(self):
        inputvalue = self.entryText.get()
        self.msgHuman(inputvalue)
        #print(self.messages[len(self.messages)-1])
        if(inputvalue.upper() == "EXIT"):
            quit()
        else:
            self.get_output(inputvalue)
            self.entryText.set("")

    def get_output(self, inputvalue):

        x=y.GetIntent(inputvalue)
        intent=x['intent']


        if intent=='Exit':
            return self.exit_dialog()

        elif self.dialog==2:
            return self.confirmation_dialog(inputvalue)

        if intent=='weather' or self.dialog==1:
            return self.weather_dialog(inputvalue)

        elif intent=='Hello':
            return self.hello_dialog()

        else:
            return self.none_dialog(inputvalue)


    def confirmation_dialog(self,inputvalue):

        if inputvalue=='Yes' or inputvalue=='yes' or inputvalue=='y' or inputvalue=='Y':
            self.dialog=1
            self.msgAI("Sounds good")
            x = self.location + " " + self.time
            self.get_output(x)
        else:
            self.msgAI("Lets start again, ask me for the weather anyplace and at any time!")
            self.dialog=0
            self.location=''
            self.time=''
            self.repeat=0

        return False


    def hello_dialog(self):
        input_complete = True
        self.msgAI("Hi! You can ask me about the weather at any place and any time!")
        return input_complete


    def none_dialog(self, inputvalue):
        null=''
        x = y.GetEntities(inputvalue)

        for entities in x:

            # deal with time
            if 'builtin.datetimeV2.' in entities['type']:
                self.time = entities['entity']
                resolution = entities['resolution']['values']
                self.timex = ''
                # timex = resolution[0]['timex']
                if str(resolution[0]['type']) == 'datetime':
                    self.timex = resolution[0]['timex']
                elif str(resolution[0]['type']) == 'date':
                    self.timex = resolution[0]['timex'] + "T00:00:00"

            if 'Places' in entities['type']:
                self.location = entities['entity']

        output = 'Do you want to know the weather'
        if self.location == null and self.time == null or self.repeat==1:
            input_complete = False
            self.msgAI("I could not understand what you are trying to say. Try again")
            self.time=''
            self.location=''
            self.repeat=0

        elif self.time == null:
            input_complete = False
            output = output + " at " + self.location + " ?"
            self.dialog = 2
            self.msgAI(output)
            self.repeat=0
        elif self.location == null:
            input_complete = False
            output = output + " for " + self.time + " ?"
            self.msgAI(output)
            self.dialog = 2
            self.repeat=0
        else:
            output = output + " at " + self.location + " for " + str(self.time) + " ?"
            self.msgAI(output)
            self.dialog = 2
            self.repeat=0


        return FALSE


    def weather_dialog(self,inputvalue):
        null = ''
        if self.dialog==0:
            self.dialog=1
            self.time=null
            self.place=null
        input_complete = True
        x = y.GetEntities(inputvalue)

        resolution = []
        for entities in x:

            # deal with time
            if 'builtin.datetimeV2.' in entities['type']:
                self.time = entities['entity']
                resolution = entities['resolution']['values']
                self.timex = ''
                # timex = resolution[0]['timex']
                if str(resolution[0]['type']) == 'datetime':
                    self.timex = resolution[0]['timex']
                elif str(resolution[0]['type']) == 'date':
                    self.timex = resolution[0]['timex'] + "T00:00:00"

            if 'Places' in entities['type']:
                self.location = entities['entity']
        # at this point we know if we have necessary information

        if self.location == null and self.time == null:
            input_complete = False
            self.msgAI("please give a time and place")
        elif self.time == null:
            input_complete = False
            self.msgAI("For when would you like forecast?")
        elif self.location == null:
            input_complete = False
            self.msgAI("For where would you like a forecast?")
        else:

            # self.msgAI("has both information")
            input_complete = True
            locationObj.get_result(self.location)
            # self.msgAI(timex)
            weather_forecast.getResult(locationObj.lat, locationObj.long, self.timex)
            weather_forecast.formatted_address = locationObj.formatted_address;
            self.msgAI(weather_forecast.printResult())
            #self.time = null
            #self.place = null
            self.dialog = 0
            self.repeat=0
        self.entryText.set("")
        return input_complete


    def exit_dialog(self):
        self.msgAI("Goodbye!")
        self.location=''
        self.time=''
        self.repeat=0
        quit()
        return True
