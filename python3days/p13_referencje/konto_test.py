from konto import Konto

def test_konto_init():
    konto = Konto(1313, 'Ala Kowalska')
    assert konto.numer == 1313
    assert konto.wlasciciel == 'Ala Kowalska'
    assert konto.saldo == 0


def test_konto_wplata():
    konto = Konto(1313, 'Ala', 1000)
    konto.wplata(200)
    assert konto.saldo == 1200


def test_konto_wyplata():
    konto = Konto(1313, 'Ala', 1000)
    konto.wyplata(300)
    assert konto.saldo == 700
