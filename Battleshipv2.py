#/* Battleship Final Project
#Battleship.py
#Robert Robinson
#rrobin08
#Section 3*/

#Import graphics
from graphics import *
#Import randrange
from random import randrange

#Create the class for computer ships
class cpuShip:
    #Structure the class
    def __init__(self,x,y):
        #Set the ships to equal the coordinates
        self.coords=str(x)+","+str(y)
    
#Set up the window    
def winSetup():
    #Create a window that is 800 by 800 pixels
    win=GraphWin("Battleship v1",800,800)
    #Set the coordinates to white
    win.setBackground("white")
    #Make the window 8 units tall and 8 units wide
    win.setCoords(0,0,8,8)
    
    return win

#List the instructions for the game
def instructionBoard():
    
    win=GraphWin("Battleship Instructions",800,800)
    win.setBackground("lightblue")
    win.setCoords(0,0,8,8)
    title=Text(Point(4,7),"Instructions")
    title.setStyle("bold")
    title.setSize(24)
    title.draw(win)
    rule1=Text(Point(4,6),"The objective of this game is to guess the location of enemy ships.")
    rule1.draw(win)
    rule2=Text(Point(4,5),"Do not click past a coordinate entry box without entering a number.")
    rule2.draw(win)
    rule3=Text(Point(4,4),"Entering a coordinate to fire at is only nessecary when the grid is empty.")
    rule3.draw(win)
    rule4=Text(Point(4,3),"To quit, enter q in one of the firing boxes")
    rule4.draw(win)
    rule41=Text(Point(4,2.7),"and click twice to exit.")
    rule41.draw(win)
    rule5=Text(Point(4,2),"The game will automatically exit when you win,")
    rule5.draw(win)
    rule51=Text(Point(4,1.7),"however if you lose and it does not exit, enter q.")
    rule51.draw(win)
    rule6=Text(Point(4,1),"Click this window to continue.")
    rule6.draw(win)
    win.getMouse()
    win.close()
    
#A function that allows for the input of four ships
def shipInput(win):
    
    #Create the entry box for ship 1
    ship1X=Entry(Point(6,7),2)
    ship1X.draw(win)
    ship1Y=Entry(Point(7,7),2)
    ship1Y.draw(win)
    shipT1=Text(Point(3,7),"Enter ship 1 coordinates:")
    shipT1.draw(win)
    
    #Create the entry box for ship 2
    ship2X=Entry(Point(6,5.5),2)
    ship2X.draw(win)
    ship2Y=Entry(Point(7,5.5),2)
    ship2Y.draw(win)
    shipT2=Text(Point(3,5.5),"Enter ship 2 coordinates:")
    shipT2.draw(win)
    
    #Create the entry box for ship 3
    ship3X=Entry(Point(6,4),2)
    ship3X.draw(win)
    ship3Y=Entry(Point(7,4),2)
    ship3Y.draw(win)
    shipT3=Text(Point(3,4),"Enter ship 3 coordinates:")
    shipT3.draw(win)
    
    #Create the entry box for ship 4
    ship4X=Entry(Point(6,2.5),2)
    ship4X.draw(win)
    ship4Y=Entry(Point(7,2.5),2)
    ship4Y.draw(win)
    shipT4=Text(Point(3,2.5),"Enter ship 4 coordinates:")
    shipT4.draw(win)
    
    #Create the on screen instructions
    Instructions=Text(Point(4,1.3),"Click the window twice to enter values")
    Instructions.draw(win)
    
    win.getMouse()
    
    #Create the ship objects
    x1=ship1X.getText()
    y1=ship1Y.getText()
    ship1=str(x1)+","+str(y1)
    x2=ship2X.getText()
    y2=ship2Y.getText()
    ship2=str(x2)+","+str(y2)
    x3=ship3X.getText()
    y3=ship3Y.getText()
    ship3=str(x3)+","+str(y3)
    x4=ship4X.getText()
    y4=ship4Y.getText()
    ship4=str(x4)+","+str(y4)
    
    #Create the ship list
    shipList=[]
    shipList.append(ship1)
    shipList.append(ship2)
    shipList.append(ship3)
    shipList.append(ship4)
    
    return shipList

#Create a function that shows the enemy grid and firing boxes
def battleScreen(win,redList,blueList):
    #Clear the window
    clearWin=Rectangle(Point(0,0),Point(8,8))
    clearWin.setFill("white")
    clearWin.draw(win)
    #Create the grid
    bSquare=Rectangle(Point(3,3),Point(7,7))
    bSquare.setWidth(2)
    bSquare.draw(win)
    
    for i in range(4,7):
        gridH=Line(Point(i,3),Point(i,7))
        gridH.draw(win)
        
    for j in range(4,7):
        GridV=Line(Point(3,j),Point(7,j))
        GridV.draw(win)
    
    for k in range(1,5):
        NumH=Text(Point(k+2.5,7.5),str(k))
        NumH.draw(win)
        
    for l in range(1,5):
        NumV=Text(Point(2.5,7.5-l),str(l))
        NumV.draw(win)
        
    bText=Text(Point(1,7.5),"Battle Screen")
    bText.setSize(20)
    bText.draw(win)
        
     #Determine whether or not a box should be filled with red or blue
    for i in range(len(redList)):
        redSplit=redList[i].split(",")
        x=int(redSplit[0])
        y=int(redSplit[1])
        box=Rectangle(Point(2+x,8-y),Point(3+x,7-y))
        box.setFill("red")
        box.draw(win)
        
    for j in range(len(blueList)):
        blueSplit=blueList[j].split(",")
        x=int(blueSplit[0])
        y=int(blueSplit[1])
        box=Rectangle(Point(2+x,8-y),Point(3+x,7-y))
        box.setFill("blue")
        box.draw(win)
        
        
    #Create the entry boxes    
    EntX=Entry(Point(3,1.5),2)
    EntX.draw(win)
    TxtX=Text(Point(2,1.5),"X Coordinate:")
    TxtX.draw(win)
    
    EntY=Entry(Point(6,1.5),2)
    EntY.draw(win)
    TxtY=Text(Point(5,1.5),"Y Coordinate:")
    TxtY.draw(win)
    #Create the on screen instructions
    clickText=Text(Point(4,1),"Click the window twice to fire")
    clickText.draw(win)
    win.getMouse()
    xInput=EntX.getText()
    yInput=EntY.getText()
    clickText.setText("Click the window to continue.")
    #Return the firing coordinates
    return xInput,yInput
#Create a screen that shows the player's grid and where it has been hit
def selfScreen(shipList,cpuShotList,win):
    #Clear the window
    clearWin=Rectangle(Point(0,0),Point(8,8))
    clearWin.setFill("white")
    clearWin.draw(win)
    #Create the grid
    bSquare=Rectangle(Point(3,3),Point(7,7))
    bSquare.setWidth(2)
    bSquare.draw(win)
    
    for i in range(4,7):
        gridH=Line(Point(i,3),Point(i,7))
        gridH.draw(win)
        
    for j in range(4,7):
        GridV=Line(Point(3,j),Point(7,j))
        GridV.draw(win)
    
    for k in range(1,5):
        NumH=Text(Point(k+2.5,7.5),str(k))
        NumH.draw(win)
        
    for l in range(1,5):
        NumV=Text(Point(2.5,7.5-l),str(l))
        NumV.draw(win)
        
    for m in range(len(shipList)):
        shipSplit=shipList[m].split(",")
        x=int(shipSplit[0])
        y=int(shipSplit[1])
        box=Rectangle(Point(2+x,8-y),Point(3+x,7-y))
        box.setFill("blue")
        box.draw(win)
    #Show the computer hit markers    
    for n in range(len(cpuShotList)):
        shotSplit=cpuShotList[n].split(",")
        x=int(shotSplit[0])
        y=int(shotSplit[1])
        box=Rectangle(Point(2+x,8-y),Point(3+x,7-y))
        box.setFill("red")
        box.draw(win)
    #Create the on screen instructions
    ssText=Text(Point(1.5,7),"Self Screen")
    ssText.draw(win)
        
    Instructions=Text(Point(4,2.5),"Player ship map")
    Instructions.draw(win)
    Instructions2=Text(Point(4,1),"If you have lost, enter q in the x coordinate entry box on the battle screen to surrender.")
    Instructions2.draw(win)
    Instructions3=Text(Point(4,2.25),"Click the window to continue.")
    Instructions3.draw(win)
    
    return cpuShotList
#Determine whether or not a shot should show up as blue or red during the game
def shotMarker(shotXY,redList,blueList,shipListAI,win):
    
    count=0
    #Determine whether or not a ship has been hit
    x=shipListAI.count(shotXY)
    if x>=1:
        redList.append(shotXY)
        count=count+1
    elif x==0:
        blueList.append(shotXY)
    #Color the boxes    
    for i in range(len(redList)):
        redSplit=redList[i].split(",")
        x=int(redSplit[0])
        y=int(redSplit[1])
        box=Rectangle(Point(2+x,8-y),Point(3+x,7-y))
        box.setFill("red")
        box.draw(win)
        
    for j in range(len(blueList)):
        blueSplit=blueList[j].split(",")
        x=int(blueSplit[0])
        y=int(blueSplit[1])
        box=Rectangle(Point(2+x,8-y),Point(3+x,7-y))
        box.setFill("blue")
        box.draw(win)
        
    return redList,blueList,count
#Create the ship objects
def shipObject(infile):
    
    rawLine=infile.readline()
    coords=rawLine.split(" ")
    coords1=coords[0].split(",")
    x1=int(coords1[0])
    y1=int(coords1[1])
    cpuShip1=cpuShip(x1,y1)
    coords2=coords[1].split(",")
    x2=int(coords2[0])
    y2=int(coords2[1])
    cpuShip2=cpuShip(x2,y2)
    coords3=coords[2].split(",")
    x3=int(coords3[0])
    y3=int(coords3[1])
    cpuShip3=cpuShip(x3,y3)
    coords4=coords[3].split(",")
    x4=int(coords4[0])
    y4=int(coords4[1])
    cpuShip4=cpuShip(x4,y4)
    #Return the ship objects
    return cpuShip1, cpuShip2, cpuShip3, cpuShip4
#Allow the computer to randomly fire    
def cpuFire():
    x=randrange(1,5)
    y=randrange(1,5)
    #Create the shot coordinates
    cpuShot=str(x)+","+str(y)
    return cpuShot
#main    
def main():
    #select one of the four computer ship presets
    filenum=randrange(1,5)
    infile=open("ships"+str(filenum)+".txt","r")
    cpuShip1, cpuShip2, cpuShip3, cpuShip4=shipObject(infile)
    #Ask the name and the date for the scoreboard
    name=input("What is your name? (Scoreboard)")
    day=input("What is the date? (Scoreboard)")
    #Show the instructions
    instructionBoard()
    #Create the window
    win=winSetup()
    #Create the list of user ships
    shipList=shipInput(win)
    win.getMouse()
    #Close the window
    win.close()
    #Create the window
    win=winSetup()
    #Set all lists to nothing
    cpuShotList=[]
    redList=[]
    blueList=[]
    
    #Continue looping the game until one party wins or loses
    while win.checkKey()!='q':
        #Show the battle screen function
        xInput,yInput=battleScreen(win,redList,blueList)
        
        if xInput=='q':
            break
        
        win.getMouse()
        #Compute the player shot string
        shotXY=str(xInput)+","+str(yInput)
        #Set up the computer ship coordinate list
        shipListAI=[]
        shipListAI.append(cpuShip1.coords)
        shipListAI.append(cpuShip2.coords)
        shipListAI.append(cpuShip3.coords)
        shipListAI.append(cpuShip4.coords)
        #Run the shot marker function
        redList,blueList,count=shotMarker(shotXY,redList,blueList,shipListAI,win)
        #Determine whether or not the player has won the game. If they have, break the loop
        if len(redList)==4:
            break
        
        win.getMouse()
        #Allow the computer to fire a shot
        cpuShot=cpuFire()
        #Add that shot to a list of coordinates
        cpuShotList.append(cpuShot)
        #Show the self screen function
        selfScreen(shipList,cpuShotList,win)
        
        win.getMouse()
    #If a player wins, show a screen stating they have won and add it to the scoreboard
    if len(redList)==4:
        win.close()
        win=winSetup()
        wintext=Text(Point(4,4),"You won!")
        wintext.setSize(36)
        wintext.setTextColor("purple")
        wintext.draw(win)
        outfile=open("battleshipscore.txt","w")
        print(name,"won on",day,"\a",file=outfile)
        outfile.close()
        win.getMouse()
    #If a player loses, show a screen saying they have lost and add it to the scoreboard
    else:
        win.close()
        win=winSetup()
        wintext=Text(Point(4,4),"You lost!")
        wintext.setSize(36)
        wintext.setTextColor("purple")
        wintext.draw(win)
        outfile=open("battleshipscore.txt","w")
        print(name,"lost on",day,"\a",file=outfile)
        outfile.close()
    #Close the window
    win.close()
#End of main
main()