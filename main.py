import time
from typing import Optional

# Define the texture atlas grid (8x8)
textureAtlas = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
    ['q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
    ['y', 'z', '0', '1', '2', '3', '4', '5'],
    ['6', '7', '8', '9', '!', '@', '#', '$'],
    ['%', '^', '&', '*', '(', ')', '-', '_'],
    ['+', '=', '[', ']', '{', '}', ';', ':'],
    ['\'', '"', ',', '.', '/', '?', ' ', ' ']
]


# Function to calculate UV coordinates for a given character
def char_to_uv(character) -> Optional[tuple[float, float, float, float]]:
    # Find the character in the texture atlas
    for row_index, row in enumerate(textureAtlas):
        if character in row:
            col_index = row.index(character)

            # Calculate the UV coordinates based on the 8x8 grid
            u_min = col_index / 8.0
            v_min = row_index / 8.0
            u_max = u_min + 1 / 8.0
            v_max = v_min + 1 / 8.0

            return (u_min, v_min, u_max, v_max)

    return None

s = ["H", "e", "l", "l", "o", ",", " ", "W", "o", "r", "l", "d", "!"][::-1] * 60

character_buffer = [["_" for _ in range(60)] for _ in range(40)]

# Example usage
def main():
    for y in range(40):
        if len(s) == 0:
            break
        for x in range(60):
            if len(s) == 0:
                break
            character_buffer[y][x] = s.pop()

    cursor_position = (0, 0)

    t0 = time.perf_counter()
    for row in character_buffer:
        for char in row:
            print(char, end = "")
        print()
    t1 = time.perf_counter()
    print(f"Printing took {(t1-t0):.4f}ms.")


if __name__ == "__main__":
    main()

"""
Hello, World!Hello, World!Hello, World!Hello, World!Hello, W
orld!Hello, World!Hello, World!Hello, World!Hello, World!Hel
lo, World!Hello, World!Hello, World!Hello, World!Hello, Worl
d!Hello, World!Hello, World!Hello, World!Hello, World!Hello,
 World!Hello, World!Hello, World!Hello, World!Hello, World!H
ello, World!Hello, World!Hello, World!Hello, World!Hello, Wo
rld!Hello, World!Hello, World!Hello, World!Hello, World!Hell
o, World!Hello, World!Hello, World!Hello, World!Hello, World
!Hello, World!Hello, World!Hello, World!Hello, World!Hello, 
World!Hello, World!Hello, World!Hello, World!Hello, World!He
llo, World!Hello, World!Hello, World!Hello, World!Hello, Wor
ld!Hello, World!Hello, World!Hello, World!Hello, World!Hello
, World!Hello, World!Hello, World!Hello, World!Hello, World!
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
____________________________________________________________
"""