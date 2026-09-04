import math
from turtle import *

white = "#FFFFFF"
dark = "#1C2431"
green = "#9EE07C"

Screen().setup(width=1200, height=800)
speed(0)
width(12)

def draw_shell(shell_color, text_color):
    # рівнобічна трапеція ABCD(AD || BC, BC < AD); BC = a, AD = b, AB = c
    a = 520
    b = 680
    c = 320
    h = math.sqrt(c**2 - ((b-a)/2)**2)
    turn = 60
    # радіус для нижньої дуги
    R = 800

    x_shift = -50
    y_shift = h/2+80

    pencolor(shell_color)
    fillcolor(shell_color)

    penup()
    setheading(0)
    goto(x_shift, y_shift)
    pendown()

    begin_fill()

    forward(a/2)
    right(turn)
    forward(c)
    # кут повороту
    central_angle = math.degrees(2*math.asin((b/2)/R))
    setheading(180+central_angle/2)
    circle(-R, central_angle)
    setheading(turn)
    forward(c)
    goto(x_shift, y_shift)

    end_fill()
    penup()

    goto(x_shift-80, y_shift-h/3-65)
    pendown()
    pencolor("#F97676")
    write('404', font=('Mono', 50, 'bold'))
    penup()
    pencolor("#FFFFFF")
    goto(x_shift-80, y_shift-h/3-210)
    pendown()
    write(f'SHELL\nNOT FOUND', font=('Courier', 28))
    penup()

    home()

def draw_body(skin_color, border_color):
    body_h = 90
    body_len = 470
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    goto(-body_len/2+20, body_h-80)
    pendown()
    begin_fill()
    forward(body_len)
    circle(-body_h, 180)
    forward(body_len)
    circle(-body_h, 180)
    end_fill()
    pendown()
    home()


def draw_head(skin_color, border_color):
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    setheading(0)
    goto(-330, -120)
    pendown()
    begin_fill()

    head_r = 150
    circle(head_r)
    end_fill()
    penup()

    goto(-330-head_r/3, -100+head_r)
    dot(30, border_color)
    goto(-330+head_r/3, -100+head_r)
    dot(30, border_color)

    goto(-370, -180+head_r)
    pendown()
    forward(80)
    penup()

    home()

def draw_leg(skin_color, border_color, x_cor, y_cor):
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    setheading(-90)
    goto(x_cor, y_cor)
    pendown()
    begin_fill()

    leg_l = 110
    leg_w = 60
    angle_r = 30

    forward(leg_l)
    circle(angle_r, 90)
    forward(leg_w)
    circle(angle_r, 90)
    forward(leg_l)

    pencolor(skin_color)
    circle(angle_r, 90)
    forward(leg_w)
    circle(angle_r, 90)
    pencolor(border_color)
    penup()

    end_fill()
    home()

def draw_tail(skin_color, border_color):
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    setheading(-30)
    goto(345, -80)
    pendown()
    begin_fill()
    forward(100)
    right(150)
    forward(110)
    penup()

    end_fill()
    home()

draw_leg(green, dark, -250, -130)
draw_leg(green, dark, 100, -130)

draw_body(green, dark)

draw_leg(green, dark, -180, -150)
draw_leg(green, dark, 170, -150)

draw_shell(dark, white)
draw_head(green, dark)

draw_tail(green, dark)

speed(0)



hideturtle()
done()
