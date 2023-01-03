# Draft
# Customer Churn Epidemic

# Project Description

The phone company, Telco, is curious as to what is driving their churn rates. Taking a variety of features, I will be looking for correlation to narrow down the factors that might be driving customers to churn.

# Project Goal:

* Find drivers for customer churn at Telco. Why are customers churning?
* Construct a ML classification model that accurately predicts customer churn.
* Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

# Inital Thoughts and Questions

My initial hypothesis is that key variables will have a strong correlation to our target variable, churn, while others will have little to no correlation.

* Do people who use customer support churn more?
* Do people who pay more, whether monthly or total, churn more than those who pay less?
* Do older people churn more often than younger people?
* Does tenure length correlate in churn? Does longer tenure correlate to less churn?

# The Plan

* Acquire data from Sequel Ace database

* Prepare Data
 * drop unwanted columns
      * payment_type_id
      * internet_service_type_id      
      * contract_type_id
      * customer_id
 * drop nulls, duplicates
 * strip white space
 * change data types
 * create dummies
 * drop redundant columns
 
  
* Explore data in search of drivers of churn
   * Answer the following initial questions
       * How often does churn occur?
       * Do customers who use tech support churn more often?
       * Do customers who pay more than the monthly average churn more often?
       * Do senior customers churn more often than younger customers?
       * Do long tenure customers churn more often than short term customers?
       

# Data Dictionary


       
     
       'contract_type', 'internet_service_type', 'payment_type'

| Feature | Definition |
|:--------|:-----------|
|Gender| Binary,male or female|
|Senior_Citizen| True or False, age classification |
|partner| True or False, does the customer have a partner|
|dependents| True or False, does the customer have dependents|
|tenure| Integer, how long the customer has commerced with Telco|
|phone_service| Binary, yes or no, does the customer have phone service|
|multiple_lines| Categorical,yes,no,or no phone serivce |
|online_security| Categorical, yes, no, or no internet service|
|online_backup| Categorical, yes, no, or no internet service||
|device_protection| Categorical, yes, no, or no internet service|
|tech_support| Categorical, yes, no, or no internet service|
|streaming_tv| Categorical, yes, no, or no internet service|
|streaming_movies| Categorical, yes, no, or no internet service|
|paperless_billing| Binary, yes or no, does the customer have paperless billing|
|monthly_charges| Continous, how much the customer pays monthly|
|total_charges| Continous, how much the customer pays monthly|
|churn| True or False, the customer has stopped commerce with Telco.|
|contract_type| Categorical, month-to-month, two year, one year|
|internet_service_type| Categorical, fiber optic, dsl, none       |
|paymeny_type| Categorical, electronic check, mailed check, bank transfer, credit card |

