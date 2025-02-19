import time
import turtle
# Display
win = turtle.Screen()
win.bgcolor('black')
win.title('The clock')
# Write time
write_time = turtle.Turtle()
write_time.speed(0)
write_time.penup()
write_time.hideturtle()
write_time.color('white')
# Time
for h in range(13):
    for m in range(61):
        for s in range(61):
            write_time.goto(0, 150)
            write_time.write('Time', align='center', font=("Arial", 80, 'bold'))
            write_time.goto(0, -200)
            write_time.write('{} : {} : {}'.format(h, m, s), align='center', font=("Arial", 200, 'bold'))
            time.sleep(1)
            write_time.clear()
while True:
    win.update()
