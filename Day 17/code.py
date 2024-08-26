
# Day 17 Code Implementation

from datetime import datetime

def get_current_datetime():
    """Retrieves the current date and time."""
    return datetime.now()

def parse_datetime(datetime_string):
    """Parses a string representing a date and time into a datetime object."""
    return datetime.strptime(datetime_string, "%Y-%m-%dT%H:%M:%S")

def format_datetime(datetime_object, format_string):
    """Formats a datetime object as a string according to the specified format."""
    return datetime_object.strftime(format_string)

def add_days(datetime_object, days):
    """Adds a specified number of days to a datetime object."""
    return datetime_object + timedelta(days=days)

# Example Usage
current_datetime = get_current_datetime()
print("Current date and time:", current_datetime)

datetime_string = "2024-02-15T12:34:56"
parsed_datetime = parse_datetime(datetime_string)
print("Parsed datetime:", parsed_datetime)

formatted_datetime = format_datetime(parsed_datetime, "%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

new_datetime = add_days(parsed_datetime, 3)
print("Datetime after adding 3 days:", new_datetime)

