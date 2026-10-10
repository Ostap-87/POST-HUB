---
number: 53
date: "2026-12-23"
publish_time: "15:00"
lang: "en"
title: "The Unheated Workshop: Robots, Frost and the Letters IP on the Nameplate"
seo_title: "Robots in Unheated Plants and Outdoors: IP Ratings, Temperature, Condensation and Batteries"
meta_description: "How to run robots in cold workshops, outdoors and in washdown areas: IP codes explained (IEC 60529), operating temperatures of cobots and robot dogs, condensation and charging batteries in the cold."
slug: "unheated-workshop-robots-frost-letters-ip-on"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "4ed08d9f-54eb-427e-91fa-eb9cadda84c3"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic industrial photo in an unheated Russian workshop in winter: a collaborative robot arm wearing a fitted grey protective cover works at a bench loading parts, frost patterns on the old windows, breath visible in the cold air, a smiling worker in a padded jacket and knitted hat checks the robot, a small heater glowing near the control cabinet, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, sturdy cheerful mood of a robot ready for frost. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

Robot datasheets are usually written in a warm office. You can tell from the “operating temperature” line: 0 to 50 °C. In Shenzhen that covers most of the year. In an unheated Russian warehouse it covers roughly half of it, and not the half you need.

At Aura Robotics we source robots directly from Chinese factories, and “will it survive our plant?” comes up almost as often as “how much is it?” Here is how to read a datasheet with the environment in mind, and what happens when the datasheet and the shop floor disagree.

### 1. What the IP code means

Enclosure protection is expressed as IP plus two digits, defined internationally by IEC 60529 (in Russia, GOST 14254-2015, in force since March 2017).

**First digit: solids and dust.** For robots the top two levels matter: 5 means dust-protected (some dust may enter, but not enough to interfere), 6 means dust-tight.

**Second digit: water.** 4: splashing from any direction. 5: water jets. 6: powerful jets. 7: temporary immersion. 8: continuous immersion. 9: high-pressure, high-temperature jets, which is what sanitary washdown actually involves.

The digits are not a simple quality ladder. IP67 survives immersion, but that does not mean it survives a hot high-pressure wash. They are different tests. If your plant cleans with foam and hot pressurised water, look for that specific protection, not just a big number.

IP ratings also differ between parts of one system. A Universal Robots UR10e arm is IP54; its control box is IP44. The arm can handle splashes; the cabinet should be kept away from them. Always check the controller, pendant and charging station, not just the arm.

An IP rating is a promise made in a laboratory. The workshop was not informed.

### 2. Temperature: read the lower limit

Most industrial cobots are rated at roughly 0 to 50 °C. The UR10e: 0–50 °C, up to 90% humidity, non-condensing. The lower limit matters more: workshops rarely reach 50 °C in summer, but an unheated building can drop below zero overnight.

Outdoor robots have wider ranges. [Deep Robotics](/en/catalog/quadruped/factory/deeprobotics) says its X30 inspection quadruped operates from −20 to +55 °C and is rated IP67, while noting these are laboratory figures. The popular consumer Unitree Go2, by contrast, lists +5 to +35 °C in its manual, “optimal in fair weather”. They look like cousins. In winter they live in different climate zones.

A robot dog for trade shows and a robot dog for winter substation rounds are different purchases, even if you cannot tell them apart in a photo.

### 3. Condensation: the thaw is worse than the frost

A robot spends the night in a cold building and is moved into a warm one in the morning. Dew forms on the cold metal. You can see it on the outside. You cannot see it inside connectors and boards. “Non-condensing” in the datasheet means exactly that: condensation is outside normal operating conditions.

What helps:

- Do not move a cold robot into a warm room and switch it on immediately. Let it reach room temperature while powered off.
- Keep control cabinets powered or in a heated enclosure where temperatures swing sharply.
- For permanent cold operation, choose versions with heated electronics. Makers of cold-store AMRs regulate the temperature of key electronics to prevent condensation and icing; such machines are designed for operation down to about −25 °C.

Winter threatens a robot twice: when it arrives and when it leaves.

### 4. Batteries in the cold

For mobile robots, humanoids and robot dogs, winter is mostly a lithium-ion question.

Li-ion batteries can discharge across a wide range, roughly −20 to +60 °C, though capacity drops in the cold. Standard Li-ion cells must not be charged below freezing: metallic lithium plates onto the anode, permanently reducing capacity and safety. The charge may look perfectly normal while it happens. The best charging range is 10–30 °C.

So the charging station and spare battery storage belong in a heated room, even if the robot works in a cold one. The robot can go out into the frost. It should charge at home.

Also plan shifts around reduced runtime: a cold battery delivers less than the datasheet. How much less depends on the model and temperature, so ask the manufacturer or test it.

### 5. Dust, water, washdown: what you actually meet

**Dust.** Woodworking, cement, flour, metal chips. For an arm, first digit 5 or 6. For mobile robots, lidar and camera windows are the weak spot: dust on a sensor turns a smart robot into a blind one. Sensor cleaning belongs in the maintenance schedule, not in hope.

**Water and washdown.** Food plants need high protection classes, smooth or stainless housings and food-grade lubricants. The alternative is a protective cover. Covers exist for many arm models, but they have their own costs: they can restrict motion, impair cooling and need replacing and washing themselves. Check with the manufacturer that operation under a cover is permitted.

**Outdoors.** Sun, rain, snow, ice. For wheeled and legged robots, slopes, steps and slippery surfaces join the IP question. A wheeled robot that glides over epoxy flooring may spin helplessly on a snowy ramp.

### 6. How to check before buying

1.  Describe the environment honestly: minimum and maximum temperature, humidity, swings, dust, washdown, outdoor use.
2.  Check the IP rating of every component: arm, cabinet, pendant, charger, tooling.
3.  Ask for separate lower limits for operation, storage and charging.
4.  Ask whether a cold or washdown version exists.
5.  Where possible, test the robot in conditions close to yours before shipment.

### How we help

We source robots directly from more than 100 Chinese manufacturers and select models for the real site, not for office conditions. We show the actual unit, serial number included, on video from the factory floor and test it before shipment. One team handles the project from selection to launch.

### The bottom line

A robot never complains about the cold. It just starts doing strange things, and then stops doing anything. A person in that state at least asks for a cup of tea.

When choosing a robot for a cold plant, read the datasheet from the bottom up: the lower temperature limit first, everything else after.
