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
results = search.get_dict()
print(results)
