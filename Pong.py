# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)

# Paddle A
paddle_a = pygame.Rect(50, HEIGHT//2 - 50, 10, 100)

# Paddle B
paddle_b = pygame.Rect(WIDTH - 60, HEIGHT//2 - 50, 10, 100)

# Bóng
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

# Điểm số
score_a = 0
score_b = 0
font = pygame.font.Font(None, 36)

# Hàm vẽ các đối tượng
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, PINK, ball)
    
    # Vẽ đường giữa đứt khúc với khoảng trống lớn hơn
    for y in range(0, HEIGHT, 100):
        pygame.draw.line(screen, WHITE, (WIDTH//2, y+10), (WIDTH//2, y + 30), 5)
    
    score_display = font.render(f"{score_a} : {score_b}", True, WHITE)
    screen.blit(score_display, (WIDTH//2 - 30, 10))

# Vòng lặp chính
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Di chuyển paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= 7
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += 7
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= 7
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += 7
    
    # Di chuyển bóng
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Kiểm tra va chạm với biên trên và dưới
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    # Kiểm tra va chạm với paddle và vạch giữa
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1
    elif ball.centerx == WIDTH // 2:
        if ball.centery % 100 >= 50:  # Nếu bóng chạm vào phần vạch
            ball_speed_x *= -1
        # Nếu bóng ở khoảng trống, cho nó đi qua
    
    # Kiểm tra điểm số
    if ball.left <= 0:
        score_b += 1
        ball.center = (WIDTH//2, HEIGHT//2)
    elif ball.right >= WIDTH:
        score_a += 1
        ball.center = (WIDTH//2, HEIGHT//2)
    
    # Vẽ các đối tượng
    draw_objects()
    
    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)
