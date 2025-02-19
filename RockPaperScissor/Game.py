# imports
import turtle
import time
import random

# set up screen
wn = turtle.Screen()
wn.title("R_P_S_Game")
wn.bgcolor('gold')
wn.setup(width=600, height=600)

# Variables
win = 0
lose = 0
draw = 0

# Rock object
Rock = turtle.Turtle()
Rock.shapesize(3)
Rock.penup()
Rock.pensize(2)
Rock.speed(0)
wn.addshape('Rock2.gif')
Rock.shape('Rock2.gif')
Rock.goto(-240, -220)


# paper object
Paper = turtle.Turtle()
Paper.shapesize(3)
Paper.penup()
Paper.pensize(2)
Paper.speed(0)
wn.addshape('Paper2.gif')
Paper.shape('Paper2.gif')
Paper.goto(0, -220)

# scissors object
Scissors = turtle.Turtle()
Scissors.shapesize(3)
Scissors.penup()
Scissors.pensize(2)
Scissors.speed(0)
wn.addshape('Scissors2.gif')
Scissors.shape('Scissors2.gif')
Scissors.goto(240, -220)


# variables on screen
va = turtle.Turtle()
va.speed(0)
va.penup()
va.hideturtle()
va.color('black')
va.goto(0, 250)
va.write('Win: 0  Lose: 0  Draw: 0', align='center', font=('ds-digital', 24, 'normal'))

# Massage of win or lose or draw
ma = turtle.Turtle()
ma.speed(0)
ma.penup()
ma.hideturtle()
ma.color('white')
ma.write('', align='center', font=('ds-digital', 24, 'normal'))
ma.goto(0, 0)


# متغير يساعد على جعل اللاعب والعدو يختارا شكلاً مره واحده
RPS_times = 0
# شكل اللاعب
p_shape = ''
# شكل العدو
en_shape = ''
# هل اختار العدو شكلاً ما ؟
enemy_key = 'False'


# تعريف داله لطباعه حجره على الشاشه
def rock():
    # استدعاء المتغيرات الى داخل الداله
    global RPS_times
    global p_shape
    # اذا كان العداد يساوي صفر افعل الاتي :
    if RPS_times == 0:
        Rock2 = turtle.Turtle()
        wn.addshape('Rock_hand2.gif')
        Rock2.shape('Rock_hand2.gif')
        Rock2.shapesize(5)
        Rock2.penup()
        Rock2.pensize(2)
        Rock2.speed(0)
        Rock2.goto(-200, 0)
        # ثم اجمع قيمه العداد بواحد حتى لا يختار المستخدم اكثر من شكل
        RPS_times += 1
        # شكل اللاعب هو صخرة
        p_shape = 'Rock'
    # اذا لم يساوي صفر اذاً لا تفعل شيء
    else:
        pass


# تعريف داله لطباعه ورقه على الشاشه
def paper():
    # استدعاء المتغيرات الى داخل الداله
    global RPS_times
    global p_shape
    # اذا كان العداد يساوي صفر افعل الاتي :
    if RPS_times == 0:
        paper2 = turtle.Turtle()
        paper2.shapesize(3)
        paper2.penup()
        paper2.pensize(2)
        paper2.speed(0)
        wn.addshape('Paper_hand2.gif')
        paper2.shape('Paper_hand2.gif')
        paper2.goto(-200, 0)
        # ثم اجمع قيمه العداد بواحد حتى لا يختار المستخدم اكثر من شكل
        RPS_times += 1
        # شكل اللاعب هو ورقه
        p_shape = 'paper'

    # اذا لم يساوي صفر اذاً لا تفعل شيء
    else:
        pass


# تعريف داله لطباعه مقص على الشاشه
def scissors():
    # استدعاء المتغيرات الى داخل الداله
    global RPS_times
    global p_shape
    # اذا كان العداد يساوي صفر افعل الاتي :
    if RPS_times == 0:
        scissors2 = turtle.Turtle()
        scissors2.shapesize(3)
        scissors2.penup()
        scissors2.pensize(2)
        scissors2.speed(0)
        wn.addshape('Scissors_hand2.gif')
        scissors2.shape('Scissors_hand2.gif')
        scissors2.goto(-200, 40)
        # ثم اجمع قيمه العداد بواحد حتى لا يختار المستخدم اكثر من شكل
        RPS_times += 1
        # شكل اللاعب هو مقص
        p_shape = 'scissors'
    # اذا لم  يساوي صفر اذاً لا تفعل شيء
    else:
        pass


# تعريف داله العدو لطباعه حجره او ورقه او مقص على الشاشه
def enemy():
    # استدعاء المتغيرات الى داخل الداله
    global en_shape
    global enemy_key
    global RPS_times
    # اذا كان العداد يساوي واحد افعل الاتي :
    if RPS_times == 1:
        enemy = turtle.Turtle()
        enemy.shapesize(4)
        enemy.penup()
        enemy.pensize(2)
        enemy.speed(0)
        shape_list = ['Rock_hand_en2.gif', 'Paper_hand_en2.gif', 'Scissors_hand_en2.gif']
        shape = random.choice(shape_list)
        wn.addshape(shape)
        enemy.shape(shape)
        enemy.goto(200, 50)
        # تمت طباعه العدو على الشاشه
        enemy_key = 'True'
        RPS_times += 1
        if shape == 'Rock_hand_en2.gif':
            en_shape = 'Rock'
        elif shape == 'Paper_hand_en2.gif':
            en_shape = 'paper'
        elif shape == 'Scissors_hand_en2.gif':
            en_shape = 'scissors'

    # اذا لم يكن العداد يساوي واحد لا تفعل شيء
    else:
        pass


# داله تقوم بإعادة ضبط المتغيرات واخرى
def clear():
    global RPS_times
    global enemy_key
    # حذف النص في منتصف الشاشه
    ma.clear()
    # اعاده ضبط المتغيرات
    enemy_key = 'False'
    RPS_times = 0
    # حذف اللاعب والعدو
    gc = turtle.Turtle()
    gc.shapesize(20)
    gc.pensize(5)
    gc.penup()
    gc.speed(0)
    wn.addshape('Gold_color.gif')
    gc.shape('Gold_color.gif')
    gc.goto(200, 80)

    gc2 = turtle.Turtle()
    gc2.shapesize(20)
    gc2.pensize(5)
    gc2.penup()
    gc2.speed(0)
    wn.addshape('Gold_color.gif')
    gc2.shape('Gold_color.gif')
    gc2.goto(200, 0)

    gc3 = turtle.Turtle()
    gc3.shapesize(20)
    gc3.pensize(5)
    gc3.penup()
    gc3.speed(0)
    wn.addshape('Gold_color.gif')
    gc3.shape('Gold_color.gif')
    gc3.goto(-200, 0)

    gc4 = turtle.Turtle()
    gc4.shapesize(20)
    gc4.pensize(5)
    gc4.penup()
    gc4.speed(0)
    wn.addshape('Gold_color.gif')
    gc4.shape('Gold_color.gif')
    gc4.goto(-200, 50)


# استمع إلى الكيبورد
wn.listen()
# عند الضغط على r يتم استدعاء الدله rock
wn.onkeypress(rock, 'r')
# // // //
wn.onkeypress(paper, 'p')
# // // //
wn.onkeypress(scissors, 's')


while True:
    wn.update()
    # draw
    if RPS_times == 1:
        enemy()
    if en_shape == p_shape and enemy_key == 'True':
        ma.clear()
        ma.write('Draw!', align='center', font=('ds-digital', 24, 'normal'))
        draw += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'

    # lose
    elif en_shape == 'paper' and p_shape == 'Rock' and enemy_key == 'True':
        ma.clear()
        ma.write('You lose!', align='center', font=('ds-digital', 24, 'normal'))
        lose += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'
    # win
    elif en_shape == 'scissors' and p_shape == 'Rock' and enemy_key == 'True':
        ma.clear()
        ma.write('You win!', align='center', font=('ds-digital', 24, 'normal'))
        win += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'
    # lose
    elif en_shape == 'scissors' and p_shape == 'paper' and enemy_key == 'True':
        ma.clear()
        ma.write('You lose!', align='center', font=('ds-digital', 24, 'normal'))
        lose += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'
    # win
    elif en_shape == 'Rock' and p_shape == 'paper' and enemy_key == 'True':
        ma.clear()
        ma.write('You win!', align='center', font=('ds-digital', 24, 'normal'))
        win += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'
    # lose
    elif en_shape == 'Rock' and p_shape == 'scissors' and enemy_key == 'True':
        ma.clear()
        ma.write('You lose!', align='center', font=('ds-digital', 24, 'normal'))
        lose += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'
    # win
    elif en_shape == 'paper' and p_shape == 'scissors' and enemy_key == 'True':
        ma.clear()
        ma.write('You win!', align='center', font=('ds-digital', 24, 'normal'))
        win += 1
        va.clear()
        va.write('Win: {}  Lose: {}  Draw: {}'.format(win, lose, draw), align='center',
                 font=('ds-digital', 24, 'normal'))
        time.sleep(3)
        clear()
        enemy_key = 'False'
