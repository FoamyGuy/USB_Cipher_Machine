class FizzBuzzCipher:
    def __init__(self, keyfile):
        self.keyfile = keyfile
        with open(keyfile, "r") as f:
            self.original_keys = f.read().splitlines()

        self.current_keys = self.original_keys.copy()

    def reset_keys(self):
        self.current_keys = self.original_keys.copy()

    @staticmethod
    def fizz_shift(target_str):
        first_half = []
        second_half = []

        for i, val in enumerate(target_str):
            if i % 2 == 0:
                second_half.append(val)
            else:
                first_half.append(val)
        return "".join(first_half + second_half)

    @staticmethod
    def buzz_shift(target_str):
        first_half = []
        second_half = []
        for i, val in enumerate(target_str):
            if i % 3 == 0:
                second_half.append(val)
            else:
                first_half.append(val)
        return "".join(first_half + second_half)

    @staticmethod
    def fizzbuzz_shift(target_str):
        first_half = []
        second_half = []
        for i, val in enumerate(target_str):
            if i % 3 == 0 and i % 2 == 0:
                second_half.append(val)
            else:
                first_half.append(val)
        return "".join(first_half + second_half)

    @staticmethod
    def none_shift(target_str):
        target_list = list(target_str)
        target_list.append(target_list.pop(0))
        return "".join(target_list)


    def encrypt(self, cleartext):
        temp_char = None
        ciphertext_list = []
        for cleartext_char in cleartext:
            try:
                temp_char = self.current_keys[1][self.current_keys[0].index(cleartext_char)]
                #print(f"temp_char: {temp_char}")
                ciphertext_char = self.current_keys[3][self.current_keys[2].index(temp_char)]
                ciphertext_list.append(ciphertext_char)
            except ValueError as e:
                #print(f"value error: {cleartext_char}")
                ciphertext_list.append(cleartext_char)

            self.do_the_shift()
        return "".join(ciphertext_list)

    def decrypt(self, ciphertext):
        temp_char = None
        cleartext_list = []
        for ciphertext_char in ciphertext:
            try:
                temp_char = self.current_keys[2][self.current_keys[3].index(ciphertext_char)]
                cleartext_char = self.current_keys[0][self.current_keys[1].index(temp_char)]
                cleartext_list.append(cleartext_char)
            except ValueError:
                cleartext_list.append(ciphertext_char)
            self.do_the_shift()

        return "".join(cleartext_list)

    def do_the_shift(self):
        self.current_keys[0] = FizzBuzzCipher.fizz_shift(self.current_keys[0])
        self.current_keys[1] = FizzBuzzCipher.buzz_shift(self.current_keys[1])
        self.current_keys[2] = FizzBuzzCipher.fizzbuzz_shift(self.current_keys[2])
        self.current_keys[3] = FizzBuzzCipher.none_shift(self.current_keys[3])
