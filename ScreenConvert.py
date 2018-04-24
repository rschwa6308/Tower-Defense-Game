import tkinter 

screenWidth = 1366
screenHeight = 768


def sendSizes(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    
widthMultiplier = .8
heightMultiplier = .9
heightRatio = screenHeight / 900 * heightMultiplier
widthRatio = screenWidth / 1600 * widthMultiplier

