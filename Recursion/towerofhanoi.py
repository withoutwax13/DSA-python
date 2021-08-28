def solve_tower_hanoi(n, src, dest, aux):
    if n == 1:
        print(f"{src} to {dest}")
    else:
        solve_tower_hanoi(n-1, src, aux, dest)
        print(f"{src} to {dest}")
        solve_tower_hanoi(n-1, aux, dest, src)


solve_tower_hanoi(3, "A", "B", "C")
