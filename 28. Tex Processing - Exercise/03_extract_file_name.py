path = input().split("\\")

file_name, file_ext = path[-1].split(".")
# idx = file_full.find(".")
# file_name = file_full[:idx]
# file_ext = file_full[idx:]

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")
