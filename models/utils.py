def array_from_file(cls, path, limit=-1):
    results = []
    with open(path, encoding='utf-8') as f:
        # table header
        f.readline()
        i = 0
        line = f.readline()
        while line is not None and len(line.strip('\n')) > 0:
            results.append(cls(line.replace('\n', '')))

            i += 1
            line = f.readline()
            if i == limit:
                line = None
    return results
