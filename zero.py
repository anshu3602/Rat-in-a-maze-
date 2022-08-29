from tkinter import*
from tkinter.ttk import*
from gui import a
import random
from choo import cho
from guiman import gu

lis = [
    [0,0,1,0,1,1,1,0,0,1,1,2],
   [1,0,1,0,1,0,1,1,0,1,1,0],
   [1,1,1,1,1,1,0,1,1,0,1,0],
   [0,1,0,0,1,0,0,1,0,1,1,1],
   [1,1,0,1,1,1,0,1,1,0,1,0],
   [0,1,1,1,0,1,1,0,1,1,1,1],
   [1,1,0,1,1,0,1,1,0,0,0,0],
   [0,0,0,1,0,1,1,1,1,1,1,1],
   [1,1,1,1,1,1,0,1,1,0,1,0],
   [1,0,0,0,1,0,0,0,0,0,1,0],
   [1,0,1,1,1,1,1,1,1,1,1,0],
   [0,1,1,0,0,1,1,0,0,0,1,4]
]

do = [
    [0,0,1,0,1,1,1,0,0,1,1,1],
   [1,0,1,0,1,0,1,1,0,1,1,0],
   [1,1,1,1,1,1,0,1,1,0,1,0],
   [0,1,0,0,1,0,0,1,0,1,1,1],
   [1,1,0,1,1,1,0,1,1,0,1,0],
   [0,1,1,1,0,1,1,0,1,1,1,1],
   [1,1,0,1,1,0,1,1,0,0,0,0],
   [0,0,0,1,0,1,1,1,1,1,1,1],
   [1,1,1,1,1,1,0,1,1,0,1,0],
   [1,0,0,0,1,0,0,0,0,0,1,0],
   [1,0,1,1,1,1,1,1,1,1,1,0],
   [0,1,1,0,0,1,1,0,0,0,1,5]
]

pa = []

b=random.randint(0,4)

if b==0:
    pa=[
         "l", "l" , "d" , "r" , "d" , "d" , "d", "d", "l", "l", "u", "l", "u", "u", "u", "l", "u", "l" , "l" , "d" , "d" , "d", "d" , "l", "d" , "d", "d" , "d", "r", "d", "d", "r", "r", "r", "r", "r","r","d","r" "l", 
       ] 
if b==1:
    pa=[
     "l", "d" , "d" , "d" , "d" , "d" , "l", "l", "u", "l", "u", "u", "u", "l", "u", "l", "l", "d" , "d" , "d" , "d" , "r", "d" , "r", "d" , "r", "d" , "r", "r", "r", "d" , "d" , "d" , "d" , "r"
    ]
if b==2:
    pa=[
     "l", "d" , "d" , "d" , "d" , "d" , "l", "l", "u", "l", "u", "u", "u", "l", "u", "l", "l", "d" , "d" , "l" , "l" , "l", "d" , "d", "d" , "r", "r" , "d", "d", "d", "r" , "d" , "d" , "r" , "r", "r", "r", "r", "r", "d", "r"
    ]
if b==3:
    pa=[
     "l", "d" , "d" , "d" , "d" , "d" , "l", "l", "u", "l", "u", "u", "u", "l", "u", "l", "l", "d" , "d" , "d" , "d" , "r", "d" , "r", "d" , "d", "l" , "d", "l", "d", "r" , "r" , "r" , "r" , "r" , "r", "d", "r"
    ]
if b==4:
    pa=[
     "l", "d" , "d" , "d" , "d" , "d" , "l", "l", "u", "l", "u", "u", "u", "l", "u", "l", "l", "d" , "d" , "l" , "l" , "l", "d" , "d", "d" , "r", "r" , "d", "d", "d", "r" , "d" , "d" , "r" , "r", "r", "r", "r", "r", "d", "r"
    ]

#The path the rat will go in has been choosen randomly.

inde = 0

ind = 0

num = 0

rec = []

#Checking if user wants automatic.

if cho==1:

    a(lis) 

    for i in pa:

        #This bit of code finds the list in which the rat is in and the index in which it's present.

        for j in lis:
            
            for h in j:
                
                ind += 1
                
                if h  ==  2:

                    #rec is used to find which list the rat is in.

                    rec = j
                    
                    inde = ind
                    
                    ind = 0
                    
                    break
            ind = 0
            
        for k,g in enumerate(lis):

            #We'll use enumerate to get indexes for all lists and their elements in them.

            if lis[k] == rec:

                #rec is used to find which list the rat is in.

                if i ==  "l":
                    
                    num = inde-1

                    #Simple swapping to move the rat.

                    lis[k][num], lis[k][num-1] = lis[k][num-1], lis[k][num]

                    a(lis)
                    
                    break

                if i ==  "r":
                    
                    num = inde-1

                    #Simple swapping to move the rat.

                    if lis[k][num+1]==4:

                        a(do)

                        exit()

                    lis[k][num], lis[k][num+1] = lis[k][num+1], lis[k][num]
                    
                    a(lis)
                        
                    break

                if i ==  "u":
                    
                    num = inde-1

                    #Simple swapping to move the rat.

                    lis[k-1][num], lis[k][num] = lis[k][num], lis[k-1][num]
                    
                    a(lis)
                        
                    break

                if i ==  "d" :
                    
                    num = inde-1

                    #Simple swapping to move the rat.

                    lis[k+1][num], lis[k][num] = lis[k][num], lis[k+1][num]
                    
                    a(lis)

#Checking if user wants manual control.

if cho==0:
    
    #checker is used to tell the user and program the the rat cannot move into a wall.

    checker=0

    ho=gu(lis)

    while checker==0:
        
        #Finding the list in which the rat is present and what index.

        for j in lis:
            
            for h in j:
                
                ind += 1
                
                if h  ==  2:

                    #rec is used to find which list the rat is in.

                    rec = j
                    
                    inde = ind
                    
                    ind = 0
                    
                    break

            ind = 0
            
        for k,g in enumerate(lis):

            #We'll use enumerate to get indexes for all lists and their elements in them.

            if lis[k] == rec:

                #rec is used to find which list the rat is in.

                if ho ==  "l":
                    
                    num = inde-1

                    #This tries to see if the rat is trying to move out of the maze or into a wall.

                    try:
                        
                        if lis[k][num]==0 or lis[k][num-1]==0 or num==0:
                            
                            checker=1
                            
                            break

                    except:
                        
                        checker=1
                        
                        break
                    
                    #Simple swapping to move the rat.

                    lis[k][num], lis[k][num-1] = lis[k][num-1], lis[k][num]

                    ho=gu(lis)
                    
                    break

                if ho ==  "r":
                    
                    num = inde-1

                    #This checks if rat tried to get the cheese.

                    if lis[11][10]==2:
                            
                            a(do)
                            
                            exit()

                    #This tries to see if the rat is trying to move out of the maze or into a wall.

                    try:

                        if lis[k][num]==0 or lis[k][num+1]==0 or num==11:

                            checker=1
                        
                            break

                    except:
                        
                        checker=1
                        
                        break
                    
                    #Simple swapping to move the rat.

                    lis[k][num], lis[k][num+1] = lis[k][num+1], lis[k][num]
                    
                    ho=gu(lis)
                        
                    break

                if ho ==  "u":
                    
                    num = inde-1

                    #This tries to see if the rat is trying to move out of the maze or into a wall.

                    try:

                        if lis[k-1][num]==0 or lis[k][num]==0 or k-1<0:

                            checker=1

                            break

                    except:
                        
                        checker=1
                        
                        break
                    
                    #Simple swapping to move the rat.

                    lis[k-1][num], lis[k][num] = lis[k][num], lis[k-1][num]
                    
                    ho=gu(lis)
                        
                    break

                if ho ==  "d" :
                    
                    num = inde-1

                    #This tries to see if the rat is trying to move out of the maze or into a wall.

                    try:

                        if lis[k+1][num]==0 or lis[k][num]==0 or k==11:

                            checker=1

                            break

                    except:

                        checker=1
                        
                        break
                    
                    #Simple swapping to move the rat.

                    lis[k+1][num], lis[k][num] = lis[k][num], lis[k+1][num]
                    
                    ho=gu(lis)
                        
                    break

        if checker==1:

            checker=0

            ho=gu(lis)

print("The rat ate something\nYay.")
