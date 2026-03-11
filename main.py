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
   pass


if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]