import utils


def get_file() -> list:
    return utils.read_input_file(int)


def count_increases(data: list) -> int:
    count = 0
    for i in range(1, len(data)):
        count += data[i - 1] < data[i]
    return count


def count_increases_2(data: list) -> int:
    count = 0
    for i in range(len(data) - 3):
        wndwA = sum(data[i: i+3])
        wndwB = sum(data[i+1: i+4])
        count += wndwA < wndwB
    return count


def main():
    data = get_file()
    count = count_increases_2(data)
    print("The number of increas is: {}".format(count))


if __name__ == '__main__':
    main()
