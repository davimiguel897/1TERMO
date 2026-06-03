import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
DELAY = 6


class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo da Cobrinha")
        self.resizable(False, False)

        self.score = 0
        self.direction = "Right"
        self.next_direction = self.direction
        self.running = True

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="#111")
        self.canvas.pack()

        self.info_label = tk.Label(self, text="Score: 0", font=("Arial", 14))
        self.info_label.pack(fill=tk.X)

        self.bind_all("<Key>", self.on_key)

        self.reset_game()
        self.after(DELAY, self.game_loop)

    def reset_game(self):
        self.canvas.delete("all")
        self.score = 0
        self.direction = "Right"
        self.next_direction = self.direction
        self.running = True
        self.info_label.config(text=f"Score: {self.score}")

        start_x = WIDTH // 2
        start_y = HEIGHT // 2
        self.snake = []
        for i in range(3):
            x = start_x - i * CELL_SIZE
            y = start_y
            rect = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="#7CFC00", outline="#222")
            self.snake.append((x, y, rect))

        self.place_food()

    def place_food(self):
        cols = WIDTH // CELL_SIZE
        rows = HEIGHT // CELL_SIZE
        while True:
            cx = random.randrange(cols) * CELL_SIZE
            cy = random.randrange(rows) * CELL_SIZE
            if all(not (cx == sx and cy == sy) for sx, sy, _ in self.snake):
                break
        if hasattr(self, 'food'):
            try:
                self.canvas.delete(self.food)
            except Exception:
                pass
        self.food = self.canvas.create_oval(cx, cy, cx + CELL_SIZE, cy + CELL_SIZE, fill="#FF4500", outline="#222")
        self.food_pos = (cx, cy)

    def on_key(self, event):
        key = event.keysym
        opposites = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if key in ("Left", "Right", "Up", "Down"):
            if opposites.get(key) != self.direction:
                self.next_direction = key
        elif key == 'Return' and not self.running:
            self.reset_game()
        elif key == 'Escape':
            self.destroy()

    def game_loop(self):
        if not self.running:
            return
        self.direction = self.next_direction
        self.move_snake()
        if self.running:
            self.after(DELAY, self.game_loop)

    def move_snake(self):
        dx = dy = 0
        if self.direction == "Left":
            dx = -CELL_SIZE
        elif self.direction == "Right":
            dx = CELL_SIZE
        elif self.direction == "Up":
            dy = -CELL_SIZE
        elif self.direction == "Down":
            dy = CELL_SIZE

        head_x, head_y, head_id = self.snake[0]
        new_x = head_x + dx
        new_y = head_y + dy

        if new_x < 0 or new_y < 0 or new_x >= WIDTH or new_y >= HEIGHT:
            self.game_over()
            return

        if any(new_x == sx and new_y == sy for sx, sy, _ in self.snake):
            self.game_over()
            return

        new_rect = self.canvas.create_rectangle(new_x, new_y, new_x + CELL_SIZE, new_y + CELL_SIZE, fill="#7CFC00", outline="#222")
        self.snake.insert(0, (new_x, new_y, new_rect))

        if (new_x, new_y) == self.food_pos:
            self.score += 1
            self.info_label.config(text=f"Score: {self.score}")
            self.place_food()
        else:
            tail_x, tail_y, tail_id = self.snake.pop()
            try:
                self.canvas.delete(tail_id)
            except Exception:
                pass

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 - 10, text="GAME OVER", fill="#FF0000", font=("Arial", 28, "bold"))
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 20, text=f"Score: {self.score} — Press Enter to restart", fill="#FFF", font=("Arial", 14))


def main():
    app = SnakeGame()
    app.mainloop()


if __name__ == '__main__':
    main()
