class Box(object):
    vol = 0
    sArea = 0
    
    def __init__(self):
        boxLength = 0
        boxWidth = 0
        boxHeight = 0
    def boxVol(self):
        vol = boxLength * boxWidth * boxHeight
        print(vol)
    def boxSArea(self):
        sArea = ((boxLength * boxWidth * 2) + (boxLength * boxHeight * 2) + (boxHeight * boxWidth))
        print(sArea)
