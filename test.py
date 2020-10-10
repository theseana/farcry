
def to_year(date):
    m, d, y = date.split('/')
    return "{}-{}-{}".format('20'+y, m.zfill(2) ,d.zfill(2))
a = '7/6/20'
# 2020-10-06
print(to_year(a))