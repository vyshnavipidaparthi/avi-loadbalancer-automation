# Avi Load Balancer Mock API Automation Framework

## Overview
A lightweight Python automation framework that interacts with a **Mock Avi Load Balancer API**.  
It automates API workflows such as authentication, fetching virtual services, disabling a target service, and verifying results.  
The framework supports configuration through YAML, parallel execution, and simulated SSH/RDP actions.

---

## Features
- Modular Python structure (API handler, test runner, mocks)
- YAML-based configuration
- Parallel test execution (multi-threading)
- Mock SSH and RDP components
- Console and file logging

---

## Requirements
- Python 3.8 or newer  
- Internet connection  
- Packages listed in `requirements.txt`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Configuration
Edit **`config.yaml`** with your API credentials and target service name:
```yaml
api:
  base_url: "https://avi-mock-api-production.up.railway.app"
  username: "<your_username>"
  password: "<your_password>"
  target_vs_name: "backend-vs-t1r_1000-1"

tests:
  parallel: true
  num_threads: 2
```

---

## Folder Structure
```
avi_test_framework/
├── main.py
├── config.yaml
├── requirements.txt
├── logs/
│   └── output.log
└── framework/
    ├── api_handler.py
    ├── test_runner.py
    └── mocks.py
```

---

## Running the Project
From the project root:
```bash
python main.py
```

The script will:
1. Authenticate to the mock API  
2. Fetch available Virtual Services  
3. Identify the target Virtual Service  
4. Disable it via a PUT request  
5. Validate the change and record logs

---

## Example Output
```
🧵 Running tests in parallel mode...
✅ Login successful
📡 Fetching Virtual Services...
⚙️  Updating VS → enabled=False
✅ Virtual Service successfully disabled!
```

---

## Deliverables
- Python source files  
- YAML configuration  
- requirements.txt  
- README.md  
- logs/output.log (execution proof)

