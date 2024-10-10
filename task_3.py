import sys


def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск 1 з {source} на {target}")
        return
    hanoi(n - 1, source=source, target=auxiliary, auxiliary=target)
    print(f"Перемістити диск {n} з {source} на {target}")
    hanoi(n - 1, source=auxiliary, target=target, auxiliary=source)

def main(n):
    hanoi(n, "A", "C", "B")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python task_3.py <кількість дисків>")
        sys.exit(1)

    n = int(sys.argv[1])

    main(n)
