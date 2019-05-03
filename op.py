#Program By Rabin Pant

#importing for the GUI application
import tkinter

class AutomotiveGUI:
    def __init__(self):
        #create the main root widget
        self.main_window = tkinter.Tk()
        
        #three frames for different purpose
        #1----for displaying a msg
        #2---for displaying the check box
        #3---for displaying the total price
        
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        self.top_label = tkinter.Label(self.top_frame,\
                                       text='What services do you like?')
        
        self.top_label.pack()
        
        #Seven Integer variable to use with the checkbuttons
        self.checkButtonvar1 = tkinter.IntVar()
        self.checkButtonvar2 = tkinter.IntVar()
        self.checkButtonvar3 = tkinter.IntVar()
        self.checkButtonvar4 = tkinter.IntVar()
        self.checkButtonvar5 = tkinter.IntVar()
        self.checkButtonvar6 = tkinter.IntVar()
        self.checkButtonvar7 = tkinter.IntVar()
        
        #Set the integer variable object to 0
        self.checkButtonvar1.set(0)
        self.checkButtonvar2.set(0)
        self.checkButtonvar3.set(0)
        self.checkButtonvar4.set(0)
        self.checkButtonvar5.set(0)
        self.checkButtonvar6.set(0)
        self.checkButtonvar7.set(0)
        
        #Checkbutton displaying on the mid frame
        self.checkButton1 = tkinter.Checkbutton(self.mid_frame,\
                                                text='oil Change',\
                                                variable=self.checkButtonvar1,\
                                                command=self.oil_change)
        self.checkButton2 = tkinter.Checkbutton(self.mid_frame,\
                                                text='Lube Job',\
                                                variable=self.checkButtonvar2,\
                                                command=self.lube_job)
        self.checkButton3 = tkinter.Checkbutton(self.mid_frame,\
                                                text='Raditior Flush',\
                                                variable=self.checkButtonvar3,\
                                                command=self.radiator_flush)
        self.checkButton4 = tkinter.Checkbutton(self.mid_frame,\
                                                text='Transmission Flush',\
                                                variable=self.checkButtonvar4,\
                                                command=self.transmission_flush)
        self.checkButton5 = tkinter.Checkbutton(self.mid_frame,\
                                                text='Inspection',\
                                                variable=self.checkButtonvar5,\
                                                command=self.inspection)
        self.checkButton6 = tkinter.Checkbutton(self.mid_frame,\
                                                text='Muffler Replacement',\
                                                variable=self.checkButtonvar6,\
                                                command=self.muffler)
        self.checkButton7 = tkinter.Checkbutton(self.mid_frame,\
                                                text='Tire Rotation',\
                                                variable=self.checkButtonvar7,\
                                                command=self.tire_rotation)
        
        #packing all the checkbuttons to display in appropriate position
        self.checkButton1.pack()
        self.checkButton2.pack()
        self.checkButton3.pack()
        self.checkButton4.pack()
        self.checkButton5.pack()
        self.checkButton6.pack()
        self.checkButton7.pack()
        
        #Label widget and the total price dispalying on the bottom frame
        self.bottom_label = tkinter.Label(self.bottom_frame,text='Total:')
        self.total = tkinter.StringVar()
        self.total.set('0.00')
        self.total_label = tkinter.Label(self.bottom_frame,\
                                         textvariable = self.total)
        #pack the frame
        self.bottom_label.pack(side='left')
        self.total_label.pack(side='left')
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        #main loop begin
        tkinter.mainloop()
        
    
    ############
    ###------All the method use to update the total value
    #--------whenever user select the check box
    
    def oil_change(self):
        
        total = float(self.total.get())
        if self.checkButtonvar1.get():
            total+=26
        else:
            total-=26
        total = format(total,'.2f')
        self.total.set(total)
        
    def lube_job(self):
        total = float(self.total.get())
        if self.checkButtonvar2.get():
            total+=18
        else:
            total-=18
        total = format(total,'.2f')
        self.total.set(total)
        
    def radiator_flush(self):
        total = float(self.total.get())
        if self.checkButtonvar3.get():
            total+=30
        else:
            total-=30
        total = format(total,'.2f')
        self.total.set(total)
        
    def transmission_flush(self):
        total = float(self.total.get())
        if self.checkButtonvar4.get():
            total+=80
        else:
            total-=80
        total = format(total,'.2f')
        self.total.set(total)
    
    def inspection(self):
        total = float(self.total.get())
        if self.checkButtonvar5.get():
            total+=15
        else:
            total-=15
        total = format(total,'.2f')
        self.total.set(total)
        
    def muffler(self):
        total = float(self.total.get())
        if self.checkButtonvar6.get():
            total+=100
        else:
            total-=100
        total = format(total,'.2f')
        self.total.set(total)
    
    def tire_rotation(self):
        total = float(self.total.get())
        if self.checkButtonvar7.get():
            total+=20
        else:
            total-=20
        total = format(total,'.2f')
        self.total.set(total)
        
#creating an object of Automoitve class
joe_gui = AutomotiveGUI()
    
    
    
        