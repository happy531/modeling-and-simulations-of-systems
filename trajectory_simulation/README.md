# Projectile Simulation with Boundary Conditions

## Overview

This exercise simulates the projectile motion of an object under the influence of gravity, with predefined "good" and "bad" regions in a 2D space. The goal is to find the initial velocities and angles that result in a valid trajectory—one that crosses the "good" regions while avoiding the "bad" ones.

The simulation runs multiple trials, randomly generating initial velocities and angles, and then calculates the trajectory for each trial. It checks whether the projectile crosses the specified regions and plots the valid trajectories.

## Features

- **Projectile Motion Simulation**: Models the motion of a projectile under gravity.
- **Good/Bad Regions**: Defines regions in the 2D space that the projectile should or shouldn't cross.
- **Trajectory Validation**: Checks if the projectile crosses the "good" regions and avoids the "bad" ones.
- **Visual Output**: Plots valid trajectories (up to 5) and generates a scatter plot of valid initial speeds and angles.
- **Probability Calculation**: Computes the probability of hitting valid trajectories out of all trials.

## Simulation Details

- **Good Regions**: Represented as horizontal line segments the projectile should cross.
- **Bad Regions**: Represented as horizontal line segments the projectile should avoid.
- **Initial Speed (`v0`)**: Randomly generated between `1` and `30` m/s.
- **Angle (`alpha`)**: Randomly generated between `1` and `89` degrees.
- **Gravity (`g`)**: Constant acceleration due to gravity is `10` m/s².
- **Number of Trials**: The simulation runs for 50,000 trials to find valid trajectories.

## Output

- **Trajectory Plot**: The script will generate a plot showing the "good" and "bad" regions. It will plot up to 5 valid trajectories (in gray) that successfully cross only the "good" regions.
  
- **Scatter Plot**: A scatter plot will display valid combinations of initial speeds (`v0`) and angles (`alpha`), with labels for clarity.
  
- **Probability Output**: The console will display the probability of finding valid trajectories based on the total number of trials.

## Code Structure

- **`simulation.py`**: The main script that runs the simulation. It includes the following:
  - **Projectile Motion Functions**: Compute the projectile's trajectory using kinematic equations.
  - **Intersection Check Functions**: Validate if a trajectory crosses the "good" regions and avoids the "bad" ones.
  - **Visualization**: Plots the regions and valid trajectories using `matplotlib`.

### Key Parameters

- **Initial Speed (`v0`)**: Randomly chosen between `1` and `30` m/s.
- **Launch Angle (`alpha`)**: Randomly selected between `1` and `89` degrees.
- **Gravity (`g`)**: Set to `10` m/s².
- **Number of Trials**: 50,000 trials are used to sample possible trajectories.
  
### Good and Bad Regions
The regions in the simulation are defined as horizontal line segments:
- **Good Regions** (green):
  - Region 1: from point (1, 3) to (5, 3)
  - Region 2: from point (9, 3) to (13, 3)
  
- **Bad Regions** (red):
  - Region 3: from point (7, 4) to (7, 5)
  - Region 4: from point (7, 7) to (7, 8)

## Example Output

- **Valid Trajectories Plot**: A plot showing the regions and the valid trajectories, crossing only the good regions.
  
- **Scatter Plot**: A scatter plot of valid initial speeds and launch angles.