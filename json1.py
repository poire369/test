import json
import urllib

url = raw_input("Enter an url: ")
data = urllib.urlopen(url);
input = data.read()
contenu = json.loads(input)
sum=0
comments = contenu['comments']
for comment in comments:
	number = int(comment['count'])
	sum = sum+number
	
print sum