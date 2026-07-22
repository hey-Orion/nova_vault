## HIGH PROBABILITY — have a real story ready

### Apache Airflow
1. Walk me through a DAG you've built — what does it orchestrate, and why did you choose Airflow?
2. How do you handle a task that fails partway through a pipeline — retries, alerting, or both?
3. What's the difference between an Operator and a Sensor, and when would you reach for a Sensor?
4. How do you pass data between tasks in a DAG?
5. Why did you move from a manual/Makefile-based setup to Airflow — what problem did it actually solve?

### Docker / Docker Compose
1. How do you use Docker Compose to spin up a local dev environment with your app and a database together?
2. Walk me through a Docker-related bug you had to debug — what went wrong and how did you find it?
3. How do you keep a production image small and secure?
4. What's the difference between a bind mount and a volume, and when do you use each?
5. How do you manage environment-specific config (dev vs. prod) inside a containerized setup?

### GitHub Actions
1. Walk me through what happens when you push code to `main` in your project's CI/CD setup.
2. How do you handle secrets (API keys, DB passwords) securely in a GitHub Actions workflow?
3. What would you add to a CI pipeline to catch bugs before they reach production?
4. Have you dealt with a CI pipeline that passed locally but failed in Actions — what caused it?
5. How do you structure a workflow to run tests before allowing a merge?

### Logging + Sentry
1. A pipeline fails silently at 3 AM — how do you find out, and how do you trace the root cause?
2. What's your approach to structuring log messages so they're actually useful for debugging later?
3. How do you decide what should be a log statement versus what should trigger an alert?
4. Tell me about a bug you debugged using logs or an error-tracking tool — what was the process?
5. How do you avoid alert fatigue when setting up monitoring for a pipeline?

### PostgreSQL (design/architecture)
1. How would you design a schema for ingesting and storing time-series market/event data?
2. What's your approach to indexing — how do you decide what to index and what not to?
3. How do you handle schema changes on a table that's already in production?
4. What's the tradeoff between normalizing your schema versus denormalizing for read performance?
5. How would you structure a database to support both fast writes (ingestion) and fast analytical reads?

### Git / GitHub
1. What branching strategy do you prefer when working on a team, and why?
2. How do you handle a merge conflict in practice — walk me through your process?
3. What's your commit convention — how do you keep history readable?
4. How do you use pull requests to review your own or a teammate's code?
5. Have you had to revert a bad deploy — how did you use Git to recover?

---

## MODERATE PROBABILITY — one solid sentence, folds into other answers

### python-dotenv
1. How do you manage secrets and config locally versus in production?
2. What's the risk of hardcoding credentials directly in code, and how do you avoid it?
3. How does your app pick up different environment variables in dev vs. prod?
4. What do you do to make sure a `.env` file never ends up committed to Git?
5. How do you structure config for a project with multiple environments (dev/staging/prod)?

### Makefile
1. How do you standardize commands so the whole team runs things the same way locally?
2. What's an example of a repetitive CLI task you automated?
3. Why might a team choose a Makefile over just documenting commands in a README?
4. What's a limitation of Makefiles compared to a proper task runner or orchestrator?
5. How did your Makefile-based workflow compare once you moved to Airflow?

### YAML
1. What configuration files in your stack are written in YAML?
2. What's a common mistake people make with YAML indentation that breaks a pipeline?
3. How do you validate a YAML config before it's used in a Docker Compose or CI file?
4. Why do tools like Airflow, Docker Compose, and GitHub Actions all standardize on YAML?
5. Have you had a pipeline break because of a YAML formatting issue? What happened?

### bash / Linux / shell
1. How comfortable are you navigating and debugging things directly from the terminal?
2. What's a shell script or one-liner you've used to automate a repetitive task?
3. How do you check what's using up disk space or memory on a Linux box?
4. How would you find and kill a process that's hanging?
5. What's your go-to way of tailing and filtering logs from the command line?

---

## LOW PROBABILITY — surface-level only

### AWS/GCP basics
1. Have you used cloud storage (S3 or GCS) to land or archive data?
2. At a high level, how do you think about access permissions (IAM) for a cloud resource?
3. What's the difference between object storage and a managed database service?
4. Have you deployed anything on a cloud VM — what was involved?
5. Why might a team choose managed cloud services over self-hosting infrastructure?

### Networking & Security Basics
1. What's the difference between a public and private subnet, and why does it matter for a database?
2. Why shouldn't a production database be directly accessible from the public internet?
3. What's the basic purpose of a firewall or security group in a cloud environment?
4. How do you think about securing an API endpoint that handles sensitive data?
5. What's the difference between authentication and authorization, at a basic level
