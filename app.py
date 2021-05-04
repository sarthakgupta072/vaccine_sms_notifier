import config.app_config as app_config
from notifyVaccineAvailibility import checkSlotsForNext30Days

phone = app_config.PHONE
age = app_config.AGE
pincode = app_config.PINCODE


def main():
    checkSlotsForNext30Days(pincode, age, phone)


if __name__ == '__main__':
    main()
