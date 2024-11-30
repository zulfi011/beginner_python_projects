import curses
import time


def start_screen(stdscr):
  stdscr.clear()
  stdscr.addstr("Welcome to the Speed Typing Test!")
  stdscr.addstr("\nPress any key to begin!")
  stdscr.refresh()
  stdscr.getkey()


def display_text(stdscr, message, typ_ch, errors):
  stdscr.addstr(message, curses.color_pair(1))
  for idx, char in enumerate(message):
    key = stdscr.getkey()
    typ_ch += 1
    color = curses.color_pair(2)
    if key != char:
      errors += 1
      color = curses.color_pair(3)
    stdscr.addstr(0, idx, char, color)
  return typ_ch, errors


def all_lines():
  try:
    with open('text.txt', 'r') as r:
      return r.readlines()
  except:
    print('error while excecuting file')


def wpm_test(stdscr):
  messages = all_lines()
  typ_ch = 0
  errors = 0
  for message in messages:
    stdscr.clear()
    typ_speed = display_text(stdscr, message, typ_ch, errors)
    stdscr.refresh()
    typ_ch = typ_speed[0]
    errors = typ_speed[1]
  return typ_ch, errors


def main(stdscr):
  curses.start_color()
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

  start_screen(stdscr)
  while True:
    start_time = time.time()
    total_typ_ch, errors = wpm_test(stdscr)
    time_elapsed = max(time.time() - start_time, 1)
    wpm = round(((total_typ_ch / 5) - errors) / (time_elapsed / 60))
    stdscr.clear()
    stdscr.addstr(0, 0, 'You finished the text...')
    stdscr.addstr(1, 0, 'Your typing speed is : ')
    stdscr.addstr(f"{0 if wpm<0 else wpm}", curses.color_pair(2))
    stdscr.addstr(" wpm")
    stdscr.addstr(2, 0, "press any key to continue and q to quit...")
    stdscr.refresh()
    key = stdscr.getkey()
    if key == 'q':
      break
  curses.endwin()


curses.wrapper(main)
