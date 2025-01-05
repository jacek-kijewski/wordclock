def time_in_words(hour: int, minute: int) -> str:
    starting_words = "IT IS"
    minutes_words = ["FIVE", "TEN", "QUARTER", "TWENTY", "TWENTY FIVE", "HALF", "TWENTY FIVE",
                     "TWENTY", "QUARTER", "TEN", "FIVE"]
    hours = [
        "TWELVE", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN",
        "ELEVEN"
    ]

    next_hour = (hour + 1) % 12

    if minute < 3:
        return f"{starting_words} {hours[hour]} OCLOCK"
    elif minute < 8:
        return f"{starting_words} FIVE PAST {hours[hour]}"
    elif minute < 13:
        return f"{starting_words} TEN PAST {hours[hour]}"
    elif minute < 18:
        return f"{starting_words} QUARTER PAST {hours[hour]}"
    elif minute < 23:
        return f"{starting_words} TWENTY PAST {hours[hour]}"
    elif minute < 28:
        return f"{starting_words} TWENTY FIVE PAST {hours[hour]}"
    elif minute < 33:
        return f"{starting_words} HALF PAST {hours[hour]}"
    elif minute < 38:
        return f"{starting_words} TWENTY FIVE TO {hours[next_hour]}"
    elif minute < 43:
        return f"{starting_words} TWENTY TO {hours[next_hour]}"
    elif minute < 48:
        return f"{starting_words} QUARTER TO {hours[next_hour]}"
    elif minute < 53:
        return f"{starting_words} TEN TO {hours[next_hour]}"
    elif minute < 58:
        return f"{starting_words} FIVE TO {hours[next_hour]}"
    else:
        return f"{starting_words} {hours[next_hour]} OCLOCK"


# for i in range(0, 60):
#     print('{}: {}'.format(i, time_in_words(0, i)))

# Examples
# print(time_in_words(0, 0))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 1))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 2))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 3))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 9))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 10))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 11))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 15))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 20))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 25))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 30))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 32))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 35))  # IT IS TWELVE O'CLOCK (Noon)
# print(time_in_words(0, 40))  # IT IS HALF PAST TWELVE
# print(time_in_words(0, 45))  # IT IS QUARTER TO TWELVE
# print(time_in_words(0, 50))  # IT IS QUARTER TO TWELVE
# print(time_in_words(0, 55))  # IT IS QUARTER TO TWELVE
# print(time_in_words(1, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(2, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(3, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(4, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(5, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(6, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(7, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(8, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(9, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(10, 0))  # IT IS QUARTER TO TWELVE
# print(time_in_words(11, 0))  # IT IS QUARTER TO TWELVE
