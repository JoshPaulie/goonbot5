def time_of_day(hour: str) -> str:
    if hour in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]:
        return "morning"
    elif hour in ["12", "13", "14", "15", "16"]:
        return "afternoon"
    else:
        return "night"
