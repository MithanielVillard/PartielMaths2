import math
import matplotlib.pyplot as plt

def solide(n):
    points = []
    
    cube = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
    ]
    points.extend(cube)
    remaining = n - 8 if n > 8 else 0
    
    if remaining >= 8:
        rectangle = [
            [1.5, 0, 0], [3.5, 0, 0], [3.5, 1, 0], [1.5, 1, 0],
            [1.5, 0, 0.5], [3.5, 0, 0.5], [3.5, 1, 0.5], [1.5, 1, 0.5]
        ]
        points.extend(rectangle)
        remaining -= 8
    
    if remaining >= 4:
        triangle = [
            [0, 1.5, 0], [1, 1.5, 0], [0, 2.5, 0],
            [0, 1.5, 1]
        ]
        points.extend(triangle)
        remaining -= 4
    
    if remaining > 0:
        radius = 0.5
        height = 1
        center_x, center_y = 2, 1.5
        segments = max(10, remaining//2)
        
        for i in range(segments):
            angle = 2 * math.pi * i / segments
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append([x, y, 0])
            if len(points) < n:
                points.append([x, y, height])
    
    return points[:n]

def afficher_solide_3d(points):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    z = [p[2] for p in points]
    ax.scatter(x, y, z, c='b', s=50)
    
    def trace_forme(indices, color):
        for i in range(len(indices)-1):
            ax.plot(
                [points[indices[i]][0], points[indices[i+1]][0]],
                [points[indices[i]][1], points[indices[i+1]][1]],
                [points[indices[i]][2], points[indices[i+1]][2]],
                color=color, linewidth=2
            )
    
    if len(points) >= 8:
        trace_forme([0,1,2,3,0], 'red')
        trace_forme([4,5,6,7,4], 'red')
        for i in range(4):
            trace_forme([i, i+4], 'red')
    
    if len(points) >= 16: 
        trace_forme([8,9,10,11,8], 'green')
        trace_forme([12,13,14,15,12], 'green')
        for i in range(4):
            trace_forme([8+i, 12+i], 'green')
    
    if len(points) >= 20:
        trace_forme([16,17,18,16], 'blue')
        trace_forme([16,19], 'blue')
        trace_forme([17,19], 'blue')
        trace_forme([18,19], 'blue')
    
    if len(points) > 20:
        cyl_points = len(points) - 20
        segments = cyl_points // 2
        
        for i in range(segments):
            next_i = (i+1)%segments
            ax.plot(
                [points[20+i*2][0], points[20+next_i*2][0]],
                [points[20+i*2][1], points[20+next_i*2][1]],
                [points[20+i*2][2], points[20+next_i*2][2]],
                color='orange'
            )
        
        for i in range(segments):
            if 20+i*2+1 < len(points):
                ax.plot(
                    [points[20+i*2][0], points[20+i*2+1][0]],
                    [points[20+i*2][1], points[20+i*2+1][1]],
                    [points[20+i*2][2], points[20+i*2+1][2]],
                    color='orange'
                )
                
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Solide 3D ({len(points)} points)')
    plt.tight_layout()
    plt.show()

points = solide(50)
afficher_solide_3d(points)

