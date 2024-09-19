import exantedata_api as ed


# 1. Obtaining a token
token = ed.getToken(
    username='username',
    password='password'
)


# 2. Specifying a ticker
tickerQuery = 'TR.FOREIGNFX.SHORT.NET.D'

tickerQuery = '%.FOREIGNFX.SHORT.NET.%'

tickerQuery = 'TR.FOREIGNFX.SHORT.NET.D, TR.CBRT.SWAPS.EXGOLD.%, %.HFPROXFLOW.EQ.IN.W'


# 3.1 Metadata query
metadata = ed.getMetaData(
    token=token,
    tickerQuery=tickerQuery
)


# 3.2 Data queries

# Basic usage
data = ed.getData(
    token=token,
    tickerQuery=tickerQuery
)

# startDate and endDate params usage
data = ed.getData(
    token=token,
    tickerQuery=tickerQuery,
    startDate='2023-01-01',
    endDate='2023-12-31',
)

# pediod param usage
data = ed.getData(
    token=token,
    tickerQuery='TR.FOREIGNFX.SHORT.NET.M',
    startDate='2023-01-01',
    endDate='2023-12-31',
    period='begin'
)

# freq param usage
data = ed.getData(
    token=token,
    tickerQuery='TR.FOREIGNFX.SHORT.NET.D',
    startDate='2023-01-01',
    endDate='2023-12-31',
    freq='W'
)

# agg_method param usage
data = ed.getData(
    token=token,
    tickerQuery='TR.FOREIGNFX.SHORT.NET.D',
    startDate='2023-01-01',
    endDate='2023-12-31',
    freq='W',
    agg_method='sum',
)

# fill_method param usage
data = ed.getData(
    token=token,
    tickerQuery='TR.FOREIGNFX.SHORT.NET.M, TR.HFPROXFLOW.EQ.IN.W',
    startDate='2023-01-01',
    endDate='2023-12-31',
    fill_method='ffill',
)

# fill_value param usage
data = ed.getData(
    token=token,
    tickerQuery='TR.FOREIGNFX.SHORT.NET.M, TR.HFPROXFLOW.EQ.IN.W',
    fill_value=0,
)


# 4. Specifying proxies

# Obtaining a token with proxies
token = ed.getToken(
    username='username',
    password='password',
    proxies={
        'http': 'http://<IPADDR>:<PORT>',
        'https': 'https://<IPADDR>:<PORT>'
    }
)

# Metadata query with proxies
metadata = ed.getData(
    token=token,
    tickerQuery=tickerQuery,
    proxies={
        'http': 'http://<IPADDR>:<PORT>',
        'https': 'https://<IPADDR>:<PORT>'
    }
)

# Data query with proxies
data = ed.getData(
    token=token,
    tickerQuery=tickerQuery,
    proxies={
        'http': 'http://<IPADDR>:<PORT>',
        'https': 'https://<IPADDR>:<PORT>'
    }
)
