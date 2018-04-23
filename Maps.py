from ScreenConvert import *

test_map = [(0, 200), (1200, 200), (1200, 700), (200, 700), (200, 400), (700, 450)]
for i, (a, b) in enumerate(test_map):
     test_map[i] = (int(a * screenWidth / 1600 * widthMultiplier), int(b * screenHeight / 900 * heightMultiplier))

badPixels = [] 


def wrongPixels(mapTk, path_color):
    
    for i, j in zip(range(int(screenWidth * widthMultiplier - 1)), range(int(screenHeight * heightMultiplier - 1))) : 
        if (mapTk.get_at((j, i)) == path_color):
            badPixels.append((j, i))
            
