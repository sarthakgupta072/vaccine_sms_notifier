from sendsms import sendSms
import requests
import config.app_config as app_config
from typing import Dict
from datetime import date, timedelta

import logging

headers: Dict = {
    'Content-type': 'application/json',
}

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s ; %(levelname)s ; %(message)s ")

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def checkSlotsForNext30Days(pincode, age, phone):
    logger.info("Checking slots for the next 30 days")
    current_date = date.today()

    target_date = date(current_date.year,
                       (current_date.month + 1) % 13, current_date.day)

    if(current_date.day == 31):
        target_date = date(current_date.year,
                           (current_date.month + 1) % 13, current_date.day - 1)

    delta = timedelta(days=1)

    date_pointer = current_date

    flag = 0
    while date_pointer <= target_date:
        if(flag > 31):
            break
        slots = getVaccineSlotsByPicodeAndDate(
            pincode, date_pointer.strftime('%d-%m-%Y'), age)
        if len(slots) > 0:
            logger.info(f"Slots found on {date_pointer.strftime('%d-%m-%Y')}")
            sendSms(phone, pincode, date_pointer.strftime('%d-%m-%Y'))
            return
        date_pointer = date_pointer + delta
        flag = flag + 1
        logger.info(f"Slots NOT found on {date_pointer.strftime('%d-%m-%Y')}")
    logger.info("Slots not found in next 30 days")


def getVaccineSlotsByPicodeAndDate(pincode, date, age):
    response = requests.get(
        f"{app_config.BASE_URL}?pincode={pincode}&date={date}", headers=headers)
    results = response.json()
    sessions = results['sessions']

    available_sessions = []

    for session in sessions:
        if(int(age) >= int(session['min_age_limit'])):
            available_sessions.append(session)

    return available_sessions
