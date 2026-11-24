"""One Line of Earned Pride — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a quiet, earned moment of pride for someone in a scene, 1 to 240 characters.
"""
import os

LINE = "After three years of night shifts, she finally saw her name on the door — and for once, she didn't hurry past it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
