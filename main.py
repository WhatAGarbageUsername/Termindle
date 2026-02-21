# Wordle clone in Terminal
# Tutorial Link: https://docs.python.org/3/howto/curses.html


import curses
from curses import wrapper
import random


def startScreen(stdscr):
    stdscr.clear()

    text = ["TERMINDLE", "PRESS ANY KEY TO START"]

    stdscr.addstr((curses.LINES // 2), (curses.COLS - len(text[0])) // 2, text[0])
    stdscr.addstr((curses.LINES // 2) + 1, (curses.COLS - len(text[1])) // 2, text[1])

    stdscr.refresh()


def initColors():

    curses.start_color()

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)


def gameScreen(stdscr):

    stdscr.clear()

    correctWord = random.choice(open("words.txt").read().splitlines())
    stdscr.addstr(f"TEST: The word is {correctWord}")
    pass


def main(stdscr):

    stdscr.clear()

    # initalize the color pallette and show the start screen

    startScreen(stdscr)
    initColors()
    stdscr.refresh()
    stdscr.getkey()

    gameScreen(stdscr)
    stdscr.refresh()
    stdscr.getkey()


wrapper(main)
