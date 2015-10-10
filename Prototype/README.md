# nBodySim

This simulates many bodies under the effect of gravity. Requires numpy and pygame.

W, a, s, and d move the screen.

Z outputs memory usage stats, x clears the paths of the particles, and c deletes all the objects on screen.

Spacebar pauses the simulation, and + and - (don't use shift for either, just press the keys) speed up and slow down the simulation, respectively.

To create a new particle, click and drag to determine the size of the particle; the area of the circle is the square root of the mass.

To determine the velocity of the particle, click in the direction from which the particle would have come from; press spacebar to give it zero speed.

Press q while creating to prevent the particle from changing speed beyond the initial assignment.

Things To Add:

  Ability to center on any object
  
  Ability to show paths based on frame of reference of any object
  
  Ability to create inactive particles that move on periodic paths, not just stay still or move in a simgle direction at a single speed
  
  Adding a simulation saving and loading option
  
  Adding a finish line?
  
  Other goals
