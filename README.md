# ExanteData API python library

This is python library that can be used to easily access ExanteData API.

### 0. Installation

You can install the library with using pip
```
pip install exantedata-api
```

### 1. Obtaining a token

The token can be obtained with using the `getToken` function (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L4)**).

###### Parameters
- `username`: *Obligatory. String value.* Your ExanteData username.
- `password`: *Obligatory. String value.*  Your ExanteData password.
- `proxies`: *Optional. Dictionary value.* Only if your IT department specifies.


### 2. Specifying a ticker

There are 3 ways to specify a ticker query (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L11)**):

- You may specify particular tickers explicitly \
`tickerQuery = 'TR.FOREIGNFX.SHORT.NET.D'`
- Or use a wildcard to bring all possible tickers with a similar structure \
`tickerQuery = '%.FOREIGNFX.SHORT.NET.%'`
    - use the wildcard by replacing the country code/currency in a ticker, i.e. `%.FOREIGNFX.SHORT.NET.D` will return all countries/currencies/regions for which that ticker is available
    - use the wildcard by replacing the frequency of the ticker at the end i.e. `TR.FOREIGNFX.SHORT.NET.%` will bring all available frequencies for the ticker
- also, you may query multiple specific tickers (a list of ticker splitted by comma) \
`tickerQuery = 'TR.FOREIGNFX.SHORT.NET.D, TR.CBRT.SWAPS.EXGOLD.%, %.HFPROXFLOW.EQ.IN.W'`


### 3. Querying for data

The data can be fetched with using `getMetaData` and `getData` functions that return query results in Pandas Dataframes.

#### 3.1 getMetaData

The `getMetaData` function can be used to get metadata for requested ticker(s) (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L19)**).

###### Parameters

- `token`: *Obligatory. String value.* Authorization token.
- `tickerQuery`: *Obligatory. String value.* Ticker specification.
- `proxies`: *Optional. Dictionary value.* Only if your IT department specifies.

#### 3.2 getData

The `getData` function can be used to get available timeseries for requested ticker(s) (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L26)**).

###### Parameters

- `token`: *Obligatory. String value.* Authorization token.
- `tickerQuery`: *Obligatory. String value.* Ticker specification.
- `startDate`: *Optional. String value in YYYY-MM-DD format.* Starting date for the requested data (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L34)**)
- `endDate`: *Optional. String value in YYYY-MM-DD format.* Ending date for the requested data (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L34)**)
- `period`: *Optional. String value.* Period date format. Start of period depends on the frequency of the data and can be: start of week, start of month, start of quarter or start of year. If omitted, the API will default to end of period by calendar dates (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L42)**)
    - **end** - End of period.
    - **begin** - Beginning of period.
- `freq`: *Optional. String value.*
Set a frequency for the data to be aggrgeated to. Note, API will only adjust data to a lower frequency than it is (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L51)**)
	- **D** - Daily
	- **W** - Weekly (end of week, Friday)
	- **WS** - Weekly (start of week, Monday)
	- **W-*** - Weekly (set the end day of the week, ex: W-TUE ends the weekly aggregation on Tuesday and returns dates of the Tuesdays)
	- **WS-*** - Weekly (set the start day of the week, ex: W-TUE starts the weekly aggregation on Tuesday and returns dates of the Tuesdays)
	- **M** - Monthly (end of month)
	- **MS** - Monthly (start of month)
	- **Q** - Quarterly (end of Quarter)
	- **QS** - Quarterly (start of Quarter)
	- **A** - Annually (end of year)
	- **AS** - Annually (start of year)
- `agg_method`: *Optional. String value.* Method of data aggregation (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L60)**)
	- **last** - Returns the last known value within the aggregated group.
	- **first** - Returns the first known value from the aggregated group.
	- **mean** - Returns the mean of the values within the aggregated group.
	- **median** - Returns the median of the values within the aggregated group.
	- **sum** - Returns a sum of the values within the aggregated group.
- `fill_method`: *Optional. String value.* (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L70)**)
	- **bfill** - Fills missing values with the next known value.
	- **ffill** - Fills missing values with the last known value.
	- **interpolate** - Fills missing values as interpolated between the surrounding known datapoints.
	- **nearest** - Fills missing values with the nearest known value or last known value if equidistant.
	- **nnearest** - Fills missing values with the nearest known value or next known value if equidistant.
- `fill_value`: *Optional. String, int, or double value.* 
If `fill_method` is not specified, this value will be used to fill in NaN values. If this value is also omitted, the API will not fill NaN values (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L79)**)
- `proxies`: *Optional. Dictionary value.* Only if your IT department specifies.

### 4. Specifying proxies

If needed, proxies can be specified for all functions mentioned above (**[code example](https://github.com/exantedata/exantedata_api_test/blob/master/usage_example.py#L87)**).

### * Library source code

If you want to, you may take a look at the library source code **[here](https://github.com/exantedata/exantedata_api_test/blob/master/lib/exantedata_api/exantedata_api.py)**

### * API documentation

Documentation for the API can be found **[here](https://apidocs.exantedata.com/)**

### * Contact Support

If you experience any issues while using the library, feel free to reach out to us at **tech@exantedata.com**
