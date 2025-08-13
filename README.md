# Fred
A requests package for FRED, a data product of the Federal Reserve Bank of St. Louis.

Create an untracked file called `__auth__` and assign your FRED API key to `api_key`.

`helpers.endpoints` exhibits 30 distinct endpoints while the tuple of values assigned to each key in there is the list of accepted query parameters for that endpoint.

`app.endpoint` and `app.payload` demonstrate a sample usage via `response.content`.

https://fred.stlouisfed.org/docs/api/fred/

https://fred.stlouisfed.org/docs/api/api_key.html
