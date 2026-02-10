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




- list > use it when order matter, duplicates are allowed and you just want to iterate through items.
"I use a list when I have an ordered collection of items and duplicates are allowed, for example looping through raw records."
visual example:
users = ["u1", "u2", "u2"]

- dictionary > use it when grouping data, counting things, mapping IDs to values.
"I use a dictionary when I want to map a unique key to a value, for example grouping or counting records by day or user."
visual example:
spend_by_user = {
    "u1": 120.50,
    "u2": 75.00
}

- set > use it when you want to dedupe, track uniqueness and check if you've already seen something.
"I use a set when uniqueness matters, for example ensuring a user is only counted once per day."
visual example:
unique_users = {"u1", "u2", "u3"}

one sentece to summarise all 3: 
"lists preserve order, dictionaries map keys to values and sets enforce uniqueness"


- loops > use a for-loop to iterate over each records so I can process them one at a time.

- conditionals > decides what happens and what doesn't.
if conditions is true > do something
if conditions is false > skip or do something else

- functions > a named block of reusable logic.
use functions for:
- resuability (call it again with new data).
- readability (code is easier to follow).
- testability (easy to test one piece of logic.
- seperation of concerns (each function does one job).

"I wrap logic in functions to make the code reusable, testable, and easier to reason about". 



I'm comfortable with python fundamentals. I use lists for ordered data, dictionaries for grouping and counting, and sets for uniqueness. I rely on for-loops to process records, conditionals to handle different data scenarios, and functions to keep logic reusable and testable. 




*SQL fundamentals (joins, aggregations, correctness) 

- joins:
> inner join - returns only rows that match in both tables
> left join - returns all rows from the left table and matches from the right if they exist, otherwise null.

The key risk: row duplication
"when numbers look inflated, the first thing i check is join cardinality and whether the join is duplicating rows before aggregation."


- aggregation and group by:
> aggregation reduces many rows into fewers rows.
> group by defines the level of granularity of the result set.


- where vs having: this is about when filtering happens.
> where means filtering rows before aggregations and limits rows 
> having filters after aggregation and limits groups 

"where filters individual rows before aggregation, having filters aggregated results."

when debugging SQL, I usually start by checking rows counts at each stage, validating join logic, and making sure filters are applied in the correct place. 


"I'm comfortable with SQL fundamentals: joins, aggregation, and filtering. I'm especially careful about join cardinality and filter placement, because those are common sources of incorrect results. When debugging, I validate assumptions by checking row counts and aggregations step by step."



*dataframes (pandas / pyspark thinking)

- A dataframe is a tabular data structure with rows and columns, similar to a SQL table.

core dataframes: 
- filtering rows > keeps only rows that meet a condition
"I filter Dataframes to restrict rows based on conditions, similar to a WHERE clause in SQL."

- selecting columns > chooses relevant fields
"I select only the columns I need to reduce complexity and improve clarity".

- creating derived columns > add new columns based on existing ones
"I often create derived columns for easier grouping or analysis, like extracting dates from timestamps."

- grouping & aggregation > summarises data
"Grouping and aggregation lets me summarise data at the required granularity, just like group by in SQL."

-validation and sanity checks:
> row counts before and after transforms
> null checks on key columns
> uniqueness checks
> basic distribution checks

"After transformations, I sanity-check row counts and key columns to make sure the output matches expectations."




SQL and Dataframes solve similar problems. I tend to use SQL for straightfroward querying and aggregation, and dataframes when I need more flexible logic or step-by-step transformations. 


I'm comfortable working with dataframes. I regularly filter rows, select columns, create derived fields, and aggregate data. I always validate transformations by checking row counts and key columns, and I choose between SQL and dataframes based on the complexity of the logic. 




*real-world data engineering, trade-offs & communication

"most of my experiences is with production pipelines where reliability and data quality matter more than perfect inputs."

common trade-offs: 
- batch vs real-time
- speed vs reliability
- simplicity vs flexibility
- one-off fix vs scalable solution

"Given the business need, I chose a batch approach because it was more reliable and easier to monitor, even thought it meant higher latency."




- failures, monitoring and alerts > expect failures, detect early, don't silently ship bad data
"I assume pipelines will fail at some point, so i design with monitoring and alerts in place to detect issues early.

> row count checks
> schema checks
> missing file detection
> alerting on failures


- communication and stakeholders
"when issues occur, I focus on explaining the impact in business terms, not just technical details, and setting expectations around resolution."











