from turtle import left, right
import pygame
pygame.init()

width = 700 #500
height = 500 #300
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

FPS = 60

paddleWidth = width/35
paddleHeight = height/5

class Paddle:
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = 'white'
    self.velocity = 4

  def draw(self, win):
    pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

  def move(self, up=True):
    if up:
      self.y -= self.velocity
    else:
      self.y += self.velocity

class Ball:
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius = radius
    self.maxVelocity = 5
    self.xVelocity = self.maxVelocity
    self.yVelocity = 0
    self.color = 'white'
  
  def draw(self, win):
    pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
  
  def move(self):
    self.x += self.xVelocity
    self.y += self.yVelocity

def draw(win, paddles, ball):
  win.fill('black') #(31, 31, 31)

  for paddle in paddles:
    paddle.draw(win)

  for i in range(10, height, height//20):
    if i % 2 == 1:
      continue
    pygame.draw.rect(win, ('white'), (width//2 - 5, i, 10, height//20))
  
  ball.draw(win)
  pygame.display.update()

def handlePaddleMovement(keys, leftPaddle, rightPaddle):
  if keys[pygame.K_w] and leftPaddle.y - leftPaddle.velocity >= 0:
    leftPaddle.move(up=True)
  if keys[pygame.K_s] and leftPaddle.y + leftPaddle.velocity + leftPaddle.height <= height:
    leftPaddle.move(up=False)
  
  if keys[pygame.K_UP] and rightPaddle.y - rightPaddle.velocity >= 0:
    rightPaddle.move(up=True)
  if keys[pygame.K_DOWN] and rightPaddle.y + rightPaddle.velocity + rightPaddle.height <= height:
    rightPaddle.move(up=False)  

def main():
  run = True
  clock = pygame.time.Clock()

  leftPaddle = Paddle(10, height//2 - paddleHeight//2, paddleWidth, paddleHeight)
  rightPaddle = Paddle(width - 10 - paddleWidth, height//2 - paddleHeight//2, paddleWidth, paddleHeight)
  ball = Ball(width//2, height//2, 7)

  while run:
    clock.tick(FPS)
    draw(win, [leftPaddle, rightPaddle], ball)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
    
    keys = pygame.key.get_pressed()
    handlePaddleMovement(keys, leftPaddle, rightPaddle)

    ball.move()
    
  pygame.quit()

if __name__ == '__main__':
  main()