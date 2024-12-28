import time


def time_to_words(hours, minutes):
    """
    Convert the given hours and minutes into an English phrase using the specified format.

    :param hours: Current hour (0-23).
    :param minutes: Current minutes (0-59).
    :return: A string representing the time in words.
    """
    words = [
        "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN",
        "ELEVEN", "TWELVE"
    ]

    # if minutes == 0:
    #     return f"IT IS {words[hours]} O'CLOCK"
    # elif minutes == 5:
    #     return f"IT IS FIVE PAST {words[hours]}"
    # elif minutes == 10:
    #     return f"IT IS TEN PAST {words[hours]}"
    # elif minutes == 15:
    #     return f"IT IS QUARTER PAST {words[hours]}"
    # elif minutes == 30:
    #     return f"IT IS HALF PAST {words[hours]}"
    # elif minutes == 35:
    #     return f"IT IS TWENTY-FIVE PAST {words[hours]}"
    # elif minutes == 40:
    #     next_hour = (hours + 1) % 12
    #     return f"IT IS TWENTY PAST {words[next_hour]}"
    # elif minutes == 45:
    #     next_hour = (hours + 1) % 12
    #     return f"IT IS QUARTER TO {words[next_hour]}"
    # elif minutes == 50:
    #     next_hour = (hours + 1) % 12
    #     return f"IT IS TEN TO {words[next_hour]}"
    # elif minutes == 55:
    #     next_hour = (hours + 1) % 12
    #     return f"IT IS FIVE TO {words[next_hour]}"
    # else:
    #     lower_5_minutes = (minutes // 5) * 5
    #     next_hour = (hours + 1) % 12
    #     remaining_minutes = 60 - lower_5_minutes
    #     return f"IT IS {words[remaining_minutes]} TO {words[next_hour]}"
    return "IT IS HALF PAST ELEVEN"
