# Lab — Using VLOOKUP in Data Analysis

## Reflection Questions

1. **Retrieve the Cost of a particular order**  
   ```excel
   =VLOOKUP(V3, A$2:S$753, 18, FALSE)
— Looks up the Sales_Order# in cell V3 within the table A2:S753 and returns the value from the 18th column (“Cost”).

## Retrieve the Revenue of a particular order

=VLOOKUP(V3, A$2:S$753, 19, FALSE)
— Looks up the same Sales_Order# and returns the value from the 19th column (“Revenue”).
## Challenge Activity
- Using VLOOKUP on other datasets

- Identify your lookup key (e.g. Customer_ID, Product_Code) and ensure it’s in the leftmost column of your table.

- Define the table array to include all rows and columns you need (e.g. A2:G1000).

- Choose the column index for the field you want to retrieve (its position relative to the lookup column).

- Decide on exact match (FALSE) vs. approximate match (TRUE or omitted) based on whether your data is sorted and you need the closest value.

## To fetch a customer’s email by their ID entered in cell H3, from a table in A2:G200 where the email is in column 5:
=VLOOKUP(H3, A$2:G$200, 5, FALSE)
