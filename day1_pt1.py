def secret_entrance():
    rotations = []
    with open("./puzzle_input.txt") as f:
        for line in f:
            line = line.strip()
            if line:
                rotations.append((line[0], int(line[1:])))

    current_dial = 50
    count = 0

    for direction, steps in rotations:
        for _ in range(steps):
            if direction.lower() == "l":
                current_dial -= 1
                if current_dial < 0:
                    current_dial = 99
            if direction.lower() == "r":
                current_dial += 1
                if current_dial > 99:
                    current_dial = 0
        if current_dial == 0:
            count += 1
    return count

print(secret_entrance())
