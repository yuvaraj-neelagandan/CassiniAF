# API Automation Framework (PyTest + Allure)

## Install
```bash
pip install -r requirements.txt
```

---

## Run tests and generate Allure report
```bash
pytest -m smoke --alluredir=reports
pytest --alluredir=reports
allure serve reports
```

---

## How to get GoRest API Token
1. Visit: https://gorest.co.in/
2. Click on **Get Access Token**
3. Sign in (Google/GitHub)
4. Copy your token and paste it into `.env` as:
   ```
   GOREST_TOKEN=your_token_here
   ```

---

## Allure Report Screenshots

Below are screenshots from the generated Allure HTML Report showing various views captured after test execution.

### 1. Dashboard Overview
Displays the overall execution summary including passed, failed, and skipped test counts.  
![Allure Report - Overview](reports/1.png)

### 2. Test Suites Summary
Shows the grouping of test cases, their hierarchy, and execution status for navigation.  
![Allure Report - Test Suites](reports/2.png)

### 3. Detailed Test Results
Illustrates each test case with step details, assertions, and expected vs actual results.  
![Allure Report - Test Details](reports/3.png)

### 4. Execution Steps and Logs
Shows step-by-step execution flow with attached logs and validation details.  
![Allure Report - Execution Logs](reports/4.png)

### 5. Attachments and Artifacts
Displays screenshots, responses, and other artifacts captured during test execution.  
![Allure Report - Attachments](reports/5.png)

### 6. Graphs and Trends
Provides visual analytics for execution trends and performance statistics.  
![Allure Report - Graphs and Trends](reports/6.png)
