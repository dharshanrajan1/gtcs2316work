import pandas as pd
import numpy as np
from pprint import pprint
import csv, time
from codecarbon import EmissionsTracker

## NOTES:

# CS 2316 - Spring 2024 - HW05 Pandas
# HW05: This homework is due by Sunday, March 3rd @ 11:59PM.

# For this homework, you will need to download 'Flight_Emission_Data.csv' and place it
# in the same location as HW05.py

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW05.py - Your submission should be named exactly HW05.py
#   - Print your variables as you code in order to see what values they have
#     especially for questions with BeautifulSoup

###################################################
###################################################
"""
DATA CLEANING SECTION

The following two questions will be a little different and is made to show the value of the pandas dataframe when it comes to the carbon emissions of your code.
For these problem you will need the CodeCarbon package. Please see the CodeCarbon Guide to learn how to install and use the package. 
For the first question, you will build a funciton that will do data manipulation using the methods you are more familiar with: 
list comprehensions, csv module, etc. 

The second question will be performing the same operations using pandas.
In both parts, you will use EmissionsTracker from codecarbon to track the emissions of each function.
There's code at the very end of the file to print to the shell the emissions from each run of either function assuming they are run right after each other.
"""
###################################################
###################################################

def csv_cleaner(input_file):
    ## the below code is what i derived from working on office hours with TA Athena 
    with open(input_file, "r") as fin:
        reader = csv.reader(fin)
        input_list = [line for line in reader]

    totalco2=totalduration=0
    newlist=[]
    for line in input_list[1:]:
        if "Boeing 737" in line[5]:
            continue
        oci=line[5].split("|")[0]
        # print(oci)
        oci1=line[5].split("|")[1] if len(line[5].split("|"))>1 else "None"
        # print(oci1)
        line[-2]=line[-1] if line[-2]=="" else line[-2]
        if line[-2]=="":
            continue
        totalco2+=float(line[-2])
        totalduration+=float(line[-5])
        newlist.append(line[0:5] + line[6:] +[oci,oci1])
    # print(totalco2)
    # print(totalduration)
    finalavg=totalco2/totalduration

    for line in newlist:
        if line[-3]=="":
            line[-3] = float(round(float(finalavg) * float(line[-7]))) ## * duration its -7

    # print(input_list[0][6:])

    header= ["index"]+input_list[0][1:5] + input_list[0][6:] + ["aircraft_type_1"] + ["aircraft_type_2"]
    # return header


    # return newlist




    ## This is the approach i initially tried 

    # index_mapping = {s: i for i, s in enumerate(input_list[0])}
    # index_mapping["aircraft_type_1"] = 14
    # index_mapping["aircraft_type_2"] = 15
    # co2_emissions = duration = 0
    # popped = []
    # for i, line in enumerate(input_list[1:]):
    #     i += 1
    #     plane_types = line[index_mapping["aircraft_type"]].split("|")
    #     line.append(plane_types[0])
    #     if len(plane_types) == 1:
    #         plane_types.append("None")
    #     line.append(plane_types[1])
    #     if not line[index_mapping["co2_emissions"]]:
    #         if not line[index_mapping["avg_co2_emission_for_this_route"]]:
    #             popped.append(i)
    #             continue
    #         else:
    #             line[index_mapping["co2_emissions"]] = line[
    #                 index_mapping["avg_co2_emission_for_this_route"]
    #             ]
    #     if (
            
    #         line[index_mapping["aircraft_type_1"]] == "Boeing 737"
    #         or line[index_mapping["aircraft_type_2"]] == "Boeing 737"
    #         or line[index_mapping["aircraft_type_1"]] == "Boeing 737MAX 8 Passenger"
    #         or line[index_mapping["aircraft_type_2"]] == "Boeing 737MAX 8 Passenger"
    #     ):
    #         popped.append(i)
    #         continue
    #     co2_emissions += float(line[index_mapping["co2_emissions"]])
    #     duration += float(line[index_mapping["duration"]])
    #     line.pop(index_mapping["aircraft_type"])

    #     # # print(co2_emissions)
    #     # # print(duration)
    #     avg_emissions = co2_emissions / duration

    #     # print(avg_emissions)

    # for line in range(length(input_list[1:])):
    #     if not line[index_mapping["avg_co2_emission_for_this_route"]]:
    #         # pprint("zhi")
    #         line[index_mapping["avg_co2_emission_for_this_route"]] = float(
    #             int(avg_emissions * float(line[index_mapping["duration"]]))
    #         )
    # for i, pop in enumerate(popped):
    #     input_list.pop(pop - i)
    
    with open("cleaned_emissions_data_csv.csv", "w",newline = "") as fout:
        writer = csv.writer(fout)
        # writer.writerow(header)
        writer.writerows([header]+newlist)


    return ([header]+newlist)
    # return None


    # return input_list



    """
    Question 1

    Using the CSV module and list manipulation, you should complete the following cleaning steps on the 'Flight_Emission_Data.csv' file.

    These steps must be completed in this order to make sure that the calculations are corrrect

        1) Some of the flights contain multiple values in the "aircraft_type" column. These values are seperated by "|". Split this 
           column into 2 columns: "aircraft_type_1" and "aircraft_type_2". If there is no seperate aircraft type, simply fill this with "None" as a string
        2) Some of the indexes within the "co2_emissions" column are empty. Fill these values with the corresponding value from "avg_co2_emission_for_this_route".
           If "avg_co2_emission_for_this_route" is blank, drop these rows.
        3) Remove any flights where the aircraft type, either 1 or 2, contains the phrase "Boeing 737"
        4) Many of the "avg_co2_emission_for_this_route" values are blank, for rows where this value is blank you need to fill these by doing the following:
            a) calculate the average co2 per minute over the entire dataframe. This can be done by summing the columns for "co2_emissions" and "duration" and then
               dividing the total_co2_emissions by total_duration.
            b) fill the blank "avg_co2_emission_for_this_route" values, with the above calulated average multiplied by the duration for the missing rows
            c) this values should be rounded to 0 decimal places but left as a float
        5) Add an element to the beginning of the headers called index

    Return this list of list and write it to a csv file called "cleaned_emissions_data_csv.csv"

    This is a challenging problem and to help you along we have provided you with a couple of hints:
        HINT 1) This problem cannot be done in a single for loop. You will require atleast two for loops to complete everything. Steps 1 through 3 can be completed in one for
                loop. Replacing the elements in step 4 will require a second for loop.
        HINT 2) We have provided you with the desired output length. Before doing any of the calculation part in step 4, we would suggest returning 
                your filtered dataset and ensuring that you have the correct number of rows in your list
        HINT 3) A great way to determine if your filters are working is to run the code and then write some test code that searches through the list for any elements
                that were supposed to be filtered out. If your test code returns nothing, then there's a good chance you have done things correctly
        HINT 4) None of the individual elements of this problem are particularly challenging; however, there are alot of them. It is very important to keep your code
                organized. Go through this problem methodically in order, make sure your variables make sense and can be traced easily, and potentially leave comments
                explaining what each portion does.
        HINT 5) Be very aware of what datatypes each element is and what datatypes the outputs desire. Everything is in the prompt so read it very carefully.

    YOU MAY NOT USE PANDAS ON THIS QUESTION!!!

    Args:
        'Flight_Emission_Data.csv'
    Returns:
        list of lists

    >>> csv_cleaner('Flight_Emission_Data.csv')

    [['index', 'from_airport_code', 'from_country', 'dest_airport_code', 'dest_country', 'airline_name', 'departure_time', 'arrival_time', 'duration', 'stops', 'price', 'co2_emissions', 'avg_co2_emission_for_this_route', 'aircraft_type_1', 'aircraft_type_2'], 
     ['0', 'ALG', 'Algeria', 'MEL', 'Australia', 'Qatar Airways', '4/30/22 15:20', '5/2/22 16:10', '2390', '1', '2062', '1968000.0', 1827762.0, 'Airbus A330', 'Boeing 777'], 
     ['1', 'ALG', 'Algeria', 'SYD', 'Australia', 'Qatar Airways', '4/30/22 15:20', '5/2/22 17:25', '2465', '1', '2313', '1564000.0', 1885118.0, 'Airbus A330', 'Airbus A350'], 
     ['2', 'ALG', 'Algeria', 'MEL', 'Australia', 'Qatar Airways', '5/2/22 15:20', '5/4/22 16:10', '2390', '1', '1604', '1968000.0', 1827762.0, 'Airbus A330', 'Boeing 777'], 
     ['3', 'ALG', 'Algeria', 'SYD', 'Australia', 'Qatar Airways', '5/2/22 15:20', '5/4/22 17:25', '2465', '1', '1863', '1564000.0', 1885118.0, 'Airbus A330', 'Airbus A350']
     ...
     ['146727', 'BOM', 'India', 'SYD', 'Australia', 'Singapore Airlines', '5/1/22 23:40', '5/3/22 05:55', '1545', '1', '1239', '993000.0', '1133000.0', 'Airbus A380', 'Airbus A350'], 
     ['146728', 'BOM', 'India', 'SYD', 'Australia', 'Singapore Airlines', '5/1/22 23:40', '5/3/22 19:15', '2345', '1', '1270', '1312000.0', '1133000.0', 'Airbus A380', 'Boeing 777'], 
     ['146729', 'BOM', 'India', 'SYD', 'Australia', 'Emirates', '5/1/22 15:35', '5/2/22 22:05', '1560', '1', '1317', '1584000.0', '1133000.0', 'Boeing 777', 'Airbus A380'], 
     ['146730', 'BOM', 'India', 'SYD', 'Australia', 'Emirates', '5/1/22 19:20', '5/2/22 22:05', '1335', '1', '1317', '1567000.0', '1133000.0', 'Boeing 777', 'Airbus A380'], 
     ['146731', 'BOM', 'India', 'SYD', 'Australia', 'Emirates', '5/1/22 22:20', '5/2/22 22:05', '1155', '1', '1317', '1583000.0', '1133000.0', 'Boeing 777', 'Airbus A380']]

    length = 118320
    
    """


    
    

def pandas_cleaner(input_file):


    df = pd.read_csv(input_file, index_col=0)

    df[['aircraft_type_1', 'aircraft_type_2']] = df['aircraft_type'].str.split('|', expand=True) ## splitting out the |

    df['aircraft_type_1'] = df['aircraft_type_1'].fillna('None') ## filling none values of both type 1 and tepe 2 aircraft with none 
    df['aircraft_type_2'] = df['aircraft_type_2'].fillna('None')

    df['co2_emissions'].fillna(df['avg_co2_emission_for_this_route'], inplace=True) #if co2 is null, fill with avg 
    df.dropna(subset=['co2_emissions'], inplace=True)

    df = df[~df['aircraft_type_1'].str.contains('Boeing 737', case=False)]
    df = df[~df['aircraft_type_2'].str.contains('Boeing 737', case=False)]

    total_co2_emissions = df['co2_emissions'].sum()
    total_duration = df['duration'].sum()

    avg_co2_per_minute = total_co2_emissions / total_duration

    df['avg_co2_emission_for_this_route'] = df['avg_co2_emission_for_this_route'].fillna(
        avg_co2_per_minute * df['duration'])

    df['avg_co2_emission_for_this_route'] = df['avg_co2_emission_for_this_route'].round(0)

    df.drop(['aircraft_type'], axis=1, inplace=True)

    df.to_csv('cleaned_emissions_data_pandas.csv')
    # print(len(df))

    return df


    ## Errors I am getting:
        ## Summing duration wrong 
        ## Avg c02 is wrong(number of rows) 
        ## this question is also affecting quesitons 4 and 7 



    """
    Question 2
    
    Using the pandas module, you should complete the following cleaning steps on the 'Flight_Emission_Data.csv' file.

    These steps must be completed in this order to make sure that the calculations are corrrect

        1) Some of the flights contain multiple values in the "aircraft_type" column. These values are seperated by "|". Split this 
           column into 2 columns: "aircraft_type_1" and "aircraft_type_2". If there is no seperate aircraft type, simply fill this with "None" as a string
        2) Some of the indexes within the "co2_emissions" column are NaN. Fill these values with the corresponding value from "avg_co2_emission_for_this_route".
           If "avg_co2_emission_for_this_route" is NaN, drop these rows.
        3) Remove any flights where the aircraft type, either 1 or 2, contains the phrase "Boeing 737"
        4) Many of the "avg_co2_emission_for_this_route" values are NaN, for rows where this value is blank you need to fill these by doing the following:
            a) calculate the average co2 per minute over the entire dataframe. This can be done by summing the columns for "co2_emissions" and "duration" and then
               dividing the total_co2_emissions by total_duration.
            b) fill the NaN "avg_co2_emission_for_this_route" values, with the above calulated average multiplied by the duration for the missing rows
            c) this values should be rounded to 0 decimal places but left as a float

    Return this list of list and write it to a csv file called "cleaned_emissions_data_pandas.csv"

    NOTE: The output from this problem will be used on future problems

    Args:
        'Flight_Emission_Data.csv'
    Returns:
        pd.DataFrame

    >>> pandas_cleaner('Flight_Emission_Data.csv')

            from_airport_code from_country dest_airport_code dest_country        airline_name departure_time  arrival_time  duration  stops  price  co2_emissions  avg_co2_emission_for_this_route aircraft_type_1 aircraft_type_2
    0                    ALG      Algeria               MEL    Australia       Qatar Airways  4/30/22 15:20  5/2/22 16:10      2390      1   2062      1968000.0                        1827762.0     Airbus A330      Boeing 777
    1                    ALG      Algeria               SYD    Australia       Qatar Airways  4/30/22 15:20  5/2/22 17:25      2465      1   2313      1564000.0                        1885118.0     Airbus A330     Airbus A350
    2                    ALG      Algeria               MEL    Australia       Qatar Airways   5/2/22 15:20  5/4/22 16:10      2390      1   1604      1968000.0                        1827762.0     Airbus A330      Boeing 777
    3                    ALG      Algeria               SYD    Australia       Qatar Airways   5/2/22 15:20  5/4/22 17:25      2465      1   1863      1564000.0                        1885118.0     Airbus A330     Airbus A350
    4                    ALG      Algeria               MEL    Australia       Qatar Airways   5/6/22 15:20  5/8/22 16:10      2390      1   2298      1854000.0                        1827762.0     Airbus A330      Boeing 777
    ...                  ...          ...               ...          ...                 ...            ...           ...       ...    ...    ...            ...                              ...             ...             ...
    146727               BOM        India               SYD    Australia  Singapore Airlines   5/1/22 23:40  5/3/22 05:55      1545      1   1239       993000.0                        1133000.0     Airbus A380     Airbus A350
    146728               BOM        India               SYD    Australia  Singapore Airlines   5/1/22 23:40  5/3/22 19:15      2345      1   1270      1312000.0                        1133000.0     Airbus A380      Boeing 777
    146729               BOM        India               SYD    Australia            Emirates   5/1/22 15:35  5/2/22 22:05      1560      1   1317      1584000.0                        1133000.0      Boeing 777     Airbus A380
    146730               BOM        India               SYD    Australia            Emirates   5/1/22 19:20  5/2/22 22:05      1335      1   1317      1567000.0                        1133000.0      Boeing 777     Airbus A380
    146731               BOM        India               SYD    Australia            Emirates   5/1/22 22:20  5/2/22 22:05      1155      1   1317      1583000.0                        1133000.0      Boeing 777     Airbus A380

    [118319 rows x 14 columns]
    """

    

###################################################
###################################################
"""
DATA ANALYSIS SECTION
"""
###################################################
###################################################

def average_co2_percentage(emissions_df):
    # return round(((emissions_df['avg_co2_emission_for_this_route'] - emissions_df['co2_emissions']) / emissions_df[
    #         'avg_co2_emission_for_this_route']) * 100, 3)
    return round(((emissions_df['avg_co2_emission_for_this_route'] - emissions_df['co2_emissions']) / emissions_df['avg_co2_emission_for_this_route'] * 100).mean(), 2)
    # return op
    
    """
    Question 3

    Calulate the average emissions percentage. Emission percentage can be 
    computed by the following formula:

        ("avg_co2_emission_for_this_route" - "co2_emissions") / "avg_co2_emission_for_this_route" * 100

    Return the average of this series. Round this value to 3 decimal places.

    THIS MUST BE DONE IN ONE LINE!!!

    Args:
        emissions_df (pd.DataFrame)

    Return:
        float

    >>> average_co2_percentage(pandas_cleaner('Flight_Emission_Data.csv'))

    -36.54

    """

    

def airbus_emissions_average(emissions_df):
    # return emissions_df[emissions_df['aircraft_type_1'].str.lower().str.startswith('airbus')].groupby('aircraft_type_1')['co2_emissions'].mean().reset_index()
    return pd.DataFrame(emissions_df.dropna(subset=['aircraft_type_1'])[emissions_df['aircraft_type_1'].str.lower().str.startswith('airbus', na=False)].groupby('aircraft_type_1')['co2_emissions'].mean())
    ## Indices are out of bounds. 


    """
    Question 4

    Compute the average CO2 emissions for each aircraft model where the first aircraft 
    type is an airbus aircraft.

    THIS MUST BE DONE IN ONE LINE!!!

    Args:
        emissions_df (pd.DataFrame)

    Return:
        pd.DataFrame

    >>> airbus_emissions_average(pandas_cleaner('Flight_Emission_Data.csv'))

                                co2_emissions
    aircraft_type_1                            
    Airbus A220-100 Passenger      6.789004e+05
    Airbus A220-300 Passenger      7.066563e+05
    Airbus A318                    9.020930e+05
    Airbus A319                    7.517111e+05
    Airbus A320                    7.034364e+05
    Airbus A320neo                 6.669692e+05
    Airbus A321                    7.990989e+05
    Airbus A321 (Sharklets)        7.922473e+05
    Airbus A321neo                 6.266998e+05
    Airbus A330                    1.013587e+06
    Airbus A330-800neo Passenger   1.048893e+06
    Airbus A330-900neo             9.280391e+05
    Airbus A340                    1.327364e+06
    Airbus A350                    1.081165e+06
    Airbus A380                    1.647714e+06
    """

    

def airline_destinations(emissions_df, airport_code):
    return emissions_df[emissions_df['from_airport_code'] == airport_code].groupby('airline_name')['dest_country'].nunique()
    """
    Question 5

    Given an airport code for the depature airport count the number of unique 
    destination countries that each airline flies to.

    THIS MUST BE DONE IN ONE LINE!!!

    Args:
        emissions_df (pd.DataFrame)
        airport_code (string)

    Return:
        pandas.core.series.Series

    >>> airline_destinations(pandas_cleaner('Flight_Emission_Data.csv'), "ATH")

    airline_name
    Aegean                4
    Aer Lingus            3
    Air Baltic            2
    Air Canada            6
    Air Europa            3
    Air France           34
    Air Serbia            1
    Air Transat           2
    American              4
    Arkia                 1
    Austrian             12
    British Airways      29
    Brussels Airlines    11
    Delta                 6
    EgyptAir              7
    Emirates             23
    Ethiopian             4
    Etihad               15
    Eurowings             2
    Gulf Air              6
    ITA                   7
    Iberia               22
    Lufthansa            32
    MEA                   4
    Qatar Airways        21
    Royal Jordanian       8
    SAS                  13
    SWISS                23
    Saudia                9
    Scoot                 8
    Sky Express           1
    Turkish Airlines     38
    United                4
    Vueling               7
    Name: dest_country, dtype: int64

    """

    

def nonstop_multiday(emissions_df):
    emissions_df['O&D'] = emissions_df['from_airport_code'] + '-' + emissions_df['dest_airport_code'] 
    emissions_df['Nonstop'] = emissions_df['stops'] != 1
    emissions_df['Multiday'] = emissions_df['duration'] > (24 * 60)
    return emissions_df

    """
    Question 6

    Add three new columns to the dataframe:
        1) "O&D" - join the "from_airport_code" and the "dest_airport_code" with a hyphen
        1) "Nonstop" - if the number of stops is 1 make this value be False otherwise make this value True
        2) "Multiday" - if duration is greater than 24 hours worth of minutes make this value True else false

    You should return the modified original dataframe

    Args:
        emissions_df (pd.DataFrame)

    Return:
        pd.DataFrame

    >>> nonstop_multiday(pandas_cleaner('Flight_Emission_Data.csv'))

            from_airport_code from_country dest_airport_code dest_country        airline_name departure_time  arrival_time  duration  stops  price  co2_emissions  avg_co2_emission_for_this_route aircraft_type_1 aircraft_type_2      O&D  Nonstop  Multiday
    0                    ALG      Algeria               MEL    Australia       Qatar Airways  4/30/22 15:20  5/2/22 16:10      2390      1   2062      1968000.0                        1827762.0     Airbus A330      Boeing 777  ALG-MEL    False      True
    1                    ALG      Algeria               SYD    Australia       Qatar Airways  4/30/22 15:20  5/2/22 17:25      2465      1   2313      1564000.0                        1885118.0     Airbus A330     Airbus A350  ALG-SYD    False      True
    2                    ALG      Algeria               MEL    Australia       Qatar Airways   5/2/22 15:20  5/4/22 16:10      2390      1   1604      1968000.0                        1827762.0     Airbus A330      Boeing 777  ALG-MEL    False      True
    3                    ALG      Algeria               SYD    Australia       Qatar Airways   5/2/22 15:20  5/4/22 17:25      2465      1   1863      1564000.0                        1885118.0     Airbus A330     Airbus A350  ALG-SYD    False      True
    4                    ALG      Algeria               MEL    Australia       Qatar Airways   5/6/22 15:20  5/8/22 16:10      2390      1   2298      1854000.0                        1827762.0     Airbus A330      Boeing 777  ALG-MEL    False      True
    ...                  ...          ...               ...          ...                 ...            ...           ...       ...    ...    ...            ...                              ...             ...             ...      ...      ...       ...
    146727               BOM        India               SYD    Australia  Singapore Airlines   5/1/22 23:40  5/3/22 05:55      1545      1   1239       993000.0                        1133000.0     Airbus A380     Airbus A350  BOM-SYD    False      True
    146728               BOM        India               SYD    Australia  Singapore Airlines   5/1/22 23:40  5/3/22 19:15      2345      1   1270      1312000.0                        1133000.0     Airbus A380      Boeing 777  BOM-SYD    False      True
    146729               BOM        India               SYD    Australia            Emirates   5/1/22 15:35  5/2/22 22:05      1560      1   1317      1584000.0                        1133000.0      Boeing 777     Airbus A380  BOM-SYD    False      True
    146730               BOM        India               SYD    Australia            Emirates   5/1/22 19:20  5/2/22 22:05      1335      1   1317      1567000.0                        1133000.0      Boeing 777     Airbus A380  BOM-SYD    False     False
    146731               BOM        India               SYD    Australia            Emirates   5/1/22 22:20  5/2/22 22:05      1155      1   1317      1583000.0                        1133000.0      Boeing 777     Airbus A380  BOM-SYD    False     False

    [118319 rows x 17 columns]

    """

    

def destination_costs(emissions_df, airline, arrival_airport):
    filtered_df = emissions_df[(emissions_df['airline_name'] == airline) & (emissions_df['dest_airport_code'] == arrival_airport)]
    # filtered_df = filtered_df[~filtered_df.duplicated(subset=['price', 'departure_time'])] was told to not use .duplicated in OH 
    filtered_df=filtered_df.drop_duplicates(subset=['price', 'departure_time'])
    # print(filtered_df.sort_values(by='price', ascending=False, inplace=True))
    finaldf=filtered_df.sort_values(by='price', ascending=False, inplace=False)
    return finaldf.head(5)
    


    ## Nan values error 
    """
    Question 7

    Given an airline and an arrival airport code return a dataframe containing the top five most expensive flights to that
    destination with that airline. Remove any rows where the price and departure time are the same across both rows
    before returning the top five.

    Args:
        emissions_df        (pd.DataFrame)
        airline             (string)
        arrival_airport     (string)

    Return:
        pd.DataFrame

    >>> destination_costs(flight_data, "Lufthansa", "LIS")

            from_airport_code from_country dest_airport_code dest_country airline_name departure_time   arrival_time  duration  stops  price  co2_emissions  avg_co2_emission_for_this_route aircraft_type_1 aircraft_type_2
    28078                GRU       Brazil               LIS     Portugal    Lufthansa  5/14/22 18:15  5/15/22 15:15      1020      1   6949      5167000.0                         725000.0      Boeing 747     Airbus A321
    27914                GRU       Brazil               LIS     Portugal    Lufthansa  4/30/22 18:15   5/2/22 11:15      2220      1   5420      4136000.0                         725000.0      Boeing 747  Airbus A321neo
    27913                GRU       Brazil               LIS     Portugal    Lufthansa  4/30/22 18:15   5/1/22 23:30      1515      1   5399      4198000.0                         725000.0      Boeing 747     Airbus A321
    27972                GRU       Brazil               LIS     Portugal    Lufthansa   5/2/22 18:15   5/3/22 23:40      1525      1   5399      4136000.0                         725000.0      Boeing 747  Airbus A321neo
    145076               BOM        India               LIS     Portugal    Lufthansa   5/3/22 02:50   5/4/22 11:15      2215      1   3225      3211000.0                         900000.0      Boeing 747     Airbus A321

    """

    

###################################################
###################################################
"""
EXTRA CREDIT SECTION

The extra credit section is designed to inform you more about runtime and efficiency in your code. You must complete all
parts of this in order to receive extra credit.

For the following functions instead of replacing the "pass" statement remove the line of code that says "raise NotImplementedError"

Before completing this problem, you must run "pip install codecarbon" in terminal
"""
###################################################
###################################################

def csv_timing():
    ## this code was also predominantly done through office hours 
    # csv_tracker=EmissionsTracker()
    # csv_tracker.start()
    # start_time=time.time()
    # csv_cleaner("Flight_Emission_Data.csv")
    # endingtime=time.time()
    # CSVemissions=csv_tracker.stop()
    # totaltime=endingtime-start_time
    # finalruntime=time.time()-runtime
    # return(csv_tracker,CSVemissions,totaltime)

    """
    EXTRA CREDIT Part 1

    In this function, you will be using two new modules: the codecarbon emissions tracker and the time module for runtime.
    You will be reporting the runtime and emissions for the csv_cleaner function.

    Your code needs to do the following things:
        1) Start the emissions tracker in code carbon
        2) Record the time that the csv_cleaner function is called 
        3) Call the csv_cleaner function with the correct file name
        4) Record the time that the csv_cleaner function completes running
        5) End the emissions tracker in code carbon - this will give you the variable CSVemissions = csv_tracker.stop()

    The emissions tracker object has been provided for you. You simply need to call the start and stop methods on this object 
    before and after calling the csv_cleaner() function. This object has already been returned for you. You simply need to 
    add the other two elements to the tuple.

    Report the emissions results along with the difference in the end and start times as a tuple

    Args:
        None

    Returns:
        Tuple (csv_tracker, emissions results, time elapsed)

    >>> csv_timing()

    """

    csv_tracker = EmissionsTracker()    # UNCOMMENT THIS LINE OF CODE

    #########################
    """
    Replace the following line of code with your function
    """
    #########################
    csv_tracker.start()
    start_time=time.time()
    csv_cleaner("Flight_Emission_Data.csv")
    endingtime=time.time()
    CSVemissions=csv_tracker.stop()
    totaltime=endingtime-start_time

    #########################

    return (csv_tracker, CSVemissions, totaltime)

def pandas_timing():
    
    # finalruntime=time.time()-runtime
    # return(csv_tracker,CSVemissions,totaltime)
    """
    EXTRA CREDIT Part 2

    In this function, you will be using two new modules: the codecarbon emissions tracker and the time (time.time()) module for runtime.
    You will be reporting the runtime and emissions for the pandas_cleaner function.

    Your code needs to do the following things:
        1) Start the emissions tracker in code carbon
        2) Record the time that the csv_cleaner function is called 
        3) Call the csv_cleaner function with the correct file name
        4) Record the time that the csv_cleaner function completes running
        5) End the emissions tracker in code carbon - this will give you the variable DFemissions = df_tracker.stop()

    The emissions tracker object has been provided for you. You simply need to call the start and stop methods on this object 
    before and after calling the pandas_cleaner() function. This object has already been returned for you. You simply need to 
    add the other two elements to the tuple.

    Report the emissions results along with the difference in the end and start times as a tuple

    Args:
        None

    Returns:
        Tuple (csv_tracker, emissions results, time elapsed)

    >>> pandas_timing()

    """
    
    # UNCOMMENT THIS LINE OF CODE
    pandastrack=EmissionsTracker()
    pandastrack.start()
    start_time=time.time()
    pandas_cleaner("Flight_Emission_Data.csv")
    endingtime=time.time()
    DFemissions=pandastrack.stop()
    totaltime=endingtime-start_time

    #########################
    """
    Replace the following line of code with your function
    """
    #########################

    return (pandastrack, DFemissions, totaltime)

def efficiency_comparison():
    temptuple1=csv_timing()[1:]
    tuple2=pandas_timing()[1:]
    tupleline1=tuple2[0]-temptuple1[0]
    tupleline2=tuple2[1]-temptuple1[1]
    finaltuple=(tupleline1,tupleline2)
    return finaltuple


    """
    EXTRA CREDIT Part 3

    In this function, you will be comparing the outputs from the previous two questions

    Your code should call the csv_timing() & pandas_timing(). Both of these functions output tuples,
    you should subtract the DF emissions from the CSV emissions and then subtract the DF times from the CSV times. 
    Return these two values as a tuple: (emissions_delta, time_delta)

    Args:
        None

    Returns:
        Tuple (emissions_delta, time_delta)

    >>> efficiency_comparison()

    """

    #########################
    """
    Replace the following line of code with your function
    """
    #########################



if __name__ == "__main__":

    # Q1
    # pprint(csv_cleaner('Flight_Emission_Data.csv'))

    # # Q2
    # pprint(pandas_cleaner('Flight_Emission_Data.csv'))

    ####################################################
    ####################################################
    """
    DO NOT MODIFY CODE BELOW
    """
    try:
        flight_data = pd.read_csv("cleaned_emissions_data_pandas.csv", index_col=0)
    except:
        print("##########\n#\nYou must complete questions 1 and 2 before moving on to the next questions\n#\n##########")

    ####################################################
    ####################################################
        
    ####################################################
    ####################################################   
    """
    Q3 - 7 SHOULD ALL BE RUN INDEPENDENTLY
    """
    ####################################################
    #################################################### 
        
    # Q3
    # pprint(average_co2_percentage(flight_data))

    # Q4
    # pprint(airbus_emissions_average(flight_data))

    # # Q5
    # pprint(airline_destinations(flight_data, "ATH"))
    # pprint(airline_destinations(flight_data, "FRA"))

    # # Q6 
    # pprint(nonstop_multiday(flight_data))
        
    # # Q7
    # pprint(destination_costs(flight_data, "Lufthansa", "LIS"))
    # pprint(destination_costs(flight_data, "Air France", "FCO"))
        
    # EXTRA CREDIT Part I
    # print(csv_timing())

    # EXTRA CREDIT Part 2
    # print(pandas_timing())
        
    # EXTRA CREDIT Part 3
    print(efficiency_comparison())






