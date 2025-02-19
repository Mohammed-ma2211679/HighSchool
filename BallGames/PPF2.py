# imports
import turtle
import time
import random

# set up screen
wn = turtle.Screen()
wn.title("Square Game")
wn.bgcolor('yellow')
wn.setup(width=1000, height=600)

# Player
player = turtle.Turtle()
player.shape('square')
player.shapesize(0.5)
player.penup()
player.speed(0)
player.color('black')
player.goto(-380, 0)
# Borders

# B1
b1 = turtle.Turtle()
b1.speed(0)
b1.penup()
b1.shape('square')
b1.shapesize(stretch_wid=8, stretch_len=0.4)
b1.color('green')
b1.goto(450, 0)
# B2
b2 = turtle.Turtle()
b2.speed(0)
b2.penup()
b2.shape('square')
b2.shapesize(stretch_wid=8, stretch_len=0.4)
b2.color('black')
b2.goto(-450, 0)
# B3
b3 = turtle.Turtle()
b3.speed(0)
b3.penup()
b3.shape('square')
b3.shapesize(stretch_wid=0.4, stretch_len=6)
b3.color('black')
b3.goto(394, 80)
# B4
b4 = turtle.Turtle()
b4.speed(0)
b4.penup()
b4.shape('square')
b4.shapesize(stretch_wid=0.4, stretch_len=6)
b4.color('black')
b4.goto(394, -80)
# B5
b5 = turtle.Turtle()
b5.speed(0)
b5.penup()
b5.shape('square')
b5.shapesize(stretch_wid=0.4, stretch_len=6)
b5.color('black')
b5.goto(-394, 80)
# B6
b6 = turtle.Turtle()
b6.speed(0)
b6.penup()
b6.shape('square')
b6.shapesize(stretch_wid=0.4, stretch_len=6)
b6.color('black')
b6.goto(-394, -80)
# B7
b7 = turtle.Turtle()
b7.speed(0)
b7.penup()
b7.shape('square')
b7.shapesize(stretch_wid=3, stretch_len=0.4)
b7.color('black')
b7.goto(338, -45)
# B8
b8 = turtle.Turtle()
b8.speed(0)
b8.penup()
b8.shape('square')
b8.shapesize(stretch_wid=3, stretch_len=0.4)
b8.color('black')
b8.goto(338, 45)
# B9
b9 = turtle.Turtle()
b9.speed(0)
b9.penup()
b9.shape('square')
b9.shapesize(stretch_wid=3, stretch_len=0.4)
b9.color('black')
b9.goto(-338, -45)
# B10
b10 = turtle.Turtle()
b10.speed(0)
b10.penup()
b10.shape('square')
b10.shapesize(stretch_wid=3, stretch_len=0.4)
b10.color('black')
b10.goto(-338, 45)
# B11
b11 = turtle.Turtle()
b11.speed(0)
b11.penup()
b11.shape('square')
b11.shapesize(stretch_wid=0.4, stretch_len=3)
b11.color('black')
b11.goto(312, -18)
# B12
b12 = turtle.Turtle()
b12.speed(0)
b12.penup()
b12.shape('square')
b12.shapesize(stretch_wid=0.4, stretch_len=3)
b12.color('black')
b12.goto(312, 18)
# B13
b13 = turtle.Turtle()
b13.speed(0)
b13.penup()
b13.shape('square')
b13.shapesize(stretch_wid=0.4, stretch_len=3)
b13.color('black')
b13.goto(-312, -18)
# B14
b14 = turtle.Turtle()
b14.speed(0)
b14.penup()
b14.shape('square')
b14.shapesize(stretch_wid=0.4, stretch_len=3)
b14.color('black')
b14.goto(-312, 18)
# B15
b15 = turtle.Turtle()
b15.speed(0)
b15.penup()
b15.shape('square')
b15.shapesize(stretch_wid=8, stretch_len=0.4)
b15.color('black')
b15.goto(285, -100)

# B16
b16 = turtle.Turtle()
b16.speed(0)
b16.penup()
b16.shape('square')
b16.shapesize(stretch_wid=8, stretch_len=0.4)
b16.color('black')
b16.goto(285, 100)

# B17
b17 = turtle.Turtle()
b17.speed(0)
b17.penup()
b17.shape('square')
b17.shapesize(stretch_wid=8, stretch_len=0.4)
b17.color('black')
b17.goto(-285, -100)

# B18
b18 = turtle.Turtle()
b18.speed(0)
b18.penup()
b18.shape('square')
b18.shapesize(stretch_wid=8, stretch_len=0.4)
b18.color('black')
b18.goto(-285, 100)
# B19
b19 = turtle.Turtle()
b19.speed(0)
b19.penup()
b19.shape('square')
b19.shapesize(stretch_wid=0.4, stretch_len=29)
b19.color('black')
b19.goto(0, 180)
# B20
b20 = turtle.Turtle()
b20.speed(0)
b20.penup()
b20.shape('square')
b20.shapesize(stretch_wid=0.4, stretch_len=29)
b20.color('black')
b20.goto(0, -180)

# Enemies :

# Enemy 1
en1 = turtle.Turtle()
en1.shape('circle')
en1.shapesize(1)
en1.penup()
en1.speed(0)
en1.color('red')
en1.goto(-200, 0)
en1.dx = 40
en1.dy = 40

# Enemy 2
en2 = turtle.Turtle()
en2.shape('circle')
en2.shapesize(1)
en2.penup()
en2.speed(0)
en2.color('red')
en2.goto(-150, 0)
en2.dx = 20
en2.dy = 20
# Enemy 3
en3 = turtle.Turtle()
en3.shape('circle')
en3.shapesize(1)
en3.penup()
en3.speed(0)
en3.color('red')
en3.goto(-100, 0)
en3.dx = 40
en3.dy = 40
# Enemy 4
en4 = turtle.Turtle()
en4.shape('circle')
en4.shapesize(1)
en4.penup()
en4.speed(0)
en4.color('red')
en4.goto(-50, 0)
en4.dx = 20
en4.dy = 20
# Enemy 5
en5 = turtle.Turtle()
en5.shape('circle')
en5.shapesize(1)
en5.penup()
en5.speed(0)
en5.color('red')
en5.goto(0, 0)
en5.dx = 40
en5.dy = 40
# Enemy 6
en6 = turtle.Turtle()
en6.shape('circle')
en6.shapesize(1)
en6.penup()
en6.speed(0)
en6.color('red')
en6.goto(50, 0)
en6.dx = 20
en6.dy = 20
# Enemy 7
en7 = turtle.Turtle()
en7.shape('circle')
en7.shapesize(1)
en7.penup()
en7.speed(0)
en7.color('red')
en7.goto(100, 0)
en7.dx = 40
en7.dy = 40
# Enemy 8
en8 = turtle.Turtle()
en8.shape('circle')
en8.shapesize(1)
en8.penup()
en8.speed(0)
en8.color('red')
en8.goto(150, 0)
en8.dx = 20
en8.dy = 20
# Enemy 9
en9 = turtle.Turtle()
en9.shape('circle')
en9.shapesize(1)
en9.penup()
en9.speed(0)
en9.color('red')
en9.goto(200, 0)
en9.dx = 40
en9.dy = 40
# Stars & death times
stars = 0
death_times = 0
# Stars & death times message
sc = turtle.Turtle()
sc.speed(0)
sc.penup()
sc.hideturtle()
sc.color('black')
sc.goto(0, 250)
sc.write('Stars: 0 , Death times: 0', align='center', font=('ds-digital', 24, 'normal'))
# Wining message
wm = turtle.Turtle()
wm.speed(0)
wm.penup()
wm.hideturtle()
wm.color('green')
wm.goto(0, 0)

# Star 1
st1 = turtle.Turtle()
st1.speed(0)
st1.penup()
st1.shape('triangle')
st1.shapesize(1)
st1.color('#000080')
st1.goto(random.randint(-280, 280), random.randint(-180, 180))
# Star 2
st2 = turtle.Turtle()
st2.speed(0)
st2.penup()
st2.shape('triangle')
st2.shapesize(1)
st2.color('#000080')
st2.goto(random.randint(-280, 280), random.randint(-180, 180))
st2.degrees()
# Star 3
st3 = turtle.Turtle()
st3.speed(0)
st3.penup()
st3.shape('triangle')
st3.shapesize(1)
st3.color('#000080')
st3.goto(random.randint(-280, 280), random.randint(-180, 180))
# Star 4
st4 = turtle.Turtle()
st4.speed(0)
st4.penup()
st4.shape('triangle')
st4.shapesize(1)
st4.color('#000080')
st4.goto(random.randint(-280, 280), random.randint(-180, 180))


# Methods to move
def player_up():
    y = player.ycor()
    y += 4
    player.sety(y)


def player_down():
    y = player.ycor()
    y -= 4
    player.sety(y)


def player_right():
    x = player.xcor()
    x += 4
    player.setx(x)


def player_left():
    x = player.xcor()
    x -= 4
    player.setx(x)


# Listen to keyboard
wn.listen()
wn.onkeypress(player_up, 'w')
wn.onkeypress(player_down, 's')
wn.onkeypress(player_right, 'd')
wn.onkeypress(player_left, 'a')

while True:
    wn.update()
    # Move Enemies
    en1.sety(en1.ycor() + en1.dy)
    en2.sety(en2.ycor() - en2.dy)
    en3.sety(en3.ycor() + en3.dy)
    en4.sety(en4.ycor() - en4.dy)
    en5.sety(en5.ycor() + en5.dy)
    en6.sety(en6.ycor() - en6.dy)
    en7.sety(en7.ycor() + en7.dy)
    en8.sety(en8.ycor() - en8.dy)
    en9.sety(en9.ycor() + en9.dy)

    # Border of Enemies
    if en1.ycor() > 150 or en3.ycor() > 150 or en5.ycor() > 150 or en7.ycor() > 150 or en9.ycor() > 150:
        en1.sety(150)
        en1.dy *= -1
        en3.sety(150)
        en3.dy *= -1
        en5.sety(150)
        en5.dy *= -1
        en7.sety(150)
        en7.dy *= -1
        en9.sety(150)
        en9.dy *= -1
    elif en1.ycor() < -150 or en3.ycor() < -150 or en5.ycor() < -150 or en7.ycor() < -150 or en9.ycor() < -150:
        en1.sety(-150)
        en1.dy *= -1
        en3.sety(-150)
        en3.dy *= -1
        en5.sety(-150)
        en5.dy *= -1
        en7.sety(-150)
        en7.dy *= -1
        en9.sety(-150)
        en9.dy *= -1

    if en2.ycor() < -150 or en4.ycor() < -150 or en6.ycor() < -150 or en8.ycor() < -150:
        en2.sety(-150)
        en2.dy *= -1
        en4.sety(-150)
        en4.dy *= -1
        en6.sety(-150)
        en6.dy *= -1
        en8.sety(-150)
        en8.dy *= -1
    elif en2.ycor() > 150 or en4.ycor() > 150 or en6.ycor() > 150 or en8.ycor() > 150:
        en2.sety(150)
        en2.dy *= -1
        en4.sety(150)
        en4.dy *= -1
        en6.sety(150)
        en6.dy *= -1
        en8.sety(150)
        en8.dy *= -1

    # Borders of the walls
    # B1 border
    if (player.xcor() > 450) and (player.ycor() < (b1.ycor() + 90) and (player.ycor() > (b1.ycor() - 90))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center', font=('ds-digital', 24, 'normal'))
    # B2 border
    elif (player.xcor() < -450) and (player.ycor() < (b2.ycor() + 90) and (player.ycor() > (b2.ycor() - 90))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B3 border
    elif (player.ycor() >= 80) and (player.ycor() <= 90) and (player.xcor() > 334 and (player.xcor() < 454)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B4 border
    elif (player.ycor() <= -80) and (player.ycor() >= -90) and (player.xcor() > 334 and (player.xcor() < 454)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B5 border
    elif (player.ycor() >= 80) and (player.ycor() <= 90) and (player.xcor() < -334 and (player.xcor() > -454)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B6 border
    elif (player.ycor() <= -80) and (player.ycor() >= -90) and (player.xcor() < -334 and (player.xcor() > -454)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B7 border
    elif (player.xcor() >= 338) and (player.xcor() <= 340) and (player.ycor() < (b7.ycor() + 30) and (player.ycor() > (b7.ycor() - 30))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B8 border
    elif (player.xcor() >= 338) and (player.xcor() <= 340) and (player.ycor() < (b8.ycor() + 30) and (player.ycor() > (b8.ycor() - 30))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B9 border
    elif (player.xcor() <= -338) and (player.xcor() >= -340) and (player.ycor() < (b9.ycor() + 30) and (player.ycor() > (b9.ycor() - 30))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B10 border
    elif (player.xcor() <= -338) and (player.xcor() >= -340) and (player.ycor() < (b10.ycor() + 30) and (player.ycor() > (b10.ycor() - 30))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B11 border
    elif (player.xcor() >= 282) and (player.xcor() <= 342) and (player.ycor() < (b11.ycor() + 10) and (player.ycor() > (b11.ycor() - 10))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B12 border
    elif (player.xcor() >= 282) and (player.xcor() <= 342) and (player.ycor() < (b12.ycor() + 10) and (player.ycor() > (b12.ycor() - 10))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B13 border
    elif (player.xcor() <= -282) and (player.xcor() >= -342) and (player.ycor() < (b13.ycor() + 10) and (player.ycor() > (b13.ycor() - 10))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B14 border
    elif (player.xcor() <= -282) and (player.xcor() >= -342) and (player.ycor() < (b14.ycor() + 10) and (player.ycor() > (b14.ycor() - 10))):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B15 border
    elif (player.xcor() >= 280) and (player.xcor() <= 290) and (player.ycor() < -20 and (player.ycor() > -180)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B16 border
    elif (player.xcor() >= 280) and (player.xcor() <= 290) and (player.ycor() > 20 and (player.ycor() < 180)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B17 border
    elif (player.xcor() <= -280) and (player.xcor() >= -290) and (player.ycor() < -20 and (player.ycor() > -180)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B18 border
    elif (player.xcor() <= -280) and (player.xcor() >= -290) and (player.ycor() > 20 and (player.ycor() < 180)):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B19 border
    elif (player.ycor() >= 180) and (player.ycor() <= 190) and (player.xcor() >= -290) and (player.xcor() <= 290):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # B20 border
    elif (player.ycor() <= -180) and (player.ycor() >= -190) and (player.xcor() >= -290) and (player.xcor() <= 290):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))

    # Border of Enemies with player
    # Enemy1 border
    if (player.xcor() <= en1.xcor() + 10) and (player.xcor() >= en1.xcor() - 10) and (player.ycor() <= en1.ycor() + 10) and (player.ycor() >= en1.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy2 border
    elif (player.xcor() <= en2.xcor() + 10) and (player.xcor() >= en2.xcor() - 10) and (player.ycor() <= en2.ycor() + 10) and (player.ycor() >= en2.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy3 border
    elif (player.xcor() <= en3.xcor() + 10) and (player.xcor() >= en3.xcor() - 10) and (player.ycor() <= en3.ycor() + 10) and (player.ycor() >= en3.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy4 border
    elif (player.xcor() <= en4.xcor() + 10) and (player.xcor() >= en4.xcor() - 10) and (player.ycor() <= en4.ycor() + 10) and (player.ycor() >= en4.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy5 border
    elif (player.xcor() <= en5.xcor() + 10) and (player.xcor() >= en5.xcor() - 10) and (player.ycor() <= en5.ycor() + 10) and (player.ycor() >= en5.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy6 border
    elif (player.xcor() <= en6.xcor() + 10) and (player.xcor() >= en6.xcor() - 10) and (player.ycor() <= en6.ycor() + 10) and (player.ycor() >= en6.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy7 border
    elif (player.xcor() <= en7.xcor() + 10) and (player.xcor() >= en7.xcor() - 10) and (player.ycor() <= en7.ycor() + 10) and (player.ycor() >= en7.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy8 border
    elif (player.xcor() <= en8.xcor() + 10) and (player.xcor() >= en8.xcor() - 10) and (player.ycor() <= en8.ycor() + 10) and (player.ycor() >= en8.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Enemy9 border
    elif (player.xcor() <= en9.xcor() + 10) and (player.xcor() >= en9.xcor() - 10) and (player.ycor() <= en9.ycor() + 10) and (player.ycor() >= en9.ycor() - 10):
        player.setx(-380)
        player.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        death_times += 1
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Border of stars :
    # Star 1 border
    if (player.xcor() <= st1.xcor() + 10) and (player.xcor() >= st1.xcor() - 10) and (player.ycor() <= st1.ycor() + 10) and (player.ycor() >= st1.ycor() - 10):
        stars += 1
        st1.sety(240)
        st1.setx(240)
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Star 2 border
    elif (player.xcor() <= st2.xcor() + 10) and (player.xcor() >= st2.xcor() - 10) and (player.ycor() <= st2.ycor() + 10) and (player.ycor() >= st2.ycor() - 10):
        stars += 1
        st2.sety(240)
        st2.setx(220)
        st2.clear()
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Star 3 border
    elif (player.xcor() <= st3.xcor() + 10) and (player.xcor() >= st3.xcor() - 10) and (player.ycor() <= st3.ycor() + 10) and (player.ycor() >= st3.ycor() - 10):
        stars += 1
        st3.sety(240)
        st3.setx(200)
        st3.clear()
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Star 4 border
    elif (player.xcor() <= st4.xcor() + 10) and (player.xcor() >= st4.xcor() - 10) and (player.ycor() <= st4.ycor() + 10) and (player.ycor() >= st4.ycor() - 10):
        stars += 1
        st4.sety(240)
        st4.setx(180)
        st4.clear()
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 24, 'normal'))
    # Final line
    if (player.xcor() >= 338) and (player.ycor() < 15) and (player.ycor() > -15) and (stars <= 1):
        en1.sety(0)
        en2.sety(0)
        en3.sety(0)
        en4.sety(0)
        en5.sety(0)
        en6.sety(0)
        en7.sety(0)
        en8.sety(0)
        en9.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        wm.clear()
        wm.write('You lost, at least get two stars.', align='center', font=('ds-digital', 30, 'normal'))
        time.sleep(5)
        wm.clear()
        player.setx(-380)
        player.sety(0)
        sc.clear()
        stars = 0
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center', font=('ds-digital', 24, 'normal'))
    elif (player.xcor() >= 338) and (player.ycor() < 15) and (player.ycor() > -15) and (3 >= stars >= 2):
        en1.sety(0)
        en2.sety(0)
        en3.sety(0)
        en4.sety(0)
        en5.sety(0)
        en6.sety(0)
        en7.sety(0)
        en8.sety(0)
        en9.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        wm.clear()
        wm.write('Congratulations, you lost\nyou must have 4 stars to win.', align='center', font=('ds-digital', 30, 'normal'))
        time.sleep(8)
        wm.clear()
        player.setx(-380)
        player.sety(0)
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center', font=('ds-digital', 24, 'normal'))
    elif (player.xcor() >= 338) and (player.ycor() < 15) and (player.ycor() > -15) and (stars == 4):
        en1.sety(0)
        en2.sety(0)
        en3.sety(0)
        en4.sety(0)
        en5.sety(0)
        en6.sety(0)
        en7.sety(0)
        en8.sety(0)
        en9.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        wm.clear()
        wm.write("Did i say 4 stars?,\n i mean 50 stars", align='center', font=('ds-digital', 30, 'normal'))
        time.sleep(8)
        wm.clear()
        player.setx(-380)
        player.sety(0)
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center', font=('ds-digital', 30, 'normal'))
    elif (player.xcor() >= 338) and (player.ycor() < 15) and (player.ycor() > -15) and (stars > 50):
        en1.sety(0)
        en2.sety(0)
        en3.sety(0)
        en4.sety(0)
        en5.sety(0)
        en6.sety(0)
        en7.sety(0)
        en8.sety(0)
        en9.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        wm.clear()
        wm.write("50 mean 50 not more than that", align='center', font=('ds-digital', 30, 'normal'))
        time.sleep(8)
        wm.clear()
        player.setx(-380)
        player.sety(0)
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 30, 'normal'))
    elif (player.xcor() >= 338) and (player.ycor() < 15) and (player.ycor() > -15) and (stars == 50):
        en1.sety(0)
        en2.sety(0)
        en3.sety(0)
        en4.sety(0)
        en5.sety(0)
        en6.sety(0)
        en7.sety(0)
        en8.sety(0)
        en9.sety(0)
        st1.goto(random.randint(-280, 280), random.randint(-180, 180))
        st2.goto(random.randint(-280, 280), random.randint(-180, 180))
        st3.goto(random.randint(-280, 280), random.randint(-180, 180))
        st4.goto(random.randint(-280, 280), random.randint(-180, 180))
        stars = 0
        wm.clear()
        wm.write("Congratulations, you know the secret.", align='center', font=('ds-digital', 20, 'normal'))
        time.sleep(10)
        wm.clear()
        player.setx(-380)
        player.sety(0)
        death_times = 0
        sc.clear()
        sc.write('Stars: {} , Death times: {}'.format(stars, death_times), align='center',
                 font=('ds-digital', 30, 'normal'))
