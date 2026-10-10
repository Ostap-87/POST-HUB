---
number: 1
date: "2026-11-01"
publish_time: "15:00"
lang: "en"
title: "Cobots: The Colleague Who Never Argues. How to Choose a Collaborative Robot for the Job"
meta_description: "How to choose a cobot: real payload including the gripper, reach, cycle time, safety, integration costs and a simple payback formula. A practical buyer’s guide from Aura Robotics."
slug: "cobots-colleague-who-never-argues-how-choose"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "b35a1ed4-5435-4346-becb-f203986d6db8"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic documentary photo in a bright small Russian furniture-fittings workshop in the morning: a smiling young woman process engineer with a stopwatch and a clipboard of blank sheets times a cheerful middle-aged worker as he packs metal hinges into small cardboard boxes at a workbench, right beside them a compact white collaborative robot arm stands on a mobile steel cart with a strip of protective film still on it, waiting for its task, soft sunlight from high factory windows, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, practical optimistic mood of describing the job before choosing the robot. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

Most people choose a [cobot](/en/catalog/cobots) the way they choose a car: by the photo, the colour, and whatever the company down the road bought last year. With cars this occasionally works. With robots it does not, because the company down the road almost certainly makes a different part.

At Aura Robotics we source cobots directly from manufacturers in China, and we keep seeing the same pattern. Projects that start with “which robot should we buy?” take longer and cost more than projects that start with “what exactly will it do?” Here is the order in which we suggest thinking. It is not exciting. That is the point.

### 1. Start with the task, not the robot

A cobot is designed to work next to people without a full safety fence. That is both its strength and its limit. Typical jobs: CNC machine tending, end-of-line palletizing, screwdriving, gluing and sealing, sanding, short-run welding, camera-based inspection.

Write the task down as if for a new hire who is very literal and never asks questions. What is picked, from where, placed where, how many times per hour, and what counts as a defect. If it does not fit on one page, you are not automating a process yet. You are automating a mystery.

### 2. Payload: include the gripper

Rated payloads for cobots typically range from 3 to 20 kg, with some models reaching 25–30 kg. Mistake number one is comparing that number with the weight of the part.

The robot carries the part plus the gripper, adapter plate, cables and pneumatics. A 1.5–3 kg gripper is common. Rated payload also assumes a certain centre-of-gravity offset; hold a long part by one end, and the real limit drops.

Rule of thumb: add up the part and all tooling, then add a 20–30% margin. A 4 kg part rarely means a 5 kg cobot. It usually means an 8–10 kg one.

A robot running at its payload limit will not complain. That is exactly why you should not let it.

### 3. Reach and work envelope

Reach runs from roughly 500 mm on compact models to 1,300–1,800 mm on larger ones. Check every point, not just the convenient one: the far corner of the pallet, the top layer, the machine door. Decide where the base goes: a table, a pedestal, a mobile platform or a linear track.

Model the cell in 3D, or at least mark it on the floor with tape. Tape is cheaper than moving a foundation.

### 4. Cycle time and honest safety

A cobot is safe because it limits force and speed when it may contact a person (see ISO 10218 and ISO/TS 15066). The consequence rarely makes the brochure: in collaborative mode, a cobot is slower than an industrial robot.

If you need 30 cycles per minute, you probably need an industrial robot behind a fence. At 2–6 cycles per minute with people nearby, a cobot is ideal. In between, there are compromises, such as area scanners that let the robot speed up when nobody is around and slow down when someone approaches.

And remember that “collaborative” describes the whole cell, not just the arm. Put a sharp gripper or a blade on the flange, and the politest robot in the world becomes a hazard. The risk assessment covers the entire application.

A cobot is exactly as safe as the thing it is holding.

### 5. Precision, protection, environment

Most cobots offer repeatability of around ±0.02–0.05 mm. That is more than enough for machine tending or palletizing. For precise assembly, fixture rigidity and part positioning matter more than the datasheet.

Check the ingress rating. IP54 is fine for a typical workshop; food production with washdown needs IP66–IP67 and food-grade lubricants. Welding and sanding need protection from dust and spatter. A robot bought for a clean room rarely enjoys a real factory floor.

### 6. Where the budget actually goes

The arm is only part of the project. Add the gripper, tooling, vision system, pedestal, safety sensors, programming, commissioning and training. On many projects integration costs about as much as the robot, sometimes more.

Ask about software too: interface language, offline programming, communication with PLCs and machines (Modbus, Profinet, EtherNet/IP and so on), firmware updates, and spare parts availability.

### 7. A simple payback formula

The formula is easy. Putting honest numbers into it is the hard part:

**Payback (months) = total project cost / (monthly savings − monthly maintenance)**

Total cost includes the robot, tooling, integration, shipping and training. Savings include released operator hours (fully loaded), lower scrap, extra shifts, and fewer stoppages caused by staff shortages.

An illustrative example, for arithmetic only. A turnkey cell costs 4 million roubles. The cobot tends a machine over two shifts and frees one operator per shift, each costing the company 120,000 roubles a month fully loaded. Savings are 240,000, maintenance 20,000. Payback: 4,000,000 / 220,000 ≈ 18 months. (Illustrative numbers. Yours will differ, which is the whole reason to calculate.)

Note what is missing: there is no line for “people let go”. The released operator usually moves to work that needs judgement. A cobot replaces the most tedious hours of a shift, not the person working it.

### 8. Test the unit, not the catalogue

A catalogue describes a model. You will be running one specific unit. That is why we show clients the actual robot, serial number included, on video from the factory floor, and test it on the task before shipment. Buying directly from the manufacturer means no warehouse, showroom or importer in the price. It also leaves time to check.

### The bottom line

A well-chosen cobot is an ideal colleague: it does its job, never argues, and never takes credit. A badly chosen one is also a familiar colleague: it stands in the corner while everyone pretends this was the plan.

Start with the task. Weigh the gripper. We will help with the rest of the maths.
