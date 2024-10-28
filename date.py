from datetime import datetime, timedelta

def generate_month_days(month_number):
    # Validate month input
    if not 1 <= month_number <= 12:
        return "Invalid month number. Please enter a number between 1 and 12."
    
    # Use current year for the calendar
    year = datetime.now().year
    
    # Create the first day of the month
    first_day = datetime(year, month_number, 1)
    
    # Get the last day of the month by going to next month and subtracting one day
    if month_number == 12:
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(year, month_number + 1, 1) - timedelta(days=1)
    
    # Generate all days of the month
    days = []
    current_day = first_day
    while current_day <= last_day:
        # Get day number (1=Sunday, 2=Monday, ..., 7=Saturday)
        day_number = current_day.strftime('%u')
        # Convert day numbers: Sunday(7)->cn, Others->number+1
        day_code = 'cn' if int(day_number) == 7 else str(int(day_number) + 1)
        # Format the date with day code
        formatted_date = f"{day_code}/{current_day.strftime('%d/%m')}"
        days.append(formatted_date)
        current_day += timedelta(days=1)
    
    return days

def main():
    try:
        # Get input from user
        month = int(input("Enter a month number (1-12): "))
        
        # Generate days
        month_days = generate_month_days(month)
        
        # Write to file
        with open( f'{str(month)}.txt', 'w') as file:
            for day in month_days:
                file.write(day +   ": " +'\n')
            
        print("Days have been written to input.txt")
        
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
