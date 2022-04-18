from tkinter import*
import random
root=Tk()
root.title('Joyboy')
root.geometry('500x500')
root.configure(background='#13bc3d')
entername=Entry(root)
entername.place(relx=0.5,rely=0.2,anchor=CENTER)
friendslist=Label(root)
rn=Label(root)
Best_Anime_Charecter=Label(root)

list19=[]
def Add_Charecter():
    Charname=entername.get()
    list19.append(Charname)
    friendslist["text"]="Listed_Items"+str(list19)
def random_number():
    length=len(list19)
    random_no=random.randint(0,length-1)
    rn["text"]=str(random_no)
    Best_Anime_Charecter=list19[random_no]   
    Best_Anime_Charecter["text"]="Fan-Favorite Charecters are going to be..."+str(Best_Anime_Charecter)    
butt=Button(root,text="Fan-Favorite Charecters are",command=random_number)
butt.place(relx=0.5,rely=0.5,anchor=CENTER)
friendslist.place(relx=0.5,rely=0.4,anchor=CENTER)
but=Button(root,text="Listed_Items",command=Add_Charecter)
but.place(relx=0.5,rely=0.3,anchor=CENTER)
rn.place(relx=0.5,rely=0.6,anchor=CENTER)

Best_Anime_Charecter.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
