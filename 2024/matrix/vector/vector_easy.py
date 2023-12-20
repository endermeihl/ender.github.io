from vector_drawing import *

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

def add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

dino_vectors2=[add((-1.5,-2,5),v) for v in dino_vectors]

draw(Points(*dino_vectors),Polygon(*dino_vectors)
,Points(*dino_vectors2),Polygon(*dino_vectors2,color=red))
