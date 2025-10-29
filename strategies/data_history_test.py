from openalgo import api

# Initialize the API client
client = api(api_key='9c56d52753241db0345c2a8c576c0eea4d556523131b63c384b20f741c45f7f0', host='http://127.0.0.1:5000')

# Fetch historical data for BHEL
df = client.history(
    symbol="BHEL",
    exchange="NSE",
    interval="5m",
    start_date="2024-11-01",
    end_date="2024-12-31"
)

# Display the fetched data
print(df)

# print(type(df))
# print(df.shape)
# print(df.index)

# print(df.head())
# print(df.columns)
