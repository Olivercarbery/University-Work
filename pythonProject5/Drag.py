import math


def trajectory_drag(g, density, drag_coefficient, cross_section_area, mass, initial_velocity, initial_height, theta):
    p = density
    C_D = drag_coefficient
    A = cross_section_area
    m = mass
    v = initial_velocity
    h = initial_height
    v2 = v
    theta = math.radians(theta)

    dt = 0.01  # time step (s) constant
    t = 0
    ds = 0  # difference in distance
    s_v = h  # adds launch height to initial height
    U_v = v * math.sin(theta)  # Calculate vertical component of initial velocity
    #  print(U_v)
    # initialise velocity
    v = U_v
    # print(f'Velocity: {v}')
    s_Horizontal = []
    s_Vertical = []

    while v > 0:
        F = -((1/2)*p*(v**2)*C_D*A)-m*g  # Force acting on cannonball (F = -drag-mg)
        # print(f'Force: {F}')
        a = (F/m)  # Acceleration due to Force acting on Cannonball
        # print(f'Acceleration: {a}')
        v = U_v+a*dt
        # print(f'Velocity: {v}')
        ds = (1/2)*(U_v+v)*dt  # Calculate distance travelled between steps
        # print(f'step distance: {ds}')
        s_v += ds  # Add step distance to total distance
        s_Vertical.append(s_v)
        # print(f'total distance {s}')
        U_v = v
        t += dt
        # print(f'time: {t}')
    t_peak = t
    s_peak = s_v
    # print(f'Peak time: {t_peak}')
    # print(f'Peak height: {s_peak}'))
    #  ~~~~ Downward Trajectory (Vertical Component) ~~~~~
    U_v = 0
    while s_v > 0:
        F = m*g - ((1/2)*p*(v**2)*C_D*A)  # weight - drag on downward trajectory
        # print(f'Force: {F}')
        a = F/m  # Acceleration due to force acting on Cannonball
        # print(f'Acceleration: {a}')
        v = U_v+a*dt  # Velocity at time step
        # print(f'Velocity: {v}')
        ds = (1/2)*(U_v+v)*dt  # Position change between time step
        U_v = v
        s_v -= ds
        s_Vertical.append(s_v)
        # print(f'Position: {s_v}')
        t += dt
        # print(f'Time elapsed: {t}')

    t_total = t
    # print(f'Total time: {t_total}')
    # ~~~~~~Horizontal Motion~~~~~~~~~
    U_h = v2 * math.cos(theta)  # Horizontal initial velocity
    # print(U_h)
    t = 0  # initialise time
    s_h = 0  # Initial horizontal position
    v = U_h
    while t < t_total:
        F = -(1/2)*p*(v**2)*C_D*A  # Drag Force acting on Cannonball
        # print(f'Force: {F}')
        a = F/m  # Horizontal acceleration of Cannonball
        # print(f'Acceleration: {a}')
        v = U_h + a * dt  # Horizontal Velocity of Cannonball
        # print(f'Velocity: {v}')
        ds = (1 / 2) * (U_h + v) * dt  # Position change between time step
        U_h = v
        s_h += ds
        s_Horizontal.append(s_h)
        # print(f'Position: {s_h}')
        t += dt
        # print(f'time: {t}')
    return s_Horizontal, s_Vertical
