
def triangle_area(base, height):
    return 1/2 * base * height


def read_file(filepath):
    items =[]
    with open(filepath, r) as f:
        for line in f:
            base, height = line.split(',')
            height = height.replace('\n', '')
            if base.isnumeric() and height.isnumeric():
                items.append({
                    'base' : base,
                    'height': height
                })
    return items

if __name__ == '__main__':
    print(read_file())