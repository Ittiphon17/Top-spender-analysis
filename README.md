# Top Spender Analysis Project

**Assignment for:** Pre-interview, Full-time Workflow Automation Implementer

## 📂 Project Structure & Components

This repository contains the following key components:

### 1. Data Generation

The dataset, consisting of **10 million transaction records**, was programmatically generated to simulate a real-world scenario.

* **Tool Used:** Python
* **Script Location:** `/python/generate_data_10M.py`
* **Methodology:** To efficiently manage memory and processing, the script generates the data in **10 separate chunks**. These chunks are then combined to form the complete 10 million record dataset.
* **File:** `large_order_data_2024_10M.csv` (10,000,000 records)
* **Link:** [**Download Dataset from Google Drive**](https://drive.google.com/drive/folders/1jhWFa6HSGFsyMHxMZxaRgeLziqqbZ2KV?usp=sharing)

### 2. Analysis Script

The analysis to identify the top 10 spenders was conducted using a Jupyter Notebook, which provides a clear, step-by-step documentation of the process.

* **Tool Used:** Jupyter Notebook
* **Script Location:** `/notebook/get_top_spender.ipynb`
* **Objective:** To process the 10M record dataset and calculate the total spending for each customer, then rank them to find the top 10.

### 3. Analysis Result

The final output of the analysis is a CSV file containing the list of the top 10 spenders and their total transaction amounts.

* **Result File:** `top_spender.csv`
---
