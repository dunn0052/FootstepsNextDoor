import Console.Console

import json

if __name__ == "__main__":
    config = None
    with open('config.json') as config_file:
        config_contents = config_file.read()

        try:
            config = json.loads(config_contents)
        except json.JSONDecodeError:
            print("[ERROR] Could not decode config file")

    fps = config["FPS"]
    size = config["SIZE"]
    con = Console.Console.Console(size, fps)
    con.start()