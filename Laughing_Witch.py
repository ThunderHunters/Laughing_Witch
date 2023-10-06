# Laughing Witch Turtle

import turtle
import time
import math
import pygame

# Create a Pygame mixer for sound effects
pygame.mixer.init()

# Load the sound files (Change the path here to where you downloaded the files)

play_horse = pygame.mixer.Sound("xxx/Horse Low Grunt.wav")
play_guitar = pygame.mixer.Sound("xxx/Guitar Slide Down 02.wav")
play_frog = pygame.mixer.Sound("xxx/fff.wav")
play_laugh2= pygame.mixer.Sound("xxx/creepy laugh 2.wav")
play_laugh5= pygame.mixer.Sound("xxx/creepy laugh 5.wav")
play_laugh6= pygame.mixer.Sound("xxx/creepy laugh 6.wav")
play_bells = pygame.mixer.Sound("xxx/creepy bells.wav")
play_music = pygame.mixer.Sound("xxx/creepy music mid2.wav")

# Start the loop
while True:

    play_guitar.play()

    # Clear the screen
    turtle.resetscreen()
    turtle.hideturtle()

    # Set up the screen size
    screen_width = 600
    screen_height = 600
    turtle.setup(width=screen_width, height=screen_height)

    # Background color and colors for the drawing
    BACKGROUND_COLOR = "green"
    WITCH_HAT = "black"

    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("House of Witches")

    # Create a turtle
    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()
    my_turtle.speed(2)

    # Turn off animation updates temporarily
    screen.tracer(0)

    # Draw the moon
    my_turtle.penup()
    my_turtle.goto(-200, 150)
    my_turtle.pendown()
    my_turtle.color("green", "white")
    my_turtle.begin_fill()
    my_turtle.circle(50)
    my_turtle.fillcolor("white")
    my_turtle.penup()
    my_turtle.goto(-180, 150)
    my_turtle.pendown()
    my_turtle.end_fill()
    my_turtle.begin_fill()
    my_turtle.circle(45, -360)
    my_turtle.fillcolor("green")
    my_turtle.end_fill()
    screen.update()

    # Turn on animation updates
    screen.tracer(2)
    my_turtle.speed(2)

    # Move the turtle to the center
    my_turtle.penup()
    my_turtle.goto(0, 0)

    play_laugh6.play()

    # Wait for 2 seconds
    time.sleep(1)

    # Draw a witch's hat
    my_turtle.penup()
    my_turtle.goto(-75, 55)
    my_turtle.pendown()
    
    # Restore the original pen size
    my_turtle.pensize(5)

    # Go to position for hat
    my_turtle.penup()
    my_turtle.goto(-75, 55)
    my_turtle.pendown()

    # Draw a triangle for hat
    my_turtle.color(WITCH_HAT, WITCH_HAT)
    my_turtle.begin_fill()
    for _ in range(3):
        my_turtle.forward(100)
        my_turtle.left(120)
    my_turtle.end_fill()

    # Move to the center of the triangle
    my_turtle.penup()
    my_turtle.goto(25, 55)
    my_turtle.pendown()

    # Restore the original pen size
    my_turtle.pensize(8)

    # Draw a line for the hat brim
    line_length = 115
    my_turtle.forward(line_length / 2)
    my_turtle.backward(line_length)
    extended_line_length = 110
    my_turtle.backward(extended_line_length)
    
    # Restore the original pen size
    my_turtle.pensize(5)

    # Move pen to draw eyes
    my_turtle.penup()
    my_turtle.goto(-8, 41)
    my_turtle.pendown()

    # Draw eyes
    my_turtle.color("white")
    my_turtle.dot(15)
    my_turtle.penup()
    my_turtle.backward(30)
    my_turtle.pendown()
    my_turtle.dot(15)
    
    # Move to the center of the first white circle
    my_turtle.goto(-36, 37)
    my_turtle.pendown()

    # Draw red circles in the center of the white circles
    my_turtle.color("red")
    my_turtle.dot(6)
    my_turtle.penup()

    # Move to the center of the second white circle
    my_turtle.goto(-6, 37)
    my_turtle.pendown()

    # Draw another red circle
    my_turtle.dot(6)
    my_turtle.penup()

    # Hide the turtle
    my_turtle.hideturtle()
    screen.update()

    play_laugh2.play()

    # Wait for 2 seconds
    time.sleep(2)
   
    # Clear the screen
    turtle.clearscreen()

    # Set the background color to completely cover the existing content
    screen.bgcolor("orange")
    screen.update()

    # Set the drawing speed
    my_turtle.speed(6)

    # Wait for 1 seconds
    time.sleep(0)

    # Create a new turtle
    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()

    # Move to the center
    my_turtle.penup()
    my_turtle.goto(0, 40)
    my_turtle.pendown()

    # Set the drawing speed
    my_turtle.speed(10)

    play_music.play()

    # Draw two triangles at the center
    for _ in range(2):
        my_turtle.color("black", "black")
        my_turtle.begin_fill()
        for _ in range(3):
            my_turtle.forward(-170)
            my_turtle.left(-120)
        my_turtle.end_fill()

        # Move to the right for the second triangle
        my_turtle.penup()
        my_turtle.forward(200)
        my_turtle.pendown()

    play_laugh2.play() 

    # Move to the center
    my_turtle.penup()
    my_turtle.goto(0, -10)
    my_turtle.pendown()

    # Set the drawing speed
    my_turtle.speed(10)

    play_horse.play()

    # Draw a black circle filled in for the nose
    my_turtle.color("black", "black")
    my_turtle.begin_fill()
    my_turtle.circle(10)
    my_turtle.end_fill()
    screen.update()

    # Move to the center below the triangles for nose placement
    my_turtle.penup()
    my_turtle.goto(30, -10)
    my_turtle.pendown()

    play_bells.play()

    # Set the drawing speed
    my_turtle.speed(10)
    screen.update()

    # Draw a black circle filled in for the nose
    my_turtle.color("black", "black")
    my_turtle.begin_fill()
    my_turtle.circle(10)
    my_turtle.end_fill()
    screen.update()

    # Draw a mouth line with wiggle

    # Create a turtle
    my_turtle = turtle.Turtle()

    # Hide the turtle
    my_turtle.hideturtle()
    screen.update()

    # Set the initial position
    start_x, start_y = -180, -120
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.pendown()

    # Set the amplitude and frequency of the wave
    amplitude = 30
    frequency = 0.1

    my_turtle.pensize(8)

    # Function to draw a wiggly line
    def draw_wiggle_line(length, amplitude, frequency):
        for _ in range(int(length / 5)):
            x = my_turtle.xcor()
            y = amplitude * math.sin(frequency * x) + start_y
            my_turtle.goto(x + 5, y)

    # Draw the wiggly line
    draw_wiggle_line(400, amplitude, frequency)

    # Hide the turtle
    my_turtle.hideturtle()
    screen.update()

    # Turn on animation updates
    screen.tracer(2)

    # Wait for a few seconds before restarting
    time.sleep(1)

    play_frog.play()
    
    # Clear the screen
    turtle.clearscreen()
    screen.update()

# Keep the window open
turtle.mainloop()
