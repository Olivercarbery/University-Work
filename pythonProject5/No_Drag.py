import math


def trajectory(initial_velocity, theta, g, initial_height):
    theta = math.radians(theta)  # Convert degrees to radians
    u_v = initial_velocity * math.sin(theta)  # calculate vertical component of initial velocity
    # print(u_v)
    u_h = initial_velocity * math.cos(theta)  # calculate horizontal component of initial velocity
    # print(u_h)
    t_peak = u_v/g  # calculate time to ascend to peak
    # print(t_peak)
    s_peak = (u_v*t_peak + (1/2)*(-9.81)*t_peak**2) + initial_height  # calculate peak height
    # print(s_peak)
    t_fall = math.sqrt((2*s_peak)/g)  # Calculate time to fall
    # print(t_fall)
    v_vert = g * t_fall  # Calculate final velocity
    # print(v_vert)
    t_total = t_fall + t_peak  # calculate total time
    # print(t_total)
    s_h = u_h*t_total    # Calculate max distance
    #print(s_h)
    s_Horizontal = []
    s_Vertical = []
    #print(int(t_total))
    step = 0
    for i in range(0, int(t_total)*100):
        s_hor = u_h*step
        s_Horizontal.append(s_hor)
        # print(s_hor)
        s_vert = ((u_v*step)+(1/2)*-g*step**2)+initial_height
        # print(s_vert)
        s_Vertical.append(s_vert)
        step += 0.1

    y = s_Vertical
    for i in range(0, len(y)):
        if y[i] < 0:
            y[i] = 0

    x = s_Horizontal
    for i in range(0, len(x)):
        if x[i] > s_h:
            x[i] = s_h

    return x,y

