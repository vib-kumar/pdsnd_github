import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
daysofweek = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

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
    while True:
        city = str(input("\nSelect a city: New York City, Chicago or Washington? - ")).lower()
        if city not in CITY_DATA:
            print("Invalid city selection. Please try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("\nSelect a month: January, February, March, April, May, June, or type 'all' to apply no month filter - ")).lower()
        if month not in months:
            print("Invalid month selection. Please try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("\nSelect a day of week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or type 'all' to apply no day filter - ")).lower()
        if day not in daysofweek:
            print("Invalid day of week selection. Please try again.")
            continue
        else:
            break

    print('-'*100)
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

    #load file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to datetime datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from the Start Time column
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month == 'all':
        pass #do nothing
    else:
   	 	#change month text to month number
        month_num = months.index(month)

        #create the new dataframe
        df = df[df['Month'] == month_num]

    #filter by day of week
    if day == 'all':
        pass #do nothing
    else:
        #create the new dataframe
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]
    print('Most Common Day of Week:', most_common_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour #extract hour from the Start Time column
    most_common__hour = df['Hour'].mode()[0]
    print('Most Common Hour:', most_common__hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('\nMost Common End Station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_start_end_combination_station = df['Start-End'].mode()[0]
    print('Most Common Start and End Station Combination:', most_common_start_end_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time:',
          str(int(total_travel_time//86400)) + ' days ' +
          str(int((total_travel_time%86400)//3600)) + ' hours ' +
          str(int(((total_travel_time%86400)%3600)//60)) + ' minutes')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', str(int(mean_travel_time//60)) + ' min ' + str(int(mean_travel_time%60)) + ' sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Gender:\n', gender)

    except:
        print('Gender info not avilabale')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = str(int(df['Birth Year']).min())
        most_recent_birthyear = str(int(df['Birth Year']).max())
        most_common_birthyear = str(int(df['Birth Year'].mode()[0]))

        print('Earliest Birth Year:', earliest_birthyear)
        print('Most Recent Birth Year:', most_recent_birthyear)
        print('Most Common Birth Year:', most_common_birthyear)

    except:
        print('Birth data not avilable')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
