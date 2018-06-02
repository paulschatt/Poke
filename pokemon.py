from pokemon_data import Tile, Player
from tkinter import *
import tkinter as tk
from time import sleep

##########
tiles = list()
coordinates = list()
############
kastengröße = 25
window = tk.Tk()
c = Canvas(width = 500, height = 500, background = 'black')
c.pack()
q1 = [1,1,1,1,1,1,1,1,1,1,1,1]
q2 = [0,1,0,1,0,0,0,0,0,0,0,0]
q3 = [0,1,1,1,0,0,0,0,0,0,0,0]
q = [q1,q2,q3]
y = 0
for i in range(len(q)):
    x = 0
    for stats in q[i]:
        if stats == 1:
            if x == 75 and y == 0:
                id1 = Tile(c, x, y, True, "Hallo! Ich bin Tom!")
            else:
                id1 = Tile(c, x, y, None, None)
            tiles.append(id1)
            coordinates.append([x, y])
        x += 25
    y += 25
for tile in tiles:
    tile.get_function(coordinates, tiles)

window.update()
id1 = c.create_rectangle(0,0,25,25, fill = 'red')
player = Player(c, [id1], tiles[0])

def movement(event):
    key = event.keysym
    print(key)
    if key in ['Up', 'Down', 'Left', 'Right']:
        player.move(key)
c.bind_all('<Key>', movement)
while True:
    window.update()
    sleep(0.1)
