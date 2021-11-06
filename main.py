from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball=Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score=Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()
    
    #detectar colisão com a parede
    if ball.ycor()>290 or ball.ycor()< (-290):
        ball.bounce_y()
        
    #detectar colisão com o lado direiro
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()>-320:
        ball.bounce_x()
        
    #detectar qndo perde a bola do lado direito
    if ball.xcor()>380:
        ball.reset_position() 
        score.l_point()
        
    #detectar qndo perde a bola do lado esquerdo
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()    
    
    

screen.exitonclick()