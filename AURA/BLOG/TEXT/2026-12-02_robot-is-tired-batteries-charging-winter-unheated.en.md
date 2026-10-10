---
number: 32
date: "2026-12-02"
lang: "en"
title: "The Robot Is Tired: Batteries, Charging and Winter in an Unheated Warehouse"
seo_title: "Robot Batteries Explained: Runtime, Charging, LFP vs NMC and Cold-Weather Operation"
meta_description: "How long warehouse robots, humanoids and robot dogs really run on a charge, how LFP differs from NMC, why lithium must not be charged below freezing, and how robot batteries ship from China."
slug: "robot-is-tired-batteries-charging-winter-unheated"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

People say robots never get tired. That is true right up until the battery runs flat. Then the robot gets tired all at once, completely, and usually in the far corner of the warehouse.

The battery is the most underrated line on a spec sheet. It is read last and works first: it decides how many hours the robot actually works, what a shift costs, where the chargers go and what happens in January in an unheated building.

### Brochure hours and warehouse hours

Start with published numbers.

The Unitree Go2 robot dog has an 8,000 mAh battery and runs for about 1–2 hours in its standard versions; the EDU version, with a 15,000 mAh long-endurance pack, runs about 2–4 hours. The Unitree G1 humanoid is rated at about 2 hours. Warehouse AMRs last longer: 8–14 hours depending on load is a typical figure for an LFP-powered robot (the Danish GoPal P35, for instance, and Chinese makers quote similar ranges).

Note the words “about” and “depending”. They are not decoration. Runtime is quoted for a typical cycle: flat floor, moderate load, room temperature. Your site has ramps, heavy pallets, stops for every passing person and cold air at the dock doors, and every one of them eats watt-hours.

The spec sheet is written for the ideal warehouse. The robot works in yours.

So we plan with the brochure figure plus a margin, and count shifts rather than hours: how many robots it takes to cover eight, twelve or twenty-four hours including charging time.

### Three ways to charge

End-of-shift charging: the robot works as long as it can, then charges for several hours. Fine for one shift or a fleet with spare units.

Opportunity charging: the robot tops up in short sessions during idle moments. The GoPal P35 goes from 30% to 95% in 45 minutes and is designed around that pattern. For a 24/7 site this is usually the cheapest option because less downtime means a smaller fleet.

Battery swapping: the robot pulls in, the pack is swapped by hand or automatically, and off it goes. UBTech has shown its Walker S2 humanoid swapping its own battery. For dogs and humanoids, a spare pack is often the only way to work more than a couple of hours. But every extra pack is money, shelf space and another charger.

So ask before ordering: where will the chargers physically sit, how many do you need, is there a socket of the right rating, and will the station block an aisle? A warehouse designed without chargers becomes a warehouse full of extension leads within a month.

### LFP or NMC

Robot batteries mostly use one of two lithium-ion chemistries.

LFP (lithium iron phosphate) is heavier per unit of energy but handles more charge cycles, is more thermally stable and copes well with frequent top-ups. It suits warehouse robots, where weight matters less and cycles run into thousands a year.

NMC (nickel manganese cobalt) is lighter and more energy-dense. It suits machines where every kilogram counts: legged robots, robot dogs, humanoids.

Chemistry is not a matter of taste but of duty cycle. Frequent short charges and round-the-clock work point to LFP; a machine that carries its own battery around points to NMC. Spec sheets do not always state it, so ask, along with the number of cycles to 80% remaining capacity.

### Cold: what the brochure leaves out

Lithium-ion cells can be discharged across a wide range, roughly −20 to +60 °C, but should only be charged between 0 and +45 °C, according to Battery University’s general guidance, and robot spec sheets usually agree. The reason is physical: in the cold, lithium ions enter the anode slowly and during charging plate out as metallic lithium. The pack may appear to charge normally, but the loss of capacity and safety is permanent. Fast charging is reasonable from +5 °C; below that the current should drop, and below freezing charging should not happen at all.

The irony is that a robot can work in the cold but cannot recover in it. Much like the rest of us.

In practice, put the charging station in a heated zone even if the robot works in a cold one. A robot coming in from the cold has to warm its battery before charging; a good battery management system (BMS) does this itself or blocks charging.

Capacity drops in the cold, so winter runtime is shorter than summer runtime. Plan the fleet size accordingly.

Sensors feel the cold too. The popular Livox Mid-360 lidar operates from −20 to +55 °C and switches on self-heating below freezing, raising peak draw from 6.5 W to 14 W. Small, but it is one more line in the energy budget.

A true freezer at −25 °C needs special robot versions. That is a separate topic, covered in our article on cold-storage warehouses.

### How the battery travels from China

In logistics, a lithium battery is Class 9 dangerous goods: UN3480 when shipped on its own, UN3481 when packed with or contained in equipment. Any such shipment needs a UN 38.3 test summary.

From 1 January 2026, an IATA rule that used to be a recommendation became mandatory: lithium-ion batteries packed with equipment (UN3481, above 2.7 Wh) must ship at no more than 30% state of charge. Batteries shipped alone have been under that limit for years.

That means three things. The robot arrives half-flat, and that is normal. Spare batteries may travel differently and take longer than the robot itself. And if spares are ordered “later”, later will come later than you would like.

At Aura Robotics we calculate payback with the real number of batteries, chargers and shifts, test the actual unit before shipment and show it to the client on video with its serial number. How the batteries travel is settled in advance, not at customs.

### Five battery questions

1.  What chemistry, and how many cycles to 80% capacity?
2.  How many hours in our duty cycle, not the brochure’s?
3.  How does it charge: dock, cable or swap, and how long does it take?
4.  At what temperature is charging allowed, and what does the BMS do in the cold?
5.  How will spare batteries ship, and with what?

### The bottom line

Robots really do not get tired. They just run down, which is more honest: you know in advance when and by how much.

All that is left is to put the charger somewhere warm. The robot will not mind. The battery will remember.
