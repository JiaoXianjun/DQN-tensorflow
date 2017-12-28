import curses
import time

def fill_disp_win(win, lane_data):
  print lane_data
  for i in range(len(lane_data)):
    win.addch(1,i,lane_data[i])
  win.refresh()

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(1)

begin_x = 0; begin_y = 0
height = 2; width = 32
#win = curses.newwin(height, width, begin_y, begin_x)
win = curses.newpad(height, width)

lane_data = [80 for i in range(width)]
lane_data[10] = 81
lane_data[11] = 81
lane_data[12] = 81

#fill_disp_win(win, lane_data)
for i in range(len(lane_data)-2):
  print lane_data[i], i
  win.addch(1,i,lane_data[i])
win.refresh(0,0,0,0,1,31)

time.sleep(2)

curses.nocbreak(); stdscr.keypad(0); curses.echo(); curses.endwin()

