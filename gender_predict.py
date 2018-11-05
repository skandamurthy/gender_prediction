import requests, json

def getGenders(names):
	url = ""
	cnt = 0
	answer = []
	for name in names:
		if url == "":
			url = "name[0]=" + name
		else:
			cnt += 1
			url = url + "&name[" + str(cnt) + "]=" + name
	req = requests.get("https://api.genderize.io?" + url)
	# loading the json file 
	results = json.loads(req.text)
	for a_result in results:
		if result["gender"] is not None:
			answer.append(result["gender"])
		else:
			answer.append("None")
	return answer


#test case
# We have to feed data via list and it returns a list
gender_predict = getGenders(["Suhas"])
for a_name in gender_predict:
	print(a_name)