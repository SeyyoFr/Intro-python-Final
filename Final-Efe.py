from tkinter import Tk, Canvas, PhotoImage
import random

class SnakeGame:
    def __init__(self):
        self.window = Tk()
        self.window.title("SNAKE GAME")

        self.width = 600
        self.height = 400
        self.top_area = 50

        self.canvas = Canvas(self.window, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.snake_size = 25
        self.direction = "Right"
        self.score = 0
        self.lives = 3
        self.game_over = False

        self.apple_image = PhotoImage(file="apple.png")
        self.apple_image = self.apple_image.subsample(20, 20)

        self.heart_image = PhotoImage(file="heart_red.png")
        self.heart_image = self.heart_image.subsample(45, 45)

        self.black_heart_image = PhotoImage(file="black_heart.png")
        self.black_heart_image = self.black_heart_image.subsample(55, 55)

        self.reset_snake()
        self.create_food()

        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)
        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>", self.move_down)

        self.draw_game()
        self.animate()

        self.window.mainloop()

    def reset_snake(self):
        self.snake = [
            [100, 100],
            [75, 100],
            [50, 100],
            [25, 100]
        ]
        self.direction = "Right"

    def create_food(self):
        food_ok = False

        while food_ok == False:
            x = random.randrange(0, self.width, self.snake_size)
            y = random.randrange(self.top_area, self.height, self.snake_size)

            self.food = [x, y]
            food_ok = True

            for part in self.snake:
                if part == self.food:
                    food_ok = False

    def draw_head(self, x, y):
        self.canvas.create_rectangle(
            x, y,
            x + self.snake_size,
            y + self.snake_size,
            fill="darkgreen",
            outline="black"
        )

        if self.direction == "Right":
            self.canvas.create_oval(x + 15, y + 6, x + 19, y + 10, fill="black")
            self.canvas.create_oval(x + 15, y + 15, x + 19, y + 19, fill="black")

            self.canvas.create_line(
                x + self.snake_size, y + 12,
                x + self.snake_size + 7, y + 12,
                fill="red", width=2
            )
            self.canvas.create_line(
                x + self.snake_size + 7, y + 12,
                x + self.snake_size + 10, y + 10,
                fill="red", width=2
            )
            self.canvas.create_line(
                x + self.snake_size + 7, y + 12,
                x + self.snake_size + 10, y + 14,
                fill="red", width=2
            )

        elif self.direction == "Left":
            self.canvas.create_oval(x + 6, y + 6, x + 10, y + 10, fill="black")
            self.canvas.create_oval(x + 6, y + 15, x + 10, y + 19, fill="black")

            self.canvas.create_line(
                x, y + 12,
                x - 7, y + 12,
                fill="red", width=2
            )
            self.canvas.create_line(
                x - 7, y + 12,
                x - 10, y + 10,
                fill="red", width=2
            )
            self.canvas.create_line(
                x - 7, y + 12,
                x - 10, y + 14,
                fill="red", width=2
            )

        elif self.direction == "Up":
            self.canvas.create_oval(x + 6, y + 6, x + 10, y + 10, fill="black")
            self.canvas.create_oval(x + 15, y + 6, x + 19, y + 10, fill="black")

            self.canvas.create_line(
                x + 12, y,
                x + 12, y - 7,
                fill="red", width=2
            )
            self.canvas.create_line(
                x + 12, y - 7,
                x + 10, y - 10,
                fill="red", width=2
            )
            self.canvas.create_line(
                x + 12, y - 7,
                x + 14, y - 10,
                fill="red", width=2
            )

        elif self.direction == "Down":
            self.canvas.create_oval(x + 6, y + 15, x + 10, y + 19, fill="black")
            self.canvas.create_oval(x + 15, y + 15, x + 19, y + 19, fill="black")

            self.canvas.create_line(
                x + 12, y + self.snake_size,
                x + 12, y + self.snake_size + 7,
                fill="red", width=2
            )
            self.canvas.create_line(
                x + 12, y + self.snake_size + 7,
                x + 10, y + self.snake_size + 10,
                fill="red", width=2
            )
            self.canvas.create_line(
                x + 12, y + self.snake_size + 7,
                x + 14, y + self.snake_size + 10,
                fill="red", width=2
            )

    def draw_game(self):
        self.canvas.delete("all")

        self.canvas.create_text(
            60, 25,
            text="Score: " + str(self.score),
            fill="black",
            font=("Arial", 13)
        )

        self.canvas.create_text(
            self.width - 130, 25,
            text="Lives:",
            fill="black",
            font=("Arial", 13)
        )

        for i in range(3):
            if i < self.lives:
                image_to_use = self.heart_image
            else:
                image_to_use = self.black_heart_image

            self.canvas.create_image(
                self.width - 85 + (i * 28),
                25,
                image=image_to_use
            )

        self.canvas.create_line(
            0, self.top_area,
            self.width, self.top_area,
            fill="lightgray"
        )

        for i in range(len(self.snake)):
            part = self.snake[i]
            x = part[0]
            y = part[1]

            if i == 0:
                self.draw_head(x, y)
            else:
                self.canvas.create_rectangle(
                    x, y,
                    x + self.snake_size,
                    y + self.snake_size,
                    fill="green",
                    outline="black"
                )

        food_x = self.food[0]
        food_y = self.food[1]

        self.canvas.create_image(
            food_x + self.snake_size / 2,
            food_y + self.snake_size / 2,
            image=self.apple_image
        )

        if self.game_over == True:
            self.canvas.create_text(
                self.width / 2,
                self.height / 2,
                text="GAME OVER",
                fill="red",
                font=("Arial", 30, "bold")
            )

    def move_left(self, event):
        if self.direction != "Right":
            self.direction = "Left"

    def move_right(self, event):
        if self.direction != "Left":
            self.direction = "Right"

    def move_up(self, event):
        if self.direction != "Down":
            self.direction = "Up"

    def move_down(self, event):
        if self.direction != "Up":
            self.direction = "Down"

    def move_snake(self):
        head = self.snake[0]
        new_head = [head[0], head[1]]

        if self.direction == "Right":
            new_head[0] = new_head[0] + self.snake_size
        elif self.direction == "Left":
            new_head[0] = new_head[0] - self.snake_size
        elif self.direction == "Up":
            new_head[1] = new_head[1] - self.snake_size
        elif self.direction == "Down":
            new_head[1] = new_head[1] + self.snake_size

        if new_head[0] < 0 or new_head[0] >= self.width or new_head[1] < self.top_area or new_head[1] >= self.height:
            self.lives = self.lives - 1

            if self.lives == 0:
                self.game_over = True
            else:
                self.reset_snake()
                self.create_food()

            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score = self.score + 1
            self.create_food()
        else:
            self.snake.pop()

    def animate(self):
        if self.game_over == False:
            self.move_snake()
            self.draw_game()

            if self.game_over == False:
                self.window.after(150, self.animate)

game = SnakeGame()