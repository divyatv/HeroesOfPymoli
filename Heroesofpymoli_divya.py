#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# ## Player Count

# In[2]:


######################################################################
#####   DIVYA TV    #############################
## Import the csv file and initialize a dataframe.
## Perform mathematical operations on the columns.
######################################################################


### Import packages needed for the work. Pandas for dataframes.
import pandas as pd
import numpy as py

#Loading CSV file using pandas
file_to_load = "Resources/purchase_data.csv"

#printing the path of the file
print ("path of the file", file_to_load)

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

# Reading the file again to keep the original file to use when needed.
purchase_data_original = pd.read_csv(file_to_load)

## Not printing now. Uncomment if you need to see the entire csv file.
#print(purchase_data_original)


# * Display the total number of players
# 

# In[5]:


# Display the total number of players. There are duplicate SNs- same people - not counting them.

total_number_of_players=purchase_data["SN"].nunique()
#print ("total number of players=", total_number_of_players)
totalplayers=pd.DataFrame({'Total Players':[purchase_data["SN"].nunique()]})
#print(totalplayers)

##Diaplay the total number of players.
totalplayers.style


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[6]:



### Perform mathematical operations.
### 1. Calculate number of unique Items.
### 2. Calcualte avarage price.

NumberofUniqueItems=purchase_data["Item ID"].nunique()
#print ("total number of unique items=", NumberofUniqueItems)

NumberofPurchases=purchase_data["Purchase ID"].nunique()
#print (" Number of Purcharses=", NumberofPurchases)

AveragePrice=float(round((purchase_data["Price"].mean()), 2))
#print ("Average=", AveragePrice)

##Displaying dollars in correct format
AveragePrice1='${:,.2f}'.format(AveragePrice)

## Converting revenue from float to display in dollars.
Revenue= float(purchase_data["Price"].sum())
Revenue1='${:,.2f}'.format(Revenue)

### Create a dictionary with calculations.
newdf={'Number of Unique Items':[NumberofUniqueItems],
       'Average Price':[AveragePrice1],
       'Number of Purchases':[NumberofPurchases],
       'Total Revenue':[Revenue1]
       }

## Initialize the dataframe from the dictionary above.
df=pd.DataFrame(newdf)
#print (df)
df.style


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[7]:


### *** Ignore the commented code. They are retained for furure reference. *** ###

##Genders=purchase_data["Gender"].unique()
#print(Genders)

#GenderCounts=purchase_data["Gender"].value_counts()
#print (GenderCounts)
#print(purchase_data)

## Create a data frame dropping all the duplicate SN
#newdataframe=purchase_data.drop_duplicates(subset='SN', keep='first', inplace=True)
#print(newdataframe)

#DataFrame.drop_duplicates(subset=None, keep=’first’, inplace=False)

#################################################################################
## Calculate the following:
## 1. Number of Male, female, other players.
## 2. Calculate percentage gender wise
#################################################################################

Gender_Count=purchase_data.groupby("Gender")["SN"].nunique()
#print (newlist)
percentage=(purchase_data.groupby("Gender")["SN"].nunique()/total_number_of_players)*100
#print (percentage)

## Merging the tables for gender and percentages into one.
merge_table = pd.merge(Gender_Count, round(percentage), on="Gender")
#print("merged table=", merge_table)

## Renaming the columns to match the expected output.
renamed_df=merge_table.rename(columns = {'SN_x':'Total Count','SN_y':'Percentage of Players'}, inplace = False)
#print(renamed_df)

#renamed_df.index
#renamed_df.reindex(['Male', 'Female', 'Other / Non-Disclosed'])

#Sorting the rows based on Total Count.
renamed_df=renamed_df.sort_values(by='Total Count', ascending=0)

renamed_df.style


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[8]:


#####################################################################################
### Calculate -- BY GENDER
### 1. Purchase count
### 2. Average purchase price
### 3. Average purchase total per person etc. by gender
####################################################################################

NumberofUniqueItems=purchase_data["Item ID"].nunique()
#print ("total number of unique items=", NumberofUniqueItems)

NumberofPurchases_groupbyGender=purchase_data.groupby("Gender")["Purchase ID"].nunique()
#print ("Purchase_Count=", NumberofPurchases_gender)

AveragePrice_groupbyGender=purchase_data.groupby("Gender")["Price"].mean()
#AveragePrice_gender_dollar='${:,.2f}'.format(float(AveragePrice_gender))
#print(AveragePrice_groupbyGender)
#print ("Average Purchase Price by gender", AveragePrice_gender)

TotalPurchase_groupbyGender=purchase_data.groupby("Gender")["Price"].sum()
#print ("Total Purchase value=", TotalPurchase_gender)

## Gender_Count=purchase_data.groupby("Gender")["SN"].nunique()
Average_purchase_per_person=(TotalPurchase_groupbyGender/Gender_Count)
#Average_purchase_pp1='${:,.2f}'.format(Average_purchase_pp)
#print(Average_purchase_pp)
##'${:,.2f}'.format(AveragePrice)

### Creating a list from the calcualted values.
Summary_list=[NumberofPurchases_groupbyGender, round(AveragePrice_groupbyGender, 2),TotalPurchase_groupbyGender, round(Average_purchase_per_person, 2)]
#print(Summary_list)

## Initializing a dataframe from the list created above.
PA_Summary_df=pd.DataFrame(Summary_list)
#print(PA_Summary_df)


##Transpose the data - all rows to columns using numpy dot T
Summary_table_transposed=PA_Summary_df.T

##*** Igonore the commented code - they were used during first round of work. *** ###
#df=Summary_table_transposed - testing the rename of columns with same names.
#df = df_column_uniquify(df) -error- 'Summary_table_transposed_column_uniquify' is not defined - didnt work
#Summary_table_transposed=Summary_table_transposed_column_uniquify(Summary_table_transposed)

#df.rename(columns={ df.columns[1]: "new_col_name" }) - didnt work
#Summary_table_transposed=Summary_table_transposed.rename(columns={Summary_table_transposed.columns[1]:"Divya"}) 

##df.columns.values[index] = "New name" - Works!!
#df.columns.values[1] = "New name"
#df.head()

## Renamig the columns index wise.
Summary_table_transposed.columns.values[1]="Average Purchase Price"
Summary_table_transposed.columns.values[0]="Purchase Count"
Summary_table_transposed.columns.values[2]="Total Purchase Price"
Summary_table_transposed.columns.values[3]="Avg total Purchase Per Person"


## Dataframe with same columns names cause problems.
#Summary_table_transposed=Summary_table_transposed.rename(index=1, columns = {"Purchase ID":"Purchase Count","Price":"Average Purchase Price",
#"Price":"Total Purchase Price", "Unnamed 0":"Avg total Purchase per person"}, inplace = False)
#Summary_table_transposed.columns
#print(Summary_table_transposed)
#Summary_table_transposed.head()

###################################################################################
### ******** Fuction to display prices in dollars. *******
###################################################################################
def displaydollar(list):
    newlist=[]
    for value in list:
        x=float(value)
        dollar= '${:,.2f}'.format(x)
        newlist.append(dollar)
    #print(newlist)    
    return(newlist)

#pdToList = list(dataPd['2']) - convert to list and call function displaydollar to display currency in dollars.
AveragePurchasePrice=list(Summary_table_transposed['Average Purchase Price'])
TotalPurchasePrice=list(Summary_table_transposed['Total Purchase Price'])
AvgtotalPurchasePerPerson=list( Summary_table_transposed['Avg total Purchase Per Person'])

## *** Function calls *** ##
## Function calls to display currencies in dollars and assign them back to the dataframe
Summary_table_transposed['Average Purchase Price']=displaydollar(AveragePurchasePrice)
Summary_table_transposed['Total Purchase Price'] =displaydollar(TotalPurchasePrice)
Summary_table_transposed['Avg total Purchase Per Person']=displaydollar(AvgtotalPurchasePerPerson)

## Display dataframe 
Summary_table_transposed



# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[9]:


##################################################################################
######  Calculate age demographics  #################
##################################################################################


##Dropping duplicate entries of SN to help with the calculations.
purchase_data = purchase_data.drop_duplicates(subset='SN', keep='first')

# create bins and group for lables for the bins.
bins=[0, 9, 14, 19, 24, 29, 34, 39, 120]
group=['<10', '10-14','15-19', '20-24', '25-29', '30-34', '35-39', '40+' ]


## ***  pd.cut - at  Age and assign bins and labels
newdf = pd.cut(purchase_data["Age"], bins, labels=group)

# Place the data series into a new column inside of the DataFrame
purchase_data["Agebin"] = pd.cut(purchase_data["Age"], bins, labels=group)

# Calculate total players and percentages.
sumtable=purchase_data.groupby("Agebin")["SN"].nunique()
sumtabledf=pd.DataFrame(sumtable)
sumtabledf=sumtabledf.rename(columns={'SN': 'Total Players'})

sumtabledf["Percentage players"]=round((sumtabledf['Total Players']/purchase_data["SN"].nunique())*100, 2)
#print(sumtabledf)

### Display the dataframe calculated.
sumtabledf.style


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[10]:


###################################################################################################
#### Purchasing Analysis.
#### Calculate Purchase count, Average purchase price, Average Purchase total per person by age.
###################################################################################################

#Create bins and lables for binning.
purchase_bin=[0, 9, 14, 19, 24, 29, 34, 39, 120]
purchase_lables=['<10', '10-14','15-19', '20-24', '25-29', '30-34', '35-39', '40+' ]

#pd.cut at Age to get data sorted into bins.
#pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise')
purchase_summary_table=pd.cut(purchase_data_original['Age'], bins=purchase_bin, labels=purchase_lables)

#Calculate Purchase count.
purchase_data_original['age label']=purchase_summary_table
purchase_data_summary=purchase_data_original.groupby('age label')["Purchase ID"].nunique()

## Initialize the dataframe with the calculations.
Purchase_data_summarydf=pd.DataFrame(purchase_data_summary)

#Rename Purchase ID column to Purchase count.
Purchase_data_summarydf=Purchase_data_summarydf.rename(columns={"Purchase ID": "Purchase Count" })

## Calculate Average Purchase price
Purchase_data_summarydf['Average Purchase Price']=displaydollar(round(purchase_data_original.groupby('age label')["Price"].mean(), 2))

## Calculate Total Purchase Value
Purchase_data_summarydf['Total Purchase Value']=displaydollar(purchase_data_original.groupby('age label')["Price"].sum())
#purchase_data.groupby("Gender")["Price"].sum()

## Calculate Average Total Purchase per person.
Purchase_data_summarydf['Average Total Purchase per Person']=displaydollar(round(purchase_data_original.groupby('age label')["Price"].sum()/sumtabledf['Total Players'], 2))

## Move first row to last row to match the expected output.
#print(df.apply(np.roll, shift=1))
#df.reindex(np.roll(df.index, shift=1))

Purchase_data_summarydf=Purchase_data_summarydf.reindex(py.roll( Purchase_data_summarydf.index, shift=-1))

##Display the dataframe.
Purchase_data_summarydf


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[11]:


########################################################################################
#### Top Spenders ###############
#### Sorting columns ##############
########################################################################################

## Calcualte top spenders.
top_spenders=pd.DataFrame(purchase_data_original.groupby('SN')['Purchase ID'].nunique())

#Rename the column to match the expected output
top_spenders.rename(columns={"Purchase ID":"Purchase Count"},inplace = True)

## Calculate Total Purchase Value
top_spenders['Total Purchase Value']=purchase_data_original.groupby('SN')['Price'].sum()

## Calculate Average purchase price
top_spenders['Average Purchase Price']=displaydollar(round(top_spenders['Total Purchase Value']/top_spenders['Purchase Count'], 2))

## Sort Total Purchase Value in descending order
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
top_spenders=top_spenders.sort_values('Total Purchase Value', ascending=False, inplace=False)

###***** Function call ****** ###
## Calling function to display currency in dollars.
TotalPurchaseValue=list(top_spenders['Total Purchase Value'])
top_spenders['Total Purchase Value']=displaydollar(TotalPurchaseValue)

## Re-arranging the columns to make sure the output looks exactly the same as expected.
top_spenders=top_spenders[['Purchase Count', 'Average Purchase Price','Total Purchase Value' ]]

## Display portion of the dataframe using head.
top_spenders.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[12]:


#############################################################################
#### Most popular items ##################
#############################################################################


### Ignore commented code ** ###
#itemid=purchase_data['Item ID']
#itemname= purchase_data.groupby('Item ID')['Item Name'].unique()
#itemprice=purchase_data.groupby('Item ID')["Price"].unique()
#purchasecount =purchase_data.groupby('Item ID')['Purchase ID'].nunique()
#totalpurchasevalue=purchase_data.groupby('Item ID')["Price"].sum()

#most_popular_items1={'Item ID':itemid, 'Item Name':itemname,'Item Price':itemprice,'Total Purchase Value':totalpurchasevalue}
#most_popular_itemsdf=pd.DataFrame(most_popular_items1)
#most_popular_itemsdf


###############################################################################################

## Initialise a dataframe
## perform calculations

most_popular_items=pd.DataFrame(purchase_data_original.groupby('Item ID')['Purchase ID'].nunique()) 

## Rename the column to match expected output
most_popular_items.rename(columns={"Purchase ID":"Purchase Count"},inplace = True)

## Adding colummns to the dataframe with more calculations.
most_popular_items['Item Name']= purchase_data_original.groupby('Item ID')['Item Name'].unique()

most_popular_items['Item Price']=displaydollar(purchase_data_original.groupby('Item ID')["Price"].unique())

most_popular_items['Total Purchase Value']= displaydollar(purchase_data_original.groupby('Item ID')["Price"].sum())

#### Sort the values - Sort the purchase count column in descending order
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
most_popular_items=most_popular_items.sort_values('Purchase Count', ascending=False)
most_popular_items=most_popular_items[['Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']]


## Display the portion f the dataframe.
most_popular_items.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[13]:


#############################################################################
#### Most profitable items ##################
#############################################################################


#### Intialize a dataframe with calculations.
most_profitable_items=pd.DataFrame(purchase_data_original.groupby('Item ID')['Purchase ID'].nunique()) 

## Rename the column to match the expected output.
most_profitable_items.rename(columns={"Purchase ID":"Purchase Count"},inplace = True)
#most_profitable_items.head()
most_profitable_items['Item Name']= purchase_data_original.groupby('Item ID')['Item Name'].unique()

### *** Function call ****
##displaydollar - is a function call to display currencies in dollars.
most_profitable_items['Item Price']=displaydollar(purchase_data_original.groupby('Item ID')["Price"].unique())

most_profitable_items['Total Purchase Value']= purchase_data_original.groupby('Item ID')["Price"].sum()

##Sort the total purchase value in descending order
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
most_profitable_items=most_profitable_items.sort_values('Total Purchase Value', ascending=False)

## Re-arrange the columns to match the expected output
most_profitable_items=most_profitable_items[['Item Name', 'Purchase Count', 'Item Price', 'Total Purchase Value']]

### *** Function call ****
##Display currencies in dollars calling function 'displaydollar'
TotalPurchaseValueMP=list(most_profitable_items['Total Purchase Value'])
most_profitable_items['Total Purchase Value']=displaydollar(TotalPurchaseValueMP)

## Display the portion f the dataframe.
most_profitable_items.head()


#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
#most_profitable_items=most_profitable_items.sort_values('Total Purchase Value', axis=0, ascending=True, inplace=False)
#most_profitable_items.head()


# In[ ]:




