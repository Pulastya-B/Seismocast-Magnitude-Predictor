# This is the code for the Extraction of Dataset from the USGS Earthquake Catalog

pip install quaker-db

import pandas as pd
import requests
from io import StringIO
import time

def fetch_usgs_data(start, end, min_mag=4.5):
    url = (
        f"https://earthquake.usgs.gov/fdsnws/event/1/query?"
        f"format=csv&starttime={start}&endtime={end}"
        f"&minmagnitude={min_mag}&orderby=time"
    )
    print(f"Fetching from {start} to {end}...")
    response = requests.get(url)
    if response.status_code == 200:
        df = pd.read_csv(StringIO(response.text))
        print(f"✅ {len(df)} records fetched.")
        return df
    else:
        print(f"❌ Failed: {response.status_code}")
        return pd.DataFrame()

# Break into 4-year safe chunks
chunks = [
    ("2000-01-01", "2003-12-31"),  # Already fetched
    ("2004-01-01", "2005-12-31"),
    ("2006-01-01", "2007-12-31"),
    ("2008-01-01", "2009-12-31"),
    ("2010-01-01", "2011-12-31"),
    ("2012-01-01", "2013-12-31"),
    ("2014-01-01", "2015-12-31"),
    ("2016-01-01", "2017-12-31"),
    ("2018-01-01", "2019-12-31"),
    ("2020-01-01", "2020-12-31"),
    ("2021-01-01", "2021-12-31"),
    ("2022-01-01", "2022-12-31"),
    ("2023-01-01", "2024-06-27"),
    ("2024-07-01", "2024-12-31"),
    ("2025-01-01", "2025-6-25"),
]

all_data = []
for start, end in chunks:
    df = fetch_usgs_data(start, end)
    if not df.empty:
        all_data.append(df)
    time.sleep(1)

final_df = pd.concat(all_data, ignore_index=True)
final_df.to_csv("usgs_earthquake_data_2000_2025.csv", index=False)
print("✅ All done! Saved as usgs_earthquake_data_2000_2025.csv")

