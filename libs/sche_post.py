from models import Sche

def main(date, time):
    data = Sche.query.filter(
        Sche.date==date,
        Sche.time==time).first()
    if data.MoreInfo:
        return data.MoreInfo
    else:
        return 'empty'
