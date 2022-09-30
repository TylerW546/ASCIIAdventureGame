import random

# Biomes add the empty space character on the left and the inportant charactors on the right, 1 = recource hill
biomes = [  
  ["\N{TOP PARENTHESIS}", "\N{TOP PARENTHESIS}", "__", "__", "__", "__", "__", "__", "__", "__", "\N{TOP PARENTHESIS}", "\N{TOP PARENTHESIS}", 1], 
  [" ", " ", " ", " ", "~", "~", "~", "\N{LEFT DOUBLE WIGGLY FENCE}"],
  [" ", " ", "\N{APL FUNCTIONAL SYMBOL DELTA STILE}"],
  [" ", "~", "2", "*"]]
# GET SEEDS --------------------------------------------------------------------------------
# Character Seed(For Biome Decor)
seed = [random.randint(1, 13) for j in range(16)]
# Biome Seed(For Biome)
biomeseed = [random.randint(1, 13) for j in range(16)]




def findspace(x, y, grids, history, objects):#procedural number generation, outputs character given x and y
  try:
    objects[(x, y)]
  except:
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
      history[(x, y)]
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
      return(history[(x, y)])
    return(outnum)
  else:
    return(objects[(x, y)])


def biome_finder(x, y, grids):# biome_finder, uses part of PNG system to output what biome the charactor is on
  seednum = ((x // grids) ^ (y // grids)) % len(biomeseed)
  vert = (y // grids) % biomeseed[seednum] * 20
  if biomeseed[seednum] ^ biomeseed[seednum % 15] == 0:
    horiz = (x // grids) % (biomeseed[seednum] ^ biomeseed[seednum % 1] + biomeseed[seednum]) * 3
  else:
    horiz = (x // grids) % (biomeseed[seednum] ^ biomeseed[seednum % 15]) * 3
  biome = (y // grids) + (x // grids)
  biome ^= (vert // (horiz + 1))
  biome %= len(biomes)
  return(biome)