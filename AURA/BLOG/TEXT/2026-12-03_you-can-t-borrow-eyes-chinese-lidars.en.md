---
number: 33
date: "2026-12-03"
lang: "en"
title: "You Can’t Borrow Eyes: Chinese Lidars and Depth Cameras Inside Your Robot"
seo_title: "Lidars and Depth Cameras for Robots: Hesai, RoboSense, Livox and Orbbec Explained"
meta_description: "Which Chinese lidars and 3D cameras ship in mobile robots, humanoids and robot dogs, how 2D lidar differs from 3D, how dust, sunlight and glass confuse sensors, and what to ask before you buy."
slug: "you-can-t-borrow-eyes-chinese-lidars"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

Robots are usually judged by their legs, their arms and their price. The eyes come as standard, and nobody thinks about them until the robot politely stops in front of a glass door it insists is not there. Or refuses to drive past a patch of sunlight.

We have covered how robots navigate before: lidar, QR codes, floor markings. This piece is about the sensors themselves: what the little boxes on Chinese robots are, who makes them, and which lines of their spec sheets deserve attention before you buy.

### Who makes the eyes

A few years ago lidar was an expensive toy for self-driving cars. Today it goes into lawn mowers.

China’s two largest lidar makers, Hesai and RoboSense, grew up in automotive and are moving fast into robotics. In Q2 2025 Hesai shipped 49,000 robotics lidars (8.4 times a year earlier) and RoboSense 34,400. In April 2025 Hesai agreed to supply 300,000 JT-series units to Dreame for robotic lawn mowers. In the first half of 2026 RoboSense sold 282,600 robotics lidars, up 510% year on year, and describes itself as the world’s number one in the segment.

The third notable name is Livox, whose Mid-360 sits, for example, in the head of the Unitree G1 [humanoid](/en/catalog/humanoid). Orbbec is a major supplier of depth cameras for robots.

The good news for buyers: a Chinese robot almost certainly sees the world through Chinese eyes. A spare sensor comes from the same supply chain, not from a hunt for a discontinued camera on another continent.

### 2D and 3D: a slice versus a space

A 2D lidar scans a single horizontal plane, like a lighthouse beam. It sees rack legs, walls and trolley wheels at its mounting height. Anything above or below does not exist for it, so a floor-level 2D lidar will not notice forklift tines at chest height. That is not a flaw. It is geometry.

A 3D lidar sees volume. The Hesai JT128 covers 360° horizontally and 189° vertically, a little more than a hemisphere, and weighs 265 g. The Livox Mid-360 covers 360° by −7° to 52°, ranges to 40 m on 10%-reflective targets, produces 200,000 points per second and is rated IP67. A sensor like this lets a robot notice an overhanging load, a step or a platform edge.

A 2D lidar answers “where am I?”. A 3D lidar answers “what is around me?”. A depth camera answers “what exactly is that in front of my nose?”

That is why many robots carry several: lidar for navigation, a camera for the near field and for manipulation.

### Depth cameras: close and detailed

A depth camera, stereo or structured-light, builds a 3D picture of what is right in front of the robot. It is cheaper than lidar, adds colour to depth, and matters wherever the robot picks things up rather than just driving.

Take the Orbbec Gemini 335: a working range from 0.1 m to 20 m and beyond, but an optimal range of 0.26 to 3 m. That is the honest zone: a few metres. It operates from −10 to +45 °C, is rated IP5X for dust, and is specified for both darkness and outdoor use thanks to combined active and passive stereo.

The “20 metres” on a depth camera spec sheet is a bit like a car’s top speed in a city: true, and of no practical use.

### What dust, sunlight and glass do

Now for what the box does not say.

Glass and mirrors. A laser passes through clear glass or bounces off mirrored surfaces. The robot either misses the glass partition or sees a phantom corridor in the reflection. The fix is organisational: frosted film or a stripe on the glass, or a no-go zone on the map.

Black and shiny. Dark matte surfaces absorb the beam and cut range, which is why lidar range is quoted separately for 10% and 80% reflectivity: 40 m and 70 m for the Mid-360. Black pallet wrap and polished stainless steel are old enemies.

Sunlight. Bright light floods the receiver and the camera. Lidars are tested against ambient light (the Mid-360’s range is quoted at 100,000 lux), but test the robot at your own dock doors on a sunny day.

Dust, steam, snow. Airborne particles return false points, and a robot may stop in front of a dust cloud it takes for a wall. In abrasive environments and wash areas, check the sensor’s protection rating and how often the window needs wiping.

Cold. The Mid-360 runs down to −20 °C and self-heats below freezing; the Gemini 335 is rated to −10 °C. In an unheated warehouse that is a limit, not a margin.

The most honest sensor test is not in a lab. It is at your loading dock on a bright January morning.

### What to ask before you buy

1.  Which sensors are fitted: lidar model, camera model, how many and where?
2.  Is any sensor a certified safety scanner, or is it navigation only? These are different things, and safety is a separate article.
3.  What temperature range and protection rating do the sensors have, not just the robot?
4.  Can a sensor be replaced on site, and what does a spare cost?
5.  How does the robot behave near glass, in sunlight and in dust? Is there video from a similar site?

We always ask the factory that last question. We buy directly from Chinese manufacturers, calculate payback, show the client the actual unit with its serial number on video, and test it before shipment, where possible in conditions close to yours. To see the sensors working in person, join an Aura Robotics Tour buying trip.

### The bottom line

A robot does not see the world. It sees a point cloud. Sometimes the cloud is more accurate than the world, sometimes the other way round.

Our job is to keep the “sometimes” to a minimum in your warehouse. And do put a stripe on that glass door. People notice it better too.
