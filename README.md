# Largest Companies Data Science Project

This project is a university-level implementation that combines data analysis and machine learning using Object-Oriented Programming (OOP) in Python. It is divided into two main components:

1. A Jupyter Notebook for structured data exploration and visualization using OOP principles.
2. A Streamlit-based graphical interface (GUI app) to predict company success probability using a trained Support Vector Machine (SVM) model.

---

## Table of Contents

- [Largest Companies Data Science Project](#largest-companies-data-science-project)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Objectives](#objectives)
  - [Project Components](#project-components)
    - [1. Jupyter Notebook: OOP-Based Data Analysis](#1-jupyter-notebook-oop-based-data-analysis)
      - [Description](#description)
      - [Functionalities](#functionalities)
      - [Main Class: `CompanyData`](#main-class-companydata)

---

## Overview

This project analyzes a dataset of the world's 100 largest companies by market capitalization. It includes data preprocessing, exploratory data analysis (EDA), and prediction of the company’s success probability based on financial and categorical attributes like revenue, employees, sector, and country.

---

## Objectives

- Apply Object-Oriented Programming to structure a data science workflow.
- Perform statistical analysis and visualizations of real-world financial data.
- Build a trained machine learning model (SVM) for predicting success probability.
- Deploy a user-friendly GUI using Streamlit for model interaction.

---

## Project Components

### 1. Jupyter Notebook: OOP-Based Data Analysis

**File:** `projectoop.ipynb`

#### Description

This notebook encapsulates the entire data analysis process in a class-based structure using OOP. It allows for clean, reusable, and maintainable code when exploring and visualizing data.

#### Functionalities

- Load dataset
- Show sample records
- Generate descriptive statistics
- Plot histograms of numerical columns
- Plot heatmaps of feature correlations

#### Main Class: `CompanyData`

```python
class CompanyData:
    def __init__(self, file_path)
    def explore_data(self, n=5)
    def data_statistics(self)
    def plot_histogram(self, column)
    def plot_heatmap(self)
