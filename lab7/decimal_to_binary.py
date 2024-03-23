def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    result = ""
    q = decimal

    while q != 0:
        r = q % 2
        result = str(r) + result
        q //= 2

    return result