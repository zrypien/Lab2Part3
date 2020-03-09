import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount' : 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalucateTotalImpurePrice(invoice, products):
        invoice.totalImpurePrice(products)
        assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalDiscount(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 5.62

def test_CanCalucateTotalPurePrice(invoice, products):
        invoice.totalImpurePrice(products)
        assert invoice.totalImpurePrice(products) == 69.38