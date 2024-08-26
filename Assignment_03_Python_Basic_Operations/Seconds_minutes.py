# Function to convert seconds to minutes
def seconds_to_minutes(seconds):
    return seconds / 60

# Function to convert minutes to seconds
def minutes_to_seconds(minutes):
    return minutes * 60

# Example usage
seconds = float(input("Enter time in seconds: "))
minutes = float(input("Enter time in minutes: "))

converted_minutes = seconds_to_minutes(seconds)
converted_seconds = minutes_to_seconds(minutes)

print(f"{seconds} seconds is equal to {converted_minutes:.2f} minutes.")
print(f"{minutes} minutes is equal to {converted_seconds:.2f} seconds.")
