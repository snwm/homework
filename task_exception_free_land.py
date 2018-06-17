def get_free_land(s, p):
    s = s[0] * 100
    p = p[0] * p[1]

    if not s:
        raise ValueError("Не задана площадь участка")
    elif not p:
        raise ValueError("Не задана площадь грядки")
    elif p > s:
        raise ValueError("Размер грядки больше размера участка")

    return s % p
