## Inspiration
Traffic Lights in Copenhagen, Denmark. People are able to smoothly flow through intersections due to the fact that traffic lights constantly monitor traffic and change lights accordingly. Here in Edmonton, there could be no cars crossing the intersection for what feels like hours, yet you still have to wait for the whole cycle to go through until you get a green light.

## What it does
Reduces wait times at traffic lights by constantly counting cars using a light detector, and cycles the traffic lights accordingly to reduce waypoints.

## How we built it
Breadboard with LEDs, photresistors, and an LCD screen with a Raspberry Pi Pico to control everything.

## Challenges we ran into
Implementing multithreading to keep track of cars while traffic lights were operating.

## Accomplishments that we're proud of
We finished within the time limit. We were able to work together as a team to create a working prototype that displays the functionality we set out to accomplish.

## What we learned
MicroPython, multithreading, servo, photoresistors as a sensor to detect cars.

## What's next for Smart Traffic Control
Scaling it up to a microcontroller with more pins, implementing bus and pedestrian priority, and using lasers for vehicle detection (longer range).
