import requests
import argparse
from os import path


def upload_file(file_path, duration: str):
    url = "https://litterbox.catbox.moe/resources/internals/api.php"
    files = {"fileToUpload": open(file_path, "rb")}
    data = {"reqtype": "fileupload", "time": duration}
    return requests.post(url, files=files, data=data)


def make_embed_link(file_link: str):
    return f"https://embeds.video/{file_link}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required=True)

    # Validate file path exists on filesystem
    if not path.isfile(parser.parse_args().file):
        print("File does not exist")
        exit(1)

    # Send file to server
    response = upload_file(parser.parse_args().file, "1h")

    if not response:
        print("Failed to upload file")
        exit(1)

    print(make_embed_link(response.text))


if __name__ == "__main__":
    main()
