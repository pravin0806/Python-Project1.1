#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Budget game

def budget_game():
    #mumbai bot

    #user welcome
    print('welcome mumbai The city Dreams!')
    print('-'*30)
    #uska nam pucho
    user_name=input('please Enter Your Name:')
    #greeting karo
    print('hello',user_name.title())
    #tera budget kya hain
    budget=int(input('Enter your budget here:'))
    #1000> ola se ja
    if budget>1000:
        print('ola se ja')
    #500-1000 auto se ja
    elif budget>=500 and budget<1000:
        print('auto se ja')
    #100-500 bus se ja
    elif budget>=100 and budget<500:
        print('bus se ja')
    #100-10 train se ja 
    elif budget>=10 and budget<100:
        print('train se ja')
    #10 se kam ghar pe ja
    else:
        print('ghar pe ja')
    print('-'*30)

# Head and Tails Game

def head_and_tails():
    #welcome  user head and tail game!!
    print('-'*30)

    print('Welcome to world of Chanel!')
    #ask the user wether he want heads or tails
    user_input=input('Choose Heads or Tails')
    #display his choice
    print('you chose:',user_input.title())
    #coin toss(random.choice)
    import random
    if(random.choice('ht'))=='h':
        coin_toss=('Heads')
    else:
        coin_toss=('Tails')
    #diplay coin toss
    print('coin Result:',coin_toss)
    #compare user choie and coin toss
    if user_input.lower()==coin_toss.lower():
        print('you win')
    else:
        print('you lose!')

    print('-'*30)

# Dice Game

def dice_game():
    #welcome user
    print('Welcome to the Dice game')
    print('-'*30)

    #ask the user whether he want 1,2,3,4,5,6
    user_input=int(input('choose 1 2 3 4 5 6'))
    #diplay his choice
    print('you chose:',user_input)
    import random

    dice_roll=random.randrange(1,7)
    print('Dice roll',dice_roll)
    if user_input==dice_roll:
        print('you Win')
    else:
        print('you lose')
        
    print('-'*30)




# Matrication Table

def matrication_table():
    print('welcome Multiplication Table')
    num=int(input("Enter a number:"))


    #loop use karnege
    for a in range(1,11):
             print(num,'x',a, '=', num*a)
    print('-'*30)




# Cube 

def cube():
    #multiplication table 1 to100
    mul=int(input("Enter number here:"))
    #fir nsted lopp laginge
    for i in range(1,mul+1):
        print("\n")
        for j in range(1,11):
            print(i,"x",j,"=",i*j)

# Factorial

def factorial():
    print('Welcome to Factorial Game')
    print('-'*30)

    num=int(input("Enter no here"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print( num,' of factorial number answer is',fact)
    print('-'*30)




 #Fibonacii series

def fibonacii_series():
    print(' Welcome to Fibonacii series')
    n=int(input("Enter no"))
    x=0
    y=1
    z=0
    while(z<=n):
        print(z)
        x=y
        y=z
        z=x+y
    print('-'*30)



# Password Generator

def password_generator():
    print('Welcome Password Generator')
    #password generator
    print("Welcome to Password generator")
    #how many ch of pass do u want
    le=int(input("how many character of password do u want"))
    import random
    #condition
    password=''
    if le<8:
        print("use more character for strong password")
    else:
        li=[]
        for i in range(le):
            password=password+(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_'))
            

    print(password) 
    print('-'*30)




# CountDown

def countdown():
    print('Welcome to countdown Game')
    #first install countdown lib 
    #then import
    from countdown import countdown
    #taking user input for minutes
    minutes=int(input("Enter minute-"))
    #taking userinput for seconds
    seconds=int(input("Enter second-"))
    # Create a countdown of 1 minute and 10 seconds
    countdown(mins=1, secs=10) #here store the min and sec in countdown
    print('-'*30)





# Mind Game



def mindgame():
    print('welcome to Mind Game')

    import time
    import random

    #guess any no u want
    print("guess any no u want")
    time.sleep(5)
    #make double of it
    print("make double of it")
    time.sleep(5)
    # choose any no 1 to 1000
    li=[]
    for i in range(4):
        li.append(random.randrange(1,100))
    for i in li:
        print('add number',i)

    time.sleep(5)
    #make half of it
    print("make half of it")
    time.sleep(5)
    print('-'*30)

    #subtract the guess no
    print("subtract the guess no")
    time.sleep(5)
    print('-'*30)

    #your answer
    print("you got",sum(li)/2)


import tkinter as tk

#main window
window=tk.Tk()

#window title
window.title("Python Project")

#size
window.geometry('480x340')

#lable
tk.Label(window,text='PYTHON PROJECT',font=('Helvetica',17)).place(x=110,y=10)
tk.Label(window,text='Made by -: Pravin Jadhav',font=('Helvetica',12)).place(x=140,y=50)

#button
tk.Button(window,text='Budget\n Game',command=budget_game,height=2,width=18).place(x=20,y=100)
tk.Button(window,text='COIN TOSS',command=head_and_tails,height=2,width=18).place(x=175,y=100)
tk.Button(window,text='DICE',command=dice_game,height=2,width=18).place(x=330,y=100)
tk.Button(window,text='MULTIPLICATION\nTABLE',command=matrication_table,height=2,width=18).place(x=20,y=160)
tk.Button(window,text='FACTORIAL',command=factorial,height=2,width=18).place(x=175,y=160)
tk.Button(window,text='FIBONACCI\nSEQUENCE',command=fibonacii_series,height=2,width=18).place(x=330,y=160)
tk.Button(window,text='PASSWORD\nGENERATOR',command=password_generator,height=2,width=18).place(x=20,y=220)
tk.Button(window,text='COUNTDOWN',command=countdown,height=2,width=18).place(x=175,y=220)
tk.Button(window,text='MIND_GAME',command= mindgame,height=2,width=18).place(x=330,y=220)

#main loop
window.mainloop()


# In[ ]:





# In[ ]:




