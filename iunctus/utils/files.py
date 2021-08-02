import os


def match(string, patterns=[], any_pattern=False):
    matches = (pattern.match(string) for pattern in patterns)
    if any_pattern:
        return any(matches)
    else:
        return all(matches)


def find(path, recursive=False):
    if recursive:
        for root, _, files in os.walk(path):
            for file in files:
                yield os.path.join(root, file)
    else:
        for file in os.listdir(path):
            yield os.path.join(path, file) if path != "." else file


def filter_file(file, patterns=[], any_pattern=False):
    return os.path.isfile(file) and match(
        os.path.basename(file), patterns=patterns, any_pattern=any_pattern
    )
