# Wordle clone in Terminal


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

    curses.init_pair(
        1, curses.COLOR_YELLOW, curses.COLOR_BLACK
    )  # letter is in word but not in the correct spot
    curses.init_pair(
        2, curses.COLOR_GREEN, curses.COLOR_BLACK
    )  # letter is in word and in correct spot


def gameScreen(stdscr):

    stdscr.clear()

    correctWord = random.choice(open("words.txt").read().splitlines())

    congrats = ["YOU WIN\n", f"THE WORD WAS {correctWord}\n"]
    fail = ["OUT OF LIVES\n", f"THE WORD WAS {correctWord}\n"]

    guessNum = 0

    while True:
        guessing = True

        while guessing:
            curses.echo()
            userGuess = stdscr.getstr(5)
            userGuess = userGuess.decode(
                "utf-8"
            ).lower()  # why the fuck does getstr return a byte

            stdscr.refresh

            checking = True
            guessing = False

        while checking:
            for i in range(5):
                if userGuess[i] == correctWord[i]:
                    stdscr.addch(guessNum, i, userGuess[i], curses.color_pair(2))

                elif userGuess[i] in correctWord:
                    stdscr.addch(guessNum, i, userGuess[i], curses.color_pair(1))
                else:
                    stdscr.addch(guessNum, i, userGuess[i])

            guessNum += 1
            stdscr.addstr("\n\n")
            checking = False

            if userGuess == correctWord:
                stdscr.addstr(
                    (curses.LINES // 2),
                    (curses.COLS - len(congrats[0])) // 2,
                    congrats[0],
                )
                stdscr.addstr(
                    (curses.LINES // 2) + 1,
                    (curses.COLS - len(congrats[1])) // 2,
                    congrats[1],
                )
                break

            if guessNum == 6:
                stdscr.addstr(
                    (curses.LINES // 2), (curses.COLS - len(fail[0])) // 2, fail[0]
                )
                stdscr.addstr(
                    (curses.LINES // 2) + 1, (curses.COLS - len(fail[1])) // 2, fail[1]
                )
                break


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
