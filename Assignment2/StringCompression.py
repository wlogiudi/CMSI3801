def compress_string(s):
    if not s:
        return s
    
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    
    compressed.append(s[-1] + str(count))

    compressed_str = ''.join(compressed)
    
    return compressed_str if len(compressed_str) < len(s) else s

# Example usage:
input_str = "aaabcccccaaa"
compressed_result = compress_string(input_str)
print(compressed_result)
