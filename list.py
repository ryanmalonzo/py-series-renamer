import json

if __name__ == "__main__":
    with open("series.json") as series_json:
        series = json.load(series_json)
        for entry in series:
            print(
                f'{entry["name"]} - Season {entry["season"]} Episode {entry["episode"]}'
            )
