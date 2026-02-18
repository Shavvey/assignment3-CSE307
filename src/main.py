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

def func6(arr: np.ndarray):
    arr[arr >= 5 and arr <= 10] = True
    print(filter)


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


if __name__ == "__main__":
    main()
