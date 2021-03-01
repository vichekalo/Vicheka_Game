#  IMPORTS
import tkinter as tk
#  MAIN
root = tk.Tk()
root.geometry("600x600")
canvas = tk.Canvas(root)
root.title('welcome gamers')

#add image
myImage= tk.PhotoImage(file='player.png')
myCoin=tk.PhotoImage(file='coin.png')
myEnemy=tk.PhotoImage(file='monster.png')
myGoal=tk.PhotoImage(file='flag.png')
myWall=tk.PhotoImage(file='wall.png')
myBackground=tk.PhotoImage(file='backg.png')

#Note
empty=0
wall=1
player=2
coin=3
monster=4
goal=5


# Main VARIABLES
grid =[
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

#  FUNCTION
def arrayToDrawing():
    global myImage,myCoin
    canvas.delete("all")
    canvas.create_image(160,310, image=myBackground)

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
            
    return None

#Make player can moves right,left,up,down

def PositionOfPlayer(grid) :
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row]== 2:
                position=[column,row]
    return position

def MoveRight(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    if grid[playerrow][playercolumn +1]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow][playercolumn +1]=2
    arrayToDrawing()

def MoveLeft(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    if grid[playerrow][playercolumn -1]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow][playercolumn -1]=2
    arrayToDrawing()

def MoveUp(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn = position[1]
    if grid[playerrow-1][playercolumn ]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow-1][playercolumn ]=2
    arrayToDrawing()

def MoveDown(event):
    global grid
    position = PositionOfPlayer(grid)
    playerrow = position[0]
    playercolumn  = position[1]
    if grid[playerrow+1][playercolumn ]!=1:
        grid[playerrow][playercolumn ]=0
        grid[playerrow+1][playercolumn ]=2
    arrayToDrawing()

#Bind 
canvas = tk.Canvas(root)
root.bind("<Left>", MoveLeft) #LEFT CLICK
root.bind("<Right>", MoveRight)  #RIGHT CLICK
root.bind("<Up>", MoveUp) #Up CLICK
root.bind("<Down>", MoveDown)  #Down CLICK

canvas.pack(expand=True, fill="both")
arrayToDrawing()
root.mainloop()









