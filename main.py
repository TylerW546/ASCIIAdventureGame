#given a x and y value will output a charactor given seed, biomeseed, and biomes

def png(x, y):#procedural number generation
  seednum = ((x // grids) ^ (y // grids)) % len(biomeseed)
  vert = (y // grids) % biomeseed[seednum] * 20
  if biomeseed[seednum] ^ biomeseed[seednum % 15] == 0:
    horiz = (x // grids) % (biomeseed[seednum] ^ biomeseed[seednum % 1] + biomeseed[seednum]) * 3
  else:
    horiz = (x // grids) % (biomeseed[seednum] ^ biomeseed[seednum % 15]) * 3
  biome = (y // grids) + (x // grids)
  biome ^= (vert // (horiz + 1))
  biome %= len(biomes)
      
        
  try:
    history.index([x, y])        
  except:
    outnum = y + x
    seednum = (x ^ y) % len(seed)
    vert = y % seed[seednum] * 20
    if seed[seednum] ^ seed[seednum % 15] == 0:
      horiz = x % (seed[seednum] ^ seed[seednum % 1] + seed[seednum]) * 3
    else:
      horiz = x % (seed[seednum] ^ seed[seednum % 15]) * 3
    outnum ^= (vert // (horiz + 1))
    outnum %= len(biomes[biome])
    outnum = str(outnum)
    # map[j][k] = biomes[map[j][k]]
      

          #coverting numbers in to ther charactors
    outnum = biomes[biome][int(outnum)]
    
    if y % grids == 0:
      if x % grids == 0:
        outnum = "+"
      else:
        outnum = "-"
    else:
      if x % grids == 0:
        outnum = "|"
  
  else:
    outnum = biomes[biome][len(biomes[biome])]
  return(outnum)



#makes the start of what you see
def generatestart():
  for j in range(render):
    for k in range(render):
      if (ycord-j) % grids == 0:
        if (k+xcord) % grids == 0:
          map[j][k] = "+"
        else:
          map[j][k] = "-"
      else:
        if (k+xcord) % grids == 0:
          map[j][k] = "|"
        else:
          map[j][k] = png(k+xcord, ycord-j) 


#prints map and the screen
def renderer():
  for j in range(render):
    for k in range(render):
      if j == charposy and k == charposx:
        screen.addstr(j, k * 2, '{0:5}'.format(character), curses.color_pair(1))
        if direction == 1:
          screen.addstr(j, k * 2, '{0:5}'.format(character + "<"), curses.color_pair(1))
        elif direction == 2:
          screen.addstr(j + 1, k * 2, '{0:5}'.format("^"), curses.color_pair(1))
        elif direction == 3:
          screen.addstr(j, k * 2, '{0:5}'.format(">" + character), curses.color_pair(1))
      
      elif j == charposy + 1 and k == charposx and direction == 2:
        screen.addstr(j, k * 2, '{0:5}'.format("^"), curses.color_pair(1))

      elif map[j][k] == "+" or map[j][k] == "|" or map[j][k] == "-":
        screen.addstr(j, k * 2, '{0:5}'.format(map[j][k]), curses.color_pair(2))

      else:
        screen.addstr(j, k * 2, '{0:5}'.format(map[j][k]), curses.color_pair(3))

  


#0 = up, 1 = right, 2 = down, 3 = left
def move(movedirection):

  if movedirection == 0:
    for j in range(render - 1):
      for k in range(render):
        map[render-j-1][k] = map[render-j-2][k]#6y, 10x

    for j in range(render):
      map[0][j] = png(xcord+j, ycord)
  
  
  if movedirection == 1:
    for j in range(render):
      for k in range(render-1):
        map[j][k] = map[j][k+1]

    for k in range(render):
        map[k][render-1] = png(xcord+render-1, ycord-k)

   

  if movedirection == 2:
    for j in range(render):
      for k in range(render-1):
        map[k][j] = map[k+1][j]

    for j in range(render):#j=0
          map[render-1][j] = png(xcord+j, ycord-render+1)


  if movedirection == 3:
    for j in range(render):
      for k in range(render):
        map[j][render-k-1] = map[j][render-k-2]

    for k in range(render):
          map[k][0] = png(xcord, ycord-k)



def melee(dir):

  if dir == 0:
    screen.addstr("HELLO")
  if dir == 1:
    pass
  if dir == 2:
    pass
  if dir == 3:
    pass


# #persedual generation equation:
# #seed = remainder after deviding x + y cords by seed length.
# #to vertical cordinate remaider after dividing by seed.
# #horizontal cordinate remainder after dividing by seed xor the next seed in list.
# #xor the previos equations together.




# #equations for previus equation idea
# # make the seednum: ((xcord + k) ^ (ycord + j)) % len(seed)

# #current number seed xor next seed: seed[seednum] ^ seed[seednum % 15]

# #Seednum is the position in the seed that we use.





import curses
import time
import random
biomes = [
  ["\N{TOP PARENTHESIS}", "_", "_", "_", "_", "\N{TOP PARENTHESIS}"], 
  ["\N{LEFT DOUBLE WIGGLY FENCE}", "~", "~", "~", "~", "~", " ", " "],
  ["\N{DOUBLE LOGICAL AND}", "_", "_"]]
# \N{APL Functional Symbol Delta Stile}


# GET SEEDS ------------------------------------------------------

# seed = [11, 1, 3, 2, 5, 3, 6, 3, 6, 4, 9, 3, 4, 6, 2, 4]
# biomeseed = [3, 6, 4, 9, 3, 5, 1, 6, 8, 4, 3, 8, 3, 6, 3, 5]
# Character Seed(For Biome Decor)
seed = [random.randint(1, 13) for j in range(16)]

# Biome Seed(For Biome)
biomeseed = [random.randint(1, 13) for j in range(16)]





# SCREEN SETTINGS ------------------------------------------------

# Walking space that does not change surroundings. Needs to be odd
boundbox = 2

# Biome size
grids = 100

# Dimensions of screen. Needs to be odd.
render = 25

# 
speed = 1 #Reciprocal of value is speed. Ex: 5 = 1/5 speed.

#contains cordinates of every thing that happened and puts a blank space there
history = []

# DEFAULTS AND DEFINING VARIABLES ---------------------------------

# Map is the 2 Dimensional array that creates the screen.
map = [[0 for j in range(render)] for k in range(render)]

# Cords are the top left of the screen after factoring speed.

# xcord = 0
# ycord = 0
xcord = -(render // 2)
ycord = render // 2

# The X and Y coordinates (of top left) without speed involed.
xcordinput = 0
ycordinput = 0

# Character position on screen after factoring speed.
charposx = render // 2
charposy = render // 2

# Character position on screen witout speed involved.
charposxinput = render // 2 * speed
charposyinput = render // 2 * speed

# For character animation.
character = "O"
characterturns = 0

# Initiate screens.
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(1)
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_WHITE, -1)
curses.init_pair(2, curses.COLOR_WHITE, -1)
curses.init_pair(3, curses.COLOR_WHITE, -1)

direction = 1

generatestart()
renderer()

while True:

  
  characterturns += 1
  if character == "O" and characterturns > 60: # Number at end makes O stay longer.
    character = "o"
    characterturns = 0
  elif character == "o" and characterturns > 100: # Number at end makes o stay longer.
    character = "O"
    characterturns = 0

  valid = 0
  char = screen.getch()
  
  if char == curses.KEY_RIGHT:
    direction = 1
    if charposx == render // 2 + (boundbox // 2 - 1):
      xcord += 1
      move(direction)
      
    else:
      charposx += 1
      
    valid = 1
  elif char == curses.KEY_LEFT:
    direction = 3
    if charposx == render // 2 - (boundbox // 2 - 1):
      xcord -= 1
      move(direction)
      
    else:
      charposx -= 1
      
    valid = 1
  elif char == curses.KEY_UP:
    direction = 0
    if charposy == render // 2 - (boundbox // 2 - 1):
      ycord += 1
      move(direction)
      
    else:
      charposy -= 1
      
    valid = 1
  elif char == curses.KEY_DOWN:
    direction = 2      
    if charposy == render // 2 + (boundbox // 2 - 1):
      ycord -= 1
      move(direction)
      
    else:
      charposy += 1
      
    valid = 1
  elif char == curses.KEY_BACKSPACE:
    melee(direction)

  time.sleep(.001)
  renderer()


  if valid == 1:
    # xcord = xcordinput // speed
    # ycord = ycordinput // speed
    # charposx = charposxinput // speed
    # charposy = charposyinput // speed
    pass
  
  time.sleep(.05)
