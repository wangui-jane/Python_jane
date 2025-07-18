# Lab: Preparing Data

## Part 1: Explore a Sample Set of Data

### Step 1: Open and Inspect
- Opened **Bike Sales_Prepare_Lab 3.4.7.xlsx** in Excel.
- Expanded truncated columns to view full data.

### Step 2: Review Data Issues
Identified issues that could skew analysis:
1. **Duplicate Entries** in **Sales_Order #**  
   - Orders **261695** appear in rows 2 & 3  
   - Orders **261701** appear in rows 8 & 9  
2. **Missing Values** (blank cells) at:  
   - **Day** (row 12)  
   - **Age_Group** (row 17)  
   - **Product_Description** (row 23)  
   - **Order_Quantity** (row 24)  
3. **Combined Fields** in **Product_Description** (model, size, and color all in one cell).  
4. **Extra Spaces** in **Country** entries (leading, trailing, and embedded).  
5. **Inconsistent Text Case** in **Country** (mix of upper/lower).  
6. **Zero Values** in **Unit_Cost** & **Unit_Price** (row 9).  
7. **Abbreviated Gender Codes** (`F`/`M`) reduce readability and consistency.

---

## Part 2: Data Cleaning

### Step 1: Finding Duplicates
- Highlighted duplicates in **Sales_Order #** via Conditional Formatting.

### Step 2: Fixing and Removing Duplicates
1. Corrected row 3’s **Sales_Order #** from 261695 → **261696**.  
2. Deleted the exact duplicate row 9 (duplicate of row 8).

### Step 3: Finding & Filling Empty Cells
- Highlighted blanks in the sheet via Conditional Formatting.  
- Filled blanks with source values:  
  - C12 → **5**  
  - G17 → **Youth (<25)**  
  - M23 → **Mountain-200 Black, 42**  
  - N24 → **4**

### Step 4: Parsing `Product_Description`
- Inserted columns and used **Text to Columns**:  
  1. Split on comma → extracted **Size** into new column N.  
  2. Split on space → extracted **Color** into new column O.  
- Renamed column M → **Model**, N → **Size**, O → **Color**.

### Step 5: Removing Extra Spaces
- Used **LEN** to detect extra spaces in **Country**.  
- Applied **TRIM** in a helper column, then **Paste Values** back to **Country**.  
- Deleted helper columns.

### Step 6: Standardizing Text Case
- Added a helper column and used **LOWER()** to convert **Country** to lowercase.  
- Pasted values back and removed helper column.

### Step 7: Highlighting & Correcting Zero Values
- Highlighted zeros in **Unit_Cost** & **Unit_Price** via Conditional Formatting.  
- Corrected row 9’s values:  
  - **Unit_Cost** = 1252  
  - **Unit_Price** = 769  

### Step 8: Find & Replace Gender Codes
- Replaced `F` → `Female` (50 replacements).  
- Replaced `M` → `Male` (39 replacements).

### Step 9: Spell Check
- Ran Excel’s Spelling tool on all text columns.  
- **0** misspelled words found.

### Step 10: Remove Formatting
- Cleared formatting from **Age_Group** column to reset alignment.

