---
number: 31
date: "2026-12-01"
lang: "en"
title: "Gears Decide Everything: Strain Wave, RV or Planetary, and What It Means for the Buyer"
seo_title: "Strain Wave vs RV vs Planetary Reducers in Robots: Service Life, Backlash, Maintenance"
meta_description: "Where robots use strain wave, RV cycloidal and planetary reducers, what rated lives of 6,000 and 7,000 hours really mean, when to change the grease, and what to ask the factory before you buy."
slug: "gears-decide-everything-strain-wave-rv-or"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

At a trade show people ask a robot what it can do. At acceptance they ask what it cost. Three years later an engineer asks what is inside it, usually at the exact moment something inside it starts to crunch.

What is inside is almost always a reducer. A robot’s motor is fast and weak; a joint needs to be slow and strong; a set of gears sits between them and translates. Reducers are often said to account for up to a third of the cost of a traditional industrial robot. The figure is repeated so often it has become folklore, but the order of magnitude stands: this is not a line item, it is a third of the machine.

Here are the three types you will meet most often, and what each means for a buyer.

### Strain wave: slim, precise, slightly highly strung

A strain wave (harmonic) reducer contains a part that is designed to bend. A thin flexible cup with teeth rolls inside a rigid ring and moves only a couple of teeth per input revolution. The result is a high ratio in a single stage (typically 50:1 to 160:1 and beyond), near-zero backlash and a compact package.

That is why strain wave gears sit in cobot joints, industrial robot wrists and many humanoid arms: wherever precision and low weight matter and loads are moderate.

Their life is rated in an unusual way. What wears out first is not a tooth but the wave generator bearing. At Harmonic Drive, the benchmark maker, the CSF series has a rated L10 life of 7,000 hours and the CSG series 10,000 hours; L50, the point at which half of units are still running, is five times longer at 35,000 and 50,000 hours. All at rated torque and speed. Read carefully: L10 means one in ten may fail earlier. It is statistics, not a promise.

A part that flexes millions of times without breaking is great news for engineers and terrible news for worriers.

China now makes its own. The largest local supplier, Suzhou Leaderdrive, holds about 27.5% of Chinese shipments according to QY Research; its 2025 revenue grew 47% to 571 million yuan, and its customers reportedly include Unitree, UBTech and AgiBot. In autumn 2026 it started the process of listing in Hong Kong. For a buyer the point is not the stock market. It is that a repair kit for a Chinese cobot is now more likely to come from Suzhou than from Japan.

### RV: heavy, stiff and patient

An RV cycloidal reducer has two stages: a planetary stage followed by cycloidal discs rolling on pins. It is heavier and more complex than a strain wave gear but handles large torques and shocks. It lives in the base and shoulder of a large industrial robot, the first three axes that carry everything else.

The benchmark is Nabtesco. Its RV-E series has a rated life of 6,000 hours at rated torque and a rated output speed of 15 rpm, with backlash and lost motion under 1 arc-minute for most sizes and rated torques from 58 to 4,410 N·m.

Now the important part. 6,000 hours sounds alarming: on two shifts that is eighteen months. But Nabtesco’s life formula scales linearly with lower speed and roughly to the power of 10/3 with lower torque. Run the reducer at 70% of rated torque and the formula gives about three times the catalogue life. So the real question is not “what is the reducer’s life?” but “what share of its rating will it see in our cell?” The duty cycle answers that, not the brochure.

Rated life is not a lifespan. It is a reference point, like the height printed in a passport photo.

Chinese RV makers such as Zhejiang Shuanghuan Driveline are growing, but in heavy axes Japanese suppliers still hold a larger share than in strain wave gears.

### Planetary: simple, tough, honest

Anyone who has taken apart a cordless drill has seen a planetary gear: a sun, planets and a ring. It is cheaper, simpler, takes shocks well and, crucially for walking machines, is backdrivable: push the joint from outside and the motor feels it.

That is why legged robots like planetary stages. A teardown of the Unitree G1 presented by Munro Live in September 2026 showed the same actuator design in the hips, knees, shoulders and elbows, each with a two-stage planetary gearbox of roughly 15:1. A leg has to absorb a landing, not just place a foot, and a low-ratio planetary lets it.

The price of simplicity is backlash. Fine for a knee, unacceptable for precision assembly.

### What this means when you buy

Cobots and light arms almost always use strain wave gears in the joints. Ask for the reducer maker, the series, and the rated life, or better, the calculated life for your duty cycle.

Medium and heavy industrial robots use RV in the main axes and other types in the wrist. Ask which axes use what, and from whom.

Humanoids and robot dogs often use planetary actuators in the legs and other types in the arms. Ask what a complete joint actuator costs and how long it takes to arrive: it will be replaced as a unit, not gear by gear.

A word on grease. Nabtesco’s standard grease replacement interval for RV reducers is 20,000 hours, sooner if the grease is contaminated or ambient temperature is 40 °C or above. Harmonic Drive sets intervals from a chart of input revolutions and temperature, cut by the cube of any excess when average torque exceeds the rating. 20,000 hours is five years on two shifts at 250 days a year: just long enough for everyone to forget who signed the acceptance certificate.

Put it in the maintenance schedule on day one. The robot will remind you otherwise, later and louder.

### Five questions for the factory

1.  Which reducers are on which axes, and who makes them?
2.  What is the rated and calculated life under our load?
3.  What is the backlash or lost motion when new, and what wear is acceptable?
4.  What grease, what interval, and can it be changed on site?
5.  What does a complete reducer or joint actuator cost, and what is the lead time?

At Aura Robotics we put these questions to the factory during selection, include planned component replacement in the payback calculation, show the client the actual unit with its serial number on video from the factory floor, and test it before shipment. If you would rather look under the cover yourself, join an Aura Robotics Tour buying trip: factories show reducers far more willingly than catalogues do.

### The bottom line

The buyer sees a robot. The engineer sees a reducer. The accountant sees depreciation.

All three are right. But the first to know about wear is whoever stands next to the joint when it starts taking a moment longer than usual. By then, there should be a spare on the shelf.
