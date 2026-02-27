What is your understanding of who TheyDo is? 

"From what I understand, TheyDo helps large companies get a clearer picture of their customer journeys. So instead of different teams working in silos, it brings everything into
one structured place, so they can actually see where customers are struggling and decide what to prioritise. And I think the interesting part is that it connects those journeys to 
real business outcomes, not just visual maps."

- My understanding is that it's a platform that helps companies manage and optimise customer journeys in a more structured way, especially at enterprise scale.


Why TheyDo specifically? What stood out to you about us?

"What stood out to me is that you're not just creating visual journeys maps, you're helping enterprises actually prioritise and opertionalise customer experience. From what I 
understand, the platform brings together different teams and data into one structured system, so companies can clearly see where customers are struggling and tie that back to 
measurable outcomes. I'm really interested in that intersection between customer insight and real business impact, especially enterprise scale. That feels like a meaningful space to
build in."




So tell me about your experience?

- So I'm currently working as a data engineer in a production environment where I own pipelines end-to-end. From pulling data from external systems through to transforming it
and making sure stakeholders can rely on it.

pause

- A big part of my role is taking quite messy or unclear business requirements and turning them into structured datasets. I spend a lot of time thinking about modelling properly
so things are scalable and easy to maintain.

pause 

- And I'd say the other thing I focus on a lot is reliability. I've worked on reducing operational issues by seperating concerns in pipelines, adding monitoring, and making sure
failures don't create big downstream problems.


what's motivating you to explore new opportunities at this stage in your career? 

"I've learned a lot in my current role around building reliable production systems and owning pipelines end-to-end. At this stage, I'm looking for something with more 
architecural ownership and impact, ideally in a SaaS environment. I'm particularly interesting in working closer to product, where the data layer directly supports 
decision-making and feature development. That kind of end-to-end ownership and product proximity is something I'm really motivated by."



We're a fully remote, async team with a lot of autonomy. How do you work in environments where there isn't a lot of structure or ticket assignment? 

"My first role at GoPuff was fully remote, so I'm comfortable working async and managing my own priorities. In environments with high autonomy, I make sure I'm clear on outcomes and
impact rather than just tasks. I tend to structure my own work based on what will unblock others or move the needle most, and I communicate proactively so there's visibility even
without constant meetings. I actually enjoy that level of ownership, it pushes me to think more strategically about what I'm building."



What would success look like for you in your first six months here? 

By six months, I'd expect to have taken full ownership of at least one meaningful initiative and delivered measurable impact from it. I'd want to be fully comfortable with the data
platform and ecosystem, and understand how it connects to product and business priorities. I'd also aim to have built strong working relationships across product and engineerings so
I can proactively identify opportunities rather than react to requests. For me, success would mean I'm trusted to shape decisions, not just execute tasks. 



Questions for the talent manager: 
- How is the data team currently structured? and how does this role fit into the broader growth plans?
- How close does the data team work with product and engineering?
- From your perspective, what traits tend to stand out in candidates who do really well in this team?



> PART 2 -

Can you walk me through a data system you designed end-to-end, including the key decisions you made? 

one project I worked on was rebuilding the PayPal ingestion pipeline for payments reporting. The business needed accurate weekly consolidated payment data, but the existing solution was unreliable and only captured a single day due to an API limitation. 

When I reviewed the API constraints, I discovered it only allowed single-day extraction. So instead of continuing with a weekly monolithic load, I redesigned the system into two pipelines: a daily ingestion pipeline that extracted and stored raw data and a seperate aggregation pipeline that consolidated those daily files into a weekly output for downstream processing. 

The key decision was seperating ingestion from aggregation. That improved failure isolation, simplified retries and reduced operational risk. The trade-off was slightly more orchestration complexity, but the reliability gains justified it. 

As a result, we replaced an unusable dataset with a trusted payments table that now supports accurate reporting on PayPal transactions, including different PayPal payment types. It significantly improved confidence in payment-related KPIs. 



what makes a good data model? 

a good data model has a clearly defined level of detail, seperates measurable events from descriptive context and uses consistent keys to maintain clean relationships between 
tables. It avoids duplication and unecessary complexity, making it easy to understand and extend. Ultimately a good model supports accurate analysis while remaining 
maintainable over time. 



how do you see data engineering enabling our AI platform? 

For an AI-powered platform, the quality of the output is directly tied to the quality of the underlying data. If the data is inconsistent, poorly modelled or unreliable, the ai 
layer can produce misleading insights. Data engineering ensure that entities are clearly defined, relationships are structured and pipelines are reliable and reproducible. 
That foundation allows AI features to operate consistently and scale with confidence. 




growth outside day-to-day

outside of my day-to-day work, I focus on deepening my understanding of scalable data architecture and modelling patterns, especially around designing systems for long-term 
maintainability. I also spend time exploring how AI capabilities integrate with structured data platforms, because I'm interested in building systems that enable intelligent 
features, not just reporting. 


what specifically have you improved? 

I think I've become more deliberate. Before, I might focus on getting something working. Now I think more about structure up front - how it could fail, how it could scale and where someone else could easily understand it later. 


Questions: 
what are the biggest data platform challenges you're currently facing?
> data foundation
When you're deciding who to move forward with for this role, what tends to stand out most to you or what qualities are you mainly looking for?  
>communication
>sense of ownership
-If I joined, what would success look like in the first 6 months?
> subject matter expert for the infrstrastucture ( a lot of reverse engineering)
> pick one, two of those to generate results (with tangible action). 
