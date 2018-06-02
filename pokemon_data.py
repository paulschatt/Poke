kastengröße = 25
class Tile():
    def __init__(self, canvas, x, y, person, speech):
        self.canvas = canvas
        id1 = self.canvas.create_rectangle(x, y, x+kastengröße, y+kastengröße, fill = 'green')
        self.design = [id1]
        self.coordinates = [x, y]
        self.directions = []
        self.neighbor_tiles = {}
        self.person = None
        if person == True:
            self.person = Person(canvas, x, y)
            self.person.set_speech(speech)
    #Koordinaten wiedergeben
    def return_coordinate(self):
        return self.coordinates
    #Tile mit Richtungsvermerk an benachbarten Tile linken
    def link_tile(self, direction, tile):
        self.neighbor_tiles[direction] = tile
    #eigene Koordinaten verändern und wiedergeben
    def dif_coords(self, x, y):
        tupel = self.return_coordinate()
        return [tupel[0]+x, tupel[1]+y]
    #Mit benachbarten Tiles verbinden
    def get_function(self, coordinates, tileslist):
        if self.dif_coords(kastengröße, 0) in coordinates:
            self.directions.append("Right")
            i = coordinates.index(self.dif_coords(kastengröße, 0))
            self.link_tile("Right", tileslist[i])
        if self.dif_coords(-kastengröße, 0) in coordinates:
            self.directions.append("Left")
            i = coordinates.index(self.dif_coords(-kastengröße, 0))
            self.link_tile("Left", tileslist[i])
        if self.dif_coords(0, kastengröße) in coordinates:
            self.directions.append("Down")
            i = coordinates.index(self.dif_coords(0, kastengröße))
            self.link_tile("Down", tileslist[i])
        if self.dif_coords(0, -kastengröße) in coordinates:
            self.directions.append("Up")
            i = coordinates.index(self.dif_coords(0, -kastengröße))
            self.link_tile("Up", tileslist[i])
    #mögliche Richtungen wiedergeben
    def return_directions(self):
        return self.directions
    def return_linked_tile(self, direction):
        return self.neighbor_tiles[direction]

    def return_persons(self):
        return self.person
    def persons(self):
        if self.person != None:
            return True
        else:
            return False

class Player():
    def __init__(self, canvas, design, current_tile):
        self.canvas = canvas
        self.design = design
        self.current_tile = current_tile
    def beweg(self, x, y):
        for design in self.design:
            self.canvas.move(design, x, y)
    def move(self, direction):
        if direction in self.current_tile.return_directions():
            self.current_tile = self.current_tile.return_linked_tile(direction)
            if direction == 'Up':
                self.beweg(0, -kastengröße)
            elif direction == 'Down':
                self.beweg(0, kastengröße)
            elif direction == 'Left':
                self.beweg(-kastengröße, 0)
            elif direction == 'Right':
                self.beweg(kastengröße, 0)
        if self.current_tile.persons() == True:
            self.current_tile.return_persons().speak()
class Person():
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        id1 = self.canvas.create_rectangle(x, y, x+kastengröße, y+kastengröße, fill = 'purple')
        self.design = (id1)
        self.speech = None
        self.x = x
        self.y = y
    def set_speech(self, speech):
        self.speech = speech
    def speak(self):
        id1 = self.canvas.create_rectangle(0,350,500,500,fill="white")
        id2 = self.canvas.create_text(3,380,fill="black",text=str(self.speech),font=(30))
       
