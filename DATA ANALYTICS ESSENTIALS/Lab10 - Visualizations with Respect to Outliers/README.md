# Lab — Interpret Visualizations with Respect to Outliers

## Part 1: Examine a Dataset for Outliers

1. **Which December date had the largest sales quantity?**  
   - December 19 had the largest daily sales, with a total of **43** orders.

2. **Which entry contributes most to the Sum of Order_Quantity outlier on December 19?**  
   - Sales Order **#000261740** (Quantity 43) is responsible for the spike.

3. **What value is returned by `=LARGE($E$4:$E$27, 1)`?**  
   - **43**, the highest Sum of Order_Quantity in the range.

4. **What function returns the lowest six values?**  
   - Use the `SMALL` function, for example:  
     ```excel
     =SMALL($E$4:$E$27, ROW($1:6))
     ```

## Reflection Questions

**List the factors that could determine whether data outliers should or should not be considered in the final analysis of a dataset:**  
- **Validity of Data:** Exclude outliers caused by data‐entry or measurement errors; retain valid extreme values.  
- **Sample Size & Influence:** In small datasets, removing an outlier can significantly skew results; in large datasets, a few outliers may have negligible impact.  
- **Analytical Purpose:** For modeling typical behavior, you might trim extremes; for risk or peak‐event analysis, you must include them.  
- **Statistical Methods Used:** Some metrics (like mean) are sensitive to extremes—consider using medians or robust estimators if keeping outliers.  
- **Domain Knowledge:** Business or scientific context may dictate that certain extreme values are meaningful (e.g., bulk orders, rare events).

## Challenge Activity

**Consider scenarios where excluding outliers could have significant impact on the final data analysis if excluded from consideration:**  
- **Fraud Detection:** Unusually large transactions are key signals—excluding them conceals fraudulent behavior.  
- **Healthcare Monitoring:** Extreme vital‐sign readings indicate critical conditions—omitting them risks patient safety.  
- **Disaster Response Planning:** Peak loads or traffic spikes during emergencies inform capacity planning—filtering them out underprepares systems.  
- **Marketing Campaign Evaluation:** Promotional spikes reflect campaign success—excluding these outliers underestimates ROI.  
