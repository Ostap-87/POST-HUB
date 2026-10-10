---
number: 17
date: "2026-11-23"
rubric: "Tech (роботы)"
category: "tech"
lang: "en"
title: "Copying Allowed"
subtitle: "Chinese robot makers are giving away millions of recorded movements that cost them entire data factories. Why would the top student hand their homework to the whole class?"
meta_description: "AgiBot World has more than a million trajectories from a hundred robots, Beijing’s RoboMIND has been downloaded 20 million times, and Lightwheel has released 100,000 hours of first-person video. Why Chinese companies hand competitors free data to train robots, and what they get in return. A wry essay."
excerpt: "Chinese robot makers are giving away millions of recorded movements that cost them entire data factories. Why would the top student hand their homework to the whole class?"
tag: "Robots"
time: "5 min"
slug: "copying-allowed"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/09_Личный_блог_Tech_50_статей.docx"
---

> “Can I copy your homework?” “Sure. Good luck reading my handwriting.” — A schoolyard exchange. Now an industry strategy.

Every school class has an unwritten hierarchy. The top student does the homework. Everyone else copies it. The top student pretends to mind, but hands over the notebook. Even back then, I suspect, they got more than they gave: influence, respect, and the right to decide whose handwriting counts as correct.

I copied. Let me admit that up front to avoid awkwardness later. Nobody considers my handwriting correct to this day.

China’s robotics industry today works like that class. Except the notebooks cost millions of dollars. And the top students hand them out without being asked.

## The internet can’t teach you to walk

Start with what robots actually need to learn from. A language model can learn from the internet: there’s endless text, and people spent forty years writing it for free. A robot doesn’t need text. It needs movement. How to pick up a mug. How to fold a towel. How not to crush an egg. None of that is on the internet. Every movement has to be recorded: a human operates the robot, the robot repeats, the sensors log it.

GF Securities, cited in Chinese media, estimates that embodied AI models need at least 10 million hours of such data, and the world has collected less than 5% of that. By the end of June 2026, China had more than 70 data collection sites running and 46 more planned or under construction.

The internet can teach you to talk. It can’t teach you to walk. We knew that already, from people.

## The thickest notebook in human history

The first serious shared textbook was the international Open X-Embodiment dataset from 2023: 22 different robots, 21 research institutions, 527 skills. A workbook pieced together from many schools, in many handwritings.

Then, at the end of 2024, Shanghai’s AgiBot published its own. AgiBot World holds more than a million trajectories from a hundred robots across more than two hundred tasks, recorded at the company’s own data factory together with the Shanghai AI Lab. In spring 2025 it added an open model, GO-1, which its authors say performs about 30% better on average when pre-trained on this dataset than on Open X-Embodiment.

A million trajectories. That’s a million times someone showed a robot how to pick up, put down, open and close. As a school notebook, it would be the thickest one in human history. And it was given away.

There’s one detail I, as a marketer, like most. All hundred robots in the dataset are AgiBot’s own model. So the textbook is free. But it was written for a particular brand of desk.

## Twenty million downloads

Speaking of the state. The Beijing Humanoid Robot Innovation Center released its RoboMIND dataset, and at the end of 2025 a second version: more than 310,000 trajectories for two-armed robots, six robot types, over 700 tasks and a separate set of recordings with tactile sensors. In September 2026 the center said downloads had passed 20 million, doubling in the previous month.

Twenty million downloads. Nobody has downloaded my slide decks that many times, and I emailed them to everyone.

In spring 2026, the robot maker Leju started an open embodied-AI dataset community under the OpenAtom open-source foundation and released a dataset that labels 41 robot joints. And Shanghai’s Lightwheel, together with Hugging Face, used this summer’s World Robot Conference to release 100,000 hours of first-person video: people cooking, cleaning and fixing things, with a camera on their heads recording it all. That’s no longer a textbook for robots. It’s a textbook about people, written for robots to read.

Frankly, I’m a little worried. If robots learn everything from us, they’ll learn procrastination too.

## The textbooks are free, the money is in the desks

Now the real question. Why? Why would companies locked in a fight to the death give each other their most valuable asset?

Here’s an absurd answer in five points. All honest except the last.

1.  Nobody has enough data. When everyone is thirsty, you dig the well together and fight over the buckets later.
2.  Different companies’ data don’t stack: different formats, different labeling, different hands. Whoever releases the most for free first gets to set the format. And formats are forever. Ask anyone who’s tried to plug a laptop in abroad.
3.  A textbook recorded on your robots works best on your robots. A free textbook is the best ad for a paid desk.
4.  Students and researchers who trained on your data later come looking for jobs. At your company. Already up to speed.
5.  Sharing is beautiful. It says so in the press releases. Sometimes people even believe it.

The textbooks are free. The money is in the desks.

It’s the same logic as China’s open-weight language models, which I’ll write about separately. Except there they give away the brains, and here they give away the muscle memory.

## Four or five names before yours

That’s about it. No, not quite.

I remember how textbooks were passed down at my school. You got them from the library, and inside the cover was a little table: name, class, year. Four or five names before yours. And notes in the margins: something underlined here, a doodled face there, a problem someone solved right in the book and probably got scolded for.

You read the textbook, and you read everyone who studied before you.

Chinese robots are learning from that kind of book now. It holds millions of movements made by people the robot will never meet: someone’s hand picking up a mug, someone’s hand folding a towel.

Copying is allowed. Just remember whose notebook it was.

**Sources**

1.  Global Times, сентябрь 2026 — https://www.globaltimes.cn/page/202609/1369689.shtml (RoboMIND: 20+ млн скачиваний, 300 000+ траекторий, 700+ задач; оценка GF Securities: не менее 10 млн часов, накоплено менее 5 %; 70+ тренировочных площадок к концу июня 2026 г. и 46 в планах или стройке по данным CAICT и Синьхуа).
2.  iTiger / CLS, «Beijing Humanoid Robot Innovation Center’s Open-Source Dataset RoboMIND Surpasses 20 Million Downloads», 02.09.2026 — https://www.itiger.com/news/1122828665 (20 млн скачиваний, удвоение за месяц).
3.  arXiv 2512.24653, «RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence», 31.12.2025 — https://arxiv.org/abs/2512.24653 (310 000+ траекторий, шесть типов роботов, 739 задач, 12 000 эпизодов с тактильными данными).
4.  The Robot Report, «AgiBot releases humanoid manipulation dataset to enable large-scale learning», 30.12.2024 — https://www.therobotreport.com/agibot-releases-humanoid-manipulation-dataset-to-enable-large-scale-learning/ (более 1 млн траекторий, 100 роботов).
5.  OpenDriveLab, «AgiBot World Colosseo» — https://opendrivelab.com/AgiBot-World (217 задач, 100+ однотипных роботов AgiBot G1, модель GO-1, около 30 % прироста к обучению на OXE, партнёры: Shanghai AI Lab, HKU).
6.  arXiv 2310.08864, «Open X-Embodiment: Robotic Learning Datasets and RT-X Models», 2023 — https://arxiv.org/abs/2310.08864 (22 робота, 21 организация, 527 навыков).
7.  iTiger, «China’s First Open-Source Community for Embodied AI Datasets Established», 19.03.2026 — https://www-web.itiger.com/news/1183769806 (сообщество открытых датасетов по инициативе Leju и OpenAtom, набор OpenLET, 41 сустав).
8.  KuCoin News, «Global First: Guanglun Intelligence Opens Source 100,000 Hours of Human Data», 08.2026 — https://www.kucoin.com/news/flash/global-first-100-000-hours-of-human-data-open-sourced-by-guanglun-intelligence (Lightwheel, EgoSuite-Open100K, 100 000 часов, с Hugging Face, WRC 2026, несовместимость форматов разных компаний).
