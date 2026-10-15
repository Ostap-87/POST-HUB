---
number: 33
date: "2026-11-28"
publish_time: "15:00"
rubric: "Tech (искусственный интеллект)"
category: "tech"
lang: "zh"
title: "一千二百种语言，一个聊天机器人"
subtitle: "AI为什么说不好泰语和爪哇语？谁在教它东南亚的语言？阿里巴巴又在其中扮演什么角色？"
meta_description: "东南亚语言在互联网上存在感很低，在大模型里也一样。阿里达摩院的SeaLLMs、改用千问底座的新加坡SEA-LION、印尼的Sahabat-AI、马来西亚的ILMU、泰国的Typhoon——谁在教AI说本地话，又是为了什么。一篇自嘲随笔。"
excerpt: "AI为什么说不好泰语和爪哇语？谁在教它东南亚的语言？阿里巴巴又在其中扮演什么角色？"
tag: "人工智能"
time: "6 分钟"
slug: "1-200-languages-one-chatbot"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/09_Личный_блог_Tech_50_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "1ed65b53-6bac-488b-a842-96705439b207"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic candid photo on the wooden veranda of a traditional Javanese house in Yogyakarta in the late afternoon: a young girl holds up a smartphone and speaks into it with a big grin, while her grandmother in a batik sarong laughs beside her and leans in to listen to the answer, a tray of tea and fried bananas between them, tropical plants and warm slanting sunlight, the phone screen not visible, wide 16:9 composition with a calm, uncluttered lower-left corner, warm hopeful mood of a machine learning the language of a grandmother. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

我能用东南亚语言自信说出口的全部内容：

1.  泰语的“谢谢”。
2.  越南语的“谢谢”。
3.  印尼语的“谢谢”。
4.  “不要辣”——所有语言一起上，主要靠表情。
5.  “买单”——用手势。从河内到雅加达，这门语言人人都懂；看上账单的速度，它在当地应该算母语。

清单很短。但事实证明，在这个地区，我和人工智能很长一段时间里水平差不多。区别是，我从来没假装会。

## 互联网上没有的语言

先说最基本的。大模型是从互联网上学的，而互联网上主要是英语，其次是中文，再往后是其他大语种。按当地开发者常引用的说法，东南亚有一千二百多种语言。越南语、泰语、印尼语、马来语、他加禄语、高棉语、老挝语、缅甸语——这些还只是有自己国家的。还有使用者数以千万计的爪哇语，以及巽他语、巴厘语、巴塔克语。人们用它们生活、砍价、唱摇篮曲，只是很少在网上写。

互联网上没有的语言，对机器来说不存在；对说这门语言的奶奶来说，互联网也不存在。算打平。

最早把这当成生意问题、而不是文化问题的，说来有趣，是中国公司。2023年12月，阿里达摩院发布SeaLLMs，参数70亿和130亿，覆盖越南语、印尼语、泰语、马来语、高棉语、老挝语、他加禄语和缅甸语。分析师说得很直白：需要它的，是出海东南亚的中国电商和物流企业——本地主播难招、难管，成本还高。

这才叫真实的需求文档。不是“保护语言多样性”，而是“我们需要一个会用高棉语说‘打折’、还从不请假的销售”。别忘了，阿里在东南亚有Lazada。对Lazada来说，语言不是语言学，是收银台。

科技行业里最诚实的动机，是商业动机。至少它不假装自己是公益。

## 新加坡式中立

再看新加坡——一个凡事先做预算、再做表格的国家。2023年12月，新加坡启动了7000万新元的国家多模态大模型计划，旗舰产品是AI Singapore的东南亚语言模型SEA-LION。

SEA-LION过去一直基于Meta的模型家族。2025年11月发布的Qwen-SEA-LION-v4，底座换成了阿里的Qwen3-32B。Qwen3本身用119种语言和方言训练，新加坡团队又追加了一千多亿个东南亚语言token。新模型在区域榜单SEA-HELM上位列2000亿参数以下开源模型第一，而且32GB内存的机器就能跑——差不多一台好点的笔记本。

新加坡是个从不选边站的中立国。它只选泰语说得最好的那个。这就是新加坡式中立。

## 语言有了“按字计价”

其他邻居则决定：自己的语言自己教。

印尼：2024年11月，电信运营商Indosat和GoTo（Gojek和Tokopedia的母公司）推出Sahabat-AI，意思是“AI朋友”。它懂印尼语、爪哇语、巽他语、巴厘语和巴塔克语；2025年又推出700亿参数版本，并强调数据和算力都留在印尼境内。Indosat的CEO称它是“国家资产”。

马来西亚：2025年8月12日，总理安瓦尔亲自发布ILMU，由YTL AI Labs与马来亚大学联合开发。开发方称，它在马来语测试MalayMMLU上超过了全球头部模型。我没法验证——我的马来语，止步于上面清单的第3条。

泰国：早在2024年初，SCBX集团旗下的SCB 10X就开源了70亿参数的泰语模型Typhoon。按开发方的说法，它处理泰语文本的速度是GPT-3.5的2.62倍。原因在于泰文词与词之间不加空格，用英语训练的模型会把它切得过碎——而每一块都要花钱。

于是，在AI时代，语言有了“按字计价”。泰语原本是一门“贵”语言，现在被降了价。语言学第一次成了降本增效的项目。

## 先来商人，后来词典

把这些放在一起看，画面挺有意思：各国政府讲主权、讲数据本地化、讲国家资产；本地公司用本国语言做模型；而引擎盖下面，越来越多地装着中国开源模型——因为它懂亚洲语言，免费，用之前也不必请示谁。

这不是什么阴谋，只是邻里关系。中国卖家比中国模型先到东南亚，先学会了用当地话砍价，模型跟在后面，就像代表团后面跟着的翻译。

在亚洲，向来如此：先来商人，后来词典。

## 没写过说明书，却唱过无数摇篮曲

最后，有个念头一直放不下。爪哇语有数千万人在说，却几乎没进互联网——不是因为它不好，而是因为人们更多地说它，而不是写它：在饭桌上，在集市上，在村子的晚上。这些语言几乎没写过一份说明书，却唱过无数首摇篮曲。

现在，机器开始学它们了。我愿意相信，这不只是为了收银台。愿意相信总有一天，日惹的某个孩子会用奶奶的语言问手机一个问题，而手机会回答。不完美，带口音，但会回答。

顺便说一句，我说“谢谢”到现在也带口音。大家照样听得懂。

**来源**

1.  Yicai Global, «Alibaba’s Damo Academy unveils AI models geared to Southeast Asia», 13.12.2023 — https://www2.yicaiglobal.com/news/alibabas-damo-academy-debuts-llms-made-for-southeast-asia (SeaLLMs: 7 и 13 млрд параметров, восемь языков, мотивация китайской e-commerce и логистики).
2.  TechNode, «Singapore’s national AI program drops Meta model and switches to Alibaba’s Qwen», 25.11.2025 — https://technode.com/2025/11/25/singapores-national-ai-program-drops-meta-model-and-switches-to-alibabas-qwen/ (Qwen-SEA-LION-v4 на Qwen3-32B, 119 языков, 100+ млрд токенов, первое место в SEA-HELM, программа на 70 млн сингапурских долларов с декабря 2023 г.).
3.  eCommerceNews Asia, «AI Singapore & Alibaba unveil regional model for 1,200 languages», 25.11.2025 — https://ecommercenews.asia/story/ai-singapore-alibaba-unveil-regional-model-for-1-200-languages (более 1200 языков в регионе, 32 ГБ памяти).
4.  FutureCIO, «Indosat and GoTo launch a new 70-billion-parameter model with a multilingual chat service», 06.06.2025 — https://futurecio.tech/indosat-and-goto-launch-a-new-70-billion-parameter-model-with-a-multilingual-chat-service/ (Sahabat-AI с ноября 2024 г., 70 млрд параметров, индонезийский, яванский, сунданский, балийский, батакский; данные в Индонезии; слова Викрама Синхи).
5.  Malay Mail, «PM Anwar launches ILMU, Malaysia’s first home-grown multimodal AI», 12.08.2025 — https://www.malaymail.com/news/malaysia/2025/08/12/pm-anwar-launches-ilmu-malaysias-first-home-grown-multimodal-ai/187359 (YTL AI Labs и Университет Малайя, расшифровка названия, заявления о MalayMMLU).
6.  SCB, «SCB 10X Typhoon», 01.2024 — https://www.scb.co.th/en/about-us/news/jan-2024/scb-10x-typhoon (Typhoon-7B, Apache 2.0, обработка тайского в 2,62 раза быстрее GPT-3.5).
