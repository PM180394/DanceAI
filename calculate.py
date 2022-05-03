import math

def obtain_landmarks(landmarklist):
	landmarks=[]
	for lmark in landmarklist.landmark:
		landmark= ({'x': lmark.x, 'y': lmark.y})
		landmarks.append(landmark)
		
	return landmarks
	
		
def relative_distance(landmarklist, origin_x, origin_y):
	distance=[None]* len(landmarklist)
	for i in range (0,len(landmarklist)):
		distance[i]= math.dist([origin_x, origin_y],[landmarklist[i].x, landmarklist[i].y])			
	return distance					
