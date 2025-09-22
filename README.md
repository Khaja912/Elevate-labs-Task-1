# Elevate-labs-Task-1
Perfect ✅ Here’s a **short, professional summary** you can directly use in your **GitHub README.md** for the Netflix dataset cleaning project:

---

# 🎬 Netflix Movies & TV Shows Dataset Cleaning

This project cleans and prepares the **Netflix Titles dataset** for analysis using **Python (pandas)** and **WPS Spreadsheets (Excel)**.

---

## 📌 Cleaning Steps

1. **Load Dataset**

   * Import `netflix_titles.csv` into Python (pandas) or WPS Excel.

2. **Handle Missing Values**

   * Fill blanks with placeholders:

     * `director` → *Unknown*
     * `cast` → *Not Available*
     * `country` → *Unknown*
     * `date_added` → `01-01-1900`
     * `rating` → *Unknown*
     * `duration` → *Unknown*

3. **Remove Duplicates**

   * Dropped duplicate rows (none found in dataset).

4. **Standardize Text**

   * `country` → Title Case
   * `rating` → Uppercase
   * Removed extra spaces

5. **Convert Dates**

   * `date_added` converted to **DD-MM-YYYY** format.

6. **Rename Columns**

   * Lowercase with underscores (`show_id`, `date_added`, `release_year`, etc.).

7. **Fix Data Types**

   * `release_year` → integer
   * `date_added` → datetime

8. **Save Cleaned Dataset**

   * Exported as `netflix_cleaned.csv`.

---

## ✅ Final Outcome

* Clean, consistent, and analysis-ready dataset
* Suitable for **EDA (Exploratory Data Analysis)**, **visualizations**, and **machine learning models**

---

👉 Do you want me to also format this README with **code snippets** (Python cleaning script) included, so others can directly run it from GitHub?
