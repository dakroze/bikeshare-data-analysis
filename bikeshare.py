import time
import pandas as pd
import numpy as np
from my_input_function import input_filter
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago','new york city','washington']
MONTHS = ['all','january','february','march','april','may','june']
DAYS = ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n\nHello! Let\'s explore some US bikeshare data!\n')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid         inputs
    print('\nChicago, New York City or Washington. Input your city.')
    city = input_filter(CITIES)
    print('\nFor what month do you need data for? Input required month. If you need all months, type \'all\'.')
    month = input_filter(MONTHS)
    print('\nMonday, Tuesday, ... Sunday? Please input required day. If you need all days, type type \'all\'.')
    day = input_filter(DAYS)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # filename variable holds the csv file from the CITY_DATA dictionary
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time']  = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day']   = df['Start Time'].dt.day_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april','may','june','july','august']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april','may','june','july','august']
    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]

    # Convert from numerical to string representation
    convrt_month = months[(common_month - 1)].title()
    print('The most common month is: {}\n'.format(convrt_month))

    # TO DO: display the most common day of week
    common_day = df['Day'].mode()[0]
    print('The most common day is: {}\n'.format(common_day))

    # TO DO: display the most common start hour (from 0 to 23)
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('The most common hour is: {}hrs\n'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    sstation = df['Start Station'].mode()[0]
    print('\nMost commonly used start station is: {}\n'.format(sstation))

    # TO DO: display most commonly used end station
    estation = df['End Station'].mode()[0]
    print('\nMost commonly used end station is: {}\n'.format(estation))

    # TO DO: display most frequent combination of start station and end station trip
    Start,End= df[['Start Station','End Station']].mode().loc[0]
    print('\nMost frequent combination of start station and end station trip is: {} to {}\n'.format(Start,End))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    print('\nTotal Travel Time is: {}\n'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = np.mean(df['Trip Duration'])
    print('\nMean Travel Time is: {}\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_ct = df['User Type'].value_counts()
    
    # iterate through user type summary
    for i,ct in enumerate(user_type_ct):
        print('\n{}: {}\n'.format(user_type_ct.index[i],ct))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: #check to see if this column exists
        user_gender_ct = df['Gender'].value_counts()
        for i,ct in enumerate(user_gender_ct):
            print('\n{}: {}\n'.format(user_gender_ct.index[i],ct))
    else:
        print('\'Gender\' data for is not available for selected city.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest =  np.min(df['Birth Year'])
        most_recent = np.max(df['Birth Year'])
        most_common = df['Birth Year'].mode()[0]
        print('\nEarliest, Most recent, and Most common year of birth are: {}, {}, {} respectively.\n'.format(earliest,most_recent,most_common))

    else:
        print('\n\'Birth Year\' data is not available for selected city.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Prompts user response and displays 5 rows of file raw data"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    pd.set_option('display.max_columns',300)
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
