---
number: 35
date: "2026-12-05"
publish_time: "15:00"
lang: "en"
title: "The Robot Speaks Chinese: Software, SDKs, Localisation and Programming Without an Interpreter"
seo_title: "Chinese Robot Software: Interface Languages, SDKs, ROS 2 and Offline Programming"
meta_description: "How Chinese cobots and humanoids are programmed: teach pendants and graphical tools, scripts, SDKs and ROS 2, offline programming. What to do when menus are only in Chinese and English, and what to check before you buy."
slug: "robot-speaks-chinese-software-sdks-localisation-programming"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "b803bfb9-d3a0-46c2-a844-52198ac9ac46"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic candid photo in a bright Russian workshop: two young engineers at a laptop on a workbench next to a white collaborative robot arm, one typing and the other holding the robot's teach pendant, the robot arm smoothly sets a part into a fixture and both high-five with big smiles, the laptop screen shows blurred abstract lines of code with no readable characters, daylight from large windows, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, triumphant mood of programming the robot without a translator. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

A Chinese robot arrives and the first thing it does is say hello. In Chinese. Then, with luck, in English. Other languages sometimes appear in the menu, and people usually find out whether yours is one of them on commissioning day, just after the interpreter has left.

The good news: a robot is not a novel, and nobody needs to read every menu. The bad news: the parts that do need reading are best checked before purchase. Here is how the software side of a Chinese robot is put together, and where the surprises hide.

### Three levels of conversation

Level one is the pendant or app: a tablet, a teach pendant or a web interface. Operators and technicians use it to set points, assemble programs from blocks, start and stop.

Level two is the manufacturer’s scripting language. When blocks run out, people write code. Each manufacturer has its own, which matters: programming skills on one cobot do not automatically carry over to another.

Level three is the SDK and external control: the interfaces that connect the robot to your PLC, MES, warehouse software or your own Python or C++ program. ROS 2, the open robotics framework used in research and increasingly in industry, lives here too.

Operators need level one, engineers level two, integrators level three. Trouble starts when all three are the same person.

### What specific manufacturers offer

From public documentation:

[Dobot](/en/catalog/cobots/factory/dobot). DobotStudio Pro supports block programming (Blockly), Lua scripting, hand-guided teaching, and TCP/IP and Modbus for external control. On interface language the manual is brief and honest: choose the display language in settings, and if the language you need is not there, contact technical support. Translation: ask in advance.

Elite Robots. CS-series cobots have an open ROS 2 driver listed in the official ROS package index, supporting ROS 2 Humble on Ubuntu 22.04 and relying on the manufacturer’s own SDK. An Elite cobot can join a ROS 2 system without home-made bridges.

[JAKA](/en/catalog/cobots/factory/jaka). The robot is operated through the JAKA Zu app, which, for example, the RoboDK driver connects to over standard Ethernet, so tasks can be programmed and run from an external environment.

Unitree. Openness is part of the business model. GitHub hosts unitree_sdk2 (Go2, B2, H1), a Python version that adds G1, unitree_ros2 for Go2 and B2, a MuJoCo simulator, reinforcement learning code and an imitation learning framework for the G1 and the Dex3 hand. For a research lab, that is close to a ready environment. For a warehouse, it is a toolkit that still needs work.

[AgiBot](/en/catalog/humanoid/factory/agibot). The X2 humanoid comes with AimDK, a set of ROS 2 interfaces in C++ and Python for motion, joints, hands, navigation, voice and diagnostics. Some modules, such as advanced vision, are marked “to be released”.

Note that wherever SDKs are concerned, the languages are C++ and Python and the documentation is in English and Chinese. SDK documentation in other languages is still rare.

### When the menu is not in your language

First, do not panic. An industrial robot’s interface has a few dozen screens; an operator uses five to seven. They can be covered in a short local-language guide with screenshots. That is a day’s work for an engineer, not a translation of War and Peace.

Second, choose the training language. Most Chinese robots have an English interface, which works for technicians. Train on it from day one, so that a year later nobody is pressing buttons by colour.

Third, check whether your language exists, and in which version. Some manufacturers add localisations in particular software releases or at a large partner’s request. “Available” and “available in your version” are different statements; check on the actual firmware of the actual unit.

Menu localisation is like a translated washing machine manual: useful, but people start the wash before they finish reading.

Fourth, leave untranslated menus alone. Service screens, safety parameters and calibration belong to people who read them in the original or work from the manufacturer’s documentation. A misunderstood checkbox in a safety menu costs more than an interpreter.

### Offline programming: learning while working

Offline programming means writing and testing a program in a computer model, then loading it into the robot, which keeps working meanwhile. For welding, painting and complex paths it is standard; for cobots on simple tasks, teaching on site is often enough.

If you plan to program offline, check three things: whether your robot model exists in your chosen tool (RoboDK or the manufacturer’s own simulator), whether there is a post-processor for its controller, and whether the controller version matches the one the tool supports. The last one sounds dull, and it is exactly where projects trip.

### ROS 2: when you need it and when you do not

You need ROS 2 if the robot is part of a system you are building yourself: research, a mobile manipulator, an unusual cell with several sensors. An official driver then saves weeks.

You do not need ROS 2 if the robot does one task and talks to the line through a PLC. There, Modbus, Profinet or EtherNet/IP and digital I/O matter more.

One planning detail: ROS 2 releases have support windows. Humble, which many drivers target today, is supported until May 2027; the next long-term release, Jazzy, until May 2029. For a multi-year project, ask the manufacturer when its driver will move to the newer release.

### Five software questions before you buy

1.  Which interface languages are in the software version the robot will ship with?
2.  What is the manufacturer’s programming language, and is there graphical programming?
3.  Is there an open SDK, in which languages, with what documentation?
4.  Is there an official ROS 2 driver, and for which release?
5.  How is the software updated: does it need internet access, who installs updates, what happens to existing programs?

At Aura Robotics we ask the factory these questions during selection. One team takes the client from model choice to commissioning, so “what language is the menu in?” does not get lost between departments. Before shipment we test the actual unit and show it on video with its serial number, including the pendant screen running the software version that will ship to you. On an Aura Robotics Tour factory visit you can try the software hands-on.

### The bottom line

The robot really does speak Chinese. But it obeys the program, not the language.

And a program, like a good technician, can be taught. You just need to know in advance which language the first lesson will be in.
