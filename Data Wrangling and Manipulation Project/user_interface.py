#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating list of menu for the user to choose

def user_selection():
    """
        Function to show userinterface at the begining
    """
    print(f"""\nPlease select one of the follwing feature you want to use:
            {"[A]":<5} A - Host details
            {"[B]":<5} B - Advance features
            {"[C]":<5} C - Visualise 
            {"[D]":<5} D - Exit
            """)
    
def menu():
    """
        Function to show user interface when user choose get host_details
    """
    print(f"""\nPlease select one of the following options of your choice:
              {"[A]":<5} A - Get host info using host id
              {"[B]":<5} B - Get host details for a specified location
              {"[C]":<5} C - Get detials for a specified property type
              {"[D]":<5} D - Get host acceptance rate by host location
              {"[E]":<5} E - Exit
              """)

def advance_menu():
    """
        Function to show user interface when user choose advance feature option
    """
    print(f"""\nPlease select one of the following advance menu of your choice:
    {"[A]":<5} A - Get top ten most popular amenities
    {"[B]":<5} B - Get the average price of each stay in each location
    {"[C]":<5} C - Get the average review scores rating for each location
    {"[D]":<5} D - Get average price of each property type
    {"[E]":<5} E - Exit
    """)
          
def visualise():
    
    """
        Function to show user interface when user choose visualise option
    """
    print(f"""\nVisualise data
              please select one of the following options:
              {"[A]":<5} A - Visualise the proportion of number of bedrooms using piechart
              {"[B]":<5} B - Visualise the number of listing for each room using bar chart
              {"[C]":<5} C - Visualise the relationship between accomodates and price using scatter plot
              {"[D]":<5} D - Visualise the Airbnb prices from 2019-2022 using subplots
              {"[E]":<5} E - visualise the realtion between rating and review score
              {"[F]":<5} F - Exit
              """)
          
def try_again():
          """
              Function to let user user choose either to try more option from the selected
              feature or change the feature
          """
          print(f"""\nDo you want to use other options or change the feature?
            {"[A]":<5} A - Try more option
            {"[B]":<5} B - Change feature
            {"[C]":<5} C - Exit
            """)

