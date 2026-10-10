---
number: 10
date: "2026-11-10"
publish_time: "15:00"
lang: "en"
title: "The Inspection Round That Never Happened: How to Calculate Payback on an Inspection Robot for Substations and Industrial Sites"
seo_title: "Substation Inspection Robots: ROI, Thermal Imaging and the Cost of a Missed Fault"
meta_description: "How to assess payback on an inspection robot for substations and industrial sites: consistent rounds, thermal imaging, cold-weather limits and the cost of a missed fault. Lessons from China and an illustrative calculation."
slug: "inspection-round-that-never-happened-how-calculate"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "a8707a5d-57aa-44da-a9f1-37dd0ab6a796"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic documentary photo at a Russian electrical substation on a crisp sunny winter morning: a wheeled outdoor inspection robot with a pan-tilt thermal camera mast rolls along a gravel path between transformers and busbar structures covered in hoarfrost, its camera pointed at a busbar connection, in the background an electrician in an orange insulated jacket with a thermos gives it a thumbs-up, long blue morning shadows and glittering frost, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, reassuring mood of a round that never gets skipped. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

Equipment rounds are the most tedious job at a substation. Someone walks a route, reads gauges, listens to a transformer, and writes it all down. When everything is fine, which is nearly always, the round looks like wasted time.

You only see the value of a round when it did not happen. A freezing night, someone decides “we checked yesterday”, and the busbar joint that has been heating up for a week picks that very night.

The payback of an inspection robot is not measured in rounds completed. It is measured in failures that never occurred. Here is how to put a number on that, and where a robot genuinely makes sense.

### 1. What is happening in China

Chinese grid operators have moved from pilots to procurement. According to Interesting Engineering, citing Jiemian and the South China Morning Post, State Grid Corporation of China plans to buy around 8,500 robots in 2026: roughly 5,000 quadrupeds, 3,000 wheeled dual-arm robots and 500 humanoids, with a 2026 budget of 6.8 billion yuan. The tasks: patrolling remote substations and mountain terrain, monitoring the network, working in hazardous areas. It is a plan, not a result, but the scale speaks for itself.

On the ground: at a 220 kV substation in Linyi, Shandong province, [Deep Robotics](/en/catalog/quadruped/factory/deeprobotics) deployed a LYNX M20 wheel-legged robot for fast patrols alongside an X30 quadruped for close-up thermal imaging. The company reports that the inspection cycle was cut by two-thirds.

### 2. What is happening in Russia

In Russia the subject is on the agenda, though still at the development stage. In August 2025, CNews reported that Rosseti Kuban had commissioned a mobile robotic system for 110 kV outdoor switchyards. It is meant to diagnose equipment in the visible, infrared and acoustic ranges, flag defects automatically, and carry out switching operations under operator supervision. The company cited ageing infrastructure (more than 70% of equipment running past its rated service life) and staff shortages. The project is scheduled to take 27 months.

Old equipment and too few people. That is exactly the combination in which a patrol robot pays back fastest.

### 3. Why consistency beats heroics

Thermal imaging is the main tool for finding overheating joints, and it comes with a subtlety every thermographer knows. Russia’s guidelines for infrared diagnostics of electrical equipment (RD 153-34.0-20.363-99) note that the temperature of a joint is proportional to the square of the current. Readings should therefore be compared at similar loads.

A person who walks the route whenever they can takes readings at different loads each time, which makes comparison hard. A robot walks the same route at the same hour, to the same points, from the same angle. A month later you do not have a pile of snapshots; you have a time series, and it shows which joint is slowly creeping upwards.

An inspection robot is not valuable because it sees better than a person. It looks the same way every time, which is how it notices when something has changed.

### 4. Engineering limits: frost, ice, batteries

Honesty matters here. The Deep Robotics X30 is rated IP67, operates from −20 to +55 °C, runs for 2.5–4 hours and climbs stairs and slopes up to 45°. The manufacturer itself notes these are laboratory figures.

On many Russian sites, winter goes another 10–20 degrees below −20 °C. So the project must answer: where does the robot live between rounds (a heated enclosure with a charging station), how many rounds are needed in winter, what happens with ice and snow on the route, and how many rounds fit into one charge. A wheeled robot on a level site is cheaper and more durable; a legged one earns its keep where there are stairs, cable trenches and kerbs. For indoor switchgear, Chinese utilities have long used rail-mounted robots: no legs, and no question of how to climb a step.

Choose the robot that will survive your January, not the most agile one.

### 5. An illustrative calculation

All figures are illustrative.

**Part one: people’s time.** Three rounds a day, 1.5 hours each, about 1,640 hours a year. At a fully loaded 1,000 roubles an hour, that is about 1.6 million roubles a year. A robot with station, heated enclosure, thermal camera, integration with the monitoring system and training costs around 10 million roubles, plus 0.4 million a year in maintenance. On labour alone, payback takes more than eight years.

This is where many projects are shelved. Wrongly, because it is only half the calculation.

**Part two: the missed fault.** Suppose a failure caused by an overheating joint costs this site 20 million roubles: equipment repair, undelivered energy, contractual penalties, the emergency crew. If, without regular inspection, such a failure happens on average once every seven years, and the robot catches the defect in time, the expected saving is about 3 million a year. Add the labour saving and subtract maintenance: 4.2 million a year. Payback in about 2.5 years.

Every site will have its own numbers. What matters is a new line in the calculation: the cost of the round that never happened.

For remote and unmanned substations the case is stronger still. There, the expensive part is not the round but the drive: sending a crew dozens of kilometres to look at a pressure gauge.

### 6. Where you do not need a robot

A small urban substation that already has staff on duty. A site where fixed thermal cameras already watch the key components: sometimes a couple of fixed sensors are cheaper and more reliable than a mobile robot. A site where the route changes every week because of construction.

A robot pays back where rounds are long, regular, unpleasant or dangerous, and people are scarce. If at least two of these are missing, check your numbers carefully.

### 7. How we approach a project

At Aura Robotics we source inspection robots, legged and wheeled, directly from Chinese manufacturers. We start with the route, the climate and the list of faults you need to catch, and choose the model afterwards. We show the actual unit on video from the factory floor, serial number included, and test it on the task before shipment.

### The bottom line

A lineman who has listened to transformers for thirty years can hear more than any microphone. A robot cannot do that. But it will turn up at exactly three in the morning, in frost or rain, and look at the same joint it looked at yesterday.

Nobody notices the failure that did not happen. That is precisely the job.
