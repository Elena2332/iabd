'''{
    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center
}'''
#########  recompensa-sac modelo41  ###########
def reward_function(params):
    # Leer parámetros de entrada
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = abs(params['steering_angle'])
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']

    # Inicializar la recompensa
    reward = 1e-3  # Evitar cero para no interrumpir el entrenamiento

    ### Evitar zigzag ###
    # Penalización para grandes ángulos de giro
    ABS_STEERING_THRESHOLD = 15  # Ángulo límite para penalizar
    if steering_angle > ABS_STEERING_THRESHOLD:
        reward *= 0.65  # Penaliza si el ángulo de giro es demasiado alto

    ### Premiar ir centrado ###
    # Definir marcadores basados en la anchura de la pista
    marker_1 = 0.1 * track_width  # Cercano al centro
    marker_2 = 0.25 * track_width  # Moderadamente cerca
    marker_3 = 0.5 * track_width  # Lejos del centro
    
    # Recompensa basada en la distancia desde el centro
    if distance_from_center <= marker_1:
        reward += 1.5  # Máxima recompensa por estar cerca del centro
    elif distance_from_center <= marker_2:
        reward += 0.8  # Recompensa moderada
    elif distance_from_center <= marker_3:
        reward += 0.3  # Recompensa baja
    else:
        reward = 1e-3  # Penalización fuerte por estar fuera de pista

    ### Penalizar velocidades bajas ###
    # Recompensa basada en la velocidad
    MIN_SPEED = 1.2  # Velocidad mínima deseada
    TARGET_SPEED = 2.3  # Velocidad ideal
    if speed < MIN_SPEED:
        reward *= 0.5  # Penaliza velocidades demasiado lentas
    elif speed >= MIN_SPEED and speed <= TARGET_SPEED:
        reward += (speed - MIN_SPEED) * 0.5  # Recompensa por velocidades dentro del rango deseado
    elif speed > TARGET_SPEED:
        reward += 0.3  # Incentiva velocidades superiores, pero no demasiado

    ### Bonificación por mantener todas las ruedas en la pista ###
    if all_wheels_on_track:
        reward += 0.5  # Recompensa adicional por mantener estabilidad

    # si se ha salido penalizamos
    if params['is_offtrack']:
        reward += -2

    return float(reward)
