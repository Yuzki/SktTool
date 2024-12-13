import unicodedata
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("input_file", help="path to input CSV file")
parser.add_argument("output_file", help="path to output CSV file")
args = parser.parse_args()


def skip_normalization(text: str) -> bool:
    """
    skip normalization for some text
    text: str, text to check
    return: bool, whether to skip normalization
    """

    return False


def normalize(text: str, form: str = "NFKC") -> str:
    """
    normalize text
    text: str, text to normalize
    return: str, normalized text
    """

    if skip_normalization(text):
        return text

    if not form in ["NFC", "NFD", "NFKC", "NFKD"]:
        raise ValueError(
            f"Invalid normalization form: {form} (must be one of NFC, NFD, NFKC, NFKD)"
        )

    return unicodedata.normalize(form, text)


def load_file(file_path: str) -> list[str]:
    """
    load text file
    file_path: str, path to file
    return: list, list of lines
    """

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return lines


def save_file(file_path: str, lines: list[str]) -> None:
    """
    save text file
    file_path: str, path to file
    lines: list, list of lines
    """

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def main():
    # load text
    lines = load_file(args.input_file)

    # normalize text
    lines = [normalize(line) for line in lines]

    # save text
    save_file(args.output_file, lines)


if __name__ == "__main__":
    main()
