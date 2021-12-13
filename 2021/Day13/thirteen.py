import numpy as np
import utils


def process_point(point: str) -> np.ndarray:
    return np.array(point.split(','))


def process_fold(fold: str) -> tuple:
    fold = fold.split('=')  # Splits into 'fold along [x|y]' and '[d+]'
    axis = fold[0][-1]
    line = int(fold[1])
    return axis, line


def create_points_map(points: np.ndarray) -> np.ndarray:
    x_coords, y_coords = points[:, 0], points[:, 1]
    max_x, max_y = x_coords.max(), y_coords.max()
    points_map = np.zeros((max_x + 1, max_y + 1), dtype=int)
    points_map[x_coords, y_coords] = 1
    return points_map


def pre_process_data(data: str) -> tuple:
    points, folds = data.split('\n\n')
    points = utils.map_list(process_point, points.split('\n')).astype(int)
    folds = utils.map_list(process_fold, folds.split('\n'))
    return create_points_map(points), folds


def get_data() -> tuple:
    return utils.read_whole_file(pre_process_data)


def fold_along_x(points_map: np.ndarray, line: int) -> np.ndarray:
    fold_start = line + 1
    fold = np.flip(points_map[fold_start:, :], 0)

    start = line - len(fold)
    points_map = points_map[:line, :]
    points_map[start:line, :] |= fold
    return points_map


def make_fold(points_map: np.ndarray, axis: str, line: int) -> np.ndarray:
    if axis == 'x':
        return fold_along_x(points_map, line)
    else:
        return fold_along_x(points_map.transpose(), line).transpose()


def get_dots_after_one_fold(points_map: np.ndarray, folds: np.ndarray) -> int:
    axis, line = folds[0]
    points_map = make_fold(points_map, axis, line)
    return points_map.sum()


def print_map(points_map: np.ndarray):
    points_map = points_map.transpose().astype(str)
    points_map[points_map == '0'] = ' '
    points_map[points_map == '1'] = '#'
    points_map = utils.map_list(lambda x: ''.join(x), points_map).astype(str)
    print('\n'.join(points_map))


def get_code(points_map: np.ndarray, folds: np.ndarray):
    for axis, line in folds:
        points_map = make_fold(points_map, axis, line)
    print_map(points_map)


def main():
    data = get_data()
    points = get_dots_after_one_fold(*data)
    print("The number of points after one fold is {}".format(points))

    get_code(*data)


if __name__ == '__main__':
    main()
