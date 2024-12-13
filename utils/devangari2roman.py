from unicodedata import normalize

dev_roman_vowel = {
    "अ": "a",
    "आ": "ā",
    "इ": "i",
    "ई": "ī",
    "उ": "u",
    "ऊ": "ū",
    "ऋ": "r̥",
    "ॠ": "r̥̄",
    "ऌ": "l̥",
    "ॡ": "l̥̄",
    "ए": "e",
    "ऐ": "ai",
    "ओ": "o",
    "औ": "au",
}
dev_roman_vowel_join = {
    "ा": "ā",
    "ि": "i",
    "ी": "ī",
    "ु": "u",
    "ू": "ū",
    "ृ": "r̥",
    "ॄ": "r̥̄",
    "ॢ": "l̥",
    "ॣ": "l̥̄",
    "े": "e",
    "ै": "ai",
    "ो": "o",
    "ौ": "au",
}
dev_roman_consotant = {
    "क": "k",
    "ख": "kh",
    "ग": "g",
    "घ": "gh",
    "ङ": "ṅ",
    "च": "c",
    "छ": "ch",
    "ज": "j",
    "झ": "jh",
    "ञ": "ñ",
    "ट": "ṭ",
    "ठ": "ṭh",
    "ड": "ḍ",
    "ढ": "ḍh",
    "ण": "ṇ",
    "त": "t",
    "थ": "th",
    "द": "d",
    "ध": "dh",
    "न": "n",
    "प": "p",
    "फ": "ph",
    "ब": "b",
    "भ": "bh",
    "म": "m",
    "य": "y",
    "र": "r",
    "ल": "l",
    "व": "v",
    "श": "ś",
    "ष": "ṣ",
    "स": "s",
    "ह": "h",
    "ळ": "ḷ",
}
dev_roman_visarga_anunasika = {"ः": "ḥ", "़": "ṃ", "ं": "ṁ", "ँ": "m̐"}
dev_roman_sign = {"ऽ": "'", "।": "/", "॥": "//"}
dev_roman_virama = {"्": ""}
dev_roman_number = {
    "०": "0",
    "१": "1",
    "२": "2",
    "३": "3",
    "४": "4",
    "५": "5",
    "६": "6",
    "७": "7",
    "८": "8",
    "९": "9",
}

devanagari_to_iso = {
    **dev_roman_vowel,
    **dev_roman_vowel_join,
    **dev_roman_consotant,
    **dev_roman_visarga_anunasika,
    **dev_roman_sign,
    **dev_roman_virama,
    **dev_roman_number,
}


def devanagari_to_iso15919(text: str) -> str:
    """
    convert devanagari to roman (iso15919)
    text: str, devanagari text
    return: str, iso15919 text
    """

    result = ""

    for idx, char_dev in enumerate(text):
        if char_dev in devanagari_to_iso:
            # replace devanagari to roman
            roman = devanagari_to_iso[char_dev]

            # check whether to be added "a"
            if idx < len(text) - 1:
                # if the next character is consonant, add "a" to the end of the roman
                if char_dev in dev_roman_consotant and (
                    text[idx + 1] in dev_roman_consotant
                    or text[idx + 1] in dev_roman_visarga_anunasika
                    or text[idx + 1] == " "
                ):
                    roman += "a"
            result += roman
        else:
            result += char_dev

    return result


def test():
    # テスト
    devanagari_text = "अभ्यासातिशयस्तथा न विहितस्तादृक् श्रुतं नार्जितं"
    iso_text = "abhyāsātiśayastathā na vihitastādr̥k śrutaṁ nārjitaṁ"

    print("Devanagari to ISO 15919:", devanagari_to_iso15919(devanagari_text))
    print("Expected:", iso_text)


def normalize_dict(dictionary):
    return {k: normalize("NFKC", v) for k, v in dictionary.items()}


if __name__ == "__main__":
    test()

    # normalize dict
    dev_roman_vowel = normalize_dict(dev_roman_vowel)
    dev_roman_vowel_join = normalize_dict(dev_roman_vowel_join)
    dev_roman_consotant = normalize_dict(dev_roman_consotant)
    dev_roman_visarga_anunasika = normalize_dict(dev_roman_visarga_anunasika)
    dev_roman_sign = normalize_dict(dev_roman_sign)
    dev_roman_virama = normalize_dict(dev_roman_virama)
    dev_roman_number = normalize_dict(dev_roman_number)

    print(f"{dev_roman_vowel=}")
    print(f"{dev_roman_vowel_join=}")
    print(f"{dev_roman_consotant=}")
    print(f"{dev_roman_visarga_anunasika=}")
    print(f"{dev_roman_sign=}")
    print(f"{dev_roman_virama=}")
    print(f"{dev_roman_number=}")
