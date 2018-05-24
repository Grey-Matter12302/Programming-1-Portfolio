class Pyramid(object):
    vol = 0
    sArea = 0
    
    def __init__(self):
        pyramidLength = 0
        pyramidWidth = 0
        pyramidHeight = 0
    def pyramidVol(self):
        vol = pyramidLength * pyramidWidth * pyramidHeight
        print(vol)
    def pyramidSarea(self):
        sArea = ((pyramidLength * pyramidWidth * 2) + (pyramidLength * pyramidHeight * 2) + (pyramidHeight * pyramidWidth))
        print(sArea)
