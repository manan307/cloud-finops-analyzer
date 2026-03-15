# Cloud FinOps Analyzer

Cloud FinOps Analyzer is a Python-based dashboard that simulates cloud infrastructure usage and analyzes cloud cost patterns using FinOps principles.

The system detects idle resources, identifies potential cost savings, and visualizes cloud spending through an interactive Streamlit dashboard.

---

## Problem Statement

Organizations using cloud platforms such as:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)

often face challenges in managing cloud costs effectively.

Common problems include:

- Idle compute resources running unnecessarily
- Over-provisioned infrastructure
- Unexpected spikes in cloud spending
- Lack of visibility into service-level costs

This project demonstrates how FinOps techniques can help monitor and optimize cloud spending.

---

## Features

- Cloud cost monitoring dashboard
- Service-level cost analysis
- Idle resource detection
- Estimated cost savings calculation
- Cost anomaly detection
- Dynamic cloud workload simulation
- Interactive dashboard using Streamlit

---

## Project Architecture

Cloud Data Generator  
        ↓  
Cloud Usage Dataset (CSV)  
        ↓  
Cost Analysis Engine  
        ↓  
Optimization Rules  
        ↓  
Streamlit Dashboard  

---

## Tech Stack

Programming Language:
- Python

Libraries:
- pandas
- streamlit

Tools:
- Git
- GitHub
- VS Code

---

## Project Structure
cloud-finops-analyzer
│
├── analyzer.py
├── app.py
├── data_generator.py
├── rules.py
├── requirements.txt
├── .gitignore
│
└── data
└── cloud_cost.csv


## How to Run the Project

### 1. Clone the Repository
git clone https://github.com/manan307/cloud-finops-analyzer.git


### 2. Navigate to Project Folder/ Change Directory
cd cloud-finops-analyzer


### 3. Create Virtual Environment
python -m venv env


### 4. Activate Virtual Environment

Windows: env\Scripts\activate

Mac/Linux: source env/bin/activate


### 5. Install Dependencies
pip install -r requirements.txt


### 6. Run the Application
streamlit run app.py



---

## Dashboard Features

### Total Cloud Cost
Displays the total cost of all simulated cloud resources.

### Service-Level Cost Breakdown
Shows spending distribution across services such as EC2, RDS, S3, and Lambda.

### Idle Resource Detection
Resources with CPU utilization below 5% are flagged as idle.

### Optimization Suggestions
The system recommends stopping or downsizing unused resources.

### Cost Anomaly Detection
Detects sudden increases in cloud spending.

---

## Dynamic Cloud Data Simulation

The dashboard includes a button:

Generate New Cloud Data

Clicking this button generates new simulated cloud resource data and updates the dashboard.

---

## Future Improvements

- Integration with real cloud APIs (AWS, Azure, GCP)
- Kubernetes cost monitoring
- Machine learning based cost anomaly detection
- Multi-cloud cost comparison

---

## Author

Manan Poddar

GitHub:  
https://github.com/manan307

---

## License

This project is created for educational and demonstration purposes.


