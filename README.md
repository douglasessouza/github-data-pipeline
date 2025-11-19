# 🔄 GitHub Data Pipeline  
*A fully automated Python pipeline that fetches repository metadata from the GitHub API, processes the data using pandas, and uploads the results back to GitHub using the Content API.*

---

## 📌 Overview  
This project demonstrates a real-world **Data Engineering workflow**, including:

- Extracting data from a public API (GitHub REST API v3)  
- Processing and transforming the data with Python (pandas)  
- Saving clean outputs as CSV  
- Automating upload of the processed files to another repository  
- Organizing the solution into a professional engineering folder structure  

This end-to-end pipeline can be extended to cloud workflows (AWS/GCP), job scheduling (Airflow/Prefect), or data warehouse ingestion (BigQuery/Snowflake).

---

## 🏗️ Architecture

```markdown
## 🏗️ Architecture

```mermaid
flowchart TD
    A[Fetch Repositories (GitHub API)] --> B[Process Data (pandas)]
    B --> C[Save CSV Files]
    C --> D[Upload CSV via GitHub Content API]
    D --> E[Target Repository (github-language-analysis)]


## **Project Structure**
github-data-pipeline/
│
├── src/
│   ├── fetch_repos.py        # Class to extract GitHub repo metadata
│   ├── transform_repos.py    # Functions to clean & process data
│   ├── upload_files.py       # Class to upload CSVs via GitHub API
│   ├── main_fetch.py         # Runs extraction + transformation
│   └── main_upload.py        # Runs file upload automation
│
├── requirements.txt
├── README.md
└── .gitignore


⚙️ **Technologies Used**
- Python 3.10+
- pandas — data transformation
- requests — API requests
- base64 — encoding for GitHub content uploads
- GitHub REST API (v3)
- Virtual environment (venv) — dependency isolation

