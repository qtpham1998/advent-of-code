import numpy as np
import utils


def reformat_crt(crt: np.ndarray) -> str:
    crt = crt.reshape((6, 40))
    return '\n'.join(map(lambda l: ''.join(l), crt))


def clock_cycle(cycle: int, x: int, crt_drawing: np.ndarray) -> (int, np.ndarray):
    if x - 1 <= (cycle - 1) % 40 <= x + 1:
        crt_drawing[cycle - 1] = '#'
    cycle += 1
    return cycle, crt_drawing


def run_program(instructions: list[str]) -> (int, str):
    x = 1
    cycle = 1
    signal_strength = 0
    checkpoint = 20
    crt_drawing = np.full((240,), '.')

    for instr in instructions:
        val = 0

        if instr == "noop":
            cycle, crt_drawing = clock_cycle(cycle, x, crt_drawing)
        if instr.startswith("addx"):
            cycle, crt_drawing = clock_cycle(cycle, x, crt_drawing)
            cycle, crt_drawing = clock_cycle(cycle, x, crt_drawing)
            val = int(instr.split(' ')[1])

        if checkpoint < cycle:
            signal_strength += x * checkpoint
            checkpoint += 40
        x += val

    return signal_strength, reformat_crt(crt_drawing)


if __name__ == "__main__":
    instrs = utils.read_input_file()
    signal_sum, drawing = run_program(instrs)
    print("Part 1: The sum of these signal strengths is {}".format(signal_sum))
    print("Part 2: The program results in the following CRT:")
    print(drawing)
