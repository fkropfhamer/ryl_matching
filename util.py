import datetime

def age(birthdate: str):
    birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
    today = datetime.datetime.today()

    delta = today - birthdate

    return delta.days // 365
