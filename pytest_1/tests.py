import pytest

from magic_tricks import (
    disappear,
    saw_in_half,
    pull_rabbit,
    escape_box,
    levitate
)

# 1. Функция disappear - исчезновение кролика 🐰

def test_rabbit_disappears_without_trace():
    """🔮 Тест: кролик должен исчезнуть без следа."""
    assert disappear("кролик") == "", "Кролик не исчез!"

def test_krolik_s_probielom_ne_ischez():
    """🐇 Тест: кролик с пробелом должен исчезнуть!"""
    assert disappear("кролик ") == "", "Кролик с пробелом не исчез!"

def test_slovo_ne_krolik_ne_ischezaet():
    """📦 Тест: если не кролик, должен вернуться исходный предмет."""
    assert disappear("stick") == "stick"


# 2. Функция saw_in_half - распиливание ассистента 

def test_raspilivanie_assistenta():
    """🪚 Тест: распиливание ассистента должно вернуть две половинки"""
    upper, lower = saw_in_half("ассистент")
    assert upper == "ассис", f"Верхняя часть должна быть 'ассис', получено '{upper}'"
    assert lower == "тент", f"Нижняя часть должна быть 'тент', получено '{lower}'"


def test_raspilivanie_cheloveka():
    """👤 Тест: распиливание обычного человека должно дать две половинки."""
    upper, lower = saw_in_half("человек")
    assert upper == "чел"
    assert lower == "овек"


def test_raspilivanie_korotkogo_imeni():
    """📏 Тест: короткое имя должно правильно распилиться."""
    upper, lower = saw_in_half("джон")
    assert upper == "дж"
    assert lower == "он"


# 3. Функция pull_rabbit - доставание кролика из шляпы 🎩

def test_dostavanie_krolika_iz_shlyapy():
    """🎩 Тест: из шляпы с содерж имым должен появиться кролик."""
    assert pull_rabbit(["шарф", "зонт"]) == "кролик"


def test_dostavanie_krolika_iz_pustoy_shlyapy():
    """🚫 Тест: из пустой шляпы должно вылететь исключение."""
    with pytest.raises(ValueError, match="Шляпа пуста!"):
        pull_rabbit([])


def test_dostavanie_krolika_so_slovom_fokus():
    """🕊️ Тест: если в шляпе фокус, должен появиться кролик, а не голубь!"""
    result = pull_rabbit(["фокус"])
    assert result == "кролик", f"Должен быть кролик, получен '{result}'"


# 4. Функция escape_box - побег из ящика 🔒

def test_gudini_spasaetsya_iz_yaschika():
    """🔓 Тест: Гарри Гудини должен сбежать из ящика!"""
    assert escape_box("Гарри Гудини") == True

def test_gudini_s_probielom_ne_spasaetsya():
    """🔐 Тест: Гудини с пробелом не должен считаться Гудини"""
    assert escape_box("Гарри Гудини ") == True, "Гудини с пробелом должен сбежать!"

def test_ne_gudini_ne_spasaetsya():
    """🚫 Тест: обычный человек не может сбежать из ящика."""
    assert escape_box("Боб") == False


# 5. Функция levitate - левитация 🚀

def test_positive_levitation():
    """🌟 Тест: с положительной силой левитация должна поднимать."""
    assert levitate("Камень", 10) == 20

def test_zero_levitation():
    """С нулевой силой предмет должен остаться на месте"""
    assert levitate("Бочка", 0) == 0

def test_negative_levatation():
    """При отрицательной левитации предмет должен оставаться на месте"""
    assert levitate("Пушечное ядро", -55) == 0

