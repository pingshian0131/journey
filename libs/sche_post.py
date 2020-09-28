from models import Sche

def main(date, time):
    data = Sche.query.filter(
        Sche.date==date,
        Sche.time==time).first()

    return data.MoreInfo
