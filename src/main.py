import numpy as np

def func1():
    arr = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            arr[i,j] = i + j
    return arr

def func2(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    last_col = arr[:, -1:]
    first_row = arr[0, :]
    return (first_row, last_col)
    
def main():
    arr = func1()
    print(arr)
    first_row, last_col = func2(arr)
    print(first_row)
    print(last_col)


if __name__ == "__main__":
    main()
