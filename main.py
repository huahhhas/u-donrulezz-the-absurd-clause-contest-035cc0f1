#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes a single absurd terms-of-service clause to /output/entry.txt
and prints it. Standard library only; no third-party imports.
"""

import os

ENTRY = (
    "Clause 14.7: by clicking Accept, you grant us a perpetual, "
    "royalty-free licence to your shadow, which we may lend to third "
    "parties on overcast days without further notice."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
