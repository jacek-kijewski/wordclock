def time_in_words(hour: int, minute: int) -> str:
    starting_words = "IT IS"
    minutes_words = ["FIVE", "TEN", "QUARTER", "TWENTY", "TWENTY FIVE", "HALF", "TWENTY FIVE",
                     "TWENTY", "QUARTER", "TEN", "FIVE"]
    hours = [
        "TWELVE", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN",
        "ELEVEN"
    ]

    if minute < 5:
        return f"{starting_words} {hours[hour]} OCLOCK"
    elif minute <= 30:
        minutes_index = minute // 5 - 1
        return f"{starting_words} {minutes_words[minutes_index]} PAST {hours[hour]}"
    else:
        minutes_index = (60 - minute) // 5 -1
        next_hour = (hour + 1) % 12
        return f"{starting_words} {minutes_words[minutes_index]} TO {hours[next_hour]}"

# Examples
# print(time_in_words(0, 0))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 2))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 5))  # IT IS TWELVE O'CLOCK (mindnight)
# print(time_in_words(0, 7))  # IT IS TWELVE O'CLOCK (mindnight)
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

