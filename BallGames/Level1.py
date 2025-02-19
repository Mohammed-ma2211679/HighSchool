from tkinter import *
# Create the windwo
window = Tk()
window.title('Ball_Game')
canvas = Canvas(bg='yellow', width=800, height=600)
canvas.pack()

# Start Drawing Lines


# The start of squre room (Left)
# -
# -
canvas.create_line(50, 250, 150, 250, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(50, 350, 150, 350, width = 3, fill = 'Black', tags = 'line')
# | |
#   |
canvas.create_line(50, 350, 50, 250, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(150, 250, 150, 285, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(150, 350, 150, 315, width = 3, fill = 'Black', tags = 'line')
# End of the squre room (Left)

# -
# -
canvas.create_line(150, 285, 200, 285, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(150, 315, 200, 315, width = 3, fill = 'Black', tags = 'line')
# |
# |
canvas.create_line(200, 285, 200, 150, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(200, 315, 200, 450, width = 3, fill = 'Black', tags = 'line')
# _______
# _______
canvas.create_line(200, 150, 600, 150, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(200, 450, 600, 450, width = 3, fill = 'Black', tags = 'line')
# | (Right)
# | (Right)
canvas.create_line(600, 150, 600, 285, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(600, 450, 600, 315, width = 3, fill = 'Black', tags = 'line')
# - (Right)
# - (Right)
canvas.create_line(600, 285, 800, 285, width = 3, fill = 'Black', tags = 'line')
canvas.create_line(600, 315, 800, 315, width = 3, fill = 'Black', tags = 'line')
# |
canvas.create_line(700, 286.5, 700, 314, width = 3, fill = 'Green', tags = 'Gline')

# End of Drawing Lines

# The ball (player)
Ball = canvas.create_oval(100, 300, 120, 320, width = 1, fill = 'white', outline = 'white')

# Eneimes
e1 = canvas.create_oval(250, 150, 270, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e1'))
e2 = canvas.create_oval(300, 150, 320, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e2'))
e3 = canvas.create_oval(350, 150, 370, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e3'))
e4 = canvas.create_oval(400, 150, 420, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e4'))
e5 = canvas.create_oval(450, 150, 470, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e5'))
e6 = canvas.create_oval(500, 150, 520, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e6'))
e7 = canvas.create_oval(550, 150, 570, 170, width = 3, fill = 'red', outline = 'red', tags = ('enemy', 'e7'))

# Move the ball
def moveBall(event):
    if event.keycode==87:
       canvas.move(Ball, 0, -10)
    elif event.keycode==65:
       canvas.move(Ball, -10, 0)
    elif event.keycode==68:
       canvas.move(Ball, 10, 0)
    elif event.keycode==83:
       canvas.move(Ball, 0, 10)
canvas.bind_all("<Key>", moveBall)


def overlaps(pl, obj):
    items = canvas.find_overlapping(*canvas.coords(obj))
    if pl in items:
        return True
    else:
        return False

# Func doesn't work
def move(obj, dire, steps, max_steps):
    o = obj
    d = dire
    s = steps
    ms = max_steps
    canvas.move(o, 0, d)
    s= s+1
    if s>=ms:
        d=d -200
        s=1

# Ugly code
Deth_time = 0
steps=1
max_steps=140
direction=2
steps2=1
max_steps2=200
direction2=1.4
steps3=1
max_steps3=280
direction3=1
steps4=1
max_steps4=175
direction4=1.6
steps5=1
max_steps5=235
direction5=1.2
steps6=1
max_steps6=155
direction6=1.8
steps7=1
max_steps7=130
direction7=2.2
def move_enemy():
    global Deth_time
    global direction
    global steps
    global max_steps
    global direction2
    global steps2
    global max_steps2
    global direction3
    global steps3
    global max_steps3
    global direction4
    global steps4
    global max_steps4
    global direction5
    global steps5
    global max_steps5
    global direction6
    global steps6
    global max_steps6
    global direction7
    global steps7
    global max_steps7
    ene = canvas.find_withtag('enemy')
    line = canvas.find_withtag('line')
    Gline = canvas.find_withtag('Gline')

    for e in ene:
        canvas.move(e1, 0, direction)
        steps= steps+1
        if steps>=max_steps:
            direction=direction *(-1)
            steps=1
        canvas.move(e2, 0, direction2)
        steps2= steps2+1
        if steps2>=max_steps2:
            direction2=direction2 *(-1)
            steps2=1
        canvas.move(e3, 0, direction3)
        steps3= steps3+1
        if steps3>=max_steps3:
            direction3=direction3 *(-1)
            steps3=1
        canvas.move(e4, 0, direction4)
        steps4= steps4+1
        if steps4>=max_steps4:
            direction4=direction4 *(-1)
            steps4=1
        canvas.move(e5, 0, direction5)
        steps5= steps5+1
        if steps5>=max_steps5:
            direction5=direction5 *(-1)
            steps5=1
        canvas.move(e6, 0, direction6)
        steps6= steps6+1
        if steps6>=max_steps6:
            direction6=direction6 *(-1)
            steps6=1
        canvas.move(e7, 0, direction7)
        steps7= steps7+1
        if steps7>=max_steps7:
            direction7=direction7 *(-1)
            steps7=1
        
        if overlaps(e, Ball):
            print("Game Over")
            Deth_time +=1
            #canvas.create_oval(100, 300, 120, 320, width = 1, fill = 'white', outline = 'white')
            canvas.unbind_all("<Key>")
        
    for l in line:
        if overlaps(l, Ball):
            print("Game Over")
            Deth_time +=1
            canvas.unbind_all("<Key>")
            return
    for g in Gline:
        if overlaps(g, Ball):
            print("You win!")
            #print('Deth times =', Deth_time)
            canvas.unbind_all("<Key>")
            return
    canvas.after(100, move_enemy)
move_enemy()
canvas.pack()
window.mainloop()
