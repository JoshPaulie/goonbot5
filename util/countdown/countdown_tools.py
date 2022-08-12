import datetime

from util.countdown.special_events import SPECIAL_EVENTS


def days_since(end_date: datetime.date, today_date: datetime.date) -> int:
    """Returns days since end_date from today_date. Used later to sort special events remaining in current year."""
    return (end_date - today_date).days


def get_special_events_remaining(today_date: datetime.date) -> list[tuple[str, int]]:
    """
    Returns list of special events remaining for this year, paired with how many days until (if any).
    The list is ordered by closest-event-first.

    Note: Without a fresh datetime object being passed every call, the countdown is stuck at whatever day the bot happened to be started
    """
    special_events_remaining = {
        special_event: days_since(date, today_date)
        for special_event, date in SPECIAL_EVENTS.items()
        if days_since(date, today_date) > -1
    }
    special_events_remaining = sorted(special_events_remaining.items(), key=lambda x: x[1])
    return special_events_remaining
