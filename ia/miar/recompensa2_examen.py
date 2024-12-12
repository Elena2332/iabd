### Modelo 2 ###
def reward_function(params):
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = abs(params['steering_angle'])
    speed = params['speed']
    
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
    
    # Recompensa por mantenerse dentro de la pista
    if params['all_wheels_on_track']:
        reward += 0.65  # Recompensa adicional por mantener estabilidad

    # Penalizacion por salida
    if params['is_offtrack']:
        reward += -3

    # Evitar zig-zag
    ABS_STEERING_THRESHOLD = 20  # Ángulo límite para penalizar
    if steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.65 

    # Recompensa basada en la velocidad
    MIN_SPEED = 1.2  # Velocidad mínima deseada
    TARGET_SPEED = 2.1  # Velocidad ideal
    if speed < MIN_SPEED:
        reward *= 0.5  # Penaliza velocidades demasiado lentas
    elif speed >= MIN_SPEED and speed <= TARGET_SPEED:
        reward += (speed - MIN_SPEED) * 0.5  # Recompensa por velocidades dentro del rango deseado
    elif speed > TARGET_SPEED:
        reward += (speed - TARGET_SPEED) * 0.7  # Incentiva velocidades superiores, pero no demasiado


    return float(reward)