from currency import Currency
class CurrencyConverter:
    exchange_rates = {
        Currency.DOLLAR : 1.0,
        Currency.RUPEES : 82.0,
        Currency.EUROS : 0.8,
        Currency.POUNDS : 0.6
    }
    @staticmethod
    def convert_currency(amount, from_currency, to_currency):
        from_rate = CurrencyConverter.exchange_rates[from_currency]
        to_rate = CurrencyConverter.exchange_rates[to_currency]

        return amount*from_rate/to_rate

