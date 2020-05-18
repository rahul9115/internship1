import urllib.request
import json
url = "https://www.analyticsinsight.net/coronavirus-affecting-startups-fundraising-activity/"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)
