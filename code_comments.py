# 1  - import modules necessary for the game
import curses
import random

# 2  - initialize the curses library to create our screen
screen = curses.initscr()

# 3  - hide the mouse cursor
curses.curs_set(0)

# 4  - getmax screen height and width
screen_hight, screen_width = screen.getmaxyx()

# 5  - create a new window
window = curses.newwin(screen_hight, screen_width, 0, 0)

# 6  - allow window to receive input from the keyboard
window.keypad(1)

# 7  - set the delay for updating the screen
window.timeout(100)

# 8  - set the x,y coordinates of the initial position of snake's head
snake_x = screen_width // 4
snake_y = screen_hight // 2

# 9  - define the initial poisiton of the snake body
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]

]

# 10 - create the food in the middle of window
food = [screen_hight // 2, screen_width // 2]

# 11 - add the food by using PI character from curses module
window.addch(food[0], food[1], curses.ACS_PI)

# 12 - set initial movement direction to right
key = curses.KEY_RIGHT

# 13 - create game loops that loops forever until player loses or quits
while True:

    # 14 - get the next key that will be pressed by user
    next_key = window.getch()

# if user doesn't input anything, key remains same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key

# 16 - check if snake collided with walls or with itself
    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
# 17 - set the new position of the snake head on the direction
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
# 18 - insert the new head to the first position of the snake

    snake.insert(0, new_head)
# 19 - check if snake ate the food
    if snake[0] == food:
        food = None  # remove food if snake ate it
# 20 - while food is removed, generate new food in a random place on screen
        while food is None:
            new_food = [
                random.randint(1, screen_hight-1),
                random.randint(1, screen_width-1)
            ]

# 21 - set the food to new food if new food generated is not in snake body and add it to screen
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
# 22 - otherwise emove the last segment of snake body
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
# 23 - update the position of the snake on the screen
