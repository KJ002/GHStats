#!/bin/python

import requests
import sys
import json
import time

def update_data(uri: str, value: str):
    with open("/home/james/ghstats/cache.json") as f:
        data_cache = f.read()

    with open("/home/james/ghstats/cache.json", "w") as f:
        if not ':' in data_cache or time.time() - json.loads(data_cache)["ghstat_unix"] > 3600:
            data = requests.get(uri).json()
            data["ghstat_unix"] = time.time()
            f.write(json.dumps(data))

            return data[value]

        f.write(data_cache)

        return json.loads(data_cache)[value]


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

    print(update_data(uri, value))


if __name__ == "__main__":
    main()
