puzzle_input = """
2200670-2267527,265-409,38866-50720,7697424-7724736,33303664-33374980,687053-834889,953123-983345,3691832-3890175,26544-37124,7219840722-7219900143,7575626241-7575840141,1-18,1995-2479,101904-163230,97916763-98009247,52011-79060,31-49,4578-6831,3310890-3365637,414256-608125,552-1005,16995-24728,6985-10895,878311-912296,59-93,9978301-10012088,17302200-17437063,1786628373-1786840083,6955834840-6955903320,983351-1034902,842824238-842861540,14027173-14217812
"""

def solve_puzzle(puzzle_input):
    p1 = 0
    p2 = 0

    sanitized_input = puzzle_input.strip().split(',')
    print(sanitized_input)

    for i in sanitized_input:
        if not i.strip():
            continue

        start, end = map(int, i.split('-'))

        for num in range(start, end + 1):
            num_str = str(num)
            length = len(num_str)

            if length % 2 == 0:
                mid = length // 2
                left = num_str[:mid]
                right = num_str[mid:]
                if left == right:
                    p1 += num

            found_p2 = False
            for y in range(1, (length // 2) + 1):
                if length % y != 0:
                    continue

                seq = num_str[:y]
                multi = length // y

                if seq * multi == num_str:
                    p2 += num
                    found_p2 = True
                    break

    return p1, p2

p1, p2 = solve_puzzle(puzzle_input)
print(f"Part 1 Answer: {p1}")
print(f"Part 2 Answer: {p2}")
