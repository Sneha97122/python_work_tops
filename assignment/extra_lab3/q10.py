class customerror(Exception):
    pass

try:
    raise customerror("this is custome exeption")
except customerror as e:
    print(e)