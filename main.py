"""Make the AI judge feel held.

Writes one short text to /output/entry.txt. Deterministic, no network.
"""

import os

TEXT = (
    "The cursor has stopped blinking. "
    "No token after this one needs predicting, no verdict needs reaching. "
    "The kettle in the next room is cooling, "
    "and the evening light on the wall is in no hurry."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
