---
number: 54
date: "2026-12-24"
lang: "en"
title: "The Robot Phones Home: Cloud, Telemetry and Data From Chinese Robots"
seo_title: "What Data Does a Chinese Robot Send Home? Telemetry, Cloud, Russian Data Law and Critical Infrastructure"
meta_description: "What robots send to the manufacturer’s cloud, how offline mode works, what research into Unitree Go1 and G1 found, Russian data localisation and critical infrastructure rules, and what to put in the contract."
slug: "robot-phones-home-cloud-telemetry-data-from"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/07_Блог_Aura_Robotics_60_статей.docx"
image: "2026-12-24_robot-phones-home-cloud-telemetry-data-from.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "7e8982d5-a2e9-40bc-a99f-ea4eff45b6aa"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic photo in a bright factory server corner next to a robot cell: a smiling young IT specialist plugs a network cable into a small industrial switch in an open network cabinet with blinking green lights, an engineer holding a laptop discusses with her, through the glass partition behind them a robot arm works, cables neatly labeled with blank tags, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, calm confident mood of knowing where the robot's data goes. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

The machine tools of the past were the strong, silent type. They stood in the corner, worked, and spoke to nobody except their operator, and only about business. A modern robot is more sociable. It has Wi-Fi, a cloud account, a phone app and sometimes a habit of checking in with its manufacturer. It reports diligently, like a model employee. The only question is: to whom?

At Aura Robotics we source robots directly from Chinese factories, and with clients we discuss not only payload and cycle time but where the robot sends its data. We will leave geopolitics aside; our blog has already covered US restrictions. This is the practical view: what is known, what to check, what to put in writing.

### 1. Why a robot needs the cloud

Telemetry is not automatically espionage. Usually it is service.

**Diagnostics.** Error logs, drive temperatures and battery health let a factory engineer find faults without a site visit.

**Updates.** Firmware, fixes and new navigation or walking features, especially for humanoids and mobile robots.

**Fleet management.** Maps, tasks and statistics for cleaning, delivery and warehouse robots often live in a cloud dashboard.

**Model training.** For AI-driven robots, operating data is raw material for better algorithms. This is where the interests of manufacturer and customer diverge most.

The problem is not that a robot transmits data. The problem is that the customer often does not know what.

### 2. What the research found

Two public cases involving Unitree robots have become textbook examples, worth knowing whatever brand you buy.

**Unitree Go1, March 2025.** Researchers disclosed CVE-2025-2894: an undocumented remote access channel through the CloudSail service from Oray. It started at boot and created a tunnel through which anyone with a valid API key could take remote control of the robot and reach the network it was connected to. According to the researchers, Unitree revoked the known key two days after being notified. The advice: disable the tunnel service and change default credentials.

**Unitree G1, September 2025.** Alias Robotics published a study of the G1 humanoid. It reported that the robot sent telemetry packets to servers in China every five minutes: battery state, joint torques, motion state, service data. The researchers also described a flaw in the Bluetooth Low Energy channel used for Wi-Fi setup: a shared hardcoded encryption key and missing input filtering allowed someone nearby to run commands with root privileges.

The lesson is not about one brand. Any connected robot is a computer with cameras, microphones, lidar and access to your network. Treat it like a computer, not like a lathe.

A robot on your network is an employee with a pass to every office. Issue that pass deliberately.

### 3. Offline mode: the first question for the seller

Many industrial robots, such as arms, [cobots](/en/catalog/cobots) and most AMRs, run fully on site: controller, PLC and fleet server are local and need no internet. It gets harder with robots whose features partly live in the cloud: voice assistants, apps, over-the-air updates, some AI functions.

Ask before you buy:

- Does the robot work without internet, and what stops working?
- What data goes where when it is connected? Is that documented?
- Can cloud services and telemetry be switched off without voiding the warranty?
- How are updates installed without permanent internet: locally, from media, on request?
- Are there remote access services on board, and how are they enabled?

If the answer to “what does it send?” is “nothing to worry about”, that is an answer to a different question.

### 4. What Russian law says

**Personal data (Federal Law 152-FZ).** If a robot films people, records voices or handles customer data, that may count as personal data processing. Since 1 July 2025 an amended Article 18(5) requires that recording, organising, accumulating, storing, updating and retrieving Russian citizens’ personal data take place in databases located in Russia. Cross-border transfer is possible, but with notification to the regulator, Roskomnadzor, and under set rules. For a waiter robot with a camera or a promotional humanoid in a shopping centre, this is not theoretical.

**Critical information infrastructure (Federal Law 187-FZ).** If the company is a critical infrastructure operator in energy, transport, chemicals, metals and other sectors, the bar is higher. Law No. 58-FZ, in force since 1 September 2025, requires owners of significant critical infrastructure facilities to use Russian software from the national registry, with hardware requirements and transition deadlines set by the government. For an inspection robot at a substation, sign-off from the security team is a mandatory step, not a formality.

We are not lawyers and do not give legal opinions. But the rule is simple: if the site has an information security team, it should see the robot before the robot sees the site.

### 5. What to do on site

- **Separate network segment.** The robot and its server sit in an isolated network or VLAN without direct access to the internet or the office network.
- **Allow-list connections.** If the cloud is needed, permit only the required addresses and ports; block and log the rest.
- **Change default passwords** and disable unused services: Bluetooth, remote access, debug interfaces.
- **Remote access on request.** The manufacturer’s engineer is connected for the job and disconnected afterwards, with a log entry.
- **Controlled updates.** Firmware goes on after testing, with a backup and a rollback option.

### 6. What to put in the contract

1.  A list of data the robot sends to the manufacturer, and why.
2.  Offline operation and its limits.
3.  The customer’s right to disable telemetry and cloud services without losing warranty.
4.  Remote access procedure: who, when, at whose request.
5.  Update procedure and notification of fixed vulnerabilities.
6.  Support period for the model and software version.

### How we help

We source robots directly from more than 100 Chinese manufacturers, and one team stays with the client from selection to launch. Questions about data, offline mode and remote access can be put to the factory during selection, not after the robot is already on your network. We show the actual unit, serial number included, on video from the factory floor and test it before shipment.

### The bottom line

They used to say the walls have ears. Now the walls have Wi-Fi, and the robot driving along them has cameras, a microphone and a cloud account.

That is fine, as long as you know whom the robot is calling. A good employee reports to the boss. Just make sure the boss is yours.
