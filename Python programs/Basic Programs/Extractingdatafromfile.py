
def triangle_area(base, height):
    return 1/2 * base * height


def read_file(file_path):
    items = []
    with open(file_path, 'r') as f:
        for line in f:
            base, height = line.split(',')
            height = height.replace('\n', '')
            if base.isnumeric() and height.isnumeric():
                items.append({
                    'base' : float(base),
                    'height' : float(height)

                })
    return items

def find_area(file_path):
    items = read_file(file_path)
    for item in items:
        area = triangle_area(item['base'], item['height'])
        print(f"The area of triange with base {item['base']} and height {item['height']} is {area}")


if __name__ =='__main__':
    print(read_file("D:\Python programs\databaseheight.txt"))
    find_area("D:\Python programs\databaseheight.txt")

