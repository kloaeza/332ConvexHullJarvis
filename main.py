from typing import List, Tuple

Point = Tuple[float, float]

# Helper function that determines the turn direction
def get_orientation(p, q, r):
    val = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

    # If values are collinear, return 0 
    if val == 0:
        return 0
    
    # If values positive, CCW, return 2
    if val > 0:
        return 2
    
    # Else values CW, return 1
    else:
        return 1

def convex_hull_jarvis(points: List[Point]) -> List[Point]:
   
    n = len(points)

    # Return if less than 3 points given
    if n < 3:
        return points
    
    # Finds leftmost point for starting anchor
    leftmost = 0

    for i in range(1, n):
        # If x coordinate smaller, leftmost = i
        if points[i][0] < points[leftmost][0]:
            leftmost = i

        # If same x coordinate, pick bottom most y coordinate
        elif points[i][0] == points[leftmost][0]:
            if points[i][1] < points[leftmost][1]:
                leftmost = 1

    hull = []
    p = leftmost

    # Gift Wrapping process
    while True:
        # Adds anchor point to hull
        hull.append(points[p])

        # Picks next point in the list as first q
        q = (p + 1) % n


if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]