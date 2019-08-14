from ScreenConvert import *
from builtins import len
'''# I don't need this stuff any more. Use of wrapper class depracates it.
test_map = [(0, 50), (1200, 200), (1200, 700), (200, 700), (200, 400), (700, 450)]
for i, (a, b) in enumerate(test_map):
     test_map[i] = (int(a * screenWidth / 1600 * widthMultiplier), int(b * screenHeight / 900 * heightMultiplier))
'''
# These next ones have to be here, global variables are declared before whole class
map_pixels =[]
badPixels = [] 
base_position = (0,0)
    
class map:
    
    def wrongPixels(map,mapTk, path_color, _base):
        # print("Bad Pixels")
        for i in range(int(screenWidth * widthMultiplier)):
            for j in range(int(screenHeight * heightMultiplier)) : 
                if (mapTk.get_at((i, j)) == path_color or _base.rect.contains(i, j, 0 , 0)):
                    badPixels.append((i, j))
                    # print(i, j)
    
        # print("End bad Pixels")
        
    def convert(self,map1):
        for i, (a, b) in enumerate(map1):
            map1[i] = (int(a * screenWidth / 1600 * widthMultiplier), int(b * screenHeight / 900 * heightMultiplier))
    
    def get_map(self):
        convert(map_pixels)
        return map_pixels
    def __len__(self):
        return len(map_pixels)

class TestMap(map):
    map_pixels = [(0, 50), (1200, 200), (1200, 700), (200, 700), (200, 400), (700, 450)]
    base_position = (screenWidth * widthMultiplier / 2, screenHeight * heightMultiplier / 2)
    map.convert(map,map_pixels)
    
class LoopyMap(map):
    map_pixels = [(0,0),(),(),(),(),(),(),(),(),(),()]
    