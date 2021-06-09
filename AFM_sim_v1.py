#!/usr/bin/env python


#######################################################
##### univie , PNM , practical class MMM          #####
#####                                             #####
##### WITec alpha300 RAS, AFM settings simulation #####
#####                                             #####
##### Version 1.0                                 #####
#####                                             #####
##### Stefan Noisternig                           #####
#####                                             #####
##### comments will be added in future version    #####
#####                                             #####
##### see also: operation guides in WITec Suite   #####
#####           Help (since WITec Suite 5.3)      #####
#######################################################


import tkinter as tk

from PIL import ImageTk, Image

from inspect import currentframe, getframeinfo
from pathlib import Path


#filename = getframeinfo(currentframe()).filename
#print(filename)
#parent = Path(filename).resolve().parent
#path= parent / "images" / "2-Raman-CCD-cooldown-wait.png"


class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=800, height=600, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1760,1400))#(self.canvas.bbox("all"))#(scrollregion=(0,0,1000,1000))

        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


        #self.original = Image.open(path)
        #self.image = ImageTk.PhotoImage(self.original)
        #self.display = tk.Canvas(self, bd=0, highlightthickness=0)
        #self.display.create_image(0, 0, image=self.image, anchor='nw', tags="IMG")
        #self.display.grid(row=0, sticky='w'+'e'+'n'+'s')


        # button widget 
        #self.b1 = tk.Button(self, text = "Click me !") 
  
        # This is where b1 is placed inside b2 with in_ option 
        #self.b1.place(x = 500, y = 500, anchor = "nw") 
        #self.canvas.create_window(10, 10, anchor='nw', window=self.b1)


        # This is what enables using the mouse:
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)



        root.title("WiTec simulation for AFM measurement")
        self.image=None

        filename = getframeinfo(currentframe()).filename
        self.parent = Path(filename).resolve().parent / "images"

        self.buttonimage1=None
        self.buttonimage2=None
        self.buttonimage3=None
        self.buttonimage4=None
        self.buttonimage5=None
        self.buttonimage6=None


        self.variableS1=tk.StringVar(root)
        self.variable1=tk.IntVar()
        self.variable2=tk.IntVar()
        self.variableD1=tk.DoubleVar()
        self.variableD2=tk.DoubleVar()
        self.variableS1=tk.StringVar(value='512')
        self.variableS2=tk.StringVar(value='512')
        self.variableS3=tk.StringVar(value='50')
        self.variableS4=tk.StringVar(value='24')
        self.variableS5=tk.StringVar(value='1')
        self.variableS6=tk.StringVar(value='0')
        self.variableS7=tk.StringVar(value='0')



        self.z_state=1
        self.klicked=False
        self.x_state=0
        self.y_state=0


    #move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)


    def frameimage(self,imagename):
        path = self.parent / imagename
        print(path)
        self.image= ImageTk.PhotoImage(Image.open(path))
        self.canvas.create_image(0,0,image=self.image, anchor="nw")


    def button1(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage1,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='center', window=button)



    def button2(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage2 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage2,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)


    def button3(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage3 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage3,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)

    def button4(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage4 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage4,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)

    def button5(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage5 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage5,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)

    def button6(self,imagename,fname,positionX,positionY):
        # button widget
        path = self.parent / imagename
        self.buttonimage6 = ImageTk.PhotoImage(Image.open(path))

        button = tk.Button(root, image=self.buttonimage6,highlightthickness=0,borderwidth=0,relief=tk.FLAT)


        button.bind('<Button-1>', lambda event: fname())
        #button.bind('<Double-1>', lambda event: self.quiting())

        self.canvas.create_window(positionX, positionY, anchor='nw', window=button)



    def numberfield(self,letterwidth,positionX,positionY):
        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: self.numbers(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)


    def dropdown1(self,positionX,positionY,*Optionlist):

        def callback():
            print(self.variableS1.get())

        self.variableS1.set(Optionlist[0])
        dropdown=tk.OptionMenu(root,self.variableS1,*Optionlist)
        self.canvas.create_window(positionX, positionY, anchor='center', window=dropdown)
        self.variableS1.trace('w',callback)


    def lasermenu(self,imagename,positionX,positionY):

        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))

        mb=tk.Menubutton(root,image=self.buttonimage1)
        #mb.grid()
        mb.menu=tk.Menu(mb,tearoff=0)
        mb["menu"]=mb.menu

        mb.menu.add_checkbutton(label="Laser on", command=self.failmessage)
        mb.menu.add_checkbutton(label="Laser off", command=self.next)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=mb)

    def checkbutton1(self,text,positionX,positionY,state=0,):
        check=tk.Checkbutton(root,text=text,variable=self.variable1)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=check)
        if state==1:
            check.select()
        self.variable1.trace('w',self.hello)

    def checkbutton2(self,text,positionX,positionY,state=0,):
        check=tk.Checkbutton(root,text=text,variable=self.variable2)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=check)
        if state==1:
            check.select()
        self.variable2.trace('w',self.hello)

    def scale1(self,positionX,positionY,text=None,length=100):
        scale=tk.Scale(root,variable=self.variableD1,orient='horizontal',from_=0,to_=0.25,resolution=0.025,length=length,label=text)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=scale)
        self.variableD1.trace('w',self.hello)

    def scale2(self,positionX,positionY,text=None,length=100):
        scale=tk.Scale(root,variable=self.variableD2,orient='horizontal',from_=0,to_=48,resolution=4.8,length=length,label=text)
        self.canvas.create_window(positionX, positionY, anchor='nw', window=scale)
        self.variableD2.trace('w',self.hello)



    def brightness_scales(self,value1=0,value2=0):
        frame2=tk.LabelFrame(root,height=70,width=340)
        scale1=tk.Scale(frame2,variable=self.variableD1,orient='horizontal',from_=0,to_=0.25,resolution=0.025,length=175,width=5)
        scale1.set(value1)
        scale1.place(x=150,y=0)
        scalelabel1=tk.Label(frame2,text="Exposure [s]")
        scalelabel1.place(x=10,y=8)
        scale2=tk.Scale(frame2,variable=self.variableD2,orient='horizontal',from_=0,to_=48,resolution=4.8,length=175,width=5)
        scale2.set(value2)
        scale2.place(x=150,y=27)
        scalelabel2=tk.Label(frame2,text="Gain [dB]")
        scalelabel2.place(x=10,y=35)
        return frame2


    def brightness_checkbuttons(self,select=True):
        frame1=tk.LabelFrame(root,height=60,width=340)
        check1=tk.Checkbutton(frame1,text="Smart Exposure",variable=self.variable1)
        if select==True:
            check1.select()
        check1.place(x=10,y=3)
        check2=tk.Checkbutton(frame1,text="Smart Gain",variable=self.variable2)
        if select==True:
            check2.select()
        check2.place(x=10,y=27)
        return frame1



    def brightness_unset(self,posX1,posY1,posX2,posY2):
        self.klicked=False

        def checksetting(*args):
            if self.variable1.get()+self.variable2.get()==0:
                if self.variableD1.get()>0.2 and self.variableD2.get()>40.0 and self.klicked==False:
                    self.next()
                    self.klicked=True
                    self.variable1.trace_vdelete('w',trace1_id)
                    self.variable2.trace_vdelete('w',trace2_id)
                    self.variableD1.trace_vdelete('w',traceD1_id)
                    self.variableD2.trace_vdelete('w',traceD2_id)
        
        frame1=self.brightness_checkbuttons()
        self.canvas.create_window(posX1, posY1, anchor='nw', window=frame1)

        frame2=self.brightness_scales()
        self.canvas.create_window(posX2, posY2, anchor='nw', window=frame2)

        trace1_id=self.variable1.trace('w',checksetting)
        trace2_id=self.variable2.trace('w',checksetting)
        traceD1_id=self.variableD1.trace('w',checksetting)
        traceD2_id=self.variableD2.trace('w',checksetting)


    def brightness_change(self,darkimagename,brightimagename,posX,posY,posX2,posY2):
        self.klicked=False

        path = self.parent / darkimagename
        darkscreen = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / brightimagename
        brightscreen=ImageTk.PhotoImage(Image.open(path))
        label=tk.Label(root,image=brightscreen)
        labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)

        def replacelabel(labelwindow,tkimage):
            self.canvas.delete(labelwindow)
            label=tk.Label(root,image=tkimage)
            labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)
            
        def checksetting(*args):
            if self.variableD1.get()<=0.08 or self.variableD2.get()<=37.0:
                replacelabel(labelwindow,darkscreen)
            elif  self.variableD1.get()>0.08 and self.variableD1.get()<0.17 and self.variableD2.get()>37.0 and self.variableD2.get()<47.0 and self.klicked==False:
                self.next()
                self.klicked=True
                self.variableD1.trace_vdelete('w',traceD1_id)
                self.variableD2.trace_vdelete('w',traceD2_id)
            else:
                replacelabel(labelwindow,brightscreen)

        frame2=self.brightness_scales(value1=0.25,value2=48)
        self.canvas.create_window(posX2, posY2, anchor='nw', window=frame2)

        traceD1_id=self.variableD1.trace('w',checksetting)
        traceD2_id=self.variableD2.trace('w',checksetting)



    def brightness_set(self,darkimagename,brightimagename,posX,posY,posX1,posY1,posX2,posY2):
        self.klicked=False

        path = self.parent / darkimagename
        darkscreen = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / brightimagename
        brightscreen=ImageTk.PhotoImage(Image.open(path))
        label=tk.Label(root,image=brightscreen)
        labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)

        def replacelabel(labelwindow,tkimage):
            self.canvas.delete(labelwindow)
            label=tk.Label(root,image=tkimage)
            labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)
            
        def checksetting(*args):
            if self.variableD1.get()<=0.08 or self.variableD2.get()<=37.0:
                replacelabel(labelwindow,darkscreen)
                if self.variableD1.get()<0.08 and self.variableD2.get()<14.0 and (self.variable1.get()+self.variable2.get())==int(2):
                    self.variable1.trace_vdelete('w',trace1_id)
                    self.variable2.trace_vdelete('w',trace2_id)
                    self.variableD1.trace_vdelete('w',traceD1_id)
                    self.variableD2.trace_vdelete('w',traceD2_id)
                    self.next()

            else:
                replacelabel(labelwindow,brightscreen)

        frame1=self.brightness_checkbuttons(select=False)
        self.canvas.create_window(posX1, posY1, anchor='nw', window=frame1)

        frame2=self.brightness_scales(value1=0.25,value2=48)
        self.canvas.create_window(posX2, posY2, anchor='nw', window=frame2)

        trace1_id=self.variable1.trace('w',checksetting)
        trace2_id=self.variable2.trace('w',checksetting)
        traceD1_id=self.variableD1.trace('w',checksetting)
        traceD2_id=self.variableD2.trace('w',checksetting)


    def setprobescreen(self,imagename,buttonimagename,posX,posY):
        path = self.parent / imagename
        self.buttonimage1 = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / buttonimagename
        self.buttonimage2 = ImageTk.PhotoImage(Image.open(path))

        label_frame=tk.LabelFrame(root,width=995,height=715)
        label=tk.Label(label_frame,image=self.buttonimage1,cursor='circle')
        label.place(x=0,y=0)
        button = tk.Button(label_frame, image=self.buttonimage2,highlightthickness=0,borderwidth=0,relief=tk.FLAT,cursor='circle')
        button.place(x=483,y=286)
        button.bind('<Button-1>', lambda event: self.next())
        self.canvas.create_window(posX, posY, anchor='nw', window=label_frame)

    
    def frequencysweep_field(self,letterwidth,positionX,positionY):

        def numbers(entry):
            try:
                number=float(entry.get())
                if number > 0.1 or number <0 :
                    self.failmessage()
                else:
                    self.next()
            except:
                self.failmessage()


        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: numbers(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)

    


    def driving_amplitude(self,letterwidth,imagen0,imagen1,imagen2,positionX,positionY,posX,posY,posX1,posY1,posX2,posY2):
        self.klicked=False

        number=0.1
        returnnumber=0.061

        path = self.parent / imagen0
        screen0 = ImageTk.PhotoImage(Image.open(path))
        path = self.parent / imagen1
        screen1=ImageTk.PhotoImage(Image.open(path))
        path = self.parent / imagen2
        screen2=ImageTk.PhotoImage(Image.open(path))

        label=tk.Label(root,image=screen0,highlightthickness=0,borderwidth=0 )
        labelwindow=self.canvas.create_window(posX, posY, anchor='nw', window=label)

        driving_amp= tk.Label(root, text = number, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=3)
        driving_amp_w=self.canvas.create_window(posX1, posY1, anchor='nw', window=driving_amp)
  
        free_amp = tk.Label(root, text = returnnumber, background='white',highlightthickness=0,borderwidth=0, height=1, width=5) 
        free_amp_w=self.canvas.create_window(posX2, posY2, anchor='nw', window=free_amp)



        def replacelabel(labelwindow,driving_amp_w,free_amp_w,tkimage,number,returnnumber):
            self.canvas.delete(labelwindow)
            label=tk.Label(root,image=tkimage,highlightthickness=0,borderwidth=0)
            labelwindow=self.canvas.create_window(posX, posY, anchor='nw',window=label)
 
            self.canvas.delete(driving_amp_w)
            driving_amp= tk.Label(root, text = number, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=3)
            driving_amp_w=self.canvas.create_window(posX1, posY1, anchor='nw', window=driving_amp)
 
            self.canvas.delete(free_amp_w)
            free_amp = tk.Label(root, text = returnnumber, background='white',highlightthickness=0,borderwidth=0, height=1, width=5) 
            free_amp_w=self.canvas.create_window(posX2, posY2, anchor='nw', window=free_amp)


        def checksetting(entry):
            try:
                number=float(entry.get())
                returnnumber=number*0.425
                if returnnumber<0 or returnnumber>3:
                    self.klicked=False
                    self.failmessage()
                elif returnnumber<0.57:
                    self.klicked=False
                    replacelabel(labelwindow,driving_amp_w,free_amp_w,screen0,number,returnnumber)
                elif returnnumber>=0.57 and returnnumber <1.4:
                    self.klicked=False
                    replacelabel(labelwindow,driving_amp_w,free_amp_w,screen1,number,returnnumber)
                else:
                    self.klicked=True
                    replacelabel(labelwindow,driving_amp_w,free_amp_w,screen2,number,returnnumber)
            except:
                self.klicked=False
                self.failmessage()



        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: checksetting(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)

        
    def setpoint(self,letterwidth,positionX,positionY):
        self.klicked=False
        def numbers(entry):
            try:
                number=float(entry.get())
                if number > 1.5 or number <1.1 :
                    self.klicked=False
                    self.failmessage()
                else:
                    self.klicked=True
            except:
                self.klicked=False
                self.failmessage()

       
        field=tk.Entry(root,width=letterwidth)
        field.bind('<Return>', lambda event: numbers(field))
        self.canvas.create_window(positionX, positionY, anchor='nw', window=field)




    def scan_settings(self,letterwidth,posX,posY,originX,originY,scale=2):

        self.klicked=False


        label1= tk.Label(root, textvariable = self.variableS1, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label1=self.canvas.create_window(posX, posY-19, anchor='nw', window=label1)

        label2= tk.Label(root, textvariable = self.variableS2, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label2=self.canvas.create_window(posX+35, posY-19, anchor='nw', window=label2)

        label3= tk.Label(root, textvariable = self.variableS3, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label3=self.canvas.create_window(posX+70, posY-19, anchor='nw', window=label3)

        label4= tk.Label(root, textvariable = self.variableS4, background='lightgray',highlightthickness=0,borderwidth=0, height=1, width=7)
        label4=self.canvas.create_window(posX+105, posY-19, anchor='nw', window=label4)

                
        rectangle_w=self.canvas.create_line(originX-round(scale*float(self.variableS3.get())*0.5),originY-round(scale*float(self.variableS4.get())*0.5),originX+round(scale*float(self.variableS3.get())*0.5),originY-round(scale*float(self.variableS4.get())*0.5),originX+round(scale*float(self.variableS3.get())*0.5),originY+round(scale*float(self.variableS4.get())*0.5),originX-round(scale*float(self.variableS3.get())*0.5),originY+round(scale*float(self.variableS4.get())*0.5),originX-round(scale*float(self.variableS3.get())*0.5),originY-round(scale*float(self.variableS4.get())*0.5),width=2,fill='yellow',tags='rectangle')
        

        def make_rectangle(rectangle_w,scale,originX,originY):
            try:
                self.canvas.delete('rectangle')
                originX_shifted=originX+round(scale*float(self.variableS6.get()))
                originY_shifted=originY-round(scale*float(self.variableS7.get()))


                rectangle_w=self.canvas.create_line(originX_shifted-round(scale*float(self.variableS3.get())*0.5),originY_shifted-round(scale*float(self.variableS4.get())*0.5),originX_shifted+round(scale*float(self.variableS3.get())*0.5),originY_shifted-round(scale*float(self.variableS4.get())*0.5),originX_shifted+round(scale*float(self.variableS3.get())*0.5),originY_shifted+round(scale*float(self.variableS4.get())*0.5),originX_shifted-round(scale*float(self.variableS3.get())*0.5),originY_shifted+round(scale*float(self.variableS4.get())*0.5),originX_shifted-round(scale*float(self.variableS3.get())*0.5),originY_shifted-round(scale*float(self.variableS4.get())*0.5),width=2,fill='yellow',tags='rectangle')
            except:
                None
 

        def checksetting(*args):
            try:
                if float(self.variableS1.get())<4 or float(self.variableS2.get())<4 or float(self.variableS3.get())<=0 or float(self.variableS4.get())<=0 or float(self.variableS1.get())>512 or float(self.variableS2.get())>512 or float(self.variableS5.get())<0 or float(self.variableS5.get())>10 :
             
                    self.klicked=False
                    self.failmessage()

                elif  float(self.variableS3.get())*0.5+abs(float(self.variableS6.get()))>50:
                    if abs(float(self.variableS6.get()))<49:
                        self.variableS3.set(str(100-2*round(abs(float(self.variableS6.get())))))
                    else:
                        self.variableS6.set('49')
                        self.variableS3.set('1')

                    make_rectangle(rectangle_w,scale,originX,originY)
                    self.klicked=False
                    self.failmessage()


                elif  float(self.variableS4.get())*0.5+abs(float(self.variableS7.get()))>50:
                    if abs(float(self.variableS7.get()))<49:
                        self.variableS4.set(str(100-2*round(abs(float(self.variableS7.get())))))
                    else:
                        self.variableS7.set('49')
                        self.variableS4.set('1')

                    make_rectangle(rectangle_w,scale,originX,originY)
                    self.klicked=False
                    self.failmessage()


                else:
                    make_rectangle(rectangle_w,scale,originX,originY)
                    self.klicked=True
            except:
                self.klicked=False
                self.failmessage()


        field1=tk.Entry(root,width=letterwidth,textvariable=self.variableS1)
        field1.bind('<Return>', lambda event: checksetting(field1))
        self.canvas.create_window(posX, posY, anchor='nw', window=field1)

        field2=tk.Entry(root,width=letterwidth,textvariable=self.variableS2)
        field2.bind('<Return>', lambda event: checksetting(field2))
        self.canvas.create_window(posX, posY+20, anchor='nw', window=field2)

        field3=tk.Entry(root,width=letterwidth,textvariable=self.variableS3)
        field3.bind('<Return>', lambda event: checksetting(field3))
        self.canvas.create_window(posX, posY+80, anchor='nw', window=field3)

        field4=tk.Entry(root,width=letterwidth,textvariable=self.variableS4)
        field4.bind('<Return>', lambda event: checksetting(field4))
        self.canvas.create_window(posX, posY+100, anchor='nw', window=field4)


        field5=tk.Entry(root,width=letterwidth,textvariable=self.variableS5)
        field5.bind('<Return>', lambda event: checksetting(field5))
        self.canvas.create_window(posX, posY+280, anchor='nw', window=field5)


        field6=tk.Entry(root,width=letterwidth,textvariable=self.variableS6)
        field6.bind('<Return>', lambda event: checksetting(field6))
        self.canvas.create_window(posX, posY+140, anchor='nw', window=field6)

        field7=tk.Entry(root,width=letterwidth,textvariable=self.variableS7)
        field7.bind('<Return>', lambda event: checksetting(field7))
        self.canvas.create_window(posX, posY+160, anchor='nw', window=field7)


        #trace1_id=self.variableS1.trace('w',checksetting)
        #trace2_id=self.variableS2.trace('w',checksetting)
        #trace3_id=self.variableS3.trace('w',checksetting)
        #trace4_id=self.variableS4.trace('w',checksetting)
        #trace5_id=self.variableS5.trace('w',checksetting)










    def numbers(self,entry):
        number=float(entry.get())+1
        print(number)
        if number > 5 :
            self.quiting()
        else:
            self.failmessage()
           
    def failmessage(self):
        fail = tk.Label(root, text = "WRONG VALUE ENTERED", background='red', height=3, width=30) 
        self.canvas.create_window(130, 200, anchor='nw', window=fail)

    def failmessage_brightness(self):
        fail = tk.Label(root, text = "Adjust Brightness first !!!", background='red', height=3, width=30) 
        self.canvas.create_window(360, 630, anchor='nw', window=fail)



    def next(self):
        self.canvas.delete("all")
        root.quit()


    def hello(self,*args):
        print("Single Click, Button-l")
        print(self.variable1.get()+self.variable2.get())
        print(self.variableD1.get())
        print(self.variableD2.get())

    def quiting(self):                           
        print("Double Click, so let's stop")
        self.canvas.delete("all")
        root.quit()

    def show(self):
        self.pack(fill="both", expand=True)
        root.mainloop()


    def z_raise(self):
        if self.z_state>1:
            self.z_state=self.z_state-1
        self.next()

    def z_lower(self):
        if self.z_state<10:
            self.z_state=self.z_state+1
        self.next()

    def z_zero_focus(self):
        self.klicked=True
        self.next()


    def x_right(self):
        if self.x_state<1:
            self.x_state=self.x_state+1
        self.next()

    def x_left(self):
        if self.x_state>0:
            self.x_state=self.x_state-1
        self.next()

    def y_up(self):
        if self.y_state<1:
            self.y_state=self.y_state+1
        self.next()

    def y_down(self):
        if self.y_state>0:
            self.y_state=self.y_state-1
        self.next()

    def cant_raise(self):
        if self.z_state<2:
            self.z_state=self.z_state+1
        self.klicked=False
        self.next()

    def cant_lower(self):
        if self.z_state>0:
            self.z_state=self.z_state-1
        self.klicked=False
        self.next()

    def cant_focusrequest(self):
        self.klicked=True
        fail = tk.Label(root, text = "CHOOSE A DIFFERENT DEFOCUS !!", background='red', height=3, width=30)
        self.canvas.create_window(570, 600, anchor='nw', window=fail)
        if self.z_state==1:
            self.next()

    def next_if_klicked(self):
        if self.klicked==True:
            self.next()
            self.klicked=False

        

if __name__ == "__main__":
    root = tk.Tk()
    p=Example(root)


#    start here
    p.frameimage("0-start-program.png")
    p.button1("b_ControlFive.png",p.next,37,432)
    p.show()
    
    p.frameimage("1-start-program.png")
    p.button2("b_ok1.png",p.next,403,531)
    p.show()

    p.frameimage("2-Raman-CCD-cooldown-wait.png")
    p.button1("b_configurations.png",p.next,235,30)
    p.show()

    p.frameimage("3_0-config-menue-AFM-AC.png")
    p.button1("b_AFM.png",p.next,293,71)
    p.show()

    p.frameimage("3-config-menue-AFM-AC.png")
    p.button1("b_AFM-AC.png",p.next,520,128)
    p.show()

    p.frameimage("5-AFM-menues.png")
    p.button2("b_Adjustment.png",p.next,5,250)
    p.show()

    p.frameimage("6-AFM-adjustment-menue.png")
    p.lasermenu("b_Laser-on.png",210,270)
    p.show()

    p.frameimage("7-AFM-adjustment-menue-laser-off.png")
    p.button2("b_z-up.png",p.next,397,745)
    p.show()

    p.frameimage("8-AFM-z-stage-up.png")
    p.button2("b_ok2.png",p.next,657,621)
    p.show()

    p.frameimage("9-AFM-pre-focus-1.png")
    p.button2("b_z-down.png",p.next,397,795)
    p.show()

    p.frameimage("10-AFM-pre-focus-2-before-brightness-adjustment.png")
    p.button3("b_y-button.png",p.next,530,150)
    p.button2("b_z-down.png",p.failmessage_brightness,397,795)
    p.show()

# find z focus

    imagelist=["11-AFM-pre-focus-2-after-brightness-adjustment.png","12-AFM-pre-focus-3.png","12-AFM-pre-focus-4.png","12-AFM-pre-focus-5.png","12-AFM-pre-focus-6.png","12-AFM-pre-focus-7.png","12-AFM-pre-focus-8.png","12-AFM-pre-focus-9.png","12-AFM-pre-focus-10.png","12-AFM-pre-focus-11.png"]

    while (p.z_state is not 7 or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist[p.z_state-1])
        p.button3("b_z-up.png",p.z_raise,397,745)
        p.button2("b_z-down.png",p.z_lower,397,795)
        p.button4("b_zero-focus.png",p.z_zero_focus,482,826)
        p.show()


# find sample region

    imagelist = ["13-AFM-heigth-zeroed.png","14-AFM-area-1.png","14-AFM-area-3-nothing.png","14-AFM-area-found.png"]
    
    p.klicked=False
    while ((p.x_state is not 1 or p.y_state is not 1) or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist[2*p.x_state+p.y_state])
        p.button3("b_x-right.png",p.x_right,562,769)
        p.button2("b_x-left.png",p.x_left,511,769)
        p.button4("b_y-up.png",p.y_up,537,745)
        p.button5("b_y-down.png",p.y_down,537,795)
        p.button6("b_zero-focus.png",p.z_zero_focus,604,834)
        p.show()


    p.frameimage("14-AFM-area-zero-x-y.png")
    p.button2("b_z-up.png",p.next,397,745)
    p.show()

    p.frameimage("15_0-AFM-mount-message.png")
    p.button2("b_ok2.png",p.next,633,458)
    p.show()

    p.frameimage("15-AFM-tip-visible-before-adjustment.png")
    p.button2("b_start-adjustment.png",p.next,212,292)
    p.show()

    p.frameimage("16-AFM-adjustment-1-cantilever-pos.png")
    p.button2("b_cant-down.png",p.next,167,716)
    p.show()

    p.frameimage("16-AFM-adjustment-1-cantilever-pos-2.png")
    p.button2("b_cant-right.png",p.next,267,691)
    p.button3("b_cant-backward.png",p.next,242,716)
    p.show()

    p.frameimage("16-AFM-adjustment-1-cantilever-pos-3.png")
    p.button2("b_illum-top.png",p.next,893,354)
    p.show()


    p.frameimage("16-AFM-adjustment-1-cantilever-pos-3-2.png")
    p.button2("b_ok2.png",p.next,645,309)
    p.show()


    p.frameimage("16-AFM-adjustment-1-cantilever-pos-3-1.png")
    p.button2("b_illum-setting.png",p.next,893,324)
    p.show()


    p.frameimage("16-AFM-adjustment-1-cantilever-pos-4.png")
    p.brightness_unset(928,402,928,585)
    p.show()

    p.frameimage("16-AFM-adjustment-1-cantilever-pos-5.png")
    p.button2("b_cant-forward.png",p.next,242,666)
    p.show()


    p.frameimage("16-AFM-adjustment-1-cantilever-pos-9-laser-z.png")
    p.brightness_change("label_dark-video.png","label_bright-video.png",385,351,1415,573)
    p.show()


    imagelist_ok=["16-AFM-adjustment-1-cantilever-pos-7-laser-z_ok.png","16-AFM-adjustment-1-cantilever-pos-8-laser-z_ok.png","16-AFM-adjustment-1-cantilever-pos-6-laser-z_ok.png"]


    p.klicked=False
    p.z_state=0
    while (p.z_state is not 1 or p.klicked is False):
        p.klicked=False
        p.frameimage(imagelist_ok[p.z_state])
        p.button2("b_cant-up.png",p.cant_raise,167,666)
        p.button3("b_cant-down.png",p.cant_lower,167,716)
        p.button4("b_ok2.png",p.cant_focusrequest,576,510)
        p.show()

    p.frameimage("16-AFM-adjustment-1-cantilever-pos-10-laser-z.png")
    p.brightness_set("label_dark-video.png","label_bright-video-final-z.png",385,351,1415,391,1415,573)
    p.show()
    
    p.frameimage("16-AFM-adjustment-1-cantilever-pos-last.png")
    p.button2("b_illum-top_off.png",p.next,1385,354)
    p.show()

    p.frameimage("17_0-AFM-adjustment-1-probe-position.png")
    p.button2("b_video-menu.png",p.next,385,324)
    p.show()

    p.frameimage("17_1-AFM-adjustment-1-probe-position.png")
    p.button2("b_set-probe-position.png",p.next,387,380)
    p.show()

    p.frameimage("17-AFM-adjustment-1-probe-position.png")
    p.setprobescreen("label_set-probe-video.png","b_probe-tip.png",385,350)#,870,635)
    p.show()

    p.frameimage("17-AFM-adjustment-1-probe-position-final.png")
    p.button2("b_next-step-1.png",p.next,212,312)
    p.show()

    p.frameimage("18-AFM-adjustment-diode.png")
    p.button2("b_ok2.png",p.next,936,971)
    p.show()

    p.frameimage("18-AFM-adjustment-diode-2.png")
    p.button2("b_z-down.png",p.next,397,1183)
    p.show()

    p.frameimage("18-AFM-adjustment-diode-3.png")
    p.button2("b_ok2.png",p.next,1050,1018)
    p.show()

    p.frameimage("18-AFM-adjustment-diode-3.png")
    p.button2("b_ok2.png",p.next,1050,1018)
    p.show()

    p.frameimage("18-AFM-adjustment-diode-4_0.png")
    p.button2("b_next-step-1.png",p.next,211,311)
    p.show()

    p.frameimage("19-AFM-adjustment-1.png")
    p.frequencysweep_field(10,212,391)
    p.show()

    p.frameimage("19-AFM-adjustment-2.png")
    p.driving_amplitude(10,"label_amplitude_small.png","label_amplitude_medium.png","label_amplitude_big.png",212,391,730,1097,280,373,617,1340)  #(self,imagen0,imagen1,image2,positionX,positionY,posX,posY,posX1,posY1,posX2,posY2):
    p.button2("b_next-step-1.png",p.next_if_klicked,211,311)
    p.show()

    p.frameimage("20-AFM-adjustment.png")
    p.setpoint(10,212,671)
    p.button2("b_next-step-1.png",p.next_if_klicked,211,311)
    p.show()

    p.frameimage("21_0-AFM-adjustment.png")
    p.button2("b_ok2.png",p.next,615,719)
    p.show()

    p.frameimage("21-AFM-adjustment-before-approach.png")
    p.button2("b_tip-approach.png",p.next,485,43)
    p.show()

    p.frameimage("23-approach-sucsess.png")
    p.button2("b_image-scan.png",p.next,6,811)
    p.show()

    p.frameimage("24-scan-window.png")
    p.scan_settings(10,211,831,884,648,scale=2)
    p.button2("b_start-scan.png",p.next_if_klicked,212,1052)
    p.show()

    p.frameimage("25-scan-window.png")
    p.scan_settings(10,211,831,1167,756,scale=5.6)
    p.button2("b_start-scan.png",p.next_if_klicked,212,1052)
    p.show()

    p.frameimage("26-scan-window.png")
    p.button2("b_tip-lift.png",p.next,508,43)
    p.show()

    p.frameimage("27-tip-lifted.png")
    p.button2("b_z-up.png",p.next,397,1133)
    p.show()

    p.frameimage("28-sample-lift.png")
    p.button2("b_ok2.png",p.next,509,775)
    p.show()

