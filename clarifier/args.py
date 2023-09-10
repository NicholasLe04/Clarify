import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file_path", "-f",
        help="file path for the file to clarify",
        default="./"
    )
    return parser.parse_args()