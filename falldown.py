#Vaibhav Choudhary gau7jk

import uvage
import random

camera = uvage.Camera(800, 600)
game_true = False
game_false = True
score = 0
y_coordinate = 0

# where the camera begins
camera.x = 400
camera.y = 350

# components of the game
player = uvage.from_color(600, 500, "cyan", 15, 15)
floor = []

def tick():
    global score
    global game_true
    global game_false
    global floor
    global player
    global y_coordinate
    global stop

    stop = uvage.from_color(400, camera.y - 300, "cyan", 800, 40)

    # The player can start the game by clicking on the mouse
    if camera.mouseclick:
        game_true = True
        game_false = False

    def visual():
        """
        This function creates the background for the game.
        :return: This function does not return anything.
        """
        global stop
        global floor

        camera.clear("black")
        camera.draw(stop)

        if game_true == True:
            for each in floor:
                camera.draw(each)

        player.draw(camera)

    def instructions():
        """
        This function explains what happens once the player begins the game by clicking the down arrow key.
        The function shows how each of the floors are created using a random number generator.
        :return: none
        """
        global game_true
        global y_coordinate
        global floor
        global score
        if game_true == True:
            if game_false == False:
                player.move_speed()
                camera.move(0, 1)

        if game_true == True:
            if game_false == False and score % 60 == 0:
                left_floor = random.randint(0, 299)
                left_width = 2 * left_floor
                right_floor = (800 + left_width + 75) * (1/2)
                right_width = 800 - (left_width + 75)

                floor.append(uvage.from_color(left_floor, camera.y + 300, "red", left_width, 15))
                floor.append(uvage.from_color(right_floor, camera.y + 300, "red", right_width, 15))
                y_coordinate = y_coordinate + 100
            if game_false == True:
                y_coordinate = y_coordinate + 0

    def x_move():
        """
        This function explains what each key does to move the player along the x-plane.
        :return: This function does not return anything.
        """
        if uvage.is_pressing("right arrow"):
            if player.x != 800:
                    player.x += 10
        if uvage.is_pressing("left arrow"):
            if player.x != 0:
                    player.x -= 10

    def y_move():
        """
        This function explains how the camera moves with relation to the player's position.
        :return: This function does not return anything.
        """
        if player.y > camera.y + 250:
            player.y = camera.y + 250
        elif player.y == camera.y + 250:
            player.y = camera.y + 250
        elif player.y < camera.y + 250:
            player.y = player.y



    def touch():
        """
        This function explains what happens when the player interacts with the floors.
        :return: This function does not return anything.
        """
        global floor
        for each in floor:
            if player.touches(each):
                player.yspeed = 0
        else:
            player.yspeed = player.yspeed + 0.25

        for wall in floor:
            if player.touches(wall):
                player.yspeed = 0

    visual()

    def displays():
        """
        This function explains what is displayed on the screen during the game.
        :return: This function does not return anything.
        """

        global game_true
        global game_false
        global score
        global stop

        if game_true == True:
            if game_false == False:
                camera.draw(uvage.from_text(700, 500 + score, str(score), 40, "magenta", bold = True))

        if game_true == False:
            if game_false == True:
                camera.draw(uvage.from_text(400, 250, "Press the mouse to start!", 60, "white", bold = True))


        if player.top_touches(stop):
            camera.move(0,0)
            camera.draw(uvage.from_text(camera.x, camera.y, "Game Over!", 50, "red"))
            game_true = False
            game_false = True



    displays()
    instructions()
    x_move()
    y_move()
    touch()

    camera.display()
    score += 1



ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)