# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
import config.sms_config as sms_config
import logging
# the following line needs your Twilio Account SID and Auth Token

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

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number


def sendSms(phoneNumber, pincode, date):
    logger.info("Sending SMS....")
    client = Client(sms_config.SID,
                    sms_config.TOKEN)
    client.messages.create(to=f"+91{phoneNumber}",
                           from_=f"{sms_config.PHONE}",
                           body=f"Hey {phoneNumber}! Vaccine slots are available at your pincode: {pincode} on {date}. Book now at https://selfregistration.cowin.gov.in/ before it gets filled!!")

    logger.info(f"SMS sent to {phoneNumber}")
