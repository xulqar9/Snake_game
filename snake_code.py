import curses
import random

class SnakeGame:
    def __init__(self):
        self.screen = curses.initscr()
        curses.curs_set(0)
        self.screen_height, self.screen_width = self.screen.getmaxyx()
        self.window = curses.newwin(self.screen_height, self.screen_width, 0, 0)
        self.window.keypad(1)
        self.window.timeout(100)

        self.snake_x = self.screen_width // 4
        self.snake_y = self.screen_height // 2
        self.snake = [
            [self.snake_y, self.snake_x],
            [self.snake_y, self.snake_x - 1],
            [self.snake_y, self.snake_x - 2]
        ]

        self.food = [self.screen_height // 2, self.screen_width // 2]
        self.window.addch(int(self.food[0]), int(self.food[1]), curses.ACS_PI)

        self.key = curses.KEY_RIGHT

    def create_food(self):
        while True:
            new_food = [
                random.randint(1, self.screen_height - 2),
                random.randint(1, self.screen_width - 2)
            ]
            if new_food not in self.snake:
                return new_food

    def game_over(self):
        self.window.addstr(self.screen_height//2, self.screen_width//2, 'Game Over!')
        self.window.refresh()
        curses.napms(2000)
        curses.endwin()
        quit()

    def play(self):
           while True: 
            self.window.addstr(0, self.screen_width - 35, 'Press X to Exit | Space to Pause')
            self.next_key = self.window.getch()
            if self.next_key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.key = self.next_key
            elif self.next_key == ord(' '):
                self.window.addstr(0, self.screen_width//2 - 5, ' PAUSED ')
                self.window.refresh()
                while True:  
                    key = self.window.getch()
                    if key == ord(' '):
                        break
            elif self.next_key == ord('x'):
                self.window.addstr(self.screen_height//2, self.screen_width//2, 'bye!')
                self.window.refresh()
                curses.napms(2000)
                curses.endwin()
                quit()

            if self.snake[0][0] in [0, self.screen_height] or \
                self.snake[0][1]  in [0, self.screen_width] or \
                self.snake[0] in self.snake[1:]:
                self.game_over()

            new_head = [self.snake[0][0], self.snake[0][1]]

            if self.key == curses.KEY_DOWN and self.key != curses.KEY_UP:
                new_head[0] += 1
            if self.key == curses.KEY_UP and self.key != curses.KEY_DOWN:
                new_head[0] -= 1
            if self.key == curses.KEY_RIGHT and self.key != curses.KEY_LEFT:
                new_head[1] += 1
            if self.key == curses.KEY_LEFT and self.key != curses.KEY_RIGHT:
                new_head[1] -= 1

            self.snake.insert(0, new_head)

            if self.snake[0] == self.food:
                self.food = self.create_food()
                self.window.addch(self.food[0], self.food[1], curses.ACS_PI)
            else:
                tail = self.snake.pop()
                self.window.addch(tail[0], tail[1], ' ')

            self.window.addch(self.snake[0][0], self.snake[0][1], curses.ACS_CKBOARD)
            self.window.border(0)
            self.window.addstr(0, 2, 'Score : ' + str(len(self.snake)-3))



if __name__ == "__main__":
    game = SnakeGame()
    game.play()
