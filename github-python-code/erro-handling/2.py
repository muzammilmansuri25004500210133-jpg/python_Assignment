class MaeksError(Exception):
    pass
try:
    marks=int(input("Enter price : "))
    if not(marks >= 0 and marks <= 50):
        raise MaeksError("marks is not berween (0-50) ")
except MaeksError as e:
    print(e)