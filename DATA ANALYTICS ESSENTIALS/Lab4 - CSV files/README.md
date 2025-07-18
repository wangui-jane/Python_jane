# Lab — Working with CSV Files

## Part 1: Opening a CSV File

### Step 1: Open Bike Sales_Lab.csv in a Text Editor

**Q1. How many columns are in the file? What are the column headings?**  
The file contains six columns:  
- `Date`  
- `Age_Group`  
- `Product_Category`  
- `Order_Quantity`  
- `Unit_Price`  
- `Revenue`  

**Q2. What is the delimiter used to separate the columns?**  
The delimiter is a comma (`,`).

### Step 2: Open Bike Sales_Lab.csv in Excel

**Q3. How many columns are displayed in Excel? Are these the same columns that you noted in the previous step?**  
Excel displays six columns with the same headings: `Date`, `Age_Group`, `Product_Category`, `Order_Quantity`, `Unit_Price`, and `Revenue`.

---

## Part 3: Fixing Common Errors in Importing CSV Files

### Incorrect File Type Error

**Q4. How would you change the extension to fix the error?**  
Rename or resave the file with a `.csv` extension (for example, change `Bike Sales_Lab.txt` or `Bike Sales_Lab.xlsx` to `Bike Sales_Lab.csv`).

### Missing Header Row Error

**Q5. How would you add the missing header row in Excel?**  
1. Open the CSV in Excel.  
2. Right-click the first row and choose **Insert** to add a blank row above.  
3. Enter the required column names in the new row 1.  
4. Save the workbook as CSV.

**Q6. How would you add the missing header row in a text editor?**  
1. Open the CSV in a text editor.  
2. Insert a new first line with the comma-separated header names.  
3. Save the file with a `.csv` extension.

### Missing Information in Columns and/or Rows

**Q7. How would you locate the empty cells in Excel?**  
Use **Go To Special**:
1. Select the entire sheet or relevant range.  
2. On the Home tab, click **Find & Select** → **Go To Special**.  
3. Choose **Blanks** and click **OK** to highlight all empty cells.

Alternatively, use **Conditional Formatting**:
- Home → **Conditional Formatting** → **Highlight Cell Rules** → **Blanks**.

---

## Challenge Activity

**Q8. How would you locate all blank entries in a large worksheet? What Excel functions can help?**  
- **COUNTBLANK:** `=COUNTBLANK(A1:Z1000)` returns the total number of blank cells in the range.  
- **ISBLANK:** `=IF(ISBLANK(A2),"Blank","Not Blank")` flags individual cells.  
- Use **Go To Special (Blanks)** or **Conditional Formatting (Blanks)** to visually locate them.  
