vehicle_speed = input('Enter vehicle speed: ')
valid_speed = int(vehicle_speed) >= 40 and int(vehicle_speed) <= 140 

print(f'Vehicle speed is valid: {valid_speed}')