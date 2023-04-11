import , json
url = "https://api.rasp.yandex.net/v3.0/search/?apikey=22d0948b-0e64-41dd-953e-23a94e5e7bd0&format=json&from=c163&to=c22177&lang=ru_RU&page=1&date=2022-05-01&transport_types=train"
res = .get(url)

with open('data.json', 'w') as outfile:
    json.dump(res.json(), outfile)

with open('data.json', 'r') as input_1:
    data = json.load(input_1)
    print(data)
#json_file.write(json.dumps(res.text))
#print(res.text)