import argparse
import json
import os
import tempfile


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--value', help='Value')
    return parser.parse_args()


def read(storage_pat):
    if not os.path.exists(storage_pat):
        return {}

    with open(storage_pat, 'r') as file:
        read_data = file.read()
        if read_data:
            return json.loads(read_data)
    return {}


def write(storage_pat, data):
    with open(storage_pat, 'w') as f:
        f.write(json.dumps(data))
        print("The data has been delivered")


def put_data(storage_pat, key, value):
    data = read(storage_pat)
    data[key] = data.get(key, list())
    data[key].append(value)
    write(storage_pat, data)


def get(storage_pat, key):
    return read(storage_pat).get(key, [])


def main(storage_pat):
    args = parse()

    if args.value and args.key:
        put_data(storage_pat, args.key, args.value)
    elif args.key:
        print(*get(storage_pat, args.key), sep=", ")
    else:
        print("We have nothing to do, bcs you haven't entered data properly. Please, try again")


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    print(storage_path)
    main(storage_path)
