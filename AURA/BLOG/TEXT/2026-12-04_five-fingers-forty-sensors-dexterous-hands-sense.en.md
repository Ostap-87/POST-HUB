---
number: 34
date: "2026-12-04"
lang: "en"
title: "Five Fingers and Forty Sensors: Dexterous Hands and the Sense of Touch"
seo_title: "Dexterous Robot Hands: Degrees of Freedom, Grip Force, Tactile Sensing and Price"
meta_description: "Which dexterous hands Chinese makers offer (Inspire Robots, DH-Robotics, PaXini and others), what degrees of freedom and fingertip force mean, what a hand costs relative to a humanoid, and when a simple gripper will do."
slug: "five-fingers-forty-sensors-dexterous-hands-sense"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
---

Nobody designed the human hand, yet everyone wants to copy it. Twenty-odd degrees of freedom, skin with thousands of receptors, and the ability to hold a cup, gesture and not drop a phone at the same time. Most of the time.

Robot hands are more modest. But the market is growing so fast that anyone buying a humanoid or manipulator now faces a question that did not exist five years ago: five fingers, or two?

### How many hands are selling

According to GGII, about 19,200 dexterous hands were sold in China in 2025, with around 70,200 expected in 2026. Nearly quadrupling in a year is not a trend. It is a crowd at the door.

Linkerbot, which we covered in our components article, says it shipped more than 10,000 hands in 2025. AgiLink was spun off from [AgiBot](/en/catalog/humanoid/factory/agibot) at the end of 2025. Industry reports say Unitree bought its hands in January–September 2025 almost entirely from a single supplier, Yinshi Robotics. Even a major humanoid maker does not necessarily build its own hands.

### Degrees of freedom: count them properly

The headline number on a hand’s spec sheet is degrees of freedom, and it comes in two flavours.

Active DoF is the number of independent motors driving the fingers. Joints is the total number of bends, including those that follow others through linkages. The Inspire Robots RH56DFX has 6 DoF and 12 joints: the fingers curl naturally, but only six motions are independently controlled. The DH-Robotics DH-5-6 also has 6 active DoF and 11 in total.

For reference, industrial grippers have 1 to 6 DoF and the human hand 22 to 27. Flagship Chinese hands have reached 22 (Linkerbot L30, Sharpa), and Yuequan Bionic shows a Y-Hand M1 with 38.

Six motors, twelve joints. Everyone moves, but six make the decisions. Rather like a board meeting.

What does this mean for a buyer? Grabbing a tote, pressing a button or turning a handle needs 6 active DoF. Small parts, tools and soft objects need more, and that is a different price bracket.

### Force: fingers are not weightlifters

The second number is force. The RH56DFX delivers up to 15 N at the fingertip and 10 N at the thumb, weighs 540 g and repeats to ±0.2 mm. The DH-5-6 offers 25 N per finger and 80 N with all fingers, at 790 g.

Fifteen newtons is about one and a half kilograms at a fingertip. Enough to hold a bottle of water, not enough to carry a ten-kilo box of parts. For that the robot uses its whole arm, with the hand just stopping the load from slipping. If your task needs a strong grip, you probably want an industrial gripper, not a dexterous hand.

A strong hand and a skilled hand are different hands. Ask any pianist who has tried to open a jar.

### Touch: why fingers need skin

Fingers without touch grip like hands in winter gloves: possible, but with extra force to be safe. Tactile sensors let a robot know that an object is in hand, that it is slipping, that it is soft.

Examples: the DH-5-6’s optional multi-point tactile sensing with a response under 0.62 ms, a pressure range up to 2 MPa and a life above 5 million cycles. PaXini, founded by alumni of Waseda University’s Sugano Lab, makes tactile sensors measuring 15 dimensions, including six-axis force and texture, with 0.01 N force resolution; its sensors start at US$49. Some hands now cover whole fingers in tactile skin, which pushes the sensor count into dozens or hundreds. Hence our title: forty sensors in a hand is now a modest number.

Touch matters for fragile, soft or slippery items: fruit, bags, cables. For identical rigid boxes it is usually overkill.

### What a hand costs

Hand prices span perhaps the widest range in robotics. Not long ago a dexterous hand cost 50,000–100,000 yuan or more. Chinese entry models now start at around US$1,500. Published examples: Linkerbot O6 lite at 3,999 yuan, AgiLink OmniHand Agile at 9,800 yuan, Linkerbot L30 at 100,000 yuan, Yuequan Y-Hand M1 at about US$85,000. A European distributor lists the Inspire RH56DFX at €4,980 including VAT.

That is roughly a 150-fold spread. For comparison, a base Unitree G1 costs 99,000 yuan in China. The industry puts hands at 10–20% of a humanoid’s cost, more for high-end builds; Morgan Stanley estimated about 17% for Tesla Optimus.

Two hands can cost half a robot. A robot’s hands, like a person’s watch, tell you what the budget was.

All prices are public manufacturer or distributor prices, for reference only, not Aura prices.

### Hand or gripper: five questions

1.  How many different items will the robot handle? One or two usually means a gripper.
2.  Does it need to manipulate an item in hand (turn, regrasp) or just pick and place?
3.  What force and what mass? Dexterous hands are weaker than grippers.
4.  Is the item fragile, soft or slippery? Then you need touch.
5.  What about service life and repair: cycles between maintenance, can a single finger be replaced, how long does a spare hand take to arrive?

A sixth question is data. A dexterous hand almost always comes with training: teleoperation, demonstrations, simulation. A hand without a program is a grand piano without a pianist: lovely furniture.

### What we do

When selecting, we look at the task, not the finger count. Sometimes the answer is a humanoid with dexterous hands, sometimes the same humanoid with a simple gripper, sometimes a cobot with a gripper for much less money. We calculate payback for each option, buy directly from Chinese manufacturers, show the actual unit with its serial number on video and test it before shipment. To see hands working on a production line rather than a show stand, join an Aura Robotics Tour.

### The bottom line

Five fingers on a robot look impressive. Two fingers are often enough.

And “do we need a hand?” is a question best asked before purchase. Afterwards it tends to become “why did we buy a hand?”
