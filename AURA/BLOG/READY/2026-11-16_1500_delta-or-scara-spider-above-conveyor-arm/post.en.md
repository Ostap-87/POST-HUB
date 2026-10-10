---
number: 16
date: "2026-11-16"
publish_time: "15:00"
lang: "en"
title: "Delta or SCARA: The Spider Above the Conveyor and the Arm on the Table"
seo_title: "Delta Robot vs SCARA: Which Robot to Choose for High-Speed Packaging"
meta_description: "Delta robots and SCARAs compared for packaging and sorting: speed, payload, work envelope, mounting, food-grade design and how many robots a line needs. A guide from Aura Robotics."
slug: "delta-or-scara-spider-above-conveyor-arm"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "ca6bc222-7797-4ec8-acbe-481d13b78ccc"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic industrial photo on a bright Russian confectionery packaging line: a ceiling-mounted delta robot with three thin arms picks round cookies from a moving conveyor at high speed with slight motion blur, while on a neighbouring steel table a SCARA robot arm calmly places small parts into a tray, a smiling woman technologist in a white coat and hairnet watches the cookies line up perfectly in plastic trays, clean white stainless-steel surfaces, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, crisp lively mood of the spider above the conveyor and the arm on the table. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

Two robots on a packaging line get mixed up more than any others, even though they look nothing alike. The delta hangs over the conveyor like a three-legged spider and snatches biscuits faster than you can see them. The SCARA sits on the table like a desk lamp with a serious work ethic and places parts precisely into nests.

They get mixed up because both catalogues say the same thing: “high-speed pick-and-place robot”. True. It is just that “pick” and “place” mean different things to each of them.

At Aura Robotics we source robots for packaging and food production directly from Chinese manufacturers. Here is where the delta wins, where the SCARA wins, and how not to buy a spider for a job that needs an arm.

### 1. Design: where the speed comes from

A delta has three (sometimes four) light parallel arms converging on a small platform with the gripper. The heavy motors are fixed at the top, on the base, and only the light linkage moves. Low moving mass means very high acceleration. That is the speed.

A SCARA is an arm of two horizontal links with a vertical axis at the end. It is stiff vertically and compliant horizontally, ideal for inserting a part: you can push down without twisting it. Some motors travel with the arm, so moving mass is higher, but so is payload.

The spider is fast because it is light. The arm is strong because it is not ashamed of its weight.

### 2. Speed: what the datasheet says

Delta. ABB states up to 120 picks per minute for its IRB 365 with 1 kg products. It is a rated figure under specified conditions, but it shows the class: about two operations per second.

SCARA. Inovance gives a standard cycle time from 0.351 s for its IR-S7 series. The standard cycle is a lab test: up 25 mm, across 300 mm, down, and back again. Divide a minute by 0.351 s and you get about 170 cycles, but a real task with vision, a moving conveyor, gripper actuation and real loads will be noticeably slower. The same applies to the delta.

So you do not compare datasheet speeds directly. You compare cycle time on your operation, with your product and your gripper.

Rated speed is speed in a vacuum. Your factory is not a vacuum, although some days it feels that way.

### 3. Payload: grams versus kilograms

The delta is for light items. ABB’s IRB 360 family covers 1 to 8 kg; the IRB 365 handles 1.5 kg. Typical jobs: sweets, biscuits, sachets, blister packs, small bakery products.

The SCARA carries more. Chinese manufacturer [EVST](/en/catalog/industrial/factory/evst)’s SCARA range spans 3 to 20 kg. That covers not just packaging but assembly, tray loading and moving parts and small boxes.

Grams in high volume: look at a delta. Kilograms with precise placement: look at a SCARA. In between, geometry decides.

### 4. Work envelope: dome versus sector

A delta works in the space beneath it, shaped like an inverted dome or a shallow cylinder. IRB 360 covers a diameter of 1.13 to 1.6 m, IRB 365 from 800 to 1,300 mm. Vertical travel is limited: deltas do not like deep cartons.

A SCARA works in a horizontal sector around its base. EVST models reach 400 to 1,000 mm, Inovance IR-S7 500–700 mm. The longer vertical axis makes the SCARA better at lowering product into a deep case or inserting a part.

Precision differs too. SCARAs in the 3–20 kg class offer repeatability of around ±0.01–0.05 mm. That matters for electronics assembly. Not for biscuits: biscuits have no idea what a hundredth of a millimetre is.

### 5. Mounting: a frame overhead or a table alongside

A delta is mounted from above. You need a rigid frame over the conveyor, and its rigidity directly affects speed: if the frame shakes, the robot runs slower or less accurately. The frame is a separate budget line and a separate question about ceiling height and maintenance access.

A SCARA bolts to a table or base beside the line, takes little space and is easier to move. If the line is cramped and there are services overhead, that may decide the matter before speed even comes up.

### 6. Food-grade design

A delta hangs directly above the product, so hygienic design is not an option in food plants, it is a condition. ABB offers a stainless IRB 360 validated to IP69K that can be washed with industrial detergents and high-pressure hot water.

SCARAs also come in cleanroom and protected versions. But if the product is exposed and the line is washed every shift, ask for the specific protection rating and materials, not just the word “food-grade”.

Above exposed food, the robot must be cleaner than the food. Otherwise it is not packaging, it is an ingredient.

### 7. How many robots: an illustrative calculation

For arithmetic only. A line produces 400 sweets a minute, to be placed into trays. Say a delta achieves 100 real picks a minute on this task with vision and conveyor tracking. You need 4 robots, or 5 with a margin for uneven flow and misses.

A SCARA with a real cycle of, say, 0.6 s would manage about 100 operations a minute, but it needs space beside the conveyor and is less suited to picking on the fly. And if the product is 3 kg boxes going into cases, the delta is out on payload alone, and no calculation is needed. (Illustrative numbers. Yours will differ, and that is fine.)

### 8. A short rule

Delta: light product, high throughput, picking from a moving conveyor with vision, hygienic design, room for a frame.

SCARA: heavier product, precise placement or insertion, deep packaging, tray loading, assembly, no room overhead and little room alongside.

### 9. Test the unit, not the catalogue

We select packaging robots from partner factories, calculate cycle time and payback on your product, show you the actual unit with its serial number on video from the factory floor and test it on your operation before shipment. Send product samples if you can: a robot that moves plastic cubes quickly will not necessarily move marshmallows just as fast. You can see these lines in person on an Aura Robotics Tour buying trip.

### The bottom line

The delta is a sprinter you must not give anything heavy. The SCARA is a craftsman you must not rush beyond his pace. A good line is one where each does his own job. A bad one is where the sprinter hauls boxes and the craftsman catches sweets on the fly. Both will cope. Neither will be happy.
