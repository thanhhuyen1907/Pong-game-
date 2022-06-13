import pygame
pygame.init()

#icon = pygame.image.load('world.png')
#pygame.display.set_icon(icon)
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font_2 = pygame.font.Font('freesansbold.ttf', 30)
score = font_2.render( 'SCORE: ', True, WHITE)
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 25
BALL_RADIUS = 10
P = 0
#soundObj = pygame.mixer.Sound('pong_sound.wav')

class Paddle:
    COLOR = WHITE
    VEL = 10
    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
    def move(self, left=True):
        if left:
            self.x -= self.VEL
        else:
            self.x += self.VEL
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    MAX_VEL = 7
    COLOR = WHITE
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 4
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

def draw(win, paddle, ball):
    win.fill(BLACK)
    paddle.draw(win)
    ball.draw(win)
    WIN.blit(score, (270,220))

def handle_collision(ball, paddle):
    global P
    point = font_2.render( str(P), True, WHITE)
    WIN.blit(point, (400,220))
    if ball.y == HEIGHT-30 :
        if ball.x >= paddle.x and ball.x <= paddle.x + paddle.width:
            ball.y_vel *= -1
            P += 1
            #soundObj.play()
        else:
            P = 0
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <=0:
        ball.y_vel *= -1
    if ball.x + ball.radius >= WIDTH:
        ball.x_vel *= -1
    elif ball.x - ball.radius <= 0:
        ball.x_vel *= -1
    
def handle_paddle_movement(keys,paddle):
    if keys[pygame.K_LEFT] and paddle.x + paddle.VEL >= 0:
        paddle.move(left=True)
    if keys[pygame.K_RIGHT] and paddle.x + paddle.VEL + paddle.width <= WIDTH:
        paddle.move(left=False)

if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    paddle = Paddle(WIDTH//2 - PADDLE_WIDTH//2,HEIGHT-30, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(50 , 50 , BALL_RADIUS)
    while run:
        clock.tick(FPS)
        draw(WIN, paddle, ball)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, paddle)
        ball.move()
        handle_collision(ball, paddle)
        pygame.display.update()