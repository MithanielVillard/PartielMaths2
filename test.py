import math
import matplotlib.pyplot as plt

def déplace_mat(I, m, G, A):

# Calcul du vecteur AG = G - A
    a = G[0] - A[0]
    b = G[1] - A[1]
    c = G[2] - A[2]

# Calcul des termes de la matrice de translation
    I11 = m * (b**2 + c**2)
    I22 = m * (a**2 + c**2)
    I33 = m * (a**2 + b**2)
    I12 = I21 = -m * a * b
    I13 = I31 = -m * a * c
    I23 = I32 = -m * b * c

# Construction de la matrice de translation
    I_trans = [
        [I11, I12, I13],
        [I21, I22, I23],
        [I31, I32, I33]
    ]

# Addition des matrices I + I_trans
    I_A = [
        [I[i][j] + I_trans[i][j] for j in range(3)]
        for i in range(3)
    ]

    return I_A

def solide(n):
    points = []
    
    # 1. Points fixes (22 points)
    fixed_points = [
        # Cube (8 points)
        [0.75,0.5,0.75], [1.25,0.5,0.75], [1.25,1.5,0.75], [0.75,1.5,0.75],
        [0.75,0.5,1.25], [1.25,0.5,1.25], [1.25,1.5,1.25], [0.75,1.5,1.25],
        
        # Rectangle (8 points)
        [0.25,0.5,0.25], [2.25,0.5,0.25], [2.25,1.5,0.25], [0.25,1.5,0.25],
        [0.25,0.5,0.75], [2.25,0.5,0.75], [2.25,1.5,0.75], [0.25,1.5,0.75],
        
        # Triangle (6 points)
        [0.75,0.5,0.75], [0.75,1.5,0.75], [0.25,0.5,0.75],
        [0.25,1.5,0.75], [0.75,0.5,1.25], [0.75,1.5,1.25]
    ]
    points.extend(fixed_points[:min(n, 22)])
    
    # 2. Répartition des points restants pour les cylindres
    remaining = max(0, n - 22)
    cylinder_count = 4
    
    if remaining > 0:
        base_segments = max(5, remaining // (2 * cylinder_count))
        extra_segments = remaining % (2 * cylinder_count)
        
        cylinder_params = [
            (0, 0.75, -0.25),  # Position cylindre 1
            (1.75, 0.75, -0.25),   # Position cylindre 2
            (1.75, 1.75, -0.25),   # Position cylindre 3
            (0, 1.75, -0.25)    # Position cylindre 4
        ]
        
        for i, (cx, cy, cz) in enumerate(cylinder_params):
            segments = base_segments + (extra_segments if i == cylinder_count-1 else 0)
            
            radius = 0.25
            height = 0.3
            
            for j in range(segments):
                angle = 2 * math.pi * j / segments
                x = cx + radius * math.cos(angle)
                z = cz + radius * math.sin(angle)
                
                points.append([x, cy, z])
                if len(points) >= n:
                    break
                    
                points.append([x, cy + height, z])
                if len(points) >= n:
                    break
    
    return points[:n]

def afficher_solide_3d(points):
    fig = plt.figure(figsize=(10, 10))
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
    
    if len(points) >= 22:
        trace_forme([16,17,19,18,16,17,19], 'blue')
        trace_forme([16,20], 'blue')
        trace_forme([18,20], 'blue')
        trace_forme([17,21], 'blue')
        trace_forme([19,21], 'blue')
        trace_forme([20,21], 'blue')
    
    
    cyl_starts = [22, 22+20, 22+40, 22+60]
    
    for cyl_start in cyl_starts:
        if len(points) > cyl_start:
            cyl_points = min(20, len(points) - cyl_start)
            segments = cyl_points // 2
            
            # Dessiner les cercles
            for i in range(segments):
                next_i = (i+1)%segments
                ax.plot(
                    [points[cyl_start+i*2][0], points[cyl_start+next_i*2][0]],
                    [points[cyl_start+i*2][1], points[cyl_start+next_i*2][1]],
                    [points[cyl_start+i*2][2], points[cyl_start+next_i*2][2]],
                    color='orange'
                )
                if cyl_start+i*2+1 < len(points):
                    ax.plot(
                        [points[cyl_start+i*2][0], points[cyl_start+i*2+1][0]],
                        [points[cyl_start+i*2][1], points[cyl_start+i*2+1][1]],
                        [points[cyl_start+i*2][2], points[cyl_start+i*2+1][2]],
                        color='orange'
                    )
    
                
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Solide 3D ({len(points)} points)')
    plt.tight_layout()
    plt.show()


points = solide(102)
afficher_solide_3d(points)
test = déplace_mat(points, 1.5, [1.0, 1.0, 1.0], [0.5, 0.5, 0.5])

