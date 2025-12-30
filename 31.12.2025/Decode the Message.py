class Solution(object):
    def decodeMessage(self, key, message):
        char_map = {" ": " "}
        current_ascii = ord('a') 

        for char in key:
            if char != " " and char not in char_map:
                char_map[char] = chr(current_ascii)
                current_ascii += 1

        decoded_message = ""
        for char in message:
            decoded_message += char_map[char]

        return decoded_message

        
