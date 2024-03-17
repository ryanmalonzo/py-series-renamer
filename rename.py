#!/usr/bin/env python

import json
from pathlib import Path
from typing import List

import click


def get_json() -> None:
    with open("series.json", "r") as file:
        series: List = json.load(file)
        return series


def save_json(name, season, episode) -> None:
    with open("series.json", "r") as file:
        data: List = json.load(file)

    found: bool = False
    for entry in data:
        if entry["name"] == name:
            found = True
            entry["season"] = season
            entry["episode"] = episode
            break

    if not found:
        data.append({"name": name, "season": season, "episode": episode})

    with open("series.json", "w") as file:
        json.dump(data, file, indent=4)


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
def rename(file_path) -> None:
    series_list: List = get_json()

    # Print series' index and name
    for index, entry in enumerate(series_list):
        print(f'{index}. {entry["name"]}')

    series_number: int = click.prompt("Series number", type=int)
    series = series_list[series_number]

    name: str = series["name"]
    season = click.prompt("Season number", type=int, default=series["season"])
    episode = click.prompt(
        "Episode number", type=int, default=series["episode"] + 1
    )

    file = Path(file_path)
    new_file_path = file.with_stem(f"{name} - S{season:02d}E{episode:02d}")

    # Rename file
    file.rename(new_file_path)

    # Save entry in json history
    save_json(name, season, episode)

    click.echo(f"Renamed series: {new_file_path}")


if __name__ == "__main__":
    rename()
