###  Modelo 1 ###
def reward_function(params):

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    progress = round(params['progress'],2)
    waypoints = params['waypoints']
    xy = (params['x'], params['y'])
    closest_waypoints = params['closest_waypoints']

    # Centrado
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
      # Recompensa segun distancia al centro
    if distance_from_center <= marker_1:
       reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    # speed
    MIN_SPEED = 1.2  # Velocidad mínima deseada
    TARGET_SPEED = 2.5  # Velocidad ideal
    if speed < MIN_SPEED:
        reward *= 0.4  # Penaliza velocidades demasiado lentas
    elif speed >= MIN_SPEED and speed <= TARGET_SPEED:
        reward += (speed - MIN_SPEED) * 0.4  # Recompensa por velocidades dentro del rango deseado
    elif speed > TARGET_SPEED:
        reward += (speed - TARGET_SPEED) * 0.65  # Incentiva velocidades superiores, pero no demasiado

    # recompensamos segun progreso del circuito
    if progress == 0.25:
        reward += 1
    elif progress == 0.5:
        reward += 2
    elif progress == 0.75:
        reward += 3
    elif progress == 0.95:
        reward += 5
    else:
        reward += 0

    # waypoints
    if xy[0] == closest_waypoints[0] and xy[1] == closest_waypoints[1]:  # si esta en el waypoint
        reward += 0.7
    elif abs(xy[0]-closest_waypoints[0])<=0.3 and abs(xy[1]-closest_waypoints[1]<=0.3): # si esta cerca del waypoint
        reward += 0.3

    return float(reward)