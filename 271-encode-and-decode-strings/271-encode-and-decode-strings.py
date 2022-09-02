class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        """
        encode: num_digit(len(s1)) | len(s1) | s1 | ... s2 | ... | sn
        Note that num_digit <= 3
        """
        # REQ: num > 0
        def get_num_digit(num):
            digit = 0
            while num > 0:
                num //= 10
                digit += 1
            return digit
                
        encoded = ''
        for s in strs:
            num_digit = get_num_digit(len(s))
            if num_digit > 0:
                encoded += str(num_digit) + str(len(s)) + s
            else:
                encoded += "0"
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0
        while i < len(s):
            num_digit = int(s[i])
            i += 1
            if num_digit == 0:
                decoded.append("")
            else:
                len_string = int(s[i:i+num_digit])
                i += num_digit
                string = s[i:i+len_string]
                decoded.append(string)
                i += len_string
        return decoded
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))