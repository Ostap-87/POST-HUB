---
number: 2
date: "2026-11-02"
lang: "en"
title: "Spec First, Video Later: How to Define the Job Before You Choose a Humanoid"
seo_title: "How to Choose a Humanoid Robot: Writing the Spec Before Picking a Model"
meta_description: "How to write a requirements spec for a humanoid robot: the task, real payload, environment, battery runtime, hand dexterity, training data and service. A method from Aura Robotics."
slug: "spec-first-video-later-how-define-job"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

Most humanoids today are chosen from videos. In the video the robot does a backflip, folds a T-shirt, dances with the presenter and pours coffee. All of it is real. What the video leaves out is how many takes came first, how much the footage was sped up, and who was standing off-camera holding the controller.

A video shows what a robot can do. A spec shows what it will do for you. These are different genres, rather like a wedding photo and a marriage.

At Aura Robotics we source humanoids directly from manufacturers in China, and our first conversation with a client is almost never about a model. It is about the job. Here is the order in which we work through it. There are no model comparisons below; they go out of date faster than they can be written.

### 1. One task, specific and boring

Start with one operation, not a job title. “The robot will work as a warehouse operative” is not a spec. It is a hope. “The robot picks an empty plastic tote from a shelf at 1.2 m and places it on a conveyor, 200 times per shift” is a spec.

That is exactly the kind of work humanoids are doing today. The most cited commercial deployment is the multi-year Robots-as-a-Service agreement between GXO and Agility Robotics (June 2024): Digit moves totes from cobots onto conveyors. It does not cook, sell or chair meetings. It carries totes.

A humanoid with one clear job works. A humanoid with ten jobs poses.

### 2. Payload, and where it is held

Humans lift things with two arms, so we assume a human-sized robot can too. The numbers are more modest than the height suggests.

From a public spec sheet: Unitree G1 has an arm payload of about 2 kg, about 3 kg for the EDU version, and the manufacturer notes it varies considerably with arm posture. Industrial models from other makers lift more, but the principle holds: rated payload assumes a convenient pose, not the far end of a shelf.

So the spec should state the mass and size of the heaviest item, the pick and place heights, and the distance from the robot’s body. If the load exceeds the rating, no model will help. A trolley will.

### 3. Environment: floors, aisles, people

Legs let a robot go where people go: stairs, thresholds, narrow aisles. You pay for that in complexity and price, so describe the route as carefully as you would for a forklift: floor type, slopes, steps, grates, wet areas, aisle widths, people nearby, night lighting.

On safety: the international standard for robots that stay upright only through active control, ISO 25785-1, is still in development. Write down whether the robot will work among people or in a fenced zone. That decides how falls, stops and speed near humans are handled.

If there are no stairs on the route, ask honestly whether you need legs at all. The same arm on a wheeled base may be cheaper and steadier. Legs belong where nothing else will do, not where they look more impressive.

### 4. Runtime: the shift versus the battery

This is the part videos never show.

As a reference point, Unitree G1 has a 9,000 mAh battery and runs for about 2 hours. An eight-hour shift therefore means at least four swaps or charges, and a spare battery is one more thing to buy, store and charge. Include the minutes spent walking to the charger.

Manufacturers solve this differently. UBTech has shown Walker S2 swapping its own battery in about three minutes, with no human involved. A good answer, but the station, its floor space and the extra batteries belong in the budget.

Specify how many hours a day you need, whether pauses are acceptable and where the charger will physically sit. A humanoid that works for two hours and charges for ninety minutes is not a full-time employee. It is a part-timer who also runs late.

### 5. Dexterity: what the hand actually does

Humanoid hands range from simple two-finger grippers to multi-finger hands with force sensing. G1, for instance, offers an optional three-finger Dex3-1 hand with 7 degrees of freedom and force control. Every finger adds capability, cost and one more thing to break.

List concrete actions: lift a tote by its handles, press a button, turn a valve, plug in a connector, open a door. If everything comes down to “pick and place”, you probably do not need a dexterous hand. Soft or small items are a different story.

### 6. Data and training: who teaches the robot

Modern humanoids learn from data: teleoperation, demonstrations, simulation. That brings work a cobot budget never had: collecting examples, labelling them, fine-tuning for your site.

Ask early: who collects the data, you or the manufacturer? Is there an open SDK? Can skills move between units? What happens to a trained model after a firmware update? Ask “how will it learn?” before “how much is it?”, because the first answer often changes the second.

### 7. Service: six months later

A humanoid is a complex machine with dozens of actuators. Ask about spare parts and lead times, remote diagnostics, update frequency, what can be repaired on site and what goes back to the factory, and training for your engineer.

### The one-page spec

Compressed, it all comes down to ten questions:

1.  What single task, and how many times per shift?
2.  Mass, size and height of the heaviest item?
3.  What route: floor, slopes, thresholds, stairs?
4.  Among people or in a fenced zone?
5.  How many hours a day, and where is the charger?
6.  What does the hand do?
7.  How does the robot get tasks and report back?
8.  Who trains it, and on what data?
9.  Which spare parts stay on site?
10. What number, three months in, tells us the project worked?

The last one is usually forgotten. That is how pilots become permanent.

### Test the unit, not the showreel

With the spec in hand, we shortlist models from partner factories, calculate payback, show the client the actual unit with its serial number on video from the factory floor, and test it on your task before shipment. Better still, see it in person on an Aura Robotics Tour buying trip.

### The bottom line

You can watch humanoid videos forever. You will work with the spec. And sometimes the most valuable thing a good spec produces is an honest “not yet”. That saves money too, and it does so immediately.
