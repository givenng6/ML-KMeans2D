import math

class Point:
    def __init__(self,p_id, x, y):
        self.x = x
        self.y = y
        self.p_id = p_id
        self.centroid = None
        
    def position(self):
        return self.x, self.y
    
    def setCentroid(self, centroid):
        self.centroid = centroid
        
    def getCentroid(self):
        return self.centroid
    
    def getID(self):
        return self.p_id
    
    def distance(self, centroid):
        x_value = math.pow((centroid.position()[0] - self.x), 2) 
        y_value = math.pow((centroid.position()[1] - self.y), 2)
        
        return math.sqrt(x_value + y_value)
        
    def oldDistance(self):
        x_value = math.pow((self.centroid.position()[0] - self.x), 2) 
        y_value = math.pow((self.centroid.position()[1] - self.y), 2)
        
        return math.sqrt(x_value + y_value)
        
        
class Centroid:
    def __init__(self, s_id, x, y):
        self.x = x
        self.y = y
        self.s_id = s_id
        self.pointsAssigned = []
        
    def position(self):
        return self.x, self.y
    
    def addPoint(self, point):
        self.pointsAssigned.append(point)
        
    def removePoint(self, point):
        self.pointsAssigned.remove(point)
        
    def getID(self):
        return self.s_id
    
    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        
    def getPointsAssigned(self):
        return self.pointsAssigned



def average(centroids):
    for centroid in centroids:
        points = centroid.getPointsAssigned()
        x_value = 0
        y_value = 0
        if(len(points) > 0):
            for point in points:
                x_value = x_value + point.position()[0]
                y_value = y_value + point.position()[1]
        
        x = x_value / len(points)
        y = y_value / len(points)
        centroid.updatePosition(x, y)



def K_Means(points, centroids):
    
    for point in points:
        for centroid in centroids:
            distance = point.distance(centroid)
            if point.getCentroid() is None:
                point.setCentroid(centroid)
                centroid.addPoint(point)
            else:
                if point.oldDistance() > distance:
                    point.getCentroid().removePoint(point)
                    point.setCentroid(centroid)
                    centroid.addPoint(point)

x_points = [0.2, 0.7, 0.3, 0.6]
y_points = [0.4, 0.3, 0.6, 0.1]

x_cent = [0.5, 0.8]
y_cent = [0.3, 0.4]

centroids = []
points = []
for i in range(len(x_points)):
    points.append(Point(i, x_points[i], y_points[i]))

for i in range(len(x_cent)):
    centroids.append(Centroid(i, x_cent[i], y_cent[i]))
    
    
assignList = [0, 0, 0, 0, 0, 0, 0]

while True:
    K_Means(points, centroids)
    average(centroids)
    
    oldList = assignList.copy()
    
    if assignList == oldList:
        break


for centroid in centroids:
    print(str(centroid.getID()) + " Centroid New Coord " + str(centroid.position()))

print("Points.......")
for point in points:
    print(str(point.getID()) + " Closer to " + str(point.getCentroid().getID()))






