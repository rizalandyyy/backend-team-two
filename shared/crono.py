from datetime import timedelta, datetime, timezone


def now():
    """Get the current UTC time."""
    return datetime.now(timezone.utc)


def back_days(days: int):
    """Get the date and time for a number of days ago."""
    return datetime.now(timezone.utc) - timedelta(days=days)


def forward_days(days: int):
    """Get the date and time of days in the future."""
    return datetime.now(timezone.utc) + timedelta(days=days)
