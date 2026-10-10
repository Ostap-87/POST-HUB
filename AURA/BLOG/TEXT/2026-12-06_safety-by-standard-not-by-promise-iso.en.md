---
number: 36
date: "2026-12-06"
lang: "en"
title: "Safety by Standard, Not by Promise: ISO 10218, ISO/TS 15066 and Area Scanners"
seo_title: "Industrial Robot and Cobot Safety: ISO 10218:2025, ISO/TS 15066 and Safety Scanners"
meta_description: "What changed in ISO 10218 in 2025, which contact force limits ISO/TS 15066 sets, which national standards apply in Russia, why safety scanners and light curtains matter, and who is responsible for a robot cell."
slug: "safety-by-standard-not-by-promise-iso"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

[Cobots](/en/catalog/cobots) are sold with the line “works next to people without fencing”. True, but incomplete. The full version reads: “can work next to people without fencing if the cell is designed, assessed and verified to the standard.” The second half does not fit on a banner.

In robot safety, a manufacturer’s word is worth exactly as much as the risk assessment attached to it. Here are the documents that assessment rests on, and what a buyer needs from them.

### ISO 10218: the 2025 revision

The core international standard for industrial robot safety is ISO 10218. Part 1 is for robot manufacturers; Part 2 is for integrators, who turn a robot, tooling and guarding into a working cell.

In 2025 both parts were revised, ISO 10218-1:2025 and ISO 10218-2:2025, for the first time since 2011. The changes that matter to buyers:

The requirements for human-robot collaboration, which used to sit in a separate technical specification, ISO/TS 15066, have been folded into the standard itself.

The terms “collaborative robot” and “collaborative operation” are gone, replaced by “collaborative application”. The logic: only a specific cell doing a specific job can be safe for collaboration, not a robot on its own.

Functional safety requirements are now explicit rather than implied, and Part 2 adds cybersecurity requirements insofar as they affect robot safety.

In other words, the standard has officially stopped believing in safe robots. It believes in safely designed cells.

### ISO/TS 15066: how hard a robot may push

The best-known part of ISO/TS 15066 is its body model of permissible forces and pressures for contact between a robot and a person. A cobot may touch you, but not hard enough to injure.

Some of the maximum permissible forces cited in the research literature: 140 N for hands and fingers, 140 N for the chest, 130 N for the skull and forehead, 65 N for the face. Each region also has pressure limits, which often prove stricter: a sharp edge at the same force produces far more pressure than a flat surface.

Hence a point often forgotten. Force limiting is built into the cobot. Pressure depends on what it is holding. A cobot carrying a sheet of metal with a sharp edge stops being safe, however perfectly its force sensors work.

A cobot is only as safe as the sharpest thing in its hand.

### What applies in Russia

Russia publishes robot safety standards in the GOST R 60 series.

GOST R 60.1.2.1-2016, safety requirements for industrial robots, Part 1: Robots, based on ISO 10218-1:2011, in force since 1 January 2018.

GOST R 60.1.2.2-2016, Part 2: Robot systems and integration, based on ISO 10218-2:2011, from the same date.

GOST R 60.1.2.3-2021, safety requirements for robots working together with humans, based on ISO/TS 15066:2016, in force since 1 November 2021.

So the national standards still mirror the previous ISO edition. In practice it is sensible to design with both in mind: the GOST R standards as the national baseline, and ISO’s 2025 edition as the direction the industry is heading, and where many manufacturers already are.

Above the standards sits the Customs Union technical regulation TR CU 010/2011 on the safety of machinery and equipment, under which conformity is confirmed on import. We cover that in a separate article.

### Scanners, light curtains and how to calculate distance

Not every cell has to be collaborative. Often it is simpler and cheaper to make the robot slow down or stop when someone approaches. That is what protective devices are for.

A safety laser scanner watches a floor area around the robot, usually with two fields: entering the outer one slows the robot, entering the inner one stops it.

A light curtain covers an opening, such as a loading window or cell entrance. Break the beam and the robot stops.

Safety mats and door interlocks do the same job mechanically.

Crucially, a mobile robot’s navigation lidar and a certified safety scanner are different devices. One helps the robot drive; the other protects people. A protective device needs a verified functional safety level, for instance under ISO 13849-1.

Mounting distance is not chosen by eye. ISO 13855 calculates it from human approach speed and the total stopping time of the system: sensor response, controller and the robot’s braking. If the robot brakes more slowly than its datasheet says, or its brakes have worn, the calculation no longer holds. So stopping time is measured on site, not copied from a catalogue.

A light curtain belongs where the calculation puts it, not where the cable happened to reach.

### Who is responsible if something happens

The short answer, in Russia: the employer. Article 214 of the Labour Code makes the employer responsible for safe working conditions and occupational risk assessment, whoever sold the robot and whoever built the cell.

The longer answer: responsibility runs along a chain. The manufacturer answers for the robot meeting its stated specifications and the technical regulation. The integrator answers for designing the cell to standard and carrying out a risk assessment (the method is set by ISO 12100). The client answers for running the cell as designed: guards stay on, scanners stay active, tooling is not changed without reassessing risk.

The most common cause of robot incidents is not the robot. It is the “temporary” fix: a scanner taped over so forklifts stop triggering it, a cell door propped open with a crate. Nothing lasts like a temporary solution.

### Five safety questions before you buy

1.  Which edition of ISO 10218 is the robot certified to, and where are the documents?
2.  Which safety functions does the controller offer (force, speed and zone limits, safe I/O), and at what level?
3.  Will the cell be collaborative or guarded, and who carries out the risk assessment?
4.  What is the robot’s stopping time with your payload?
5.  Which documents does your site need for commissioning, and who prepares them?

At Aura Robotics these questions are part of selection from the start: one team takes the client from model choice to commissioning, and protective devices are in the payback calculation from day one, not added later. Before shipment we test the actual unit and show it on video with its serial number, including its safety functions in operation.

### The bottom line

Safety standards are heavy reading. That is fair: they were written after someone had a much heavier day.

A promise can be given and taken back. A test report stays in the file. May it stay there, ideally without anyone ever needing it.
