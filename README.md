# Automated Python Data Processor

A robust, production-ready Python script designed to handle real-world business data pipelines. This project demonstrates core competencies in Python file I/O operations, structural data cleaning, exception handling, and automated reporting.

## 🚀 Key Features
* **File Parsing:** Dynamically reads and tokenizes unstructured raw text data.
* **Smart Data Cleaning:** Utilizes custom fallback logic (`try-except` equivalencies) to safely catch and normalize corrupt or missing values (`NA`, `missing`) without crashing the pipeline.
* **Automated Analytics:** Computes performance metrics, total scores, and percentage averages on the fly.
* **Executive Reporting:** Generates a beautifully structured text file (`performance_report.txt`) ready for management review.

## 📁 Project Structure
* `raw_grades.txt`: Simulated incoming messy data source.
* `process_grades.py`: The core automation and calculation engine.
* `performance_report.txt`: The final clean output report.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Concepts Used:** File Handling, List/Dictionary Manipulation, String Formatting, Conditionals.
