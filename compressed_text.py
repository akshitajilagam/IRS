# Method : Run-Length Encoding

def compress(text):
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compressed += text[i-1] + str(count)
            count = 1

    compressed += text[-1] + str(count)
    return compressed

# Create the input.txt file with sample content
with open("input.txt", "w") as f:
    f.write("AAGGTTT66") # Sample content

with open("input.txt", "r") as f:
    data = f.read()

compressed_data = compress(data)

with open("compressed.txt", "w") as f:
    f.write(compressed_data)

print("Original:", data)
print("Compressed:", compressed_data)
