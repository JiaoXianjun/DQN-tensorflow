import curses
import time

def fill_disp_win(win, lane_data, score):
  #print lane_data
  #for i in range(len(lane_data)):
  #  win.addch(1,i,lane_data[i])
  
  win.addstr(0,32,'score: '+str(score))
  win.addstr(1,0,lane_data)
  win.addch(0,70,' ')

  win.refresh()

test_in_filename = 'game_input_fake.bin'
stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.nodelay(1)

begin_x = 0; begin_y = 4
height = 2; width = 73
win = curses.newwin(height, width, begin_y, begin_x)
len_lane = 72
lane_str = ''
for i in range(len_lane):
  lane_str = lane_str + ' '
win.addch(0,len_lane-1,'B')
#win = curses.newpad(height, width)

test_in_file = open(test_in_filename,'rb')
for i in range(2):
  tmp_str_in = test_in_file.read(len_lane)
  for j in range(len(tmp_str_in)):
    tmp_pad = tmp_str_in[j]
    
    c = stdscr.getch()
    if c == curses.KEY_DOWN:
      if tmp_pad=='A':
        tmp_pad = 'X'
      else:
        tmp_pad = 'B'
      curses.flushinp()
    
    tmp_str = lane_str[1:len_lane]+tmp_pad
      
    fill_disp_win(win, tmp_str, 34)
    lane_str = tmp_str
    time.sleep(0.1)
  
test_in_file.close()
curses.nocbreak(); stdscr.keypad(0); stdscr.nodelay(0); curses.echo(); curses.endwin()

