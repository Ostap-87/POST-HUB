---
number: 4
date: "2026-11-04"
lang: "en"
title: "The Palletizer: A Robot, Some Boxes and the Night Shift"
seo_title: "How to Choose a Robotic Palletizer: Throughput, Patterns, Grippers and Space"
meta_description: "How to choose a robotic palletizing cell: cases per minute, cobot or industrial robot, pallet patterns, grippers, footprint, safety and a simple payback calculation."
slug: "palletizer-robot-some-boxes-night-shift"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "2026-11-04_palletizer-robot-some-boxes-night-shift.jpg"
image_status: "на согласовании"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "34cb0e10-b9e2-4464-8eef-1cef047cce0c"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic industrial photo at dawn at the end of a packaging line in a Russian food factory: a large four-axis palletizing robot arm places the last layer of brown cardboard boxes onto a neat pallet inside its fenced cell, a row of finished stretch-wrapped pallets stands beside it, pink sunrise light pours through high windows, two day-shift workers in work jackets arrive with paper cups of coffee and smile with surprise at the tidy stacks made overnight, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, fresh cheerful morning mood after a quiet night shift. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

End-of-line palletizing is nobody’s dream job. Lift a box, turn it, place it square, and repeat a few thousand times a shift. The night shift is the same, only worse. That is why it is the hardest job to staff, and why it is so often where factory automation begins.

The good news: a palletizer is one of the most predictable robotic cells there is. The bad news: predictable is not the same as simple. At Aura Robotics we source palletizing robots from Chinese manufacturers, and projects tend to trip over everything around the robot rather than the robot itself.

### 1. Throughput: how many cases per minute, really

Start with the number that decides everything: cases per minute arriving from the line. Not the shift average but the peak, plus your growth plans.

Then comes the fork in the road. [Cobot](/en/catalog/cobots) palletizers work next to people without full fencing, and their honest speed is about six cases per minute or less. Industrial palletizers behind guarding start at around twelve and go higher. Catalogue figures for big machines look different again: Yaskawa quotes over 1,700 cycles per hour for the PL190, FANUC up to 2,200 for the M-410iC/110. Those are standard test cycles. With a real gripper, a heavy case and the far top corner of the pallet, expect less.

You can raise throughput without changing robots by picking two or three cases per cycle. That takes the right gripper and a steady infeed.

A robot that only just keeps up is not a saving. It is a future queue on the conveyor.

### 2. What you stack: weight, size, packaging

Record the heaviest unit, its dimensions and material. A corrugated case, a shrink-wrapped bottle pack, a sack and a crate need four different grippers.

Payload works as for any robot: product plus gripper plus margin. Cobot palletizers typically handle up to about 30 lb (13–14 kg); industrial machines handle much more. Large industrial palletizers carry 180–250 kg with roughly three metres of reach, such as ABB’s IRB 660 with 3.15 m. That capacity is not for one case; it is for a gripper that lifts a whole layer.

Check packaging quality too. Crushed cases, badly glued flaps and wrinkled film cause a vacuum gripper more trouble than an extra kilogram.

### 3. Pallet patterns: geometry you did not choose

The pallet sets the rules. In Russia the usual sizes are 1200×800 and 1200×1000 mm, and every case size has its own pattern: units per layer, orientation, interlocking, slip sheets.

Patterns are usually dictated by the customer rather than the factory. Retail chains and distributors set pallet height, wrapping and labelling. Collect your key customers’ requirements first.

The more SKUs, the more software matters. Ask whether there is a pattern generator, whether an operator can add a new SKU without help, and how long changeover takes. If every new case needs a programmer, the cell will stand idle at every range change.

Stack height narrows the choice as well. Cobot palletizers typically stack up to about 1.8 m, industrial ones to about 2.5 m. If customers want tall pallets and the cobot cannot reach the top, it goes on a lift column, and the project gets more expensive.

### 4. The gripper decides

A multi-zone vacuum gripper is the most versatile option for cases: zones let it pick one, two or three and release them separately. Sacks need a fork or clamp gripper. Bottle trays need a layer gripper.

Design the gripper for the most awkward unit, not the most common one. The case that turns up once a week and weighs the most usually defines the design.

### 5. Space and safety

A typical cobot palletizing cell takes around 2.5×2.5 m; an industrial cell with guarding around 3×3 m or more. Add forklift aisles, space for empty pallets and stretch wrapping.

The key layout question is changing pallets without stopping. Two pallet stations let the robot keep working on one while a forklift clears the other. With one station, the robot waits for a human. At night, it waits longer.

Safety is governed by ISO 10218 and, for collaborative operation, ISO/TS 15066. Collaborative mode limits force and speed; for industrial speed you need guarding, light curtains or area scanners. The risk assessment covers the whole cell: robot, gripper, conveyor and pallet stations.

### 6. The night shift: who takes the pallets away?

Here is the arithmetic people skip. A 60-case pallet at six cases per minute fills in ten minutes. So every ten minutes someone has to remove it, wrap it, label it and bring an empty one.

The robot took the heaviest work away from people, but not all of it. At night you need a forklift driver, or an empty-pallet magazine, automatic wrapping and an outfeed conveyor, or a mobile robot that collects full pallets. Otherwise the “lights-out night shift” becomes a shift for one very busy person.

The robot does not get tired at night. The person clearing its pallets does.

### 7. Payback with illustrative numbers

The formula is the same as for any robot:

**Payback (months) = total project cost / (monthly savings − monthly maintenance)**

An illustrative example, for arithmetic only. A turnkey cell with gripper, conveyor and guarding costs 6 million roubles. The line runs three shifts and the robot frees one stacker per shift, each costing the company 110,000 roubles a month fully loaded. Savings are 330,000, maintenance 25,000. Payback: 6,000,000 / 305,000 ≈ 20 months. (Illustrative numbers. Yours will differ, which is the whole reason to calculate.)

Harder to put in the formula but worth counting: fewer back injuries, lower turnover, consistent pallet geometry and less transit damage. In palletizing, these lines often weigh more than expected.

### 8. Test the unit, not the catalogue

We source palletizers directly from Chinese manufacturers, calculate payback for your flow, and show you the actual unit with its serial number on video from the factory floor. Each robot is tested on the task before shipment. To see palletizing cells in person, join an Aura Robotics Tour buying trip.

### The bottom line

The palletizer is the humblest robot on the floor. It does not dance at trade shows or make the news. It just stacks boxes straight, at 3 a.m. exactly as at 3 p.m. For a job nobody volunteers for, that is quite a lot.
