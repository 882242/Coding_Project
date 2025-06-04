import random


def byte_to_bits(byte):
    return f"{byte:08b}"


def flip_bit(byte, bit_pos):
    # Flip the bit at bit_pos (0 is the leftmost bit)
    mask = 1 << (7 - bit_pos)
    return byte ^ mask


def demo_bit_flip(char):
    original_byte = ord(char)
    print(f"Original char: '{char}' (byte: {original_byte})")
    print(f"Original bits: {byte_to_bits(original_byte)}")

    bit_pos = random.randint(0, 7)
    corrupted_byte = flip_bit(original_byte, bit_pos)

    corrupted_char = chr(corrupted_byte)
    print(f"\nFlipping bit at position {bit_pos} (0 is leftmost)...")
    print(f"Corrupted bits: {byte_to_bits(corrupted_byte)}")
    print(f"Corrupted char: '{corrupted_char}' (byte: {corrupted_byte})")


# Try with letter 'd'
demo_bit_flip('d')
