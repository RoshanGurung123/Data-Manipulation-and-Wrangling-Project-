#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing necessary libaries
import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


# In[1]:


def load_csv(file_path):
    """
        Function to load csv data into list of dictionaries
        
        Returns data as a list of dictionaries 
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, encoding='utf-8') as csv_file:
                data=list(csv.DictReader(csv_file))
                return data
        else:
            print("The file doesn't exists")
    except IOError:
        print(f"Cannot read file {file_path}")


# In[3]:


# Part 1 start
def get_host_info(data):
    """
        Function to get host info by host id
        
        Args:
            data: A list of dictionaries containing Airbnb csv data return from load_csv() function
    """
    #Ask user to input host ID
    host_id=input("Enter the host id you want: ")
    
    #Check if the host ID is empty or not
    if not host_id:
        print("Error!! Host id cannot be empty")
    
    #Initializeing an empty list to store matching host details
    host_found=[]
    
    #Using for loop to iterate through every row in the data to find matching data
    for row in data:
        if host_id == row['host_id']:
            host_details={
                'Host_name':row['host_name'],
                'Description':row['description'],
                'Host_location':row['host_location'],
                'Host_since':row['host_since']

            }
            #saving the matched data in list
            host_found.append(host_details)
            
    #Print error when there are no match found
    if not host_found:
        print(f"\nThere is no data of the {host_id} id.")
    else:
        #Print host information which has been found
        for value in host_found:
                print(f"Host_name:{value['Host_name']}")
                print(f"Description:{value['Description']}")
                print(f"Host_location:{value['Host_location']}")
                print(f"Host_date:{value['Host_since']}")
                
                
#Requirement 2
def get_details_by_location(data):
    """
        Function to get host details by location
        
        Args:
            data: A list of dictionaries containing Airbnb csv data return from load_csv() function
    """
    
    #Ask user to input host location
    host_location = input("Enter a specified host location: ").lower().strip()
    
    #Print error message when the host location is empty
    if not host_location:
        print("Error: Host location cannot be empty.")
        return []

    #Creating a empty list to save matching data
    match_found = []
    
    #Using for loop to iterate through every row in the data to find matching data
    for values in data:
        if host_location == values['host_location'].lower():
            details = {
                'Host_name': values['host_name'],
                'Property_type': values['property_type'],
                'Price': values['price'],
                'Minimum_nights': values['minimum_nights'],
                'Maximum_nights': values['maximum_nights']
            }
            #Append the match found details into match_found list
            match_found.append(details)

    #Print message when there are no matching data
    if not match_found:
        print("\nNo hosts found in the specified location.")
    else:
        #print all the match found details using for loop
        print(f"\nTotal:{len(match_found)} match found for {host_location}:")
        for match in match_found:
            print(f"\nHost name: {match['Host_name']}")
            print(f"Property type: {match['Property_type']}")
            print(f"Price: {match['Price']}")
            print(f"Minimum nights: {match['Minimum_nights']}")
            print(f"Maximum nights: {match['Maximum_nights']}")

#Requirement 3
def get_details_by_property_type(data):
    """
        Function to get host details by property type
        
        Args:
            data: A list of dictionaries containing Airbnb csv data return from load_csv() function
    """
    
    #Ask user to input the property type
    property_type=input("Enter the property type:").lower().strip()
    
    #Print error message when user enter empty value
    if not property_type:
        print("The property type cannot be empty.")
        return []
    
    #Initialize empty list to store matching data
    match_found=[]
    
    #Using for loop to iterate through every row in the data to find matching data
    for values in data:
        if property_type == values['property_type'].lower():
            details={
                'room_type': values['room_type'],
                'accommodates':values['accommodates'],
                'bathrooms_text':values['bathrooms_text'],
                'bedrooms':values['bedrooms'],
                'beds':values['beds']
            }
            #Append all the matching details in match_found list
            match_found.append(details)
            
    #Print message when there are no matches found
    if not match_found:
        print(f"\nNo matches found for {property_type} property type")
    else:
        #Print all the match found details using for loop
        print(f"\nTotal:{len(match_found)} match found for {property_type}")
        for match in match_found:
            print(f"\nRoom type:{match['room_type']}")
            print(f"Accomodates:{match['accommodates']}")
            print(f"Bathroom:{match['bathrooms_text']}")
            print(f"Bedroom:{match['bedrooms']}")
            print(f"Beds:{match['beds']}")

            
# Requirement 4
def get_individual_details(data):
    """
        Function to get host response rate, acceptance rate, response time by using host location
        
        Args:
            data: A list of dictionaries containing Airbnb csv data return from load_csv() function
    """
    
    #Ask user to input host location
    host_location = input("Enter a specified host location: ").lower().strip()
    
    #Print error message when the user enter empty value
    if not host_location:
        print("Error: Host location cannot be empty.")
        return []

    #Initialize empty list to store matching data
    match_found = []
    
    #Using for loop to find all the matching data and append in match_found list
    for values in data:
        if host_location == values['host_location'].lower():
            details = {
                'host_name':values['host_name'],
                'host_response_rate': values['host_response_rate'],
                'host_acceptance_rate': values['host_acceptance_rate'],
                'host_response_time': values['host_response_time']
            }
            match_found.append(details)

    #print message when no host found from the specified location
    if not match_found:
        print(f"\nNo hosts found in {host_location} location.")
    else:
        #Print match found details of the host 
        print(f"\nTotal:{len(match_found)} match found for {host_location}:")
        for match in match_found:
            print(f"\nHost name: {match['host_name']}")
            print(f"Host response rate: {match['host_response_rate']}")
            print(f"Host acceptance rate: {match['host_acceptance_rate']}")
            print(f"Host response time: {match['host_response_time']}")


# In[2]:


# Part 2 start
def load_csv_pandas_module(file_path):
    """
        Function to load csv file into memory using pandas module
        
        Args:
            file_path:User specified location of the csv file
    """
    df_airbnb=pd.read_csv(file_path)
    return df_airbnb


#Function to get top_10 amenities
def get_top_10_amenities(df_airbnb):
    """
        Function to get top_10 amenities
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    
    #Taking only amenities from dataframe
    df_amenities=df_airbnb['amenities']
    
    #spliting amenities column by comma and seperate into seperate column
    df_split_amenities = df_amenities.str.split(',', expand=True)
    
    #convert the data from the amenities columns into row
    df_rows=pd.melt(df_split_amenities)
    
    #clean the the data by removing unwanted square bracket
    df_rows_filter = df_rows['value'].str.strip('[]')
    
    #count every amenities which has been used 
    amenities_count=df_rows_filter.value_counts().sort_values(ascending=False)
    
    #get top 10 amenities using .head() function
    amenities_top_10_count=amenities_count.head(10).index.tolist()
    
    #Print top 10 amenities
    print("\nTop 10 most popular amenities or features that Airbnb hosts provide to customer are:")
    print(amenities_top_10_count)

    
# function to calculate average stay price per location
def get_avg_price_of_stay(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    
    #Ask user input to enter the name of the location
    user_input=input("Enter the name of the location:").lower().strip()
    
    #Print error message when the input field is empty
    if not user_input:
        print("The location cannot be empty.")
        return
    
    #take unique location from host location column and lowering all the value from host_location column to compare with user input
    host_location=df_airbnb['host_location'].str.lower().unique()
    
    #Print error message when there is no match found
    if user_input not in host_location:
        print(f"{user_input} is not a valid location")
        return
    else:
    #Groupby host location to calculate average stay price
        df_groupby_location=df_airbnb.groupby(df_airbnb['host_location'].str.lower())
        df_avg_price=df_groupby_location.get_group(user_input).price.mean()
        print(f"The average stay price of {user_input} is {df_avg_price:.2f}")

    
# Function to calculate average review score per location
def avg_review_scores(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    
    #Ask user input to enter the name of the location
    user_input=input("Enter the name of the location:").lower().strip()
    if not user_input:
        print("The location cannot be empty")
        return
    
    #take unique location from host location column and lowering all the value from host_location column to compare with user input
    host_location=df_airbnb['host_location'].str.lower().unique()
    
    #Print error message there is no valid location
    if user_input not in host_location:
        print(f"{user_input} is not a valid location")
        return
    else:
        ##Groupby host location to calculate average review score rating 
        df_groupby_review_score=df_airbnb.groupby(df_airbnb['host_location'].str.lower())  
        df_avg_review_scores=df_groupby_review_score.get_group(user_input).review_scores_rating.mean()
        print(f"The average review score of {user_input} is {df_avg_review_scores:.2f}")


# Function to calculate each property type average price 
def property_type_avg_price(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    df_groupby_property=df_airbnb.groupby('property_type').price.mean()
    print(f"""The average price of each property type are:
    {df_groupby_property}""")


# In[4]:


# Part 3 start
# Function to display the proportion of number of bedrooms of Airbnb listing using pie chart  
def number_of_bedroom_piechart(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    
    #Groupby bedrooms and calculating the listing of bedrooms for each group by using size()
    df_groupby_bedroom=df_airbnb.groupby('bedrooms').size().sort_values(ascending=False)
    number_of_bed_list=df_groupby_bedroom.index.tolist()
    total_number_of_bedroom=df_groupby_bedroom.tolist()
    
    fig=plt.figure(figsize=(5,7))
    
    plt.pie(total_number_of_bedroom, labels=number_of_bed_list, startangle=0)
    plt.title("Number of bedroom in a property")

    plt.legend(title="Number of Bedrooms",loc="best", bbox_to_anchor=(1.2,1))

    plt.show()
     
#number_of_bedroom_piechart()

# function to display number of listing for each room type
def number_of_room_types(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    room_type_group=df_airbnb.groupby('room_type').size().sort_values(ascending=False)
    number_of_room_type=room_type_group.index.tolist()
    total_number_of_room_type=room_type_group.tolist()
    
    fig=plt.figure(figsize=(7,5))
    
    plt.bar(number_of_room_type,total_number_of_room_type, label="Room type")
    
    plt.xlabel('Room type')
    plt.ylabel('Total number of room types')
    
    plt.title('Total listing of each room type')
    plt.legend()
    plt.show()

# FUnction to show realtionship between accomodates and price
def relation_between_accomodates_price(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
        
    accomodates=df_airbnb['accommodates'].tolist()
    price=df_airbnb['price'].tolist()

    fig=plt.figure(figsize=(7,5))
    plt.scatter(accomodates,price)

    plt.xlabel('Accomodates')
    plt.ylabel('Price')

    plt.title('The relationship between accomodates and price')

    plt.show()
    
# function to analys Airbnb price from 2019 to 2022
def one_year_prices_analysis(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    #Convert the host since column to datetime format and adding date column
    df_airbnb["date"]=pd.to_datetime(df_airbnb["host_since"])
    
    #Take only year from the date column
    df_airbnb["year"] = df_airbnb["date"].dt.year
    fig, ax = plt.subplots(4, 1,figsize=(8, 12))
    
    #counter value
    i = 0
    
    #plot line chart by iterating year from 2019 to 2023
    for year in range(2019, 2023):
        filtered_year = df_airbnb[df_airbnb['year'] == year]
        year_groupby_date = filtered_year.groupby('date')['price'].mean()

        ax[i].plot(year_groupby_date.index, year_groupby_date.values)
        ax[i].set_xlabel('Date')
        ax[i].set_ylabel('Price')
        ax[i].set_title(f'Price analysis for {year}')
        
        #counter value increase
        i += 1
    plt.tight_layout()
    plt.show()
    
# Function to get realtionship between number of reviews and the review scores rating.
def relation_reviews_rating(df_airbnb):
    """
        Args:
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    reviews=df_airbnb['number_of_reviews']
    rating=df_airbnb['review_scores_rating']

    fig=plt.figure(figsize=(7,5))
    plt.scatter(reviews,rating)

    plt.xlabel('Number of Reviews')
    plt.ylabel('Review score rating')

    plt.title('The relationship between reviews and raing')

    plt.show()


# In[ ]:




