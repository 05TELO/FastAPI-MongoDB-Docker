import re
from datetime import datetime

email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
phone_regex = re.compile(r"^\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$")


def serialized_id(template):
    template["_id"] = str(template["_id"])
    return template


def check_field(field) -> str:
    try:
        datetime.strptime(field, "%d.%m.%Y")
        return "date"
    except ValueError:
        ...
    try:
        datetime.strptime(field, "%Y-%m-%d")
        return "date"
    except ValueError:
        ...
    if phone_regex.match(field):
        return "phone"
    if email_regex.match(field):
        return "email"
    return "text"
