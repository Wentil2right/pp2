from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    return abs(difference.total_seconds())

# Example usage:
date1 = datetime(2024, 2, 10, 12, 0, 0)  # First date
date2 = datetime(2024, 2, 11, 12, 0, 0)  # Second date

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference between the two dates in seconds:", difference_seconds)