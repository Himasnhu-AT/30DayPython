
/* DAY 17: Working with Dates and Times using the 'datetime' module.
 *
 * **Objective:**
 * - Write functions for retrieving, parsing, formatting, and manipulating dates and times.
 *
 * **Instructions:**
 * - Complete the provided functions below.
 * - Refer to the sample implementation for guidance.
 * - Run the tests to check the correctness of your code.
 *
 * **LICENSE: ALL RIGHTS RESERVED (C) 2024 @OpenEdu <git: openeduhq> @Himanshu <git: himanshu-at>
 *
 **/

from datetime import datetime, timedelta

def get_current_datetime():
    """Retrieves the current date and time."""
    # YOUR CODE HERE

def parse_datetime(datetime_string):
    """Parses a string representing a date and time into a datetime object."""
    # YOUR CODE HERE

def format_datetime(datetime_object, format_string):
    """Formats a datetime object as a string according to the specified format."""
    # YOUR CODE HERE

def add_days(datetime_object, days):
    """Adds a specified number of days to a datetime object."""
    # YOUR CODE HERE

# Example Usage (Do not modify)
current_datetime = get_current_datetime()
print("Current date and time:", current_datetime)

datetime_string = "2024-02-15T12:34:56"
parsed_datetime = parse_datetime(datetime_string)
print("Parsed datetime:", parsed_datetime)

formatted_datetime = format_datetime(parsed_datetime, "%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

new_datetime = add_days(parsed_datetime, 3)
print("Datetime after adding 3 days:", new_datetime)
