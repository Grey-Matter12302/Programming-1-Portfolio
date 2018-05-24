class Sphere(object):
    vol = 0
    sArea = 0
    
    def __init__(self):
        sphereLength = 0
        sphereWidth = 0
        sphereHeight = 0
    def sphereVol(self):
        vol = sphereLength * sphereWidth * sphereHeight
        print(vol)
    def sphereSArea(self):
        sArea = ((sphereLength * sphereWidth * 2) + (sphereLength * sphereHeight * 2) + (sphereHeight * sphereWidth))
        print(sArea)
