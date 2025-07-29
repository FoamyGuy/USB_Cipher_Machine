import os
import secrets
import random


random.seed(secrets.randbelow(999999999))

alphabet_start_idx = ord(' ')
alphabet_end_idx = ord('~')
alphabet_len = alphabet_end_idx - alphabet_start_idx

indexes = list(range(alphabet_start_idx, alphabet_end_idx + 1))
print(len(indexes))
print(indexes)
fizz_key_list = []
buzz_key_list = []

fizzbuzz_key_list = []
none_key_list = []

for i in range(alphabet_len + 1):
    cur_char_index = random.choice(indexes)
    fizz_key_list.append(chr(cur_char_index))
    indexes.remove(cur_char_index)

indexes = list(range(alphabet_start_idx, alphabet_end_idx + 1))

for i in range(alphabet_len + 1):
    cur_char_index = random.choice(indexes)
    buzz_key_list.append(chr(cur_char_index))
    indexes.remove(cur_char_index)
print(f"len: {len(indexes)}")
indexes = list(range(alphabet_start_idx, alphabet_end_idx + 1))

for i in range(alphabet_len + 1):
    cur_char_index = random.choice(indexes)
    fizzbuzz_key_list.append(chr(cur_char_index))
    indexes.remove(cur_char_index)

indexes = list(range(alphabet_start_idx, alphabet_end_idx + 1))

for i in range(alphabet_len + 1):
    cur_char_index = random.choice(indexes)
    none_key_list.append(chr(cur_char_index))
    indexes.remove(cur_char_index)


if not os.path.exists("fizzbuzz.keys"):
    with open("fizzbuzz.keys", "w") as f:
        f.write("".join(fizz_key_list) + "\n")
        f.write("".join(buzz_key_list) + "\n")
        f.write("".join(fizzbuzz_key_list) + "\n")
        f.write("".join(none_key_list) + "\n")
else:
    print("fizzbuzz.keys already exists, not overwriting.")
    print("New keys are:")

print("".join(fizz_key_list))
print("".join(buzz_key_list))
print("".join(fizzbuzz_key_list))
print("".join(none_key_list))

