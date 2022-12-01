import argparse

import yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        default="configs/config.yml",
        help="Path to config file with emulation parameters",
    )
    args = parser.parse_args()
    with open(args.config, 'r') as stream:
        print(yaml.safe_load(stream))
