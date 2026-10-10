---
number: 15
date: "2026-11-15"
publish_time: "15:00"
lang: "en"
title: "Lidar or QR Codes: The Robot That Remembers the Way and the Robot That Reads the Signs"
seo_title: "Warehouse Robot Navigation: Lidar SLAM or Floor QR Codes?"
meta_description: "How warehouse robots find their way: floor QR codes, laser SLAM and reflectors. Accuracy, floor requirements, the cost of changing routes, and where each approach wins. A guide from Aura Robotics."
slug: "lidar-or-qr-codes-robot-that-remembers"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "53edfbd6-7d5c-465d-a75a-128329a86f17"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic low-angle photo at floor level in a bright warehouse: a small flat orange warehouse robot rolls over a neat grid of small square black-and-white fiducial floor markers, sharp in the foreground, while in the soft-focus background a second mobile robot with a dome lidar sensor glides past tall racks that two warehouse workers are cheerfully rearranging with a forklift, cool white light and long floor reflections, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, clever orderly mood of two ways a robot finds its way. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

There are two ways to find your way around an unfamiliar city. One is to read the street signs and house numbers. The other is to remember: right after the pharmacy, left at the statue. The first works as long as the signs are there. The second, as long as nobody moves the statue.

Warehouse robots navigate in exactly these two ways. Some read codes on the floor. Others build a laser map of the building and recognise it by the outline of walls, columns and racks. The debate looks technical, but it is usually settled not by IT but by whoever is in charge of rearranging the warehouse.

At Aura Robotics we source warehouse robots directly from Chinese manufacturers. We have a separate guide on choosing between [AGVs](/en/catalog/agv) and AMRs. Here we go deeper into one question: how a robot knows where it is, and what it costs to explain that again.

### 1. Reading codes on the floor

A robot with QR-code navigation (more precisely, 2D codes: QR, DataMatrix or a maker’s own markers) looks down with a camera. Codes are stuck to the floor at regular intervals, each one representing exact coordinates. Between codes the robot relies on wheel odometry and an inertial unit, and corrects its position at each code.

The best-known example is Kiva, which Amazon bought in 2012 for US$775 million. Its drive units read floor codes with a downward camera and codes under the rack they lift with an upward one. Since then, goods-to-person on a code grid has become standard, and Chinese manufacturers now make a great many such machines.

### 2. Remembering the outline

A robot with laser navigation by natural features (laser SLAM) scans the building with a lidar and builds a map. At work it compares what it sees with the map to determine its position. Nothing is stuck to the floor; routes are drawn in software.

There is an in-between option: laser navigation with reflectors. Reflective targets go on walls and columns, and the robot triangulates from them. Accurate and tolerant of changing surroundings, but the reflectors must be installed and the robot needs to see at least three at all times.

And there is visual SLAM: the same idea, with a camera instead of a lidar. Cheaper sensors, more sensitive to lighting.

### 3. Often it is the same robot

Buyers often think they are choosing between two kinds of machine. In practice many makers offer one platform with different navigation. Hikrobot’s Q-series lifting robots, for example, list QR code, laser SLAM and visual SLAM options, with the same stated positioning accuracy: ±10 mm and ±1°.

So navigation is chosen for your warehouse, not for the model. The robot will accept either option. Your warehouse might not.

### 4. What codes do well

**Predictability.** The robot always knows which square it is on. Hundreds of machines on one grid run like a timetable.

**Empty halls.** Laser SLAM needs landmarks. In a vast uniform hall with identical racks or open space, it has nothing to hold on to. Codes do not care what is around them.

**Sensor cost.** A floor-facing camera is simpler and cheaper than a lidar.

The downsides are just as clear. The floor must be prepared: codes go on a flat, clean surface. They wear under forklift wheels and dirt, and need checking and replacing. Above all, a new route means new codes. Every new street needs new signs.

### 5. What lidar does well

**Flexibility.** Routes change with a mouse. A new dispatch zone is a day of an engineer’s work on the map, not a week of a crew with a tape measure.

**Mixed traffic.** The lidar also sees obstacles, which matters where people and forklifts share the space.

**Untouched floors.** Nothing to stick, nothing to wear off.

The downsides. Lidar gets confused when the surroundings change too much: pallets that stood along the wall yesterday are in the aisle today, and the room no longer looks familiar. Long identical corridors and glass are awkward too. Dust on the optics reduces accuracy, so the sensor needs cleaning. And a lidar costs more than a camera.

A code robot is lost when a marker wears off. A lidar robot is lost when someone moves the furniture. People, incidentally, suffer from both.

### 6. What changing the layout costs

This is the key question, and it should be answered over several years. For arithmetic only.

A warehouse reorganises a 2,000 m² picking zone once a year before peak season. With code navigation, assume (illustratively) one marker per square metre, and a quarter of them need to be removed and re-laid: 500 markers. At 300 roubles per marker including layout and checking, plus two days at reduced capacity, that is 150,000 roubles of work plus lost throughput.

With laser SLAM, the same change is a map and route update: say one or two days of an engineer’s time plus test runs. Noticeably less, though not zero.

If the layout stays the same for years, the maths flips: the codes are laid once, and cheaper camera-based robots pay back faster, especially in large fleets. (Illustrative numbers. Yours will differ, and that is fine.)

Choose navigation not for the warehouse you have, but for the number of times it will change during the robot’s life.

### 7. A simple rule

Codes if: goods-to-person, a dense grid, many robots, a layout stable for years, no people inside the robot zone.

Lidar if: long routes through different zones, people and forklifts nearby, a layout that changes with the seasons, a floor you cannot touch (leased premises, special coatings).

Hybrid if: a stable grid in one part of the warehouse and free routes between zones. Many manufacturers offer hybrid navigation, with the robot switching methods zone by zone, and that is often the best answer.

### 8. What to ask the supplier

1.  Which navigation options does this platform offer, and can they be combined?
2.  What are the floor flatness and surface requirements?
3.  How often do codes need checking or the lidar cleaning?
4.  How long does a route change take, and who does it: us or you?
5.  What does the robot do when it does not recognise a place or cannot see a marker?
6.  What is the stopping accuracy at a station, and under what conditions is it specified?

### 9. Test the unit, not the catalogue

We match robots and navigation to your warehouse from partner factories, calculate payback including future layout changes, show you the actual unit with its serial number on video from the factory floor and test it before shipment. You can see both approaches running in real Chinese warehouses on an Aura Robotics Tour buying trip.

### The bottom line

A code robot is like a meticulous accountant: everything in neat squares, and panic if one square is erased. A lidar robot is like an experienced driver: it will find a way anywhere, unless every road is closed at once. A warehouse needs both temperaments. Just don’t hire the accountant for a building that gets renovated every spring.
