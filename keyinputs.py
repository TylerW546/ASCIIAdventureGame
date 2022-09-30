def w():
  direction = 0
  if not (map[charposy-1][charposx]) in OBSTACLES:
    if charposy <= render // 2 - (boundbox // 2 - 1):
      ycord += 1
      map = movement.moveUp(render, map, xcord, ycord, grids, history, objects)
    else:
      charposy -= 1

def a():
  direction = 3
  if not (map[charposy][charposx-1]) in OBSTACLES:
    if charposx <= render // 2 - (boundbox // 2 - 1):
      xcord -= 1
      map = movement.moveLe(render, map, xcord, ycord, grids, history, objects)
    else:
      charposx -= 1

def s():
  direction = 2      
  if not (map[charposy+1][charposx]) in OBSTACLES:
    if charposy >= render // 2 + (boundbox // 2 - 1):
      ycord -= 1
      map = movement.moveDo(render, map, xcord, ycord, grids, history, objects )
    else:
      charposy += 1

def d():
  direction = 1
  if not (map[charposy][charposx+1]) in OBSTACLES:
    if charposx >= render // 2 + (boundbox // 2 - 1):
      xcord += 1
      map = movement.moveRi(render, map, xcord, ycord, grids, history, objects)
    else:
      charposx += 1

def collect():
  current_biome = pngbiomes.biome_finder(charposx+xcord, ycord-charposy, grids)
  if map[charposy][charposx] == biomes[current_biome][len(biomes[current_biome]) - 1]:
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

def sword():
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
    history[target] = " "

def place():
  if inventory[0] > 0 and not (xcord+charposx, ycord-charposy) in objects:
    map[charposy][charposx] = "\N{BALLOT BOX WITH X}"
    objects[(xcord+charposx, ycord-charposy)] = "\N{BALLOT BOX WITH X}"
    inventory[0] -= 1
    rendering.inventory(render, inventory, inventorypos)

def gun():
  pass

def weapon3():
  pass

def inventselectup():
  inventorypos += 1
  if inventorypos > len(inventory):
    inventorypos = 0 

def inventselectdown():
  inventorypos -= 1
  if inventorypos < 1:
    inventorypos = len(inventory)
