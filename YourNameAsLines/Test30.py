try:
    from tkinter import *
    import random

    window = Tk()
    window.title("My project")
    canvas = Canvas(bg="black", width=1200, height=1200 / 2)
    canvas.pack()

    name = str.lower(input('Please enter your name: '))
    name_l = len(name)

    # number list as num
    with open('num.txt', 'r') as num_file:
        num = num_file.readlines()
        for i in range(len(num)):
            if '\n' in num[i]:
                num[i] = num[i].replace('\n', '')

    # colors list as colors
    with open('colors.txt', 'r') as colors_file:
        colors = colors_file.readlines()
        for j in range(len(colors)):
            if '\n' in colors[j]:
                colors[j] = colors[j].replace('\n', '')

    # draw lines
    if name != 'mohammed':
        for e in range(0, name_l):
            canvas.create_line(random.choice(num), random.choice(num), random.choice(num), random.choice(num),
                               fill=random.choice(colors))
            canvas.create_line(random.choice(num), random.choice(num), random.choice(num), random.choice(num),
                               fill=random.choice(colors))
            canvas.wait_window()

    else:

        canvas.create_line(50, 50, 50, 150, width=3, fill="green")
        canvas.create_line(50, 50, 60, 150, width=3, fill="green")
        canvas.create_line(60, 150, 70, 50, width=3, fill="green")
        canvas.create_line(70, 50, 70, 150, width=3, fill="green")
        canvas.create_oval(80, 50, 140, 150, width=3, outline="green", fill="black")
        canvas.create_line(150, 50, 150, 150, width=3, fill="green")
        canvas.create_line(150, 90, 170, 90, width=3, fill="green")
        canvas.create_line(170, 90, 170, 150, width=3, fill="green")
        canvas.create_line(180, 150, 190, 50, width=3, fill="green")
        canvas.create_line(190, 50, 200, 150, width=3, fill="green")
        canvas.create_line(180, 120, 200, 120, width=3, fill="green")
        canvas.create_line(210, 50, 210, 150, width=3, fill="green")
        canvas.create_line(210, 50, 220, 150, width=3, fill="green")
        canvas.create_line(220, 150, 230, 50, width=3, fill="green")
        canvas.create_line(230, 50, 230, 150, width=3, fill="green")
        canvas.create_line(240, 50, 240, 150, width=3, fill="green")
        canvas.create_line(240, 50, 250, 150, width=3, fill="green")
        canvas.create_line(250, 150, 260, 50, width=3, fill="green")
        canvas.create_line(260, 50, 260, 150, width=3, fill="green")
        canvas.create_line(270, 50, 270, 150, width=3, fill="green")
        canvas.create_line(270, 50, 290, 50, width=3, fill="green")
        canvas.create_line(270, 100, 290, 100, width=3, fill="green")
        canvas.create_line(270, 150, 290, 150, width=3, fill="green")
        canvas.create_line(300, 50, 300, 150, width=3, fill="green")
        canvas.create_line(300, 50, 330, 100, width=3, fill="green")
        canvas.create_line(330, 100, 300, 150, width=3, fill="green")
        canvas.create_line(340, 70, 370, 150, width=3, fill="green")
        canvas.create_line(370, 150, 400, 70, width=3, fill="green")
        canvas.create_line(340, 70, 370, 100, width=3, fill="green")
        canvas.create_line(370, 100, 400, 70, width=3, fill="green")
        for i in range(0, 10):
            v = i * 0.1
            canvas.create_line(50, 1600 * v, 400, 1600 * v, width=i, fill="steelblue")
            canvas.create_line(50, 1700 * v, 400, 1700 * v, width=i, fill="steelblue")
            canvas.create_line(50, 1800 * v, 400, 1800 * v, width=i, fill="steelblue")
            canvas.create_line(50, 1900 * v, 400, 1900 * v, width=i, fill="steelblue")
            canvas.create_line(50, 2000 * v, 400, 2000 * v, width=i, fill="steelblue")
        canvas.wait_window()

except Exception as e:
    print('ERROR: ', e)
