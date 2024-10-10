import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
g = 10

# Boundaries
R1_1 = np.array([1, 3])  # good
R1_2 = np.array([5, 3])

R2_1 = np.array([9, 3])  # good
R2_2 = np.array([13, 3])

R3_1 = np.array([7, 4])  # bad
R3_2 = np.array([7, 5])

R4_1 = np.array([7, 7])  # bad
R4_2 = np.array([7, 8])

v0_min = 1
v0_range = 29

min_angle = 1
max_angle = 89
angle_range = 90

number_of_trials = 50000

valid_v0 = []
valid_angle = []

# Show the regions. Green for good, red for bad
plt.figure()
plt.plot([R1_1[0], R1_2[0]], [R1_1[1], R1_2[1]], 'g', linewidth=2)  # Good segment 1 (Green)
plt.plot([R2_1[0], R2_2[0]], [R2_1[1], R2_2[1]], 'g', linewidth=2)  # Good segment 2 (Green)
plt.plot([R3_1[0], R3_2[0]], [R3_1[1], R3_2[1]], 'r', linewidth=2)  # Bad segment 1 (Red)
plt.plot([R4_1[0], R4_2[0]], [R4_1[1], R4_2[1]], 'r', linewidth=2)  # Bad segment 2 (Red)
plt.hold = True

plotted_correct_trajectories = 0

def get_y_from_x(x, vx, vy, g):
    return vy * x / vx - 0.5 * g * (x / vx)**2

def get_x_from_y(y, vx, vy, g):
    discriminant = vy**2 - 2 * g * y
    if discriminant < 0:
        return np.array([0, 0])
    return np.array([(vx / g) * (vy + np.sqrt(discriminant)), (vx / g) * (vy - np.sqrt(discriminant))])

def check_intersection(to_be_checked, smaller, larger):
    return smaller <= to_be_checked <= larger

# Simulation loop
for _ in range(number_of_trials):
    v0 = v0_min + v0_range * np.random.rand()
    alpha = min_angle + angle_range * np.random.rand()

    v0x = v0 * np.cos(np.radians(alpha))
    v0y = v0 * np.sin(np.radians(alpha))

    flight_time = 2 * v0y / g
    time_vect = np.linspace(0, flight_time, 100)

    x_now = v0x * time_vect
    y_now = v0y * time_vect - 0.5 * g * time_vect**2

    x_values = get_x_from_y(R1_2[1], v0x, v0y, g)

    if not np.all(x_values == 0):
        crossed1good = check_intersection(x_values[0], R1_1[0], R1_2[0]) or check_intersection(x_values[1], R1_1[0], R1_2[0])
        crossed2good = check_intersection(x_values[0], R2_1[0], R2_2[0]) or check_intersection(x_values[1], R2_1[0], R2_2[0])
    else:
        crossed1good = crossed2good = False

    crossed3bad = check_intersection(get_y_from_x(R3_2[0], v0x, v0y, g), R3_1[1], R3_2[1])
    crossed4bad = check_intersection(get_y_from_x(R4_2[0], v0x, v0y, g), R4_1[1], R4_2[1])

    if crossed1good and crossed2good and not crossed3bad and not crossed4bad:
        valid_v0.append(v0)
        valid_angle.append(alpha)
        
        if plotted_correct_trajectories < 5:
            plt.plot(x_now, y_now, color=[0.5, 0.5, 0.5])
            plotted_correct_trajectories += 1

# Probability calculation
prob = len(valid_angle) / number_of_trials
print(f'Probability: {prob}')

# Plot the valid v0 and angle pairs
plt.figure()
plt.scatter(valid_v0, valid_angle, c='b', marker='o')
plt.xlabel('Initial Speed v0')
plt.ylabel('Angle α (degrees)')
plt.title('Valid pairs of v0 and α')
plt.grid(True)
plt.show()
