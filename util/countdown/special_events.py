import datetime

today = datetime.date.today()
current_year = today.year

BIRTHDAYS = {
    "Hudson": datetime.date(current_year, 2, 14),
    "Chris": datetime.date(current_year, 4, 21),
    "Alex": datetime.date(current_year, 4, 15),
    # 💔
    # "Daniel": datetime.date(current_year, 4, 3),
    # "Lex": datetime.date(current_year, 5, 20),
    "Justin": datetime.date(current_year, 6, 12),
    "Josh": datetime.date(current_year, 6, 27),
    "Matt": datetime.date(current_year, 9, 24),
    "Hobo": datetime.date(current_year, 9, 11),
    "Conrad": datetime.date(current_year, 10, 2),
    "Vynle": datetime.date(current_year, 5, 9),
}
BIRTHDAYS = {
    f"""{goon}{"'" if goon[-1] == "s" else "'s"} birthday""" + " 🧁": date for goon, date in BIRTHDAYS.items()
}

HOLIDAYS = {
    "Valentine's Day 💕": datetime.date(current_year, 2, 14),
    "Freedom Day :us_flag:": datetime.date(current_year, 7, 6),
    "Thanksgiving 🦃": datetime.date(current_year, 11, 24),
    "Christmas 🎄": datetime.date(current_year, 12, 25),
    "New Year's Eve 🥳": datetime.date(current_year, 12, 31),
}

SPECIAL_EVENTS = {**BIRTHDAYS, **HOLIDAYS}
