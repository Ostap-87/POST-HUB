---
number: 3
date: "2026-11-03"
lang: "en"
title: "AGV or AMR: How to Choose Warehouse Robots Without Rebuilding the Warehouse"
seo_title: "AGV vs AMR: How to Choose a Mobile Robot for Your Warehouse"
meta_description: "AGV vs AMR explained for buyers: load type, navigation, floor requirements, doors and lifts, safety under ISO 3691-4, WMS integration and a simple formula for fleet size."
slug: "agv-or-amr-how-choose-warehouse-robots"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

There are two ways to automate material transport in a warehouse. One is to choose a robot and then rebuild the warehouse around it. The other is to look at the warehouse first and then choose the robot. The first is more popular. The second is cheaper.

At Aura Robotics we source warehouse robots directly from Chinese manufacturers, and the “AGV or AMR?” debate almost always starts at the wrong end. People argue about navigation, then discover a threshold at the dispatch area and a door that only opens by hand. Here is a better order of questions.

### 1. The short version

An **AGV** (automated guided vehicle) follows a defined path: magnetic tape, inductive wire, floor QR codes or reflectors. It is predictable, docks precisely and loves repetitive routes. The price is rigidity: a new route means new markings.

An **AMR** (autonomous mobile robot) navigates by a map of the building, usually with lidar and cameras, plans its own path and drives around obstacles. It is more flexible: new routes are drawn in software, not on the floor. But it is less predictable in tight spaces and needs a stable environment for its map.

The line between them has blurred; many machines do both. So the real question is not “AGV or AMR?” but “how often will routes change, and how crowded will they be?”

If your layout stays the same for years, a fixed route is a feature. If it changes every season, a fixed route is an annual renovation.

### 2. The load decides the machine

Load type rules out half the options before navigation even comes up. Pallets mean autonomous stackers and forklifts, from hundreds of kilograms to tonnes. Mobile racks for goods-to-person picking mean low lifting robots that slide under the rack and bring it to a station. Carts and roll cages mean tuggers. Cases and totes mean robots with shelves or conveyor tops.

Write down the heaviest load, its dimensions and lift height, and leave a margin. A robot at its limit accelerates slower, brakes longer and drains its battery faster.

### 3. The floor: the most underrated spec

A robot sees your warehouse from below, and the first thing it sees is the floor.

Here is what that looks like on a real datasheet. Omron’s LD-90, rated for 90 kg, crosses steps of up to 10 mm and gaps of up to 15 mm. It climbs a 4.8° slope only with loads up to 60 kg and needs a level floor above that. Omron specifies a minimum floor flatness of FF25 (ACI 117), no water, oil or debris, indoor use only and no direct sunlight, which can trigger false positives on the safety scanner. Numbers differ between models; the logic does not.

Walk the route with a tape measure before choosing anything. Mark slab joints, expansion joints, ramps, grates, wet areas near dock doors and the spots where forklifts bring snow in from outside. Each one means either floor repairs or fewer machines to choose from.

A floor nobody has noticed in years gets noticed on day one. The robot reports it by stopping.

### 4. Doors, lifts and Wi-Fi

Robots do not open doors by hand. Automatic gates, shutters and lifts on the route must be controlled by the system, through a controller, I/O signals or integration with the lift manufacturer. That is a separate budget line and often a separate contractor.

Check door widths including the load and turning space. Check Wi-Fi along the whole route, especially in freezers, between steel racks and in far corners. A robot that loses connection usually behaves safely, which means it stops. A stopped robot is safe, and useless.

### 5. Safety: people on the route

ISO 3691-4:2023 sets the safety requirements for driverless industrial trucks, AGVs and AMRs included. It divides a site into zones: where people walk, where only trained staff may enter, and where people are excluded, for example by fencing. Where people are present, the vehicle must detect a person and stop before contact. Detection is tested with two objects: an upright cylinder 200 mm in diameter and 600 mm high, and a horizontal one 70 mm in diameter and 400 mm long lying on the floor, which stands in for someone who has fallen or crouched.

For your spec, this means describing where robots cross paths with people and forklifts, when, and how often. That determines speed, scanner settings and, ultimately, throughput.

### 6. WMS integration and mixed fleets

A robot knows nothing about orders. Tasks come from a fleet manager connected to your WMS or ERP. Ask which interfaces exist, who builds the integration, and how long and how much it takes.

If you might add another vendor’s machines later, you will need a common controller. VDA 5050, an open interface developed by the German industry associations VDA and VDMA, exists for exactly this, and a growing number of manufacturers, Chinese ones included, say they support it. Check before you buy, not after.

### 7. How many robots: simple arithmetic

Fleet size follows flow, not floor area:

**Robots = (tasks per hour × trip time in minutes) / (60 × utilisation)**

Trip time includes travel both ways, loading, unloading and waiting at intersections. Utilisation accounts for charging and downtime; 0.7–0.8 is a sensible starting point.

An illustrative example, for arithmetic only: 60 moves per hour, 6-minute trips, utilisation 0.75. That is 60 × 6 / (60 × 0.75) = 8 robots. Shorten each trip by one minute by moving the dispatch area, and the fleet drops to 7. Sometimes the best robotics investment is moving a rack.

One more thing: bigger fleets mean more traffic. Eight robots in a narrow aisle spend time giving way to each other. Ask the manufacturer to simulate the flow rather than multiply.

### 8. Test the unit, not the catalogue

We buy warehouse robots directly from Chinese factories, calculate payback for your flow, and show you the actual unit with its serial number on video from the factory floor. Every robot is tested before shipment. To see warehouses and factories in person, join an Aura Robotics Tour buying trip.

### The bottom line

The robot arrives in the warehouse last. Flat floors, clear routes, location-based storage and clean WMS data come first. If you have them, the robot fits in with almost no rebuilding. If you do not, the robot will not create them. It will, however, show you very clearly where they are missing.
