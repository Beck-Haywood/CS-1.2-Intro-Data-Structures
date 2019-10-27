def read_text_file(file_name):
    f = open(file_name)
    words = f.read()
    words.split()
    
    return words