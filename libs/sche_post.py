from models import Sche

def main(date, time):
    print(date, time)
    datas = Sche.query.all()
    for data in datas:
        print(data.date)
        print(data.time)
    data = Sche.query.filter(
        Sche.date==date,
        Sche.time==time).first()

    return data.MoreInfo
