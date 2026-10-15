---
number: 32
date: "2026-11-27"
publish_time: "15:00"
rubric: "Tech (искусственный интеллект)"
category: "tech"
lang: "zh"
title: "自己的模型，别人的权重"
subtitle: "韩国和日本都在造“主权AI”，既不想靠美国，也不想靠中国。结果发现，最难的是先说清楚什么叫“自己的”"
meta_description: "韩国国家AI基础模型评选：Naver因用了阿里千问的视觉编码器出局，Upstage被指与智谱模型相似后自证清白；日本Sakana AI估值26.5亿美元，政府牵头的Noetra项目投入最高一万亿日元。一篇关于“以中国为标尺的主权”的随笔。"
excerpt: "韩国和日本都在造“主权AI”，既不想靠美国，也不想靠中国。结果发现，最难的是先说清楚什么叫“自己的”"
tag: "人工智能"
time: "6 分钟"
slug: "sovereign-with-borrowed-eyes"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/09_Личный_блог_Tech_50_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "1ec208d9-3fe0-4bed-9d78-013f797703f8"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic photo on two adjacent apartment balconies in Seoul at dusk: one neighbour leans over the low partition to hand a pair of binoculars to the other, both laughing, potted plants and drying laundry on the balconies, the Han River, its bridges and the city lights spreading out before them under a violet sky, wide 16:9 composition with a calm, uncluttered lower-left corner, warm friendly mood: everyone borrows eyes from a neighbour, then learns to see on their own. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

——模型是你们自己的吗？ ——自己的。 ——全部？ ——大脑自己的，架构自己的，训练自己的。 ——眼睛呢？ ——眼睛……跟邻居借的。好眼睛，开源的，大家都在用。 ——那就不算自己的。

这不是段子。换成大白话，这就是2026年1月韩国科学技术信息通信部里发生的事。要聊亚洲的“主权AI”，我觉得从这段对话开始最合适。

2025年，韩国启动了国家级AI基础模型项目，目标是做出能和中美模型掰手腕的本土模型。入选的有五支队伍：Naver Cloud、SK电讯、LG AI研究院、NC AI，以及创业公司Upstage。政府给算力、给期限、给淘汰赛制——像选秀节目，只不过奖品不是汽车，是国家荣誉。

## 眼睛是跟邻居借的

2026年1月第一轮评审，Naver Cloud和NC AI出局。Naver的事闹得最大：它的模型性能和易用性得分都不错，但用了阿里开源千问的预训练视觉编码器和权重。视觉编码器，说白了就是模型的“眼睛”，负责把图像变成机器能理解的信号。

主管部门态度很硬：用别人的预训练权重，就不符合“独立性”标准；起码要把权重清零、从头训练。第二次官柳济明就是这么说的。Naver回应说，架构和推理引擎都是自研的，编码器可以替换。学者们则说，用开源组件是全世界的通行做法。媒体小心翼翼地提了一句：“中国因素”。

所谓主权，就是什么都能自己做。也正因为如此，谁都不会真的全部自己做。

## 最重的怀疑：肚子里是千问

两周前，韩国还上演过另一出。2026年1月1日，一家小公司的负责人在社交媒体上说，Upstage的Solar Open 100B和中国智谱的模型很像，某一层权重的相似度高达96.8%。Upstage没有在评论区吵架，而是提出邀请外部专家公开验证、在YouTube上直播，并表示愿意公开代码。第二天，指控者道了歉，承认个别层相似并不能证明抄袭。

元旦被指控，1月2日就洗清了。很多人家过年的剩菜都没吃完这么快。

但请注意，大家拿什么当尺子：不是美国模型，是中国模型。2026年，一个亚洲AI开发者能听到的最重的怀疑是：“你肚子里不会是千问吧？”

## 眼睛不能借，肌肉可以借

比赛继续。2月，Motif Technologies递补入围。2026年8月，第二轮结果公布：LG AI研究院（K-EXAONE 2.0）、SK电讯（A.X K2）、Upstage（Solar Open2）晋级；Motif出局——尽管它的模型在Artificial Analysis的榜单上进了全球前十，官方的理由是实用性得分偏低。下半年，晋级团队将获得约1000块英伟达B200，第三轮评审定在2026年下半年。

有意思的是，主权AI是用美国芯片训练的。眼睛不能借，肌肉可以借。看来眼睛离灵魂更近。

## 安静、客气，还带着鱼

再看日本。日本的主权，是日本式的：安静、客气，还带着鱼。

Sakana AI 2023年在东京成立，创始人是前谷歌研究员David Ha、Llion Jones和伊藤錬。“sakana”在日语里就是“鱼”：一群小模型，可以比一条大模型更聪明。2025年11月，公司融资200亿日元，估值26.5亿美元，三菱日联金融集团也在投资人之列。它做的是用小数据训练、针对日语和日本文化调优的模型，目前主要服务金融业，下一步是制造业和政府。

中国在造大模型，韩国在查别人的眼睛是谁的，日本在押注一群小鱼。很日本。在一个街角都是自动售货机的国家，“大”从来不是国民运动。

与此同时，日本政府也下了大注。2026年夏天，经济产业省把一个五年项目交给了名为Noetra的联合体：最高一万亿日元，约44家企业参与，核心是软银、索尼、NEC和本田。计划是：2026财年推出日语能力强的推理模型；2028年前做出能处理文字、图像、视频和声音的全模态模型；2030年前做出能驱动机器人和汽车的AI。目标说得一点不客气：既不依赖美国AI，也不依赖中国AI。

2026年7月通过的第二版《人工智能基本计划》，把这叫作“开放的AI主权”：不依赖特定供应商，也不依赖特定国家。

开放的主权。这个词我琢磨了很久。大概意思是：门是自己的，但不装锁——免得邻居多心。

## 这些动静其实是一种恭维

从中国这边看，这些动静其实是一种恭维。五年前，主权AI的意思是“不依赖美国”；现在是“既不依赖美国，也不依赖中国”，而且后半句说得格外用力。中国开源模型好用又好拿，邻居们得专门检查一下，家里是不是已经住进来一个。

对一个产品最好的广告，就是竞争对手专门立规矩不许用它。

不过，最后一句话还是留给历史，而不是部委。日文一半是汉字；朝鲜半岛用汉字书写了许多个世纪，直到世宗大王创制了自己的文字，汉字词至今仍留在韩语词典里。今天用来训练主权AI的“主权语言”，本身就是从别人的字里长出来的。

那又怎样？它们后来都成了自己的。花了几百年，但成了。

眼睛谁都借过。学会看，得靠自己。

**来源**

1.  The Korea Herald, «Open-source use, China-linked concerns fuel reputational risks in national AI race», 20.01.2026 — https://www.koreaherald.com/article/10658913 (пять команд, выбывание Naver Cloud из-за визуального энкодера и весов Qwen, позиция министерства и замминистра Рю Чжэ Мёна, критика экспертов, «китайский фактор»).
2.  The Korea Times, «LG AI Research, SK Telecom, Upstage survive next cut in national AI model project», 18.08.2026 — https://www.koreatimes.co.kr/business/tech-science/20260818/lg-ai-research-sk-telecom-upstage-survive-next-cut-in-national-ai-model-project (выбывание Naver Cloud и NC AI в январе, Motif в феврале, итоги второго этапа, K-EXAONE 2.0, A.X K2, Solar Open2, Motif 3 — 10-е место по AAII, около 1000 B200).
3.  Venture Square, «업스테이지 ‘AI 표절 논란’ 종결», 04.01.2026 — https://www.venturesquare.net/1030519/ (обвинение 1 января, 96,8 %, публичная проверка, извинение 2 января).
4.  TechCrunch, «Sakana AI raises $135M Series B at a $2.65B valuation to continue building AI models for Japan», 17.11.2025 — https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan (основатели, 20 млрд иен, MUFG, японский язык и культура, финансовый сектор).
5.  TechCrunch, 19.07.2026 — https://techcrunch.com/?p=3144105 (Noetra: до 1 трлн иен за пять лет, около 44 компаний, SoftBank, Sony, NEC, Honda, этапы 2026–2028–2030, цель не зависеть от американского и китайского ИИ).
6.  Let’s Data Science, «Japan Targets Sovereign AI Model and 10 Million Robots», 01.07.2026 — https://letsdatascience.com/news/japan-targets-sovereign-ai-model-and-10-million-robots-83b74c54 (решение METI о проекте Noetra, первый транш 387,3 млрд иен).
7.  MLex, «Japan adopts second AI basic plan, targets agentic AI and sovereignty», 14.07.2026 — https://www.mlex.com/mlex/artificial-intelligence/articles/2500643/japan-adopts-second-ai-basic-plan-targets-agentic-ai-and-sovereignty («открытый подход к суверенитету», без зависимости от отдельных поставщиков и стран).
