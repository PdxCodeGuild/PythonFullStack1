# Practice: Grocery

Write a very simple HTTP API that returns the price of various items in the grocery in a few different currencies.

Have support for the following currencies:

* USD
* EUR
* CNY
* JPY

Make routes for:

*   `GET /product/PRODUCT_NAME/price` should respond with the price in dollars.
    The response should look like `PRODUCT_NAME is AMOUNT dollars`.
    Return a `404 NOT FOUND` if trying to get an unknown product.

*   `GET /product/PRODUCT_NAME/price/CURRENCY` should respond with the price in that currency.
    The response should look like `PRODUCT_NAME is AMOUNT CURRENCY`.
    Return a `404 NOT FOUND` if trying to get an unknown product, and a `400 BAD REQUEST` if trying to convert to an unknown currency.

In `models.py`, add the following data:

```py
PRODUCTS = [
    {
        'name': 'apple',
        'price_dollars': 1.0,
    },
    {
        'name': 'pear',
        'price_dollars': 1.5,
    },
    {
        'name': 'grape',
        'price_dollars': 0.75,
    },
]
```
