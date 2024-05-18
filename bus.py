from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import time
from datetime import *
import random
import mysql.connector as mysql
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import shutil
import os
import pandas

#Title of the project
root=Tk()
root.title("bus registration project")
root.geometry("1920x1080")
label=Label(root,text="BUS REGISTRATION AND PAYMENT SYSTEM",font=("arial","20","italic","bold"))
label.pack()

menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=file)

    #components of menubar
file.add_command(label="New file!",command=None)
file.add_command(label="open",command=None)

file.add_command(label="Save",command=None)
file.add_separator()
def hi3():                   #destroy the screen
    root.destroy()

file.add_command(label="Exit",command=hi3)

#adding bus picture int eh frame
#adding  background
'''img =ImageTk.PhotoImage(Image.open("C:\\Users\\gopin\\Downloads\\buss.jpg"))
panel = Label(root, image=img)
panel.pack(side = "bottom", fill="both", expand="true")'''

    #adding edit bar


root.configure(menu=menubar)
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Cut",command=None)
edit.add_command(label="Copy",command=None)
edit.add_command(label="Paste",command=None)
edit.add_separator()

    #adding options of help button

help_=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=help_)
help_.add_command(label="license",command=None)
help_.add_command(label="contact",command=None)
help_.add_command(label="about us",command=None)
help_.add_separator()
help_.add_command(label="About app",command=None)

    #clock
def clock():
    bb=datetime.now()
    current=bb.strftime("%H:%M:%S")
    label1["text"]=current
    root.after(1000,clock)
    
   #time
label1=Label(root,font=("article 30"),fg="black")
label1.place(x=1200,y=5)
clock()
text1=Label(root,text="Time",font=("","18",""))
text1.place(x=1250,y=70)

 #Passenger name
name=StringVar()
name1=Label(root,text="Passenger",font=("","18",""))
name1.place(x=80,y=80)
name2=Entry(root,font=("","18",""),textvariable=name)
name2.place(x=250,y=80)

#distination

#customer location
dis=StringVar()
dis1=Label(root,text="Distination start",font=("","18",""))
dis1.place(x=80,y=170)
dis2=Entry(root,font=("","18",""),textvariable=dis)
dis2.place(x=250,y=170)

#to variable
to=Label(root,text="To",font=("","12","")).place(x=350,y=215)

#cuatomer last location
loc=StringVar()
loc1=Label(root,text="Distination End",font=("","18",""))
loc1.place(x=80,y=250)
loc2=Entry(root,font=("","18",""),textvariable=loc)
loc2.place(x=250,y=250)

#Bus available by checkbox
bus=StringVar()
bus1=Label(root,text="Bus selection",font=("","18","")).place(x=80,y=320)
course_selection=["--select Bus--","Archana","Bevilnest", "Dapercet", "Electron", "Flutogen", "Greenbus", "Marine_travels","Roseberry","Pnkernet","Saroja travels","Vanakumango","Venila","Zero gravity"]
combo=ttk.Combobox(root,values=course_selection,width=20,height = 20,textvariable=bus)
combo.place(x=253,y=325)
def comboo(*args):
    return bus.get()
bus.trace('w',comboo)

# Email id
email=StringVar()
email1=Label(root,text="MAil id",font=("","18","")).place(x=80,y=390)
email2=Entry(root,font=("","18",""),textvariable=email).place(x=250,y=390)

#mobile no
mobile=StringVar()
mobile1=Label(root,text = "Mobile no",font=("","18","")).place(x=80,y=450)  
mobile2= Entry(root,font=("","18",""),textvariable=mobile).place(x=250,y=450)

#Informations
info=Label(root,text="NOTE",font=("","12",""),foreground="red").place(x=1200,y=130)
info1= Label(root,text="1. Our serivices are completly free for low class peoples")
info1.place(x=1100,y=170)
info2= Label(root,text="2. Only 1,20,000 LPA families can only use this service")
info2.place(x=1100,y=190)
info3= Label(root,text="3. Head of the family should show their company id card for our verification")
info3.place(x=1100,y=210)
info4= Label(root,text="4. Maximum 6 persons can travel from a family")
info4.place(x=1100,y=230)
info5= Label(root,text="5. If any issues or problem may contact our services")
info5.place(x=1100,y=250)



#payment paid
payment=StringVar()
payment1=Label(root,text="Payment paid",font=("",18,"")).place(x=80,y=520)
payment2=Checkbutton(root,text="Yes",font=("",18,""),variable=payment,onvalue=1,offvalue=0,height=1,width=2).place(x=270,y=520)
payment3=Checkbutton(root,text="No",font=("",18,""),variable=payment,onvalue=1,offvalue=0,height=1,width=2).place(x=350,y=520)


# Define the function to upload and save the image

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))  # Resize image if necessary
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        save_image(file_path)
        messagebox.showinfo("Success", "Image uploaded successfully!")
 
def save_image(file_path):
    save_dir = "C:\\Users\\gopin\\OneDrive\\Pictures\\Saved Pictures"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    filename = os.path.basename(file_path)
    shutil.copy(file_path, os.path.join(save_dir, filename))
    print("Image saved to:", os.path.join(save_dir, filename))

 # Create and pack widgets
uploadbutton = Label(root,text="upload screenshot", font=("","18","")).place(x=80,y=600)
upload_button = ttk.Button(root, text="Upload Image", command=upload_image)
upload_button.place(x=330,y=600)
 
image_label = ttk.Label(root)
image_label.place(x=600,y=900)

#Paseenger seats
seat=StringVar()
seat1=Label(root,text = "Seat reserving",font=("","18","")).place(x=600,y=80)  
#seat2= Entry(root,font=("","18",""),textvariable=seat).place(x=800,y=80)
seat2=["--select Bus--","Window seat","Center Seat"]
combo=ttk.Combobox(root,values=seat2,width=20,height = 20,textvariable=seat)
combo.place(x=800,y=82)
def comboos(*args):
    return seat.get()
bus.trace('w',comboos)

#head of the family
head=StringVar()
head1=Label(root,text = "Head of family",font=("","18","")).place(x=600,y=170)  
head2= Entry(root,font=("","18",""),textvariable=head).place(x=800,y=170)

#Occupation
occupation=StringVar()
occupation1=Label(root,text = "Occupation",font=("","18","")).place(x=600,y=250)  
occupation2= Entry(root,font=("","18",""),textvariable=occupation).place(x=800,y=250)

#Number of passengers
pas=StringVar()
pas1=Label(root,text="Passengers",font=("","18","")).place(x=600,y=320)
pas2=["--select Members--","1","2","3","4","5","6"]
combo=ttk.Combobox(root,values=pas2,width=20,height = 20,textvariable=pas)
combo.place(x=800,y=320)

#qr button
def hii():
    #f=open("jaysree_qr.jpg")
    image_path='C:\\Users\\gopin\\Downloads\\jaysree_qr.jpg'
    if os.path.exists(image_path):
        img=Image.open(image_path)
        img.show()
    else:
        print("Image isn't available")
    
qr=Button(root,text="Qr Scanner",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black",command=hii)
qr.place(x=1150,y=340)

#qr text
t=Label(root,text="Requestion",font=("","12",""),foreground="red").place(x=1180,y=300)

#date of registration
date=StringVar()
date1 = Label(root,text="Reservation date",font=("","18","")).place(x=600,y=390)
date2= Entry(root,font=("","18",""),textvariable=date).place(x=800,y=390)

#ticket reserving date
date_r=StringVar()
date1_r= Label(root,text="Applying date",font=("","18","")).place(x=600,y=450)
date2_r= Entry(root,font=("","18",""),textvariable=date_r).place(x=800,y=450)


#reqestion for qr box
#Informations
info=Label(root,text="NOTE",font=("","12",""),foreground="red").place(x=1200,y=130)
info1= Label(root,text="1. Please provide an payment for our convinent fee")
info1.place(x=1100,y=410)
info2= Label(root,text="2. provide only 300rs per family")
info2.place(x=1100,y=430)
info3= Label(root,text="3. Verification box is provided in a form")
info3.place(x=1100,y=450)

#Service number
sn=Label(root,text="Helpline service",font=("","12",""),foreground="red").place(x=1160,y=510)
sn1= Label(root,text="1. Meera Sri - 63810 27119")
sn1.place(x=1100,y=550)
sn2= Label(root,text="2. Sowndharya - 87543 40806")
sn2.place(x=1100,y=570)
sn3= Label(root,text="3. Janani - 78100 93181")
sn3.place(x=1100,y=590)
sn4= Label(root,text="4. Jayasree - 70927 79615")
sn4.place(x=1100,y=610)
sn5= Label(root,text="5. Gunavarshini - 63827 88327")
sn5.place(x=1100,y=630)



#Save button
def mayir():
    import mysql.connector as mysql
    mydb= mysql.connect(host="localhost",user="root",password="1234",database="clg",auth_plugin="mysql_native_password")
    mycursor=mydb.cursor()
    mycursor.execute("insert into entry2(Pasenger, Start_, End_, Bus_Selection, Mail_id, Mobile_no, Payment, seat, family_head, occupaton, Count, Reserve_date, Applying_date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name.get(), dis.get(), loc.get(), comboo(), email.get(), mobile.get(), payment.get(), seat.get(), head.get(), occupation.get(), pas.get(), date.get(), date_r.get()] )
    print("Details are saved sucessfully")
    mydb.commit()
    root.destroy()

label=Button(root,text="Save details",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black",command=mayir)
label.place(x=1170,y=710)

#exit button
def hiii():                     #destroy the screen
    messagebox.showerror("Askquestion","Are you sure?")
    root.destroy()
exits=Button(root,text="Cancel",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black", command=hiii)
exits.place(x=1380,y=710)






