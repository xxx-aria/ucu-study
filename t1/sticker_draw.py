import math
from turtle import *

WHITE = "#FFFFFF"
DARK = "#1C2431"
GREEN = "#9EE07C"
RED = "#F97676"

Screen().setup(width=1200, height=800)
speed(0)
PEN_WIDTH = 12
width(PEN_WIDTH)

def draw_4(num_h, num_w):
    # 90 + 140 + 130 = 360
    setheading(90)
    forward(num_h)
    left(140)
    forward(num_w * 7/6)
    left(130)
    forward(num_w)


def draw_0(num_h, num_w):
    straight_line = num_h - num_w
    setheading(0)
    circle(num_w/2, 90)
    forward(straight_line)
    circle(num_w/2, 180)
    forward(straight_line)
    circle(num_w/2, 90)
    circle(num_w/2, -90)
    angle = math.degrees(math.atan((straight_line/num_w)))
    diag = math.sqrt(straight_line ** 2 + num_w ** 2)
    setheading(angle)
    forward(diag)


def draw_shell(shell_color, text_color, error_color):
    # рівнобічна трапеція top_w || bottom_w (side_len - бічна)
    top_w = 520
    bottom_w = 680
    side_len = 320
    trap_h = math.sqrt(side_len**2 - ((bottom_w-top_w)/2)**2)

    side_angle = 60
    # радіус для нижньої дуги
    radius = 800

    x_shift = -50
    y_shift = trap_h/2 + 80

    pencolor(shell_color)
    fillcolor(shell_color)
    penup()
    goto(x_shift, y_shift)
    setheading(0)
    pendown()
    begin_fill()
    forward(top_w/2)
    right(side_angle)
    forward(side_len)

    # кут повороту
    central_angle = math.degrees(2*math.asin((bottom_w/2)/radius))
    setheading(180 + central_angle/2)
    circle(-radius, central_angle)

    setheading(side_angle)
    forward(side_len)
    goto(x_shift, y_shift)
    end_fill()
    penup()

    y_shift_text = y_shift - trap_h/3
    goto(x_shift - 15, y_shift_text - 30)
    pencolor(error_color)
    pendown()

    num_h = 100
    four_w = 80
    zero_w = 50
    width(PEN_WIDTH - 2)
    draw_4(num_h, four_w)
    penup()
    goto(x_shift + 55, y_shift_text - 30)
    pendown()
    draw_0(num_h, zero_w)
    penup()
    goto(x_shift + 165, y_shift_text - 30)
    pendown()
    draw_4(num_h, four_w)
    width(PEN_WIDTH)
    penup()

    pencolor(text_color)
    goto(x_shift - 80, y_shift_text - 205)
    write('SHELL\nNOT FOUND', font=('Courier', 28))
    home()


def draw_body(skin_color, border_color):
    body_h = 90
    body_len = 470
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    goto(-body_len/2 + 20, body_h - 80)
    setheading(0)
    pendown()
    begin_fill()
    forward(body_len)
    circle(-body_h, 180)
    forward(body_len)
    circle(-body_h, 180)
    end_fill()

    penup()
    home()


def draw_head(skin_color, border_color):
    head_r = 150
    head_x = -330
    head_y = -120
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    goto(head_x, head_y)
    setheading(0)
    pendown()
    begin_fill()
    circle(head_r)
    end_fill()
    penup()
    goto(head_x - head_r/3, head_y + 20 + head_r)
    dot(30, border_color)
    goto(head_x + head_r/3, head_y + 20 + head_r)
    dot(30, border_color)
    goto(head_x - 40, head_y - 60 + head_r)
    pendown()
    forward(80)

    penup()
    home()


def draw_leg(skin_color, border_color, x_cor, y_cor):
    leg_l = 110
    leg_w = 60
    corner_r = 30
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    goto(x_cor, y_cor)
    setheading(-90)
    pendown()
    begin_fill()
    forward(leg_l)
    circle(corner_r, 90)
    forward(leg_w)
    circle(corner_r, 90)
    forward(leg_l)
    # місце, де нога з'єднується з тілом (без контуру)
    pencolor(skin_color)
    circle(corner_r, 90)
    forward(leg_w)
    circle(corner_r, 90)
    end_fill()

    penup()
    home()


def draw_tail(skin_color, border_color):
    tail_x = 345
    tail_y = -80
    pencolor(border_color)
    fillcolor(skin_color)
    penup()
    goto(tail_x, tail_y)
    setheading(-30)
    pendown()
    begin_fill()
    forward(100)
    right(150)
    forward(110)
    end_fill()

    penup()
    home()

# лапи позаду тіла
draw_leg(GREEN, DARK, -250, -130)
draw_leg(GREEN, DARK, 100, -130)

draw_body(GREEN, DARK)

# лапи перед тілом
draw_leg(GREEN, DARK, -180, -150)
draw_leg(GREEN, DARK, 170, -150)

draw_shell(DARK, WHITE, RED)
draw_head(GREEN, DARK)

draw_tail(GREEN, DARK)

hideturtle()
done()
