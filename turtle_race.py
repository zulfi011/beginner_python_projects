import turtle
import random

COLORS = ["red","blue","green","black","orange","pink","purple","yellow","brown","gray"]
WIDTH,HEIGHT = 700, 700

def start_race(racers,colors):
    while True:
        for racer in racers:
            racer.fd(random.randint(1,20))
            if racer.xcor()>=WIDTH//2 -20:
                return colors[racers.index(racer)]

def create_turtles(colors):
    racers = []
    ypos = HEIGHT//(len(colors)+1)
    for i in range(len(colors)):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(colors[i])
        racer.penup()
        racer.setpos(-WIDTH//2 + 20,-HEIGHT//2 + (i+1)*ypos)
        racer.pendown()
        racer.pencolor(colors[i])
        racers.append(racer)
    return racers

def draw_finish_line():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.setpos(WIDTH//2 -20 ,HEIGHT//2)
    t.pendown()
    t.pensize(5)
    t.speed(0)
    t.goto(WIDTH//2 -20,-HEIGHT//2)

def bets(colors,players):
    colors = colors[0:players]
    while True:
        clr_ch = ''
        for i in colors:
            clr_ch += i + "\n"
        bet = turtle.textinput('place bet: ',clr_ch +' which color: ').lower()
        if bet in colors:
            return bet

def players_amt():
    while True:
        line = turtle.textinput('','turtles 2-10 or q to quit').lower()
        if line == 'q':
            quit()
        elif line.isdigit() and 2<=int(line)<=10:
            return int(line)

def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('racing game!!!')

def main():
    init_screen()
    players =  players_amt()
    random.shuffle(COLORS)
    colors = COLORS[0:players]
    bet = bets(colors,players)
    turtle.textinput('','enter to start race!!')
    draw_finish_line()
    racers = create_turtles(colors)
    race = start_race(racers,colors)
    if bet == race:
        turtle.textinput('','you won')
    else:
        turtle.textinput('',f'you lost {race} is the winner')

    turtle.Screen().exitonclick()

main()