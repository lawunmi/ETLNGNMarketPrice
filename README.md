# ETL Pipeline – Nigerian Market Price Data

A modular Python ETL pipeline that extracts Nigerian market price data from a CSV source, applies data transformations and cleaning, and loads the results into a PostgreSQL database. Built as part of a data engineering learning programme to demonstrate real-world pipeline design patterns.

---

## Project Structure

```
ETLNGNMarketPrice/
├── config/          # Database connection and pipeline configuration
├── logs/            # Pipeline execution logs
├── src/             # Core ETL logic (extract, transform, load)
├── market_data.csv  # Source data file
└── .gitignore
```

---

## Pipeline Overview

```
market_data.csv  →  Extract  →  Transform  →  Load  →  PostgreSQL
```

| Stage | Description |
|---|---|
| **Extract** | Reads raw Nigerian market price data from a local CSV file |
| **Transform** | Cleans, validates, and restructures the data for analytical use |
| **Load** | Inserts the transformed records into a PostgreSQL database table |

---

## Tech Stack

- **Language:** Python 3
- **Data Processing:** Pandas
- **Database:** PostgreSQL
- **Configuration:** External config files (no hardcoded credentials)
- **Logging:** Python `logging` module — execution logs written to `logs/`

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL (running locally or via a cloud instance)
- Required Python packages (install via pip):

```bash
pip install pandas psycopg2-binary sqlalchemy python-dotenv
```

### Configuration

Update the database connection settings in the `config/` directory before running the pipeline. Ensure your PostgreSQL instance is running and the target database exists.

### Running the Pipeline

```bash
python src/index.py
```

Logs will be written to the `logs/` directory for monitoring and debugging.

---

## Data Source

The source data (`market_data.csv`) contains Nigerian market price records. The pipeline processes this file on each run, applying transformations before persisting the data to PostgreSQL.

---

## Key Features

- **Modular design** — extraction, transformation, and loading are separated into distinct components
- **External configuration** — database credentials and settings are managed outside the codebase
- **Logging** — pipeline run events and errors are captured in structured log files
- **Reusable structure** — the project layout follows conventions suitable for extension to other data sources or destinations

---

## Future Improvements

- Add scheduling with Apache Airflow to run the pipeline 
- Extend to pull live market price data from a REST API
- Add data validation checks (e.g. null checks, type enforcement) before loading
- Containerise with Docker for easier deployment


