# Eliya Statema
# 3/6/25
# Rainfall

def main():
    month_names = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
    rainfall = []
    print("Enter the total rainfall per month: ")

    for month in month_names:
        while True:
            try:
                rain = float(input(f"Enter rainfall for {month}: "))
                if rain >= 0:
                    rainfall.append(rain)
                    break
                else:
                    print("Rainfall cannot be negative. Please enter a positive number or 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total_rain = sum(rainfall)
    average_rain = total_rain / len(rainfall)

    highest_rainfall = max(rainfall)
    highest_month = month_names[rainfall.index(highest_rainfall)]

    lowest_rainfall = min(rainfall)
    lowest_month = month_names[rainfall.index(lowest_rainfall)]

    print("Yearly Rainfall:")
    print(f"Total rainfall for the year: {total_rain:.1f}")
    print(f"Average monthly rainfall: {average_rain:.1f}")
    print(f"Month with highest rainfall: {highest_month}")
    print(f"Month with lowest rainfall: {lowest_month}")

if __name__ == "__main__":
    main()