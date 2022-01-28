#!/bin/python

import requests
import sys
import json
import time

def read_cache() -> str:
    with open("/home/james/ghstats/cache.json") as f:
        return f.read()

def get_data(uri: str, value: str) -> str:
    with open("/home/james/ghstats/cache.json", "w") as f:
        if read_cache() == "" or time.time() - json.loads(read_cache())["ghstat_unix"] > 3600:
            data = requests.get(uri).json()
            data["ghstat_unix"] = time.time()
            f.write(json.dumps(data))

    return json.loads(read_cache())[value]


def main() -> None:
    if len(sys.argv) < 3:
        print(f"Not enough arguments! Arguments provided: {sys.argv}")
        return

    user = sys.argv[1]
    value = sys.argv[2].lower()

    if not value in [
        "login",
        "id",
        "node_id",
        "type",
        "site_admin",
        "name",
        "company",
        "blog",
        "location",
        "email",
        "hireable",
        "bio",
        "twitter_username",
        "public_repos",
        "public_gists",
        "followers",
        "following",
        "created_at",
        "updated_at",
    ]:
        print(f"{value} is not a valid value!")
        return

    uri = f"https://api.github.com/users/{user}"

    print(get_data(uri, value))


if __name__ == "__main__":
    main()
