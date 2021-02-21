import pygame
import play
from random import randint

# if a==b:
n = 0

fon = play.new_image(image = 'fon.png')
    
you_lose = play.new_image(
    image = "You_lose.png")
you_lose.hide()

''' tilda-макет сайт, tilda- сделать кам сайт'''



bird = play.new_image(
    image = 'bird1.png',
    x = -250,
    y = 0,
    size = 150)

status = 1
def drow_truba(y_cor, rast):
    delta = 475
    truba2 = play.new_image(
        image = 'truba2.png',
        x = 450,
        y = y_cor - delta,
        size = 100,
        )

    truba = play.new_image(
        image = 'truba.png',
        x = 450,
        y = y_cor + rast,
        size = 100,
    )
    truba.satus = 1
    score = play.new_image(
        image = 'score.png',
        x = -300,
        y = 200
    )

    return truba, truba2

bird.start_physics(obeys_gravity = True, bounciness = False)

truba_list = []

restart_button = play.new_image(
    image = "restart_button.png",
    x = 200,
    y = -150
)
restart_button.hide()

score_numbere = play.new_text(
    words = '0',
    x = -300,
    y = 165,
    color = 'red'
)

exit_button = play.new_image(
    image = "exit_button.png",
    x = -200,
    y = -150
)
exit_button.hide()

@play.repeat_forever
async def do():
    global status, n
    if status==1:
        a = drow_truba(randint(-200, 200), randint(200, 230))
        n = n + 1
        score_numbere.words = str(n)
        truba_list.append(a)
        await play.timer(3)
    else:
        for truba in truba_list:
            truba[0].remove()
            truba[1].remove()
            truba_list.remove(truba)
            status = 2


@play.repeat_forever
async def run():
    for truba in truba_list:
        truba[0].x-= 5
        truba[1].x-= 5
        
@exit_button.when_clicked
def do():
    exit()

@restart_button.when_clicked
def do():
    global status
    status = 1
    bird.start_physics(bounciness = False)
    bird.show()
    bird.y = 0
    exit_button.hide()
    restart_button.hide()
    you_lose.hide()




@play.repeat_forever
def lose():
    global status
    if status == 1:

        for truba in truba_list:
            if truba[0].x < -400:
                # truba_list.hide(truba)
                truba[0].remove()
                truba[1].remove()
                truba_list.remove(truba)
            if bird.is_touching(truba[0]) or bird.is_touching(truba[1]):
                you_lose.show()
                bird.stop_physics()
                bird.hide()
                status = 0
                exit_button.show()
                restart_button.show()


@play.repeat_forever
async def fly_image():
    if status==1:
        if play.key_is_pressed("W", "w", "Ц", "ц", "up", "space"):
            bird.image = "bird2.png"
            await play.timer(0.5)
        else:
            bird.image = "bird1.png"

@play.repeat_forever
async def fly():
    if status==1:
        if play.key_is_pressed("W", "w", "Ц", "ц", "up", "space"):
            bird.physics.y_speed = 30
            await play.timer(0.1)

play.start_program()
