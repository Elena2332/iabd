#########  recompensa-35  ###########
def reward_function(params):
    reward = 0
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle'])  # Absolute steering angle
    speed = params['speed']
    
    ### Centrado
    # Calculate markers at varying distances from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Reward based on distance from center
    if distance_from_center <= marker_1:
        reward = 1.5  
    elif distance_from_center <= marker_2:
        reward = 0.8
    elif distance_from_center <= marker_3:
        reward = 0.2
    else:
        reward = 1e-3  # Likely off track
    
    ### Zigzag (steering stability)
    ABS_STEERING_THRESHOLD = 15  # Threshold for penalizing steering
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.5  # Penaliza por girar muy cerrado
    
    ### Velocidad
    # Encourage higher speeds
    if speed >= 2.0:
        reward += (speed - 2.0) * 1.0  # Incentivo para que corra
    elif speed < 1.4:
        reward -= (1.4 - speed) * 0.5  # Penalizacion por lento
    
    ### Pista (track adherence)
    # Premia por estar dentro
    if params['all_wheels_on_track']:
        reward += 0.4
    if params['is_offtrack']:
        reward -= 3.0  # Penaliza por salir
    
    return float(reward)
