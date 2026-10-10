---
number: 6
date: "2026-11-06"
lang: "en"
title: "Gripper First, Robot Second: How to Choose End Effectors and Machine Vision"
seo_title: "Robot Grippers and Machine Vision: How to Choose Tooling for the Task"
meta_description: "How to choose a gripper for an industrial robot or cobot: vacuum or mechanical, calculating suction cup holding force, 2D and 3D cameras, lighting and testing on real parts."
slug: "gripper-first-robot-second-how-choose-end"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

A robot without a gripper is a very precise hand with no fingers. It can deliver thin air to any point in space to within hundredths of a millimetre. Impressive, and not much use.

Yet grippers and cameras are almost always chosen last. First comes the debate about the robot model, the budget, the delivery schedule, and only then does someone ask: “So what will it pick things up with?” At Aura Robotics we source robots and tooling from Chinese factories, and we see projects succeed or fail right here. The robot usually copes. What is on its flange often does not.

Here is the order we recommend: the part first, then the gripper, then vision, and only then the robot.

### 1. Start with the part, preferably the worst one

Collect samples: not one perfect specimen but every variant your shop floor actually produces. A crushed case, an oily part, a wet bag, a blank with a burr, the neighbouring SKU that looks almost the same.

For each, record mass, dimensions, material, surface (smooth, porous, oily, wet), how it arrives (in a fixture, loose in a bin, on a conveyor) and where it goes, to what accuracy.

Design the gripper for the most awkward part. The easy ones will take care of themselves.

### 2. Types of gripper

**Vacuum.** Suction cups or foam vacuum grippers. Good for cases, sheets, glass and smooth parts. Struggles with mesh, perforations and very porous materials unless the vacuum generator has plenty of airflow in reserve.

**Mechanical.** Two-finger parallel or three-finger centring, pneumatic or electric. Electric grippers allow force and stroke to be set in software, which helps with several SKUs. Fingers are almost always custom-made for the part, and that is fine.

**Magnetic.** For steel sheet and blanks. Fast and simple, but ferromagnetic materials only, and watch out for residual magnetism.

**Soft.** Flexible fingers for fragile or irregular items: baked goods, fruit, film-wrapped packs. In food production, food-contact materials and washdown matter.

A good gripper looks boring. If it looks like a work of art, it will probably be a work of art to repair.

### 3. Vacuum: calculate, don’t hope

Suction cup holding force is calculated, not guessed. Vacuum specialist Schmalz publishes a clear method. With the cup horizontal and the robot lifting vertically:

**F = m × (g + a) × S**

where m is part mass, g is 9.81 m/s², a is the robot’s acceleration and S is the safety factor. Schmalz recommends at least 1.5 for smooth, dense parts and 2 or more for porous, rough, oily or uneven ones.

It gets interesting when the robot moves the part sideways quickly. Then friction joins the vacuum, and the formula gains a friction coefficient μ:

**F = m × (g + a / μ) × S**

Reference values: about 0.5 for metal, glass and wood; 0.2–0.3 for wet surfaces; 0.1–0.3 for oily ones.

An illustrative example. A 5 kg case, 5 m/s² acceleration, safety factor 1.5. Lifting vertically needs 5 × (9.81 + 5) × 1.5 ≈ 111 N. Moving sideways with μ = 0.5: 5 × (9.81 + 10) × 1.5 ≈ 149 N. The same case, wet (μ = 0.25): 5 × (9.81 + 20) × 1.5 ≈ 224 N. Same mass, twice the force.

The lesson: choose the cup for how fast and in which direction the part travels, not just for its weight. Or reduce acceleration if the part slips. A robot running slower than its datasheet in testing is often not a defect but a correctly calculated gripper.

### 4. Machine vision: when you really need it

You need a camera when parts do not arrive in the same place every time: loose in a bin, randomly oriented on a conveyor, mixed cases on a pallet. Cameras also handle quality inspection and code reading. If the part always sits in a fixture, you may not need vision at all. A good fixture is cheaper than a good camera and never needs calibrating.

If you do need vision:

**2D cameras** locate a part on a plane when its height is known: on a conveyor, a table or a flat layer.

**3D cameras** (structured light, stereo, time-of-flight) produce a point cloud and are needed for bin picking, mixed-case de[palletizing](/en/catalog/palletizing) and complex shapes. Chinese manufacturers such as Mech-Mind and Hikrobot offer such systems for industrial use.

The typical 3D problems are well known. Small parts packed densely merge into one cloud. Shiny, polished and machined metal creates reflections and distortions in the point cloud, so the gripper misses. A badly placed camera casts shadows near bin walls, and parts in the corners become invisible.

### 5. Lighting: the underrated half of vision

A camera does not see the part. It sees light reflected from the part, so lighting matters as much as resolution.

Ask: does sunlight from a window reach the area (morning and evening images will differ)? Does the overhead lighting flicker? Is there glare from nearby equipment? Often the right answer is to enclose the area and add dedicated lighting. It is a cheap measure that removes expensive failures.

If you tuned a vision system by day, test it at night. And vice versa.

### 6. Budget: chosen last, but not cheap

Gripper, vacuum system, cameras, lighting, programming and recognition setup are a substantial part of the cell’s cost. In projects with complex vision they can rival the price of the robot itself. Include tooling from the first payback calculation, not as “we’ll buy it later”.

Ask your supplier who designs the fingers, what wear parts (cups, pads) cost, how quickly the gripper can be changed over for a new SKU, and who will train recognition for new parts.

### 7. Test on your parts

No datasheet replaces a test. Send the manufacturer samples, the worst ones included, and ask to see a series of picks, not one lucky take. A good question: how many picks out of a hundred succeeded, and what happened to the rest?

That is how we work: we select the robot, gripper and vision directly at Chinese factories, show you the actual unit with its serial number on video from the factory floor, and test the cell on your task before shipment. To see tooling at work in person, join an Aura Robotics Tour buying trip.

### The bottom line

The usual order is: choose the robot, then the gripper, then discover the part is slippery. We suggest the reverse: pick up the part yourself, choose what the robot will hold it with, and only then choose the robot. The robot comes last in this chain. But it is also the only one that will never say “I told you so”.
