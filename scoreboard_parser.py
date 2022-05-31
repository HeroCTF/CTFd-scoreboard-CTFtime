#!/usr/bin/env python3
"""
CTFd scoreboard parser for CTFtime JSON format.
"""
from sys import argv, exit as sys_exit
from json import dumps
import csv


PLACE_INDEX, TEAM_INDEX, SCORE_INDEX = 0, 1, 3

def scoreboard_parser(csv_path):
    """
    CSV parser for CTFd scoreboard.
    """
    scoreboard = {
        "standings": []
    }

    with open(csv_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        place = 1
        for row in reader:
            if row[PLACE_INDEX] == str(place):
                scoreboard["standings"].append({
                    "pos": place,
                    "team": row[TEAM_INDEX],
                    "score": int(row[SCORE_INDEX])
                })
                place += 1

    return scoreboard


if __name__ == '__main__':
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <path_to_csv_file>")
        sys_exit(1)

    ctftime_score = scoreboard_parser(argv[1])
    print(dumps(ctftime_score))
