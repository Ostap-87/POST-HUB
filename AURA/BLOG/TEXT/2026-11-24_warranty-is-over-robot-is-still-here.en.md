---
number: 24
date: "2026-11-24"
lang: "en"
title: "The Warranty Is Over, the Robot Is Still Here: Service, Spare Parts and Firmware in Year Two"
seo_title: "Robot Maintenance After Warranty: Spare Parts, Scheduled Servicing, Remote Diagnostics, Software Updates and Service Partners"
meta_description: "What happens to a robot bought in China after the warranty ends: which parts wear, how to stock spares, maintenance intervals, remote diagnostics, firmware update policy and who repairs the robot locally."
slug: "warranty-is-over-robot-is-still-here"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

A lot is written about buying robots. Less about commissioning them. Almost nothing about what happens a year later, when the warranty runs out. Presumably because by then everyone who was writing has moved on to the next robot.

But your robot stays. It is on its second shift, its cables flex for the thousandth time this week, the grease in its gearboxes is ageing and its battery remembers every charge. A warranty is a factory’s promise. Wear is physics. Physics makes no promises, but it never breaks one either.

At Aura Robotics we source robots directly from factories in China. Here is what to think through for years two, three and five. Ideally before you buy, because afterwards many of the answers are no longer yours to choose.

### 1. What wears out

Every robot class has its own consumables, but the list is familiar.

**Arms and cobots:** gearbox grease, cables and hoses in moving joints, encoder backup batteries, brakes.

**Mobile robots:** wheels and treads, traction batteries, sensors and lidars (to be cleaned and sometimes replaced), bumpers.

**Cleaning robots:** brushes, squeegees, filters, pumps.

**Humanoids and robot dogs:** actuators, especially in the legs, which take the impacts of walking and falling, plus hands and batteries.

**Tooling:** suction cups, gripper fingers, vacuum generators. The first things to break, and the last things anyone remembers when ordering spares.

A robot ages by its cycle counter, not by the calendar. The calendar just reminds you to look at the counter.

### 2. Scheduled maintenance: hours, not dates

Manufacturers’ schedules are usually tied to running hours. An example from a typical six-axis industrial arm schedule, as cited in an industry guide: replace gearbox grease and oil every three years or 11,520 hours, and encoder backup batteries every year or 3,840 hours, whichever comes first.

Look at 3,840. That is 16 hours a day for about 240 days — two shifts on working days. Run the robot around the clock and the intervals shrink proportionally; a three-year interval at double the load becomes eighteen months.

Encoder batteries deserve a note. Swap them with the controller powered off and the robot may lose its axis positions and need recalibrating. A small detail that turns a five-minute job into a lost day.

Ask the factory for the maintenance schedule, in your language, together with the documentation — not when the warning light comes on.

### 3. Spare parts: money on the shelf versus money lost to downtime

A spares store is always a trade-off between tied-up cash and downtime risk. A simple rule: if a part takes longer to arrive than the robot can afford to stand idle, keep it on site.

And lead time from China is not just production. It is the same logistics we described in our shipping article: from days by air to a month or two by sea, plus customs. A spare battery is, once again, dangerous goods with its own paperwork.

Split spares into three groups.

**Consumables:** suction cups, brushes, filters, fuses. Always in stock, six months’ worth.

**Critical components:** whatever stops the robot and takes long to ship: an actuator, a controller, a board, a traction battery. Decide by comparing the part’s cost with the cost of downtime over its lead time.

**Everything else:** order as needed.

Ask the manufacturer for a recommended two-year spares list before signing and put it in the specification. The spares store is the one place in a factory where empty shelves cost more than full ones.

### 4. Remote diagnostics: the factory’s eyes on your floor

Many Chinese robots can send event logs and diagnostics to the manufacturer or connect to remote support. That speeds up troubleshooting enormously: the factory engineer sees what the controller sees, not what someone managed to describe in a chat.

But remote access has an owner: your IT security team. How the channel is set up, who connects and when, what data leaves the site, whether connections can be on request only. Critical infrastructure operators face stricter requirements still. Settle it at the selection stage, not during a breakdown, when the temptation is to give everyone access to everything.

A good compromise is to export logs and program backups to your own systems regularly. Then even without a permanent connection you have something to show the factory.

### 5. Firmware: you cannot avoid updates, and you cannot rush them

Robot makers release updates often: bug fixes, new features, better navigation or walking. For humanoids and mobile robots, where software does so much, an update can change behaviour more than a hardware swap.

Hence a simple policy:

- Record the software version in the specification and acceptance report.
- Back up programs, settings and maps before any update.
- Test the update on one robot or outside production hours, not on the whole fleet on a Friday evening.
- Keep the ability to roll back.
- Ask how long the model and software version will be supported.

The best update is the one installed on Tuesday morning and forgotten by lunch.

### 6. Who repairs it: your engineer, a partner, the factory

After the warranty, service usually has three tiers.

**Your own engineer** handles scheduled maintenance, consumables and recovery from routine errors, having been trained at commissioning.

**A local service partner** — an integrator or service company that knows the model, stocks parts and can come on site. Find out whether one exists for your model before you buy.

**The factory** — complex diagnostics, major component repairs, software.

One question that is often forgotten: access to service software and the controller’s service level. If only the factory knows the password, every repair starts with an email to China and a wait for the reply. Given the time difference, tomorrow.

### Questions to ask before buying

1.  Which parts wear, and after how many hours?
2.  Is there a maintenance schedule in your language?
3.  What is the recommended two-year spares list, and what does it cost?
4.  What are lead times for critical components?
5.  How does remote diagnostics work, and what does it send?
6.  How often are updates released, and can you roll back?
7.  Is there a local service partner?
8.  Will your engineer get service-level access?

### How we help

We source robots directly from partner factories, match them to the task and calculate payback over the full ownership period, not just the purchase price. We show the specific unit on video from the factory floor with its serial number and test it before shipment.

### The bottom line

In year one the robot runs on warranty. After that it runs on care. The warranty comes with the purchase; the care you have to plan yourself.

A well-maintained robot in year five resembles a seasoned employee: knows itself, asks for nothing, quietly gets on with it. A neglected one resembles an employee too. The one who left without giving notice.
