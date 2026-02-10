first stage interview: 1 hour split into two. 30 mins conversation with two directors and 30 mins technical assessment (python task).

focus areas (for the conversation): 

- Python fundamentals (conceptually)
- SQL Joins & Aggregations
- Dataframes
- Data Quality & failures
- End-to-End pipeline thinking

focus areas (for the python task): 

- loops
- dicts / sets
- conditionals
- basic date handling
- writing a clean function
- explaining your logic out loud



five core focus area for conversation:

*problem breakdown & reasoning 

can you think before you code?

clarify requirements:
- so who is the source of the data?
- what options are there for extraction? 
- are there any constraints? 
- what transformations are needed? like datetime manipulation, joining tables to generate a new column, or simply adding an additional column, deduplications, nulls, normalising casings, safeguards to detect failures
- where is the new data going? and at what frequency?
- alerts in place for failures 
- who are the users? or key stakeholders?

i like to approach the design using the medallion archiecture of bronze, silver, gold. 

state assumptions = say what you're treating as true, because the question didn't specify it. 

- when information is missing and you cannot clarify it in the moment, you explicitly say what you're assuming so your logic is still correct and transparent. so how you handle ambiguity.
- making uncertainty visible

edge cases = the awkward, messy situations that break otherwise 'normal' logic. 
the "what could go wrong?" layer! 
> empty input, null identifiers, duplicate rows caused by joins, a mixed time zone, strings instead of timestamps, etc.

That upfront thinking (the design), usually saves time later and makes failures easier to detect and fix. 

*python fundamentals










