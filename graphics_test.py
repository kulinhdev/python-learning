import pygame
import random

# Thiết lập màn hình
WIDTH = 640
HEIGHT = 480
FPS = 15

# Thiết lập màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Khởi tạo Pygame và cửa sổ trò chơi
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rắn săn mồi")
clock = pygame.time.Clock()


# Lớp con rắn
class Snake:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.dx = 10
        self.dy = 0
        self.length = 1
        self.body = [(self.x, self.y)]

    # Di chuyển rắn
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > self.length:
            self.body.pop()

    # Vẽ rắn lên màn hình
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, 10, 10))

    # Kiểm tra va chạm của rắn với tường hoặc cơ thể
    def collide(self):
        if self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT:
            return True
        for i in range(1, len(self.body)):
            if self.x == self.body[i][0] and self.y == self.body[i][1]:
                return True
        return False

    # Kiểm tra va chạm của rắn với mồi
    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 1
            food.spawn()
        if self.length > 50:
            self.length = 50

# Lớp mồi
class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.spawn()

    # Vẽ mồi lên màn hình
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 10, 10))

    # Đặt lại vị trí của mồi
    def spawn(self):
        self.x = random.randrange(0, WIDTH - 10, 10)
        self.y = random.randrange(0, HEIGHT - 10, 10)


# Khởi tạo đối tượng rắn và mồi
snake = Snake()
food = Food()

# Vòng lặp chính của trò chơi
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = 10
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -10
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 10

    # Di chuyển rắn
    snake.move()

    # Kiểm tra va chạm của rắn
    if snake.collide():
        running = False

    # Kiểm tra nếu rắn ăn được mồi
    snake.eat(food)

    # Vẽ các đối tượng lên màn hình
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()

    # Điều chỉnh tốc độ của trò chơi
    clock.tick(FPS)

# Kết thúc chương trình
pygame.quit()
