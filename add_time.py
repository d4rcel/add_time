def add_time(start, duration, op):
    # Split the start time into hours and minutes
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Split the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate the total minutes
    total_minutes = start_hours * 60 + start_minutes + duration_hours * 60 + duration_minutes

    # Calculate the new time
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    # Determine the period (AM or PM)
    if period == 'PM':
        new_hours += 12

    # Determine the number of days later
    days_later = new_hours // 24

    # Determine the new period
    new_period = 'AM' if new_hours % 24 < 12 else 'PM'

    # Convert the new hours to 12-hour format
    new_hours = new_hours % 12
    if new_hours == 0:
        new_hours = 12

    # Format the new time
    new_time = f"{new_hours}:{new_minutes:02d} {new_period}"
    # Add the number of days later to the new time
    if days_later == 1:
        new_time += " (next day)"

    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time