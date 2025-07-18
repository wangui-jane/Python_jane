# Lab — Combining Relevant Data in Excel

## Part 2: Refreshing Data in Multiple Worksheets

### Step 1: Summarize Linked Data

1. **Value in Cell A2** (`=AVERAGE(﻿BikeSales_2021.xlsx!Q2:Q14)`)  
   **Answer:** 26,479.31

2. **Value in Cell B2** (`=AVERAGE(﻿BikeSales_2021.xlsx!R2:R14)`)  
   **Answer:** 43,764.31

### Step 2: Update & Refresh

3. **After updating Q6 to \$30,000 and refreshing**, what happens to A2?  
   **Answer:** A2 increases to **28,019.15**

4. **After refreshing Sheet1**, what is the value in cell Q6?  
   **Answer:** 30,000.00

---

## Reflection

**When would you use workbook links to keep data synchronized?**  
- **Multi-year reporting:** Consolidate each year’s sales file into a single dashboard without merging raw sheets.  
- **Departmental summaries:** Link individual department workbooks into a central KPI report.  
- **Large datasets:** Split very large tables across smaller files and link only the needed ranges.  
- **Role-based views:** Create separate reporting files for finance, marketing, etc., all driven by the same master data.  
- **Distributed collaboration:** Allow teams to maintain their own source files while a consolidated workbook stays up-to-date automatically.  
