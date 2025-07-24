def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
        return content
    return ""
