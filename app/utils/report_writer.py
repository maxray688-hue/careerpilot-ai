import os


def save_report(filename, content):

    os.makedirs("outputs", exist_ok=True)

    filepath = os.path.join("outputs", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return filepath