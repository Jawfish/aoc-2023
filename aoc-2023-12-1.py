import re

replacements = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def replace_number_words(text):
    for word, replacement in replacements.items():
        text = text.replace(word, replacement)
    return text


def sum_of_first_last_digits(text):
    cleaned_text = re.sub(r"[A-Za-z]", "", text).split("\n")
    return sum(int(line[0] + line[-1]) for line in cleaned_text)


def main():
    with open("input") as file:
        content = file.read()

    replaced_content = replace_number_words(content)
    result = sum_of_first_last_digits(replaced_content)

    print(result)


if __name__ == "__main__":
    main()
