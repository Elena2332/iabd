#########  recompensa-34  ###########
def reward_function(params):
    reward = 0
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    speed = params['speed']
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
   
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    #Zig-zag
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15
   
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.6
    else: 
        if speed < 1.8:   # penaliza si lento en las rectas
            reward -= (speed - 1.8) * 0.2 
    if speed > 1.5:  # premia si va mas rapido
        reward += (speed - 1.5) * 0.3  # Increase reward based on speed

    #salida de pista
    # recompensa por mantenerse dentro del recorrido
    if params['all_wheels_on_track']:
        reward += 0.2

    # si se ha salido penalizamos
    if params['is_offtrack']:
        reward += -2

    return float(reward)