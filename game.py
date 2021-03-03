#  IMPORTS
import tkinter as tk
from tkinter import messagebox
#add sound
import winsound
#  MAIN Code
root = tk.Tk()
root.geometry("600x655")
root.resizable(0,0)
canvas = tk.Canvas(root)
root.title('Vicheka.Lo-GamerCambodia')

#add image
myImage= tk.PhotoImage(file='player.png')
myCoin=tk.PhotoImage(file='coin.png')
myEnemy=tk.PhotoImage(file='monster.png')
myGoal=tk.PhotoImage(file='flag.png')
myWall=tk.PhotoImage(file='wall.png')
myBackground=tk.PhotoImage(file='backg.png')
##Result
myWiner=tk.PhotoImage(file='youwin.png')
myLoser=tk.PhotoImage(file='gameover.png')

#Note
empty=0
wall=1
player=2
coin=3
monster=4
goal=5

# Main VARIABLES
grid =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1],
    [1, 2, 3, 1, 1, 3, 1, 3, 4, 0, 3,1],
    [1, 4, 0, 0, 3, 4, 3, 4, 3, 0, 1,1],
    [1, 3, 3, 0, 1, 1, 1, 1, 1, 0, 0,1],
    [1, 1, 1, 0, 4, 3, 1, 3, 3, 4, 0,1],
    [1, 4, 1, 0, 1, 1, 1, 1, 1, 1, 0,1],
    [1, 3, 1, 0, 3, 4, 3, 4, 3, 1, 0,1],
    [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 0,1],
    [1, 4, 3, 0, 1, 3, 4, 3, 4, 3, 0,1],
    [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 3,1],
    [1, 3, 3, 0, 0, 0, 3, 0, 0, 0, 5,1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1], 
]

ScoreOfCoins=0
StepOfMoving=20

#  FUNCTION
def arrayToDrawing():
    global myImage,myCoin,StepOfMoving
    canvas.delete("all")
    canvas.create_image(210,310, image=myBackground)

    for Y in range (len(grid)):
        for X in range  (len(grid[0])):
            x1 = (X * 50)
            y1 = (Y * 50)
            x2 = 50 + x1
            y2 = 50 + y1
            value = grid[Y][X]
            if value != player:
                if value !=coin:
                    if value!=monster:
                        if value !=goal:
                            if value==wall:
                                canvas.create_image(x1+26,y1+27,image=myWall)
                        else:
                            canvas.create_image(x1+26,y1+27,image=myGoal)
                    else:
                        canvas.create_image(x1+26,y1+27,image=myEnemy)
                else:
                    canvas.create_image(x1+26,y1+27,image=myCoin)
            else:
                canvas.create_image(x1+23,y1+27,image=myImage)
    canvas.create_text(40,20,fill="black",font="Times 16 italic bold",text="Score: "+str(ScoreOfCoins))
    canvas.create_text(200,20,fill="black",font="Times 16 italic bold",text="Time Left: "+str(StepOfMoving))
    return None

#Make player can moves right,left,up,down

def PositionOfPlayer(grid) :
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row]== 2:
                position=[column,row]
    return position

def MoveRight(event):
    global grid, ScoreOfCoins,StepOfMoving
    StepOfMoving=StepOfMoving-1
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    oldValue = 0
    if grid[playerrow][playercolumn +1]!=1:
        grid[playerrow][playercolumn ]=0
        oldValue = grid[playerrow][playercolumn+1]
        grid[playerrow][playercolumn +1]=2
    
    if oldValue==coin:
        winsound .PlaySound('coin.wav', winsound.SND_FILENAME)
        ScoreOfCoins=ScoreOfCoins+10
    arrayToDrawing()
    if oldValue==monster:
        winsound .PlaySound('lost.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")
    if oldValue==goal and ScoreOfCoins>=50 and StepOfMoving>=0 :
        winsound .PlaySound('win.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myWiner)
        messagebox.showinfo("Success","You Win!")
    if oldValue!=goal and ScoreOfCoins<50 and StepOfMoving<0:
        winsound .PlaySound('lost.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")
    

def MoveLeft(event):
    global grid,ScoreOfCoins,StepOfMoving
    StepOfMoving=StepOfMoving-1
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    oldValue = 0
    if grid[playerrow][playercolumn-1]!=1:
        grid[playerrow][playercolumn]=0
        oldValue = grid[playerrow][playercolumn-1]
        grid[playerrow][playercolumn-1]=2
        
    if oldValue==coin:
        winsound .PlaySound('coin.wav', winsound.SND_FILENAME)
        ScoreOfCoins=ScoreOfCoins+10
    arrayToDrawing()
    if oldValue==monster:
        winsound .PlaySound('lost.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")
    if oldValue==goal and ScoreOfCoins>=50 and StepOfMoving>=0 :
        winsound .PlaySound('win.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myWiner)
        messagebox.showinfo("Success","You Win!")

def MoveUp(event):
    global grid,ScoreOfCoins,StepOfMoving
    StepOfMoving=StepOfMoving-1
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    oldValue = 0
    if grid[playerrow-1][playercolumn ]!=1:
        grid[playerrow][playercolumn ]=0
        oldValue = grid[playerrow-1][playercolumn]
        grid[playerrow-1][playercolumn ]=2
    
    if oldValue==coin:
        winsound .PlaySound('coin.wav', winsound.SND_FILENAME)
        ScoreOfCoins=ScoreOfCoins+10
    arrayToDrawing()
    if oldValue==monster:
        winsound .PlaySound('lost.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")
    if oldValue==goal and ScoreOfCoins>=50 and StepOfMoving>=0 :
        winsound .PlaySound('win.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myWiner)
        messagebox.showinfo("Success","You Win!")
    

def MoveDown(event):
    global grid,ScoreOfCoins,StepOfMoving
    StepOfMoving=StepOfMoving-1
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn  = position[1]
    oldValue = 0
    if grid[playerrow+1][playercolumn ]!=1:
        grid[playerrow][playercolumn ]=0
        oldValue = grid[playerrow+1][playercolumn]
        grid[playerrow+1][playercolumn ]=2
    if oldValue==coin:
        winsound .PlaySound('coin.wav', winsound.SND_FILENAME)
        ScoreOfCoins=ScoreOfCoins+10
    arrayToDrawing()
    if oldValue==monster:
        winsound .PlaySound('lost.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myLoser)
        messagebox.showinfo("Lost","You Lost!")
    if oldValue==goal and ScoreOfCoins>=50 and StepOfMoving>=0 :
        winsound .PlaySound('win.wav', winsound.SND_FILENAME)
        canvas.create_image(300,300,image=myWiner)
        messagebox.showinfo("Success","You Win!")

#Bind 
canvas = tk.Canvas(root)
root.bind("<Left>", MoveLeft) #LEFT CLICK
root.bind("<Right>", MoveRight)  #RIGHT CLICK
root.bind("<Up>", MoveUp) #Up CLICK
root.bind("<Down>", MoveDown)  #Down CLICK

canvas.pack(expand=True, fill="both")
arrayToDrawing()
root.mainloop()