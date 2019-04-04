from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO
 
##SETUP CHANNEL
GPIO.setmode(GPIO.BCM)
 
#GUI DEF
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
 
##CLASS FOR LED'S
class led:
    def __init__(self,pin,state,name):
        self.pin = pin
        self.state = state
        self.name = name
        GPIO.setup(self.pin, GPIO.OUT)
       
    def onOff(self):
        if self.state is True:
            self.state = False
            GPIO.output(self.pin, self.state)
            print("led off")
        else:
            self.state = True
            GPIO.output(self.pin, self.state)
            print("Led On")
           
    def setOff(self):
        if self.state is True:
            self.state = False
            GPIO.output(self.pin, self.state)
            print(self.name + " set to off")
                                 
##CLOSE WINDOW AND TURN OFF LED's
def close(window):
    window.destroy()
    GPIO.cleanup()
    print("closewindow")
 
##FOR LIMITING TO ONE LED AT A TIME
def oneLED(name):
    if name is "red":
        red.onOff()
        green.setOff()
        blue.setOff()
    if name is "green":
        green.onOff()
        blue.setOff()
        red.setOff()
    if name is "blue":
        blue.onOff()
        green.setOff()
        red.setOff()
       
## ASSIGNING PIN, STATE AND NAME TO EACH LED
red = led(pin = 12, state =  False, name = "red")
green = led(pin = 16, state = False, name = "green")
blue = led(pin = 20, state = False, name = "blue")
 
## WIDGETS
redButton = Button(win, text = 'Red LED', font = myFont, command= lambda: oneLED(red.name), bg = 'red', height = 1, width = 24)
redButton.grid(row=0,column=1)
greenButton = Button(win, text = 'Green LED', font = myFont, command = lambda: oneLED(green.name), bg = 'green', height = 1, width = 24)
greenButton.grid(row=1,column=1)
blueButton = Button(win, text = 'Blue LED', font = myFont, command =  lambda: oneLED(blue.name), bg = 'blue', height = 1, width = 24)
blueButton.grid(row=2,column=1)
endButton = Button(win, text = 'Close', font = myFont, command = lambda: close(win), bg = 'white', height = 1, width = 24)
endButton.grid(row=3,column=1)
