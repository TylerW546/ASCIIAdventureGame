OBSTACLES = ["\N{BALLOT BOX WITH X}"]


import movement
import rendering
import pngbiomes
import curses
import time
import random 
import interactions
import keyinputs



def test_collect(char, biomes, biome):
  if char == biomes[current_biome][len(biomes[current_biome]) - 1]:
    return(True)
  return(False)
  



# Biomes add the empty space character on the left and the inportant charactors on the right, 1 = recource hill
biomes = [  
  ["\N{TOP PARENTHESIS}", "\N{TOP PARENTHESIS}", "__", "__", "__", "__", "__", "__", "__", "__", "\N{TOP PARENTHESIS}", "\N{TOP PARENTHESIS}", 1], 
  [" ", " ", " ", " ", "~", "~", "~", "\N{LEFT DOUBLE WIGGLY FENCE}"],
  [" ", " ", "\N{APL FUNCTIONAL SYMBOL DELTA STILE}"],
  [" ", "~", "2", "*"]]
# GET SEEDS ----------------------------------------------------------
# Character Seed(For Biome Decor)
seed = [random.randint(1, 13) for j in range(16)]
# Biome Seed(For Biome)
biomeseed = [random.randint(1, 13) for j in range(16)]
# SCREEN SETTINGS ----------------------------------------------------
# Walking space that does not change surroundings. Needs to be odd.
boundbox = 9
# Biome size.
grids = 5
# Dimensions of screen. Needs to be odd.
render = 17
# WORLD DATA ----------------------------------------------------------
# cleared land
history = {}
objects = {}
# inventory - wood - metal
inventorypos = 0
inventory = [0, 0]
# USER PLACED BLOCKS INFO --------------------------------------------
# user placed block item count
block_value = {"\N{BALLOT BOX WITH X}" : (1, 0)}
# DEFAULTS AND DEFINING VARIABLES ------------------------------------
# Map is the 2 Dimensional array that creates the screen.
map = [[0 for j in range(render)] for k in range(render)]
xcord = render // -2 + random.randint(-50, 50)
ycord = render // 2 + random.randint(-50, 50)
# Character position on screen after factoring speed.
charposx = render // 2
charposy = render // 2
# For character animation.
character = "O"
charframe = 0
#Charactersword
swordx = charposx
swordy  = charposy + 1
sword = "|"
swordcount = 0
# Initiate screens.
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(1)
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, 1, -1)
curses.init_pair(2, curses.COLOR_BLUE, -1)
curses.init_pair(3, curses.COLOR_RED, -1)
curses.init_pair(4, curses.COLOR_BLACK, -1)
curses.init_pair(5, curses.COLOR_YELLOW, -1)
curses.init_pair(6, curses.COLOR_WHITE, -1)


# Character looking direction. Up, Right, Down, Left = 0, 1, 2, 3
direction = 1
#HEALTH
MAXHEALTH = 1
health = 10
extrahealth = 12
damage = 0

rounds = 0

current_biome = 0

map = movement.map_creation(xcord, ycord, render, grids, history, objects, map)
rendering.display(map, render, character, xcord, ycord, charposx, charposy)
rendering.health(MAXHEALTH, health, extrahealth, render)

# GAME LOOP ----------------------------------------------------------
while health > 0:
  damage = 0

  if charframe > 60 and character == "O":
    character = "o"
    charframe = 0
  elif charframe > 100 and character == "o":
    character = "O"
    charframe = 0
  charframe += 1
  



  char = screen.getch()
  try:
    if char != curses.KEY_BACKSPACE and char != curses.KEY_UP and char != curses.KEY_DOWN:
      char = chr(char).lower()
  except:
    char = ""

  if char == "d":
      direction = 1
      if not (map[charposy][charposx+1]) in OBSTACLES:
        if charposx >= render // 2 + (boundbox // 2 - 1):
          xcord += 1
          map = movement.moveRi(render, map, xcord, ycord, grids, history, objects)
        else:
          charposx += 1
  elif char == "a":
      direction = 3
      if not (map[charposy][charposx-1]) in OBSTACLES:
        if charposx <= render // 2 - (boundbox // 2 - 1):
          xcord -= 1
          map = movement.moveLe(render, map, xcord, ycord, grids, history, objects)
        else:
          charposx -= 1
  elif char == "w":
      direction = 0
      if not (map[charposy-1][charposx]) in OBSTACLES:
        if charposy <= render // 2 - (boundbox // 2 - 1):
          ycord += 1
          map = movement.moveUp(render, map, xcord, ycord, grids, history, objects)
        else:
          charposy -= 1
  elif char == "s":
      direction = 2      
      if not (map[charposy+1][charposx]) in OBSTACLES:
        if charposy >= render // 2 + (boundbox // 2 - 1):
          ycord -= 1
          map = movement.moveDo(render, map, xcord, ycord, grids, history, objects )
        else:
          charposy += 1
  elif char == curses.KEY_BACKSPACE:
    current_biome = pngbiomes.biome_finder(charposx+xcord, ycord-charposy, grids)
    if test_collect(map[charposy][charposx], biomes, current_biome):
      map[charposy][charposx] = biomes[current_biome][0]
      history[(charposx+xcord, ycord-charposy)] = biomes[current_biome][0]
      if current_biome == 0:
        inventory[1] += random.randint(1, 2)
      elif current_biome == 1:
        damage += 1
      elif current_biome == 2:
        inventory[0] += random.randint(1, 2)
      elif current_biome == 3:
        inventory[0] += random.randrange(2)
      else:
        pass
        # UH OH
      rendering.inventory(render, inventory, inventorypos)
  elif char == "\\" or char == "|":
    swordcount = 0
    if direction == 0:
      target = (xcord+charposx, ycord-charposy+1)
    elif direction == 1:
      target = (xcord+charposx+1, ycord-charposy)
    elif direction == 2:
      target = (xcord+charposx, ycord-charposy-1)
    elif direction == 3:
      target = (xcord+charposx-1, ycord-charposy)
    if (target) in objects:
      rand = random.randrange(9)
      if rand > 0:
        inventory[block_value[objects[target]][1]] += block_value[objects[target]][0]
      rendering.inventory(render, inventory, inventorypos)
      del objects[target]
  
  elif char == "t": #testing, currently object placement:
    if inventory[0] > 0 and not (xcord+charposx, ycord-charposy) in objects:
      map[charposy][charposx] = "\N{BALLOT BOX WITH X}"
      objects[(xcord+charposx, ycord-charposy)] = "\N{BALLOT BOX WITH X}"
      inventory[0] -= 1
      rendering.inventory(render, inventory, inventorypos)
      if test_collect(map[charposy][charposx], biomes, current_biome):
        pass
  elif char == curses.KEY_UP:
    inventorypos += 1
    if inventorypos >= len(inventory):
      inventorypos = 0
    rendering.inventory(render, inventory, inventorypos)
  elif char == curses.KEY_DOWN:
    inventorypos -= 1
    if inventorypos < 0:
      inventorypos = len(inventory)-1
    rendering.inventory(render, inventory, inventorypos)

    
  
  
  if swordcount < 10:
    if direction == 0:
      swordy = charposy - 1
      swordx = charposx
      sword = "vertsword"
    elif direction == 1:
      swordy = charposy
      swordx = charposx + 1
      sword = "horizswordright"
      character = str(character + "—")
    elif direction == 2:
      swordy = charposy + 1
      swordx = charposx
      sword = "vertsword"
    elif direction == 3:
      swordy = charposy
      swordx = charposx - 1
      sword = "horizswordleft"
    map[swordy][swordx] = sword

    swordcount += 1

    



  #HEARTS
  if damage < 1:
    damage = round(damage)
  while extrahealth > 0 and damage > 0:
    extrahealth -= 1
    damage -= 1
  while damage > 0:
    health -= 1
    damage -= 1
  rendering.health(MAXHEALTH, health, extrahealth, render)



  
  
  rendering.display(map, render, character, xcord, ycord, charposx, charposy)
  #Reset sword position
  map[swordy][swordx] = pngbiomes.findspace(swordx + xcord, ycord - swordy, grids, history, objects)
  character = character[0]
  screen.addstr(render + 10, 0, '{0:5}'.format(""))
  
  time.sleep(.01)


#screen.clear()
screen.addstr(render + 5, render // 2, '{0:5}'.format("You died"), curses.color_pair(6))