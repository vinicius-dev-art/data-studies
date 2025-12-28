# Titanic Dataset Cleaning with Pandas

This project provides a Python script to clean and normalize the Titanic dataset,
preparing it for exploratory data analysis and machine learning tasks.

The main focus is to practice data cleaning techniques using the pandas library
while applying good software engineering practices.

---

## 📌 Problem Statement

The original Titanic dataset contains missing values and is stored in a
non-standard CSV format, where each row is enclosed in double quotes.
This formatting prevents direct parsing using standard CSV readers.

---

## ⚙️ What the Script Does

- Normalizes a malformed CSV file before loading it into pandas
- Loads the Titanic dataset into a structured DataFrame
- Handles missing values in categorical columns
- Removes rows with remaining missing values
- Saves a cleaned version of the dataset for further analysis

---

## ▶️ How to Use

1. Place the dataset file inside the `data/` directory.
2. Run the script from the project root:

python code01.py

## 💾 The cleaned dataset will be saved as:

data/Titanic-Dataset-cleaned.csv

## 📂 Project Structure
├── code01.py
├── README.md
└── data/
    ├── Titanic-Dataset.csv
    └── Titanic-Dataset-cleaned.csv

## 🛠️ Technologies Used

- Python 3
- pandas
- pathlib

## ⚠️ Important Note

The original dataset is stored in a non-standard CSV format where each row is
enclosed in quotes and internal quotes are escaped.
The script includes a preprocessing step to normalize the file before loading
it into pandas.

## 🚀 Possible Improvements

- Add logging instead of standard output
- Make missing-value handling configurable
- Add unit tests
- Validate dataset schema automatically