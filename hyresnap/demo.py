import requests


def func():
    url="https://countriesnow.space/api/v0.1/countries/population/cities"
    response = requests.get(url=url)
    # print(response.json())

    response_json = response.json()
    # print(response_json['data'])
    city_data = response_json['data']
    cities = []
    print(type(city_data))

    for data in city_data:
        city = data['city']
        # print(city)
        total_population = 0
        total_year = 0
        for population_data in data['populationCounts']:
            year = population_data['year']
            value = float(population_data['value'])
            # print(year)
            # print(value)
            if value>0:
                total_year += 1
                total_population += value
        if total_year > 0:
            average_population = total_population//total_year
            if average_population > 12000:
                cities.append(city)

    for city in cities:
        print(city)






func()