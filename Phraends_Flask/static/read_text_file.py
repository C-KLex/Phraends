def read_text_file(file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()
    return sentences