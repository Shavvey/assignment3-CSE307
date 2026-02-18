import numpy as np


def func1():
    arr = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            arr[i, j] = i + j
    return arr


def func2(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    last_col = arr[:, -1:]
    first_row = arr[0, :]
    return (first_row, last_col)


def func3(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    odd_rows = arr[1::2, :]
    even_cols = arr[:, 0::2]
    return (odd_rows, even_cols)


def func4(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    first_two_rows = arr[0:2, :]
    last_two_cols = arr[:, 2:]
    return (first_two_rows, last_two_cols)


def func5(arr: np.ndarray) -> np.ndarray:
    arr[arr % 2 == 1] = -1
    return arr


def func6(arr: np.ndarray) -> np.ndarray:
    values = np.array([])
    # NOTE: apply boolean filter to 2D array is ambiguous
    for elem in arr.flatten():  # flatten to 1D array
        if elem >= 5 and elem <= 10:
            values = np.append(values, [elem])
    return values


def func7(arr: np.ndarray):
    temp = arr[:, 0].copy()  # copy col into new object
    arr[:, 0] = arr[:, 1]  # set first to second
    arr[:, 1] = temp  # set second to copy of first (stored in temp)
    return arr


def func8() -> np.ndarray:
    arr = np.zeros((8, 8))
    arr[1::2, 0::2] = 1  # odd rows and even cols
    arr[0::2, 1::2] = 1  # even rows and odd cols
    return arr


def func9() -> np.ndarray:
    arr = np.zeros((5, 5))
    arr[0, :] = 1
    arr[-1, :] = 1
    arr[:, 0] = 1
    arr[:, -1] = 1
    return arr


def func10(arr: np.ndarray, div: int) -> np.ndarray:
    if len(arr.shape) > 1 and arr.shape[0] % div != 0:
        raise ValueError("[ERROR]: Expected 1D array of elems!")
    res = np.zeros((div, div))
    for row in range(div):
        res[row, :] = arr[row * div : (row + 1) * div]
    return res


def main():
    print("==FUNC1==")
    arr = func1()
    print(arr)
    first_row, last_col = func2(arr)
    print("==FUNC2==")
    print(first_row)
    print(last_col)
    odd_rows, even_cols = func3(arr)
    print("==FUNC3==")
    print(odd_rows)
    print(even_cols)
    first_two_rows, last_two_cols = func4(arr)
    print("==FUNC4==")
    print(first_two_rows)
    print(last_two_cols)
    print("==FUNC5==")
    odds_removed = func5(arr)
    print(odds_removed)
    print("==FUNC6==")
    print(func6(func1()))
    print("==FUNC7==")
    print(func7(func1()))
    print("==FUNC8==")
    print(func8())
    print("==FUNC9==")
    print(func9())
    print("==FUNC10==")
    print(func10(np.array([i for i in range(9)]), 3))


if __name__ == "__main__":
    main()
