OBSTACLES = ["\N{BALLOT BOX WITH X}"]

# runs the changes to the map for map and holw screen generation
import pngbiomes


def map_creation(x, y, render, grids, history, objects, map):
  for j in range(render):
    for k in range(render):
      if (y-j) % grids == 0:
        if (k+x) % grids == 0:
          map[j][k] = "+"
        else:
          map[j][k] = "-"
      else:
        if (k+x) % grids == 0:
          map[j][k] = "|"
        else:
          map[j][k] = pngbiomes.findspace(k+x, y-j, grids, history, objects)
  return (map)


def moveUp(render, map, x, y, grids, history, objects):
  for j in range(render - 1):
    for k in range(render):
      map[render-j-1][k] = map[render-j-2][k]
  for j in range(render):
    map[0][j] = pngbiomes.findspace(x+j, y, grids, history, objects)
  return(map)


def moveRi(render, map, x, y, grids, history, objects):
  for j in range(render):
    for k in range(render-1):
      map[j][k] = map[j][k+1]
  for k in range(render):
    map[k][render-1] = pngbiomes.findspace(x+render-1, y-k, grids, history, objects)
  return(map)


def moveDo(render, map, x, y, grids, history, objects):
  for j in range(render):
    for k in range(render-1):
      map[k][j] = map[k+1][j]
  for j in range(render):
    map[render-1][j] = pngbiomes.findspace(x+j, y-render+1, grids, history, objects)
  return(map)


def moveLe(render, map, x, y, grids, history, objects):
  for j in range(render):
    for k in range(render):
      map[j][render-k-1] = map[j][render-k-2]
  for k in range(render):
    map[k][0] = pngbiomes.findspace(x, y-k, grids, history, objects)
  return(map)