Terminal. make docker_run.

Say:

​"Hi, I'm a DataOps engineer, and I'll start by running the project first, so while it runs, I’ll walk you through the system."

Move README. Small scroll.

Say:

“This is Dataflow Sentinel. I built this to demonstrate how a production data pipeline ensures reliability. The goal is automated data quality enforcement - ensuring we catch schema drifts before they reach downstream analytics.”

Open docs/architecture.md.

Say:

“I’m using a medallion architecture here. Bronze holds raw data, Silver handles Pydantic validation and cleaning, and The gold generates the final aggregates.”

Move cursor across layers.

“I’ve implemented a validation gate. If the payload fails the Pydantic model, the pipeline triggers an alert instead of ingesting bad data.”

Open src/pipeline.py. Small scroll.

Say:

“This is the orchestration logic. The pipeline is fully idempotent. I’m using SQL Upserts so it can safely handle retries without manual cleanup or duplicate records.”

Switch to terminal.

Say:

​"As you can see in the terminal, ingestion and validation are complete. The validated records have been promoted to the database, and the final aggregates are generated."

Open data/gold/. Open aggregates.csv then freshness.json.

Say:

“The Gold folder gives us our final results. These are the analytics-ready aggregates along with freshness metrics to ensure that the data isn’t stale.”

Open GitHub Actions, then switch to Sentry.

Say:

“For production, I’m using GitHub Actions for automation and Sentry for real-time observability and debugging.”

Return to README.

Say:

“Overall, this is a reproducible system designed to prevent data corruption. Thanks for watching!”

Stop recording.
