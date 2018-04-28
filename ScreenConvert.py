from win32api import GetSystemMetrics

screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)
widthMultiplier = .8
heightMultiplier = .9
heightRatio = screenHeight / 900 * heightMultiplier
widthRatio = screenWidth / 1600 * widthMultiplier
