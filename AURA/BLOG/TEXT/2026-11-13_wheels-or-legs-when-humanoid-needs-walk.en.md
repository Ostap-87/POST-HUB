---
number: 13
date: "2026-11-13"
lang: "en"
title: "Wheels or Legs: When a Humanoid Needs to Walk and When It Can Just Roll"
seo_title: "Wheeled vs Bipedal Humanoid Robots: Which to Choose for a Factory or Warehouse"
meta_description: "Wheeled and bipedal humanoids compared: stability, battery runtime, arm payload, footprint, price and the tasks where legs are genuinely needed. A comparison from Aura Robotics."
slug: "wheels-or-legs-when-humanoid-needs-walk"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

Say “humanoid” and people picture a metal person: two arms, two legs, a head. The arms and head are uncontroversial. The legs, over the past two years, have become a serious debate, because many Chinese manufacturers now build humanoids that have a wheeled base where the legs should be.

It looks as if the robot rode to work on a scooter and decided not to get off. It is funny right up to the moment you compare battery runtimes.

At Aura Robotics we source humanoids directly from Chinese manufacturers, and “wheels or legs?” comes up in almost every project. Below we go through the parameters that decide it. We are not ranking models; we take one public example from each side to get a sense of the numbers.

### 1. Physics: standing still is work too

A bipedal robot stays upright not because of its shape but because it is constantly controlling its balance. The leg actuators work even when the robot is doing nothing. Cut the power and it falls. A wheeled humanoid on a wide base is statically stable: switch it off and it stays where it is.

Two consequences. Energy: a biped spends part of its charge simply not falling over. Safety: the international standard for robots that stay upright only through active control, ISO 25785-1, is still in development, so the fall scenario near people has to be worked out in your own project.

A biped rests the way a tightrope walker rests. It doesn’t.

### 2. Runtime: two hours versus four

From public specs. Unitree G1, one of the most widespread bipedal humanoids, weighs about 35 kg, carries a 9,000 mAh battery and runs for about 2 hours. The wheeled AgiBot G2 weighs 185 kg, has 1,652 Wh of battery, runs for about 4 hours and has two hot-swappable batteries, so it never needs to be switched off.

Five times the mass is not a flaw of the wheeled robot; it is the design strategy. A heavy base acts as a counterweight and a place for a large battery. A biped cannot do that: every extra kilogram has to be carried and balanced.

Bipedal makers solve this their own way. UBTech has shown Walker S2 swapping its own battery in about three minutes. A good answer, but the swap station, its floor space and the spare batteries belong in the budget.

Wheels never get tired of standing. Legs do, even when nobody asks them to walk.

### 3. Arms: how much the robot lifts

Unitree G1 has a rated arm payload of about 2 kg (about 3 kg for the EDU version), which the maker says varies with arm posture. AgiBot G2 handles 5 kg per arm and 10 kg with both.

That does not mean every wheeled robot is stronger than every biped. It means a stable base lets designers fit stronger arms, because the legs do not have to compensate for their weight. If your box weighs 8 kg, check which robots can lift it at all before arguing about legs.

### 4. Footprint and speed

A wheeled base takes up room. G2’s is 64 × 76 cm, wider than a person’s shoulders. An 80 cm aisle is tight for it, especially with people around. A biped goes wherever a person goes and turns on the spot.

Wheels, on the other hand, are faster and smoother. G2 travels at up to 1.5 m/s, moves sideways and rotates in place. For shuttling between workstations that matters more than climbing stairs the workshop does not have.

Working height does not require legs either: G2’s body height adjusts from 122.5 to 179.5 cm. The robot bends and straightens at the torso instead of squatting.

### 5. Where legs are genuinely needed

Legs make sense where the environment was built for people and nobody is going to rebuild it:

- stairs and steps without ramps;
- thresholds, floor grates, cable covers;
- narrow passages where a wheeled base cannot turn;
- uneven or outdoor surfaces;
- research work where walking itself is the subject.

That last one is where bipeds are strongest today. G1 starts at US$13,500 before tax and shipping, an accessible platform for labs and universities. But a research platform price and an industrial robot price are different things, and comparing them directly is misleading.

### 6. Where legs are surplus

On a flat factory or warehouse floor, where the robot moves between stations, picks parts from a table, places them in totes and tends a conveyor. Here legs add complexity, extra load on actuators and fewer working hours.

A simple test: walk the robot’s route yourself and count the steps. If the answer is zero, you are probably choosing wheels. If there is even one step that cannot be replaced by a ramp, legs.

Legs are for where the floor turns into stairs. Everywhere else it is a matter of taste, and taste is not a budget line.

### 7. One table

| Parameter               | Biped (e.g. Unitree G1) | Wheeled (e.g. AgiBot G2) |
|-------------------------|-------------------------|--------------------------|
| Mass                    | ~35 kg                  | 185 kg                   |
| Runtime                 | ~2 h                    | ~4 h, hot-swap batteries |
| Arm payload             | ~2 kg (~3 kg EDU)       | 5 kg, 10 kg dual-arm     |
| Stairs and thresholds   | yes                     | no                       |
| Stable when powered off | no                      | yes                      |
| Base footprint          | human-sized             | 64 × 76 cm               |

The table illustrates a principle, not a ranking. Models vary widely within each class, and we match them to the task, not to the table.

### 8. Test the unit, not the video

In the videos the biped dances and the wheeled one folds laundry. Your task is probably neither. So we shortlist models for your operation from partner factories, calculate payback, show you the actual unit with its serial number on video from the factory floor and test it on your task before shipment. To see both types working in person, join an Aura Robotics Tour buying trip.

### The bottom line

Nature gave people legs because wheels are useless in a forest. Engineers gave robots wheels because there is no forest in a factory. Both are right. Choose not by which robot looks more human, but by how many steps there are on its route.
