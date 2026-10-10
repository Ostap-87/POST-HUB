---
number: 55
date: "2026-12-25"
lang: "en"
title: "Daily, Monthly, Twice a Year: A Robot Maintenance Routine Your Own Team Can Run"
seo_title: "In-House Robot Maintenance: Daily, Monthly and Annual Routines"
meta_description: "What to do with a robot every day, month and six months: inspections, safety tests, sensor cleaning, batteries, backups and the maintenance log. Examples from cobot, AMR and robot dog manuals."
slug: "daily-monthly-twice-year-robot-maintenance-routine"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

There are two kinds of robot owners. The first maintain their robot on schedule. The second maintain it on demand, meaning when it stops. The second group saves a little time every week and loses a lot of it all at once, usually at the end of the quarter.

In our article on after-warranty service we covered spare parts, firmware and whom to call when something breaks. This one is about what your own people do, on a schedule, so you have to call less often. At Aura Robotics we source robots directly from Chinese factories and always advise clients to obtain the maintenance schedule before they buy.

### 1. The manufacturer writes the schedule, you run it

The key document is the maintenance manual for your specific model. There is no universal routine “for all robots”: an arm, a cleaning robot and a robot dog wear differently and fail differently. The logic, though, is shared: frequent simple checks go to the operator, rare and complex ones to the technician or service engineer.

**Cobot.** In Universal Robots’ e-Series inspection plan, base and tool mounting bolts are checked monthly; joint lids and their screws, flat rings, the robot cable and its connector, and joint screws every six months. The same items are rechecked after any heavy collision. UR also recommends monthly safety tests: emergency stop, freedrive, backdrive, safety I/O, confirming safety settings match the risk assessment, and a backup.

**Cleaning robot.** For the Pudu MT1: weekly, wipe the drive and auxiliary wheels and clean the vision sensors and lidar with a soft dry cloth; every two weeks, empty and wash the dustbin and clean the air filter. Brushes are replaced when worn.

**Robot dog.** The Unitree Go2 manual says to verify functionality through the app before use and, when needed, calibrate the legs and IMU on a level surface with a calibration ruler.

Notice how different these are in spirit. For the [cobot](/en/catalog/cobots) it is bolts and safety. For the cleaner, dirt and sensors. For the dog, calibration. Copying your neighbour’s routine only works if your neighbour bought the same robot.

### 2. Every day, every shift: five minutes for the operator

Daily checks belong to the operator, with no tools and no engineer. A typical list (confirm it against your model’s manual):

- **Visual check.** Damage to housing, cables, hoses, tooling. Grease leaks, foreign objects in the work area.
- **Sensors.** Clean windows on lidars, cameras and safety scanners. Dust on a sensor is the main cause of a mobile robot’s “strange” behaviour.
- **Tooling.** Suction cups, gripper fingers, vacuum. These wear faster than the robot.
- **Safety.** Emergency stops, light curtains and guards working.
- **Battery.** Charge level, connector condition, no swelling.
- **Controller messages.** Any new warnings in the log.

Five minutes at the start of a shift save five hours in the middle of it.

### 3. Weekly and monthly: the technician’s job

- **Fastener torque.** Base, tool and tooling bolts, checked with a torque wrench to the manual’s values.
- **Safety function tests.** Emergency stop, brakes, safety zones, using the manufacturer’s method, with results recorded.
- **Control cabinet cleaning.** Fan filters and internal dust. Many manufacturers explicitly forbid compressed air on the arm and controller, because it drives dust past the seals. Universal Robots recommends an ESD-safe vacuum cleaner.
- **Wheels and drive** on mobile robots: tread wear, threads and stretch film wound around axles.
- **Backups.** Programs, settings, navigation maps, safety parameters. Stored somewhere other than the robot itself.

### 4. Every six months and every year: the deep check

- **Full inspection** of seals, cables in moving parts and connectors.
- **Lubrication and gearboxes**, strictly to the manufacturer’s intervals and grease types. Intervals are usually tied to operating hours, so work out in advance when they fall due on your shift pattern.
- **Calibration.** Positioning accuracy, sensors, legs on walking robots, cameras and tool centre point.
- **Batteries.** Capacity and condition. A detail for Russian winters: standard Li-ion batteries must not be charged below freezing, or they lose capacity permanently. Keep charging and storage in a heated room.
- **Manufacturer or partner service check**, if the manual or warranty requires it.

Storage matters too. Manufacturers usually have rules for long idle periods; Universal Robots, for example, advises against storing a robot for more than six months without a visual inspection.

### 5. The maintenance log: dull and invaluable

Maintenance that was not written down did not happen, as far as both the warranty and human memory are concerned. The log should show:

- date, the robot’s operating hours and the type of work;
- who did it;
- what was found and what was replaced;
- safety test results;
- a backup confirmation.

Paper, spreadsheet or maintenance management system, it does not matter. What matters is that it starts on day one and can be shown to the factory when you need a warranty repair. The manufacturer’s first question will be: “Did you do the maintenance?” “Of course” without a log sounds unconvincing in any language.

### 6. Who does what

**Operator**: daily inspection, cleaning sensors and tooling, battery check, recording issues.

**Technician**: weekly and monthly work, safety tests, backups, replacing minor consumables.

**Service engineer or partner**: gearbox lubrication, calibration, component replacement, anything needing service-level access.

An illustrative estimate for one cobot on two shifts: 5–10 operator minutes per shift, about an hour of technician time a month, one service engineer day every six months. (Illustrative only: your model’s manual and environment will set the real figures.)

### How we help

We source robots directly from more than 100 Chinese manufacturers and request documentation, including the maintenance schedule, during selection. We show the actual unit, serial number included, on video from the factory floor and test it before shipment. One team runs the project from selection to launch, so the maintenance routine can be built into staff training at commissioning.

### The bottom line

A robot does not get tired, but it does wear out. It does not complain, but it keeps count. A skipped check breaks nothing today. It goes on a tab that arrives later, as a single bill.

The best robot in the plant is the one you only ever hear about from the maintenance log.
