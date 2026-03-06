Why Batch first Incremental loads and CDC where needed: 

avoids unnecessary streaming complexity while still capturing data changes efficiently.

this lowers operational overheads,
scalable ingestion 
easier pipeline management and ability to evolve to streaming later 


why airflow: 

helps to manage dependencies, scheduling, retries and monitoring in a controlled way.

this results in reliable pipeline execution, easier failure recovery 
and clear pipeline observability. 

why append-only raw dataset:

preserve original source data and avoids modifying ingestion records 


this results in full auditabiliy, easier debugging and reliable recovery if downstream
transformations fail. 



why dbt:

allows for resuable transformation, easier model maintenance and improves data quality


why the gold layer:

pre-aggregated curated models reduces heavy joins and repeated transformations 
in downstream queries. 

This results in faster queries, lower compute cost and consistent metric definitions.


why seperate serving layers? 

each workload has different query patterns and security needs. 

To support these needs, isolating the workload can help incident scaling and prevent 
compute contention. 


why RLS? 

using RLS filtered by customer_id will secure tenenat isolation within a shared 
dataset. 

This would prevent cross-tenant exposure, avoids creating thousands of dataset 
and scales better for SaaS platform. 


why environment seperation? 

seperate dev, staging and prod prevents dev work from impacting prod. 

This allows for safer deployments, controlled testing before release and production
stability. 


why IaC:

Provisioning infrastructure using terraform (terragrunt) defines infrastructure 
through version-controlled code. 

This will result in reproducible environments, consistent deployments and prevents
configuration drift. 


why Incremental pipelines?

Incremental processing instead of full refreshes processes new or changed data only.

This lowers compute cost, enables faster pipelines and safe reruns from last 
successful state. 

Partioning & Clustering? 

partioning large tables in BigQuery to limit data scanning during queries which 
results in faster query performance and reduces scan costs. 


why Observability?

Monitoring, DBT tests and alerts can detect failures and data quality issues early.

This will strengthen operational visibility, faster incidents resolution and a more
reliable platform. 



Why LLM semantic layer? 

Curated semantic dataset for AI querying can prevent LLM from accessing raw complex
schemas. 

This can help AI to read simpler queries, reduce hallucination risk and maintain 
a control on data exposure. 


Layered architecture: 

Raw, silver and gold deperation. 

Seperating ingestion, transformation and serving responsibilities allows for easier 
debugging, modular development and safer platform evolution. 




