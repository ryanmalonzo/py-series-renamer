import json
from pathlib import Path
from typing import List

import click


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
@click.option(
    "-n", "--name", type=str, required=True, help="The name of the series."
)
@click.option(
    "-s", "--season", type=int, required=True, help="The season number."
)
@click.option(
    "-e", "--episode", type=int, required=True, help="The episode number."
)
@click.argument("file_path", type=click.Path(exists=True))
def rename(name, season, episode, file_path) -> None:
    file = Path(file_path)
    new_file_path = file.with_stem(f"{name} - S{season:02d}E{episode:02d}")

    # Rename file
    file.rename(new_file_path)

    # Save entry in json history
    save_json(name, season, episode)

    click.echo(f"Renamed series: {new_file_path}")


if __name__ == "__main__":
    rename()
