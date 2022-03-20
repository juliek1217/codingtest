-- Count the EMployees
-- The data for the number employed at several famous IT companies is maintained in the COMPANY table. Write a query to print the IDs of the companies that have more than 10000
SELECT ID FROM COMPANY
WHERE EMPLOYEES >= 10000;