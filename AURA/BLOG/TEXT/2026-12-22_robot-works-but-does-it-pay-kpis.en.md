---
number: 52
date: "2026-12-22"
lang: "en"
title: "The Robot Works. But Does It Pay? KPIs to Track From Day One"
seo_title: "Robot KPIs After Commissioning: OEE, MTBF, MTTR and Checking Payback Against the Plan"
meta_description: "Which robot metrics to record from launch day: OEE, availability, MTBF, MTTR, scrap and utilisation. How to pull data from the controller and compare actual payback with the original calculation a year later."
slug: "robot-works-but-does-it-pay-kpis"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

Every robot has two ages. One is on its nameplate, counted from the production date. The other is in a spreadsheet, counted from the day someone first asks: “Is it actually paying for itself?” That usually happens about a year in, at a budget meeting. And it turns out nobody can answer. The robot is clearly working. What it has earned is not clear at all.

At Aura Robotics we calculate payback for clients before they buy. But a pre-purchase calculation is a forecast. To compare it with reality a year later, data collection has to start on launch day, not on meeting day.

### 1. Baseline first, robot second

The most common mistake happens before launch. Nobody records how the cell performed without the robot: output per shift, scrap, headcount, downtime. A year later the robot is compared with memories, and memories always favour the past.

So the first task is a baseline over a few weeks before launch: output, scrap, labour hours, downtime and its causes. Without it, every robot KPI is a number without a partner.

Payback you cannot compare with the past is not payback. It is an opinion.

### 2. OEE: one number made of three

Overall equipment effectiveness is the most widely used metric, and it works for a robotic cell just as well as for a machine tool. It was introduced by Seiichi Nakajima as part of Total Productive Maintenance.

**OEE = availability × performance × quality.**

- **Availability**: actual run time divided by planned production time. Breakdowns, changeovers and waiting for parts all count here.
- **Performance**: actual output compared with what the ideal cycle time would allow.
- **Quality**: good parts as a share of total output.

Nakajima defined world-class OEE as above 85%. Industry analysts estimate that most plants actually run at roughly 40–60%. Multiplication is unforgiving: 90% availability, 95% performance and 92% quality give about 79%. Three good grades multiply into one average one.

OEE also shows where time goes. Very often the robot itself is fine and availability is low because nobody delivered the parts. The robot is idle; the forklift is to blame.

### 3. MTBF and MTTR: how often it fails, how fast it recovers

**MTBF** (mean time between failures) is total operating time divided by the number of failures. 2,000 hours over 90 days with 10 failures gives an MTBF of 200 hours.

**MTTR** (mean time to repair) is total repair time divided by the number of repairs. 30 hours across 10 failures gives an MTTR of 3 hours.

Availability = MTBF / (MTBF + MTTR). In this example: 200 / 203 ≈ 98.5%. (Illustrative numbers.)

Some caveats. Do not count planned stops or program changes as failures. Do not mix different robot models in one figure. And do not draw conclusions from ten failures: a point estimate on a small sample swings widely. After a year you will have enough data to speak with confidence.

MTBF tells you how well you chose the robot. MTTR tells you how well you organised everything else. The second is usually easier to fix.

### 4. What else to record from day one

**Utilisation.** How many hours a day the robot actually runs. The plan may have said two shifts; reality delivered one and a half. This is the single most common source of variance.

**Released labour hours.** How many person-hours left the task, and where those people went. If operators are still standing next to the robot, there are no savings, just an extra colleague made of steel.

**Scrap and rework.** Part of a robot’s payback often comes from consistency, not wages. If scrap fell, the numbers should show it.

**Operating costs.** Electricity, tooling consumables, spare parts, technician hours, external service. Often forgotten, which makes the robot look better on paper than in the accounts.

**Stoppage log.** Date, time, cause, duration, who fixed it. The dullest document in the cell, and the most valuable a year later.

### 5. Where the data comes from

The good news: most modern robot controllers keep event logs, error histories and cycle counters. The bad news: someone has to get the data out.

- **Controller logs.** Export from the pendant or via the manufacturer’s service software. At a minimum, download and archive them regularly.
- **PLC exchange.** The robot sends “cycle complete”, “error” and “waiting” signals to the line controller over industrial protocols (Modbus TCP, Profinet, EtherNet/IP and others, depending on the model), and from there into SCADA or MES.
- **OPC UA.** There is an industry companion specification, OPC UA for Robotics (VDMA 40010), presented in 2018: a common data model for asset management, condition monitoring and preventive maintenance. Check with the manufacturer whether your model supports it.
- **Vendor cloud dashboards.** Mobile and [cleaning](/en/catalog/cleaning) robots often report statistics through an app or cloud. Convenient, but find out where the data lives and whether you can export it.

If digital collection is not set up yet, start on paper. A handwritten stoppage log beats a perfect monitoring system scheduled for next year.

### 6. The one-year review: an illustrative example

Pre-purchase plan (illustrative): the project costs 6 million roubles, expected savings are 300,000 roubles a month on two shifts, payback is 20 months.

Actuals after a year (also illustrative): the robot averaged one and a half shifts, because the second shift did not always get parts. Savings came to about 225,000 a month, pushing payback to roughly 27 months.

What the KPIs showed: MTBF normal, MTTR low, quality up. The problem was utilisation, not the robot. The fix lies in cell logistics, not repairs. Without data, the meeting would have concluded: “the robot did not meet expectations”. (All figures illustrative.)

### How we help

We source robots directly from more than 100 Chinese manufacturers and calculate payback before purchase. We show the actual unit, serial number included, on video from the factory floor and test it before shipment. One team handles the project from selection to launch, so the assumptions in the payback calculation can become the list of what to measure once the robot is running.

### The bottom line

A robot cannot defend itself at a budget meeting. It will not mention that it was idle because of the forklift, or that scrap fell because of it. The numbers will say it, provided somebody wrote them down.

A year on, everyone will remember what the robot cost. Only the log will remember what it earned.
