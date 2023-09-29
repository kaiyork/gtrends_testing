from serpapi import GoogleSearch
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json

params = {
  "api_key": "replace this with your api key to make it work",
  "engine": "google_trends",
  "q": "python",
  "date": "today 1-m"
}

search = GoogleSearch(params)
##SERPAPI results are stored in a dictionary
results = search.get_dict()
##check intial dictionary
df = pd.DataFrame.from_dict(results)
df.to_csv('trends.csv',index=False)
##homing in on dictionary of interest
test = results['interest_over_time']
df2 =pd.DataFrame.from_dict(test)
df2.to_csv('trends2.csv',index=False)
