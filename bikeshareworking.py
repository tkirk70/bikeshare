import time
import pandas as pd
import numpy as np
import calendar

start_time_total = time.time()

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA:
        city = input("What city would you like to explore? ")
    else:
        print("One moment, please. ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("What month would you like to look at? ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What day are you interested in? ")

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

    df = pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    mode_month = df['month'].mode()[0]
    mode_month = calendar.month_name[mode_month]
    print(mode_month)
    # TO DO: display the most common day of week
    mode_day = df['day'].mode()[0]
    mode_day = calendar.day_name[mode_day]
    print(mode_day)
    # TO DO: display the most common start hour
    mode_hour = df['hour'].mode()[0]
    print(mode_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used end station
    mode_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", mode_start_station)
    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ", mode_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' to ' + df['End Station']
    mode_trip = df['trip'].mode()[0]
    print("The most common combination of start and end stations is: ", mode_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(total_time)
    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()
    print(average_time)
    max_time = df['Trip Duration'].max()
    print(max_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    # print('The total amount of user types is:\n{}'.format(user_count))
    # print('\nCalculating User Stats...\n')
    print("subscriber:")
    print(user_count.loc['Subscriber'])
    print("customer:")
    print(user_count.loc['Customer'])


    # TO DO: Display counts of gender
    count_gender = df['Gender'].value_counts()
    # print('The gender stats are:\n{}'.format(count_gender))
    # print('\nCalculating User Stats...\n')
    print("male:")
    print(count_gender.loc['Male'])
    print("female:")
    print(count_gender.loc['Female'])



    # TO DO: Display earliest, most recent, and most common year of birth
    oldest_year = df['Birth Year'].min()
    print("The oldest rider was born in ", oldest_year)

    youngest_year = df['Birth Year'].max()
    print("The youngest rider was born in ", youngest_year)

    mode_year = df['Birth Year'].mode()[0]
    print("Most riders were born in ", mode_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(city, month, day)
        print(df.head(3))
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print("\nThe total time for the program was %s seconds " % (time.time() - start_time_total))
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
