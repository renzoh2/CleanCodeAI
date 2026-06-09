import uuid
from datetime import date, datetime

#Formatting all data to String inside Dictionary
def dict_format(data:dict):
    for key, value in data.items():
        if isinstance(value, uuid.UUID):
            data[key] = str(value)
        if isinstance(value, (datetime, date)):
            data[key] = value.isoformat()
    return data
   