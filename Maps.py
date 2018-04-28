from ScreenConvert import *

test_map = [(0, 200), (1200, 200), (1200, 700), (200, 700), (200, 400), (700, 450)]
for i, (a, b) in enumerate(test_map):
    test_map[i] = (int(a * screenWidth / 1600 * widthMultiplier), int(b * screenHeight / 900 * heightMultiplier))

badPixels = []


def wrongPixels(mapTk, path_color, _base):
    # print("Bad Pixels")
    for i in range(int(screenWidth * widthMultiplier)):
        for j in range(int(screenHeight * heightMultiplier)):
            if (mapTk.get_at((i, j)) == path_color or _base.rect.contains(i, j, 0, 0)):
                badPixels.append((i, j))
                # print(i, j)

                # print("End bad Pixels")
