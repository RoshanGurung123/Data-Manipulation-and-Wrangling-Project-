#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing user_interface, requirement modules
import user_interface
import requirement


# In[2]:


def user_choice_host_details(data,df_airbnb):
    """
        Function to show the details of the host by user choice
        
        Args:
            data: A list of dictionaries containing Airbnb csv data
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    while True:
        user_interface.menu()
        user_choice=input("Select one of the options:").strip().upper()
        if user_choice=='A':
            requirement.get_host_info(data)
            break
        elif user_choice=='B':
            requirement.get_details_by_location(data)
            break
        elif user_choice=='C':
            requirement.get_details_by_property_type(data)
            break
        elif user_choice=='D':
            requirement.get_individual_details(data)
            break
        elif user_choice=='E':
            print("Exiting.........")
            break
        else:
            print("Invalid input!! Please select one of the options")
    user_interface.try_again()
    user_entry=input("Please select one of the options:")
    if user_entry.upper().strip() == 'A':
        user_choice_host_details(data,df_airbnb)
    elif user_entry.upper().strip() == 'B':
        feature_selection(data,df_airbnb)
    else:
        print("Invalid input!!! Please select one of the following options.")
        
def advance_feature_selection(data,df_airbnb):
    """
        Function to show the advance feature like geting top 10 amenities, average price of the stay, average review score, 
        average price of property by property type
        
        Args:
            data: A list of dictionaries containing Airbnb csv data
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    while True:
        user_interface.advance_menu()
        user_choice=input("Select one of the options:").strip().upper()
        if user_choice=='A':
            requirement.get_top_10_amenities(df_airbnb)
            break
        elif user_choice=='B':
            requirement.get_avg_price_of_stay(df_airbnb)
            break
        elif user_choice=='C':
            requirement.avg_review_scores(df_airbnb)
            break
        elif user_choice=='D':
            requirement.property_type_avg_price(df_airbnb)
            break
        elif user_choice=='E':
            print("Exiting....")
            break
        else:
            print("Invalid input!! Please select one of the following options")
    user_interface.try_again()
    user_entry=input("Please select one of the options:")
    if user_entry.upper().strip() == 'A':
        feature_selection(data,df_airbnb)
    elif user_entry.upper().strip() == 'B':
        feature_selection(data,df_airbnb)
    else:
        print("Invalid input!!! Please select one of the following options.")

def feature_visualise(data,df_airbnb):
    """
        Function to visualise as per user selection
        
        Args:
            data: A list of dictionaries containing Airbnb csv data
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    while True:
        user_interface.visualise()
        user_choice=input("Select one of the options:").strip().upper()
        if user_choice=='A':
            requirement.number_of_bedroom_piechart(df_airbnb)
            break
        elif user_choice=='B':
            requirement.number_of_room_types(df_airbnb)
            break
        elif user_choice=='C':
            print("C")
            requirement.relation_between_accomodates_price(df_airbnb)
            break
        elif user_choice=='D':
            requirement.one_year_prices_analysis(df_airbnb)
            break
        elif user_choice=='E':
            requirement.relation_reviews_rating(df_airbnb)
        elif user_choice=='F':
            print("Exiting......")
            break
            
        else:
            print("Invalid input!! Please select one of the following options")    
    user_interface.try_again()
    user_entry=input("Please select one of the options:")
    if user_entry.upper().strip() == 'A':
        feature_visualise(data,df_airbnb)
    else:
        feature_selection(data,df_airbnb)
   
    
def feature_selection(data,df_airbnb):
    """
        Function to let user choose which feature to use at first
        
        Args:
            data: A list of dictionaries containing Airbnb csv data
            df_airbnb: Pandas dataframe containing data about Airbnb csv file
    """
    while True:
        user_interface.user_selection()
        user_choice=input("Select one of the following options: ").strip().upper()
        if user_choice=='A':
            user_choice_host_details(data,df_airbnb)
        elif user_choice=='B':
            advance_feature_selection(data,df_airbnb)
        elif user_choice=='C':
            feature_visualise(data,df_airbnb)
        elif user_choice=='D':
            print("Exiting....")
            break
        else:
            print("Invalid input!! Please select one of the options")


# In[ ]:




