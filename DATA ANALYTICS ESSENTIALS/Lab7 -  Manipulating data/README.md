# Lab — Manipulate Data

## Part 1: Combine Data in an Excel Spreadsheet

1. **Examined the data** in `Bike Sales_Manipulate_Lab 4.2.7.csv`.
2. **Inserted** a new column N to the right of Column M.
3. **Entered** in N2:  
   `=L2 & ", " & M2`  
   – which produced, for example,  
   `mountain-200 silver, 42`.
4. **Filled down** the formula from N2 through N89.
5. **Converted** formulas to text:  
   - Copied N2:N89  
   - Pasted **Values** over L2:L89  
6. **Deleted** the now‐empty helper columns M (Size) and N (formula).

---

## Part 2: Conditional Data Formatting

1. **Revenue Column**  
   - **Between 5 000 and 10 000** → Light Red Fill  
   - **Greater than 10 000** → Green Fill  
   - **Less than 5 000** → Yellow Fill  
   - **Sorted** the sheet by Revenue (largest to smallest) to group highlights.

2. **Profit Column**  
   - Cleared prior formatting.  
   - Applied **Above Average** → Light Red Fill for all profits > average.

3. **Country Column**  
   - Cleared prior formatting.  
   - Highlighted cells **containing “Australia”** → Green Fill.

---

## Reflection Question

> **How could dynamic conditional formatting be useful in a presentation?**

- **Immediate Visual Feedback:** Automatically highlights key values (e.g., top performers, outliers) so the audience instantly sees what matters.  
- **Live Updates:** As data changes during a demo or “what-if” scenario, formatting (and any dependent averages or thresholds) updates in real time—demonstrating impact dynamically.  
- **Focus Attention:** Guides viewers’ eyes to important data points without manual reformatting, reinforcing narrative flow.  
- **Consistency & Accuracy:** Ensures uniform application of rules across large tables, reducing human error and maintaining a polished look throughout.

---
