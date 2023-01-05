import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats



######################################

def get_churn_rate(train):
    
    values = [len(train.churn_Yes[train.churn_Yes == 0]),                               len(train.churn_Yes[train.churn_Yes == 1])] 
    labels = ['Customer','Churn', ] 

    # generate and show chart
    plt.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    
    plt.title('Churned Customers Represent 1/4 of the train data')
    
    plt.show()


######################################

def get_tech_churn(train):
    
    ''' get pie chart for percent of churn compared to tech support usage '''

    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)

    # subset of everyone who used tech support
    values = [len(train.churn_Yes[(train.tech_support_Yes == True) & (train.churn_Yes     == True)]),
            len(train.churn_Yes[(train.tech_support_Yes == True) & (train.churn_Yes ==     False)])]
    labels = ['Churned', ' Non-Churn']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax1.title.set_text('Using Tech Support')


    # create pie chart and and assign to axis object
    # subset of everyone who didnt use techsupport
    
    values = [len(train.churn_Yes[(train.tech_support_Yes == False) & (train.churn_Yes     == True)]),
            len(train.churn_Yes[(train.tech_support_Yes == False) & (train.churn_Yes        == False)])]
    labels = ['Churned', 'Non-Churn']

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax2.title.set_text('Not Using Tech Support')
    
    plt.show()

######################################

def get_chi_tech(train):
    
    ''' get result of chi2 for churn and tech support correlation'''
    
    observed = pd.crosstab(train.tech_support_Yes,train.churn_Yes)
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p}')
    
######################################

def get_month_churn(train):
   
    ''' get pie chart for percent of churn compared to monthly payments'''
    
    monthly_mean = train.monthly_charges.mean()
    
    
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(train.churn_Yes[(train.monthly_charges > monthly_mean) & (train.churn_Yes == True)]),
            len(train.churn_Yes[(train.monthly_charges > monthly_mean) & (train.churn_Yes == False)])]
    labels = ['Churned', 'Non-Churn']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax1.title.set_text('Paid More Than Average')

    # create pie chart and assign to axis object
    values = [len(train.churn_Yes[(train.monthly_charges < monthly_mean) & (train.churn_Yes == True)]),
            len(train.churn_Yes[(train.monthly_charges <= monthly_mean) & (train.churn_Yes == False)])]
    labels = ['Churned', 'Non-churn']

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax2.title.set_text('Paid Avg or Less')

    plt.show()

######################################

def get_t_monthly(train):

    ''' get t-test for mean monthly difference for those who churned vs whole group '''
    
    monthly_mean = train.monthly_charges.mean()
    a = .05
    
    # all monthly charges from customers who churned.
    churned_cust_charges = train[train.churn_Yes == 1].monthly_charges
    
    t, p = stats.ttest_1samp(churned_cust_charges, monthly_mean)
    
    print(f't = {t:.4f}')
    print(f'p = {p}')  
    
    if (p < a):
        print("We can reject the null hypothesis")
    
    else:
        print('We fail to reject the null hypothesis')
                
######################################
def get_senior_churn(train):
    
    ''' get pie chart for churn rate compare to senior citizen status'''
    
    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(train.churn_Yes[(train.senior_citizen == 1) & (train.churn_Yes == True)]),
            len(train.churn_Yes[(train.senior_citizen == 1 ) & (train.churn_Yes == False)])]
    labels = ['Churned', 'Non-Churn']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax1.title.set_text('Senior Customers')

    # create pie chart and assign to axis object
    values = [len(train.churn_Yes[(train.senior_citizen == 0) & (train.churn_Yes == True)]),
            len(train.churn_Yes[(train.senior_citizen == 0) & (train.churn_Yes == False)])]
    labels = ['Churned','Non-Churn']

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax2.title.set_text('Younger Customers')

    plt.show()
    
######################################

def get_t_senior(train):

    ''' get t-test churn rate signifcance between senior and non-seniors'''
  
    a = .05
    churn_sample = train[train.churn_Yes == 1].senior_citizen
    no_churn_sample = train[train.churn_Yes == 0].senior_citizen

    t, p = stats.ttest_ind(churn_sample, no_churn_sample, equal_var=True)
    
    print(f't = {t:.4f}')
    print(f'p = {p}')  
    
    if ((p) < a):
        print("We can reject the null hypothesis")
    
    else:
        print('We fail to reject the null hypothesis')
    
######################################

def get_tenure_rate(train):

    ''' get pie chart churn rate compared to tenure length'''

    avg_tenure = train.tenure.mean()

    # create axis object
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    # create pie chart and assign to axis object
    values = [len(train.churn_Yes[(train.tenure > avg_tenure) & (train.churn_Yes == True)]),
            len(train.churn_Yes[(train.tenure > avg_tenure) & (train.churn_Yes == False)])]
    labels = ['Churned', 'Non-Churn']

    ax1.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax1.title.set_text('Longer Tenure Customers')

    # create pie chart and assign to axis object
    values = [len(train.churn_Yes[(train.tenure < avg_tenure) & (train.churn_Yes == True)]),
            len(train.churn_Yes[(train.tenure < avg_tenure) & (train.churn_Yes == False)])]
    labels = ['Churned', 'Non-Churn']

    ax2.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax2.title.set_text('Shorter Tenure Customers')

    plt.show()

######################################

def get_t_tenure(train):

    ''' get t-test churn rate signifcance between longer tenure customers and shorter tenure customers'''
  
    a = .05
    churn_sample = train[train.churn_Yes == 1].tenure

    no_churn_sample = train[train.churn_Yes == 0 ].tenure

    t, p = stats.ttest_ind(churn_sample, no_churn_sample, equal_var=True)
    
    print(f't = {t:.4f}')
    print(f'p = {p}')  
    
    if (p < a):
        print("We can reject the null hypothesis")
    
    else:
        print('We fail to reject the null hypothesis')
    
#######################################

def get_compare():
    ''' get hard coded pie chart to compare baseline to best model'''
    
    labels = 'Churned', 'Non-Churn'
    sizes = [26, 74]

    fig, (ax1,ax2) = plt.subplots(1,2)
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=75)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    ax1.title.set_text('Baseline Prediction')

    labels = 'Churned', 'Non-Churn'
    sizes = [20, 80]
    
    ax2.pie(sizes, labels=labels, autopct='%1.1f%%',
    startangle= 90)
    
    ax2.axis('equal')

    ax2.title.set_text('Best Model')

    plt.show()
