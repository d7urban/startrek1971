import random
import TrekStrings
import Glyphs

class SparseMap:
    ''' 
    Minimalist mapping. On-demand Area epansion to full-Area views.
    '''

    class Region():
        ''' 
        Regional meta for a collection of Area maps.
        '''
        def __init__(self):
            self.name = ""

    class Area():
        ''' 
        A minimalist collection of Area-plotted Glyphs. 
        Area numbers are 1's based.
        Area plotting is 0's based.
        Names are Trekian.
        '''
        class Piece:
            '''
            Sparse data management for an increasingly minimalist world.
            '''
            def __init__(self, xpos, ypos, glyph=Glyphs.SPACE):
                self.xpos = xpos
                self.ypos = ypos
                self.glyph = glyph

        def __init__(self):
            '''
            Create an empty AREA.
            '''
            self.name = ""
            self.number = -1
            self.scanned = False
            self.objs = []

        def is_null(self):
            '''
            See if this AREA has anything important.
            '''
            dum = Area()
            return dum.name == self.name and \
                dum.number == self.number and \
                dum.scanned == self.scanned and \
                len(dum.objs) == len(self.objs)

        def is_empty(self):
            ''' Checks to see if the Area has anything ...'''
            return len(self.objs) == True

        def items(self):
            ''' Items in the Area ...'''
            return len(self.objs)

        def remove(self, xpos, ypos):
            ''' Remove an item from the Area. '''
            for ss, obj in enumerate(self.objs):
                if obj.xpos == xpos and obj.ypos == ypos:
                    self.objs.remove(obj)
                    return

        def get_map(self):
            ''' 
            Generate a map of this sector. Map is full 
            of Glyphs.SPACE on error.
            '''
            results = [[Glyphs.SPACE for _ in range(8)] for _ in range(8)]
            for obj in self.objs:
                results[obj.ypos][obj.xpos] = obj.glyph # ASSURED
            return results

        def __str__(self):
            result = ''
            for line in get_map():
                result += ''.join(line)
                result += '\n'
            return result

        def range_ok(self, xpos, ypos):
            ''' Verify that coordinates are plottable. '''
            if xpos < 0 or ypos < 0 or \
                xpos > 7 or ypos > 7:
                return False
            return True

        def get_data(self, glyph):
            results = []
            for p in self.objs:
                if p.glyph == glyph:
                    results.append(SparseMap.Area.clone(p))
            return results

        def count_glyphs(self, glyph):
            '''
            Tally the number of glyphs that we have in the Area.
            '''
            count = 0
            for p in self.objs:
                if p.glyph == glyph:
                    count += 1
            return count

        def plot_glyph(self, xpos, ypos, glyph):
            ''' 
            Sync (update or add) a glyph to the sparse array.
            Return coordinate occupied, else None on error.
            '''
            if self.range_ok(xpos, ypos) is False:
                return None
            for p in self.objs:
                if p.xpos is xpos and p.ypos is ypos:
                    p.glyph = glyph
                    return xpos, ypos
            self.objs.append(SparseMap.Area.Piece(xpos, ypos, glyph))
            return xpos, ypos

        def place_glyph(self, glyph, dest=None):
            ''' Place / randomly place a glyph into the Map. '''
            area = self.get_map()
            if not dest:
                while True:
                    xpos = random.randrange(0,7)
                    ypos = random.randrange(0,7)
                    if area[xpos][ypos] == Glyphs.SPACE:
                        self.plot_glyph(xpos, ypos, glyph)
                        return xpos, ypos                    
            else:
                self.plot_glyph(xpos, ypos, glyph)
            return dest.xpos, dest.ypos

        @staticmethod
        def clone(piece):
            ''' Copy a piece. '''
            ''' Copy a piece. '''
            return SparseMap.Area.Piece(piece.xpos, piece.ypos, piece.glyph)

    def __init__(self):
        self.initalized = False
        self.map = [[[y,x] for y in range(8)] for x in range(8)]

    def init(self, reset=False):
        if not reset and self.initalized:
            return
        for xx, row in enumerate(self.map):
            lrs = SparseMap.Region()
            for yy, col in enumerate(row):
                self.map[xx][yy] = [lrs, SparseMap.Area()]
        self.name_areas()
        self.initalized = True

    def data(self):
        ''' Enumerate thru every [Region, Area] in the Map '''
        for row in self.map:
            for col in row:
                yield col

    def areas(self):
        ''' Enumerare thru every Area on the Map '''
        for row in self.map:
            for col in row:
                yield col[1]

    def name_areas(self):
        names = list(TrekStrings.quadrantNames)
        for num, area in enumerate(self.areas(),1):
            index = random.randint(0, len(names) - 1)
            area.name = names[index]
            area.number = num
            del names[index]

    def get_sector_names(self):
        results = []
        temp = []
        for ss, col in enumerate(self.areas(),1):
            temp.append([col.number,col.name])
            if ss % 8 == 0:
                results.append(temp)
                temp = []
        results.append(temp)
        return results

    def plot(self, ones_based, xpos, ypos, glyph):
        ''' 
        Add an item to a MAP using the 1's based AREA identifier.
        Coordinates here are ZERO based.
        '''
        for area in self.areas():
            if area.number == ones_based:
                area.plot_glyph(xpos, ypos, glyph)
                return True
        return False

    def plot_ones_based(self, ones_based, xpos, ypos, glyph):
        ''' 
        Add an item to a MAP using the 1's based AREA identifier.
        Coordinates here are ONES based.
        '''
        return self.plot(ones_based, xpos -1, ypos -1, glyph)