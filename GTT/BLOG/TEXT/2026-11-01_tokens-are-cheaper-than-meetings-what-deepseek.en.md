---
number: 1
date: "2026-11-01"
lang: "en"
title: "Tokens Are Cheaper Than Meetings: What DeepSeek Did to the AI Budget"
seo_title: "DeepSeek for Business: High-Flyer and Liang Wenfeng, V3, R1, V4 and V4.1, API Prices as of October 2026, and What to See in Hangzhou"
meta_description: "How a Hangzhou lab spun out of a quant fund made the market recalculate the cost of AI: DeepSeek models from V3 to V4.1-Flash, MIT-licensed open weights, API prices as of October 2026, what adoption looked like inside Chinese companies, and the questions worth asking in Hangzhou."
slug: "tokens-are-cheaper-than-meetings-what-deepseek"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/08_Блог_Global_Tech_Tour_66_статей.docx"
image: "2026-11-01_tokens-are-cheaper-than-meetings-what-deepseek.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "bde0aaa8-2e00-4160-8918-ecca0feb5571"
image_cost: "0.5"
image_logos: "DeepSeek"
image_prompt: "Photorealistic candid photo in a sunny modern office in Hangzhou with a window view of green hills and a lake: in the background a long conference table with neatly pushed-in empty chairs, in the foreground two young colleagues at a small standing desk with a laptop laugh as they solve a task in minutes, a third colleague brings them coffee, the laptop screen is blurred with no readable characters, bright natural light, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, light energetic mood of AI that costs less than a meeting. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

Not long ago, AI sat in most company budgets as a single line called “innovation”: a round number, a vague purpose and no one expecting to report on it. Then [DeepSeek](/en/companies/deepseek) arrived, and the line had to be broken down. The intelligence itself, it turned out, costs pennies. Everything around it does not.

Here is what the Hangzhou company actually changed, what its models cost as of October 2026, and why an executive planning a trip to China should look less at the model and more at what people do with it.

### Where DeepSeek came from

The story is short and has no garage in it. In 2015 Liang Wenfeng, a [Zhejiang University](/en/companies/zhejiang-university) graduate, co-founded the quant fund High-Flyer in Hangzhou. The fund traded by algorithm, and algorithms need compute. In July 2023 the fund’s research lab was spun out as DeepSeek, financed by the fund with no outside investors.

The V3 model came out in December 2024. Its technical report contained the number everyone quoted: the final training run took 2.788 million H800 GPU hours, about $5.6 million. The same report stated plainly that this covered only the final run, not the research and experiments before it. That sentence was quoted rather less often.

On 20 January 2025 DeepSeek released R1, a reasoning model with open weights under the MIT licence. A week later, on 27 January, Nvidia shares fell about 17% and the company lost roughly $589 billion in market value, which Bloomberg called the largest one-day drop in market history.

The market repriced AI in a single trading session. Companies needed a little longer.

### What it means for business: three things

**Price.** DeepSeek models have been an order of magnitude cheaper than Western peers from the start, and that has not changed. The official pricing page in October 2026 lists two models. DeepSeek-V4.1-Flash costs $0.15–0.30 per million input tokens and $0.60–1.20 per million output tokens. DeepSeek-V4-Pro costs $0.66–1.32 and $1.98–3.96. The lower figure applies off-peak (Chinese night hours, weekends and Chinese public holidays), the higher one during weekday peaks. AI now has a night tariff, like electricity. Prices change often, so check them again before you build a business case.

**Open weights.** You can call the model over the internet, or download it and run it on your own servers. For companies that cannot send data outside (banks, manufacturers, healthcare, the public sector), that is not a detail but a precondition. The latest model at the time of writing, V4.1-Flash, released on 10 September 2026, is also MIT-licensed.

**Pace.** V3.1 arrived in August 2025, V3.2 in December, and V4 on 24 April 2026: 1.6 trillion parameters in the largest version, a one-million-token context and, for the first time, support for [Huawei](/en/companies/huawei) Ascend chips. V4.1-Flash followed in September 2026. Any model choice now goes out of date faster than the implementation contract gets signed.

### A hypothetical calculation

This is an illustration, not a quote. Say a company handles 10,000 customer messages a month. For each one, the model reads about 3,000 tokens (the message plus instructions) and writes about 500. That is 30 million input and 5 million output tokens a month.

At October 2026 peak rates, V4.1-Flash comes to roughly $9 for input and $6 for output, about $15 a month. V4-Pro comes to about $60.

Now compare that with the cost of one meeting held to decide which model to pick. Tokens have become the cheapest line in the budget. People, integration, data and time remain the expensive ones.

### What adoption looked like in China

In the winter and spring of 2025 a wave swept through China: local governments, state-owned companies, banks and hospitals announced they had connected DeepSeek. A think tank cited by China Brief counted 72 provincial and city governments that had “fully deployed” the model by early March.

By summer the Chinese outlet Leiphone, summarised by researcher Jeffrey Ding, had a more sober picture. Most deployments came through “all-in-one machines”, servers with the model preinstalled, sold to customers who already bought hardware from the vendor. Repeat orders were rare. Deployment took months of testing, on-site debugging and staff training. One salesperson said inquiries fell from hundreds a day in early March to just over ten after April. Many buyers wanted to be seen adopting the model rather than to measure what it did.

You can buy a model in a day. Putting it to work takes rather longer.

That is the main lesson for an executive. China’s experience does not say AI fails. It says the model alone does not work; the combination does: data, process, integration and people who know why they are doing it. It also says that announcing a deployment and completing one are two separate events, sometimes far apart.

### 2026: the company grows up

In 2026 DeepSeek did what many assumed it never would and took outside money. According to The Information, the first external round exceeded 50 billion yuan at a valuation above $50 billion. Reported investors included Tencent, battery maker CATL and a state fund, and outside investors reportedly received no voting rights. Reuters reported that the company is preparing to list on Shanghai’s STAR Market. No timetable has been announced, and when there is a prospectus, we will read it before we write about it.

The practical takeaway: DeepSeek is turning from a research phenomenon into a supplier with investors, a pricing policy and, probably, future disclosures. It can and should be treated as a supplier.

### Why go to Hangzhou

DeepSeek does not give tours and shows no sign of starting. The reason to go is the environment it grew out of. Hangzhou puts Zhejiang University, Alibaba’s headquarters and cloud business, robot makers and game studios within a short drive of one another. In 2025 local media grouped six local companies, DeepSeek and Unitree among them, as the “six little dragons of Hangzhou”. We covered the city as a technology cluster in our piece on China’s three robotics hubs.

For an executive, the most useful stops are not labs but companies that have already put open models to work: manufacturers, logistics operators, retailers, and the integrators selling those all-in-one machines. They can show you what model leaderboards cannot: what the whole project cost and how long it took.

### Six questions to ask on site

1.  Which model and which version are you running now, and how often do you switch?
2.  Is it on your own servers or called via the cloud? Why?
3.  How long from decision to first result?
4.  What turned out to be the most expensive part: hardware, data, integration or people?
5.  How do you measure the effect? Show us one before-and-after number.
6.  What did you try and abandon? (The most useful question, and the one answered least willingly.)

### The bottom line

DeepSeek made the world recalculate the cost of artificial intelligence. The recalculation showed that intelligence has become cheap. Experience, unfortunately, still sells at the old price.

A model downloads in minutes. Knowing what to do with it still has to be brought back from the trip.
