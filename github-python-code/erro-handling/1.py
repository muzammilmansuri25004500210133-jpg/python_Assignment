class PriceError(Exception):
    pass
try:
    price=int(input("Enter price : "))
    if price < 0:
        raise PriceError("Price shoud bi nagative ")
except PriceError as e:
    print(e)