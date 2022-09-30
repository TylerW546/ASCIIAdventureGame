# Renders screen in multiple portions
import curses

INVENTORYSLOTS = {0 : "Wood", 1 : "Metal"}

# Toggles screen and screen settings
screen = curses.initscr()
# curses.noecho()
curses.cbreak()
# screen.keypad(True)
#screen.nodelay(1)


# Renders map and cords ----------------------------------------------
def display(map, render, character, x, y, xchar, ychar):
  for j in range(render):
    for k in range(render):
      if map[j][k] == "horizswordleft":
        screen.addstr(j, k * 2, '{0:5}'.format("——"), curses.color_pair(1))
      elif map[j][k] == "horizswordright":
        screen.addstr(j, k * 2, '{0:5}'.format("—"), curses.color_pair(1))
      elif map[j][k] == "vertsword":
        screen.addstr(j, k * 2, '{0:5}'.format("|"), curses.color_pair(1))
      elif j == ychar and k == xchar:
        screen.addstr(j, k * 2, '{0:5}'.format(character), curses.color_pair(1))
      elif map[j][k] == "+" or map[j][k] == "|" or map[j][k] == "-":
        screen.addstr(j, k * 2, '{0:5}'.format(map[j][k]), curses.color_pair(2))
      elif map[j][k] == 1:
        screen.addstr(j, k*2, '{0:5}'.format("\N{TOP PARENTHESIS}"), curses.color_pair(4))
      # BIOME COLORS
      elif map[j][k] == "2":
        screen.addstr(j, k * 2, '{0:5}'.format("-"))
      # BOXES
      elif map[j][k] == "\N{BALLOT BOX WITH X}":
        screen.addstr(j, k * 2, '{0:5}'.format("\N{BALLOT BOX WITH X}"))
      # ALL OTHERS
      else:
        screen.addstr(j, k * 2, '{0:5}'.format(map[j][k]))

  screen.addstr(render, render, '{0:5}'.format(str(x + xchar) + " " + str(y - ychar) + "       "))





# renders health -----------------------------------------------------
def health(MAXHEALTH, health, extrahealth, render):
  screen.addstr(render + 2, 0, '{0:5}'.format("Health:"))

  if extrahealth == 0:
    screen.addstr(render + 3, 0 + MAXHEALTH, '{0:5}'.format(" "), curses.color_pair(2))
  for k in range(health):
    screen.addstr(render + 3, k, '{0:5}'.format("∎"), curses.color_pair(3))
  for k in range(MAXHEALTH - health):
    screen.addstr(render + 3, k + health, '{0:5}'.format("∎"), curses.color_pair(6))
  for k in range(extrahealth):
    screen.addstr(render + 3, k + MAXHEALTH, '{0:5}'.format("∎"), curses.color_pair(5))



# inventory rendering
def inventory(render, inventory, pos):
  for i in range(len(inventory)):
    if i == pos:
      screen.addstr(render + 7 + i, 0, '{0:5}'.format(" " + INVENTORYSLOTS[i] + ": " + str(inventory[i]) + "  "), curses.A_STANDOUT)
    else:
      screen.addstr(render + 7 + i, 0, '{0:5}'.format(" " +  INVENTORYSLOTS[i] + ": " + str(inventory[i]) + "  "))