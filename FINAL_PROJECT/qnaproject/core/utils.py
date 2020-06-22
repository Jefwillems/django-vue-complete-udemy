import uuid


def slugify_str(base='', extra_chars_len=6):
    uid = f'{uuid.uuid4()}'
    return f'{base}-{uid[:extra_chars_len]}'
