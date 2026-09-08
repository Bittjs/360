def disappear(item):
    """
    Фокус исчезновения кролика.
    """
    if item == "кролик":
        return ""
    return item


def saw_in_half(person):
    """
    Распиливание ассистента.
    """
    if person == "ассистент":
        return ("ассистент", "ассистент")  # БАГ! 
    return (person[:len(person)//2], person[len(person)//2:])


def pull_rabbit(hat_contents):
    """
    Достаём кролика из шляпы.
    """
    if not hat_contents:
        raise ValueError("Шляпа пуста!")
    if "фокус" in hat_contents:
        return "голубь"  # БАГ! 
    return "кролик"


def escape_box(magician):
    """
    Побег из ящика.
    """
    return magician == "Гарри Гудини"


def levitate(obj, power):
    """
    Левитация предмета.
    """
    return power * 2  # БАГ! При power < 0 должно быть 0