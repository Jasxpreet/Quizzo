from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import tkinter
import mysql.connector as mysql

questions=[" Which of the following are pre-defined or reserved words?",
           " Which of the following literals must terminate in one line?",
           " Which of the following literal has either True or False value?",
           " Which of the following are symbols logical comparison in a program?",
           " Which of the following is correct computer square of variable x in python?",
           " _______ to display the values without decimal place after division",
           " Which of the following is a correct statement?",
           " In python, the single line comments starts with _______",
           " In python, the multiline comments starts with ________",
           " _______ are additional readable information to clarify the statement in python.",
           " By default the input() function returns",
           " If a function does not return a value, what value will be returned in a function?",
           " The output of d= a + b % c is _________, if a = 12, b=5 and c=3.",
           " Evaluate x % y // x, if x = 5, y = 4",
           " Which of these arithematic operator will evaluate first?",
           " Which of these relational operator has highest operator precedence?",
           " Which of the followiing logical operator will evaluate first?",
           " How a>b>c will be interpreted by python?",
           " _____ are stored as individual characters in contiguous locations",
           " What is the output of – “5” + “5” ?"
           ]
choice=[
        ["A. Identifiers","B. Literals","C. Keywords","D. Operators"],
        ["A. Single line Strings","B. Multi line strings","C. Numeric Literals","D. All of the above"],
        ["A. Special Literals","B. Boolean Literals","C. Numeric Literals","D. String Literals"],
        ["A. Identifiers","B. Literals","C. Keywords","D. Operators"],
        ["A. x * 2","B. x power 2","C. x ** 2","D. x // 2"],
        ["A. /","B. //","C. %","D. **"],
        ["A. xyz = 10 100 1000","B. x y z = 10 100 1000","C. x, y, z = 10, 100, 1000","D. x y z= 10, 100, 1000"],
        ["A. /","B. //","C. #","D. '''"],
        ["A. /","B. //","C. #","D. '''"],
        ["A. Comments","B. Expressions","C. Tokens","D. Flow of control"],
        ["A. Integer","B. Float","C. Boolean","D. String"],
        ["A. int","B. void","C. bool","D. none"],
        ["A. 14","B. 2","C. 5","D. 17"],
        ["A. 1.0","B. 0.0","C. 0","D. 1"],
        ["A. +","B. -","C. **","D. %"],
        ["A. <","B. >=","C. <=","D. =="],
        ["A. and","B. or","C. not","D. is not"],
        ["A. a>b or a>c","B. a>b not a>c","C. a>b and a>c","D. a>b && a>c"],
        ["A. lists","B. tuples","C. strings","D. dictionaries"],
        ["A. 25","B. 55","C. 10","D. error"]
    ]
answer=[2,0,1,3,2,1,2,2,3,0,3,3,0,2,2,0,2,2,2,1]

user_ans=[]

indexes=[]

#ins=open("instruction.txt","r")
#instruction=ins.read()


def gen():
    while(len(indexes)<10):
        x=random.randint(0,19)
        
        if x in indexes:
            continue
        else:
            indexes.append(x)
                        
def showresult(score):
    l1.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    global label,label1,label2,btn 
    label=Label(win,text="Your score is:",font="times 25 bold",fg="black",justify="center",bg="blanched almond")
    label.place(x=230,y=220)

    if score!=10:
        label2=Label(win,text=str(score)+"/10",font="times 25 bold",fg="black",justify="center",bg="blanched almond")
        label2.place(x=434,y=220)
    else:
        label2=Label(win,text=str(score)+"/10",font="times 25 bold",fg="black",justify="center",bg="blanched almond")
        label2.place(x=434,y=220)
    
    btn1=Button(text="Quit",font="bold 18",command=win.destroy,bg="dark salmon")
    btn1.place(x=330,y=350)

def calc():
    global indexes, user_ans, answer
    x=0
    score=0
    for i in indexes:
        if user_ans[x]== answer[i]:
            score=score+1
        x+=1
    showresult(score)
ques=1

def select():
    global i,user_ans,l1,r1,r2,r3,r4,ques
    x=i.get()
    user_ans.append(x)
    i.set(-1)
    
    if ques<10:
        l1.config(text=questions[indexes[ques]])
        r1["text"]=choice[indexes[ques]][0]
        r2["text"]=choice[indexes[ques]][1]
        r3["text"]=choice[indexes[ques]][2]
        r4["text"]=choice[indexes[ques]][3]
        ques+=1
    else:
        calc()
def start():
    global l1,r1,r2,r3,r4
    l1=Label(win,text=questions[indexes[0]],font=("arial",12,"bold"),fg="black",bg="blanched almond")
    l1.place(x=50,y=150)

    global i 
    i=IntVar()
    i.set(-1)
    r1=Radiobutton(win,text=choice[indexes[0]][0],value=0,variable=i,font="times 12 bold",fg="black",bg="dark salmon",command=select)
    r1.place(x=270,y=200)

    r2=Radiobutton(win,text=choice[indexes[0]][1],value=1,variable=i,font="times 12 bold",fg="black",bg="dark salmon",command=select)
    r2.place(x=270,y=250)
    
    r3=Radiobutton(win,text=choice[indexes[0]][2],value=2,variable=i,font="times 12 bold",bg="dark salmon",fg="black",command=select)
    r3.place(x=270,y=300)
    
    r4=Radiobutton(win,text=choice[indexes[0]][3],value=3,variable=i,font="times 12 bold",fg="black",bg="dark salmon",command=select)
    r4.place(x=270,y=350)

def remove():
    global l,b,c
    l.destroy()
    b.destroy()
    c.destroy()
    gen()
    start()

def showinst():
		def closeinsrtuct():
			instwindow.destroy()
			
		instwindow=Tk()
		instwindow.title("Instructions")
		global fr2
		fr2=Frame(instwindow, width=500, height=340)
		ca2 = Canvas(fr2, height=340, width=500,bg="dark salmon")
		instlabel=Label(ca2,text=instruction,font="bold 14")
		close_but=Button(fr2, text="Close",width=10, height=1, command=closeinsrtuct)
		
		instlabel.place(x=20,y=40)
		close_but.place(x=200,y=290)
		ca2.pack()
		fr2.pack()
		instwindow.mainloop()

def welcome():
    global l,b,c
    l=Label(win,text="Welcome To The Quizzo",fg="black",font=("Cambria",30,"bold"),bg="blanched almond")
    l.place(x=144,y=120)

    b=Button(win,text="Start Quiz",font="bold 14",command=remove,bg="dark salmon")
    b.place(x=310,y=295)

    c=Button(win,text="Instruction",font="bold 14",command=showinst,bg="dark salmon")
    c.place(x=308,y=350)

def open_window():

    def check():
        name=Entry.get(e1)
        roll=Entry.get(e2)
        email=Entry.get(e3)
        unm=Entry.get(e4)
        password=Entry.get(e5)
        cpass=Entry.get(e6)

        if(name!="" and roll!="" and email!="" and password!="" and cpass!=""):
            if(password!=cpass):
                messagebox.showinfo("Error","Password Doesn't Match")
            else:
                con=mysql.connect(
                    host ="localhost",
                    user="root",
                    password="",
                    database="quiz"
                ) 
                cursor=con.cursor()
                cursor.execute("INSERT INTO users values('"+name+"','"+roll+"','"+email+"','"+unm+"','"+password+"','"+cpass+"')")

                cursor.execute("commit")
                messagebox.showinfo("Signup Status","Signup Successful")
                con.close()
                x=rem0()
        else:
            messagebox.showinfo("Error","please Fill All the Fields")

    global l,l1,l2,l3,l4,l5,l6,e1,e2,e3,e4,e5,e6,b1
    l=Label(win,text="Signup",fg="black",font="times 18 bold",bg="grey88")
    l.place(x=320,y=75)

    l1=Label(win,text="Name:",fg="black",font="times 14 bold",bg="blanched almond")
    l1.place(x=171,y=120)
    e1=Entry(win,bg="dark salmon",width=25,bd=3)
    e1.place(x=398,y=120)

    l2=Label(win,text="Enrollment No:",fg="black",font="times 14 bold",bg="blanched almond")
    l2.place(x=171,y=170)
    e2=Entry(win,bg="dark salmon",width=25,bd=3)
    e2.place(x=398,y=170)

    l3=Label(win,text="Email:",fg="black",font="arial 14 bold",bg="blanched almond")
    l3.place(x=171,y=220)
    e3=Entry(win,bg="dark salmon",width=25,bd=3)
    e3.place(x=398,y=220)

    l4=Label(win,text="Enter Username:",fg="black",font="times 14 bold",bg="blanched almond")
    l4.place(x=171,y=280)
    e4=Entry(win,bg="dark salmon",width=25,bd=3)
    e4.place(x=398,y=280)

    l5=Label(win,text="Enter Password:",fg="black",font="times 14 bold",bg="blanched almond")
    l5.place(x=171,y=330)
    e5=Entry(win,bg="dark salmon",width=25,bd=3)
    e5.place(x=398,y=330)

    l6=Label(win,text="Confirm Password:",fg="black",font="times 14 bold",bg="blanched almond")
    l6.place(x=171,y=380)
    e6=Entry(win,bg="dark salmon",width=25,bd=3)
    e6.place(x=398,y=380)

    b1=Button(win,text="Submit",fg="black",font="times 14 bold",bg="dark salmon",command=check)
    b1.place(x=320,y=430)

def rem1():
    global l1,l2,l0,e1,e2,b1,b2,fm,title1
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    title1.destroy()
    open_window()

def rem():
    global l1,l2,l0,e1,e2,b1,b2,fm,title1
    fm.destroy()
    l1.destroy()
    l2.destroy()
    l0.destroy()
    e1.destroy()
    e2.destroy()
    b1.destroy()
    b2.destroy()
    title1.destroy()
    welcome()

def rem0():
    global l1,l2,l3,l4,l5
    global e1,e2,e3,e4
    global e5,e6,b1
    l.destroy()
    l1.destroy()
    l2.destroy()
    l3.destroy()
    l4.destroy()
    l5.destroy()
    l6.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    e4.destroy()
    e5.destroy()
    e6.destroy()
    b1.destroy()
    login()

con=mysql.connect(
    host ="localhost",
    user="root",
    password="",
    database="quiz"
    )

cursor=con.cursor()

def user_login(uname,passw):
    try:
        cursor.execute("select * from `users` where `unm`='"+uname+"' and `password`='"+passw+"'")
        return (cursor.fetchone())
    except:
        return False

def msg():
    uname=Entry.get(e1)
    passw=Entry.get(e2)
    if (uname=="" or passw==""):
        messagebox.showinfo("Alert","Fill all Details")
    else:
        res=user_login(uname,passw)
        if res:
            messagebox.showinfo("Message","Login Successfully")
            x=rem()
        else:
            messagebox.showinfo("Alert","Login Failed")


win=tkinter.Tk()
win.title("Quizoo")
win.geometry("700x500")
win.resizable(width=False,height=False)

#back=Image.open("back.png")
#bck=back.resize((710,510))
#img=ImageTk.PhotoImage(bck,master=win)
#img2=Label(win,image=img)
#img2.place(x=0,y=0)

def login():
    global l1,l2,l0,e1,e2,b1,b2,fm,title1
    l0=Label(win,text="Login",fg="black",font=("arial",25,"bold"),bg="grey88")
    l0.place(x=305,y=110)

    fm=Frame(win,bd=4,relief=RIDGE,bg="blanched almond")
    fm.place(x=125,y=160,width=450,height=275)

    l1=Label(fm,text="Username:",fg="black",font="times 16 bold",padx=20,bg="blanched almond")
    l1.grid(row=1,column=0,padx=20,pady=40)
    e1=Entry(fm,bg="dark salmon",bd=2,font="times 12")
    e1.grid(row=1,column=1,padx=20)

    l2=Label(fm,text="Password:",fg="black",font="times 16 bold",padx=20,bg="blanched almond")
    l2.grid(row=2,column=0,padx=20,pady=40)
    e2=Entry(fm,bg="dark salmon",bd=2,font="times 12",show='x')
    e2.grid(row=2,column=1,padx=20)

    title1=Label(win, text="Quizzo",width=24,fg="black", font=("times",38,"bold"),bg="blanched almond")
    title1.place(x=0,y=0)

    b1=Button(fm,text="Login",font="times 13 bold",bg="dark salmon",command=msg)
    b1.grid(row=3,column=0,padx=70) 

    b2=Button(fm,text="Sign up",font="times 13 bold",bg="dark salmon",command=rem1)
    b2.grid(row=3,column=1)
login()

win.mainloop()