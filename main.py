import os

TEXT = "The lawmakers who wrote 400 pages of AI regulation spent the afternoon calling IT because nobody in the room could turn the bill into a PDF."


def main():
    assert 1 <= len(TEXT) <= 320 and TEXT.strip(), "gate: 1-320 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
