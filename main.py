import argparse
import importlib
import sys

def run_exercise(exercise_name, input_filename, solve_part1 = True, solve_part2 = True):
    # Dynamic Import
    try:
        module = importlib.import_module(f"exercises.{exercise_name}")
    except ModuleNotFoundError:
        print(f"Error: Could not find file '{exercise_name}.py'")
        return

    # Convention: file "ex01" -> class "Ex01"
    # .title() converts "ex01" to "Ex01"
    class_name = exercise_name.title()

    if not hasattr(module, class_name):
        print(f"Error: Could not find class '{class_name}' inside '{exercise_name}.py'")
        return

    SolverClass = getattr(module, class_name)

    print(f"--- Running {class_name} ---")
    solver = SolverClass(input_filename)

    if solve_part1:
        res = solver.solve_part1()
        if res is not None: print(f"Part 01 solved : '{res}'")
        else: print(f"Part 01 has not been solved")

    print(f"#" * 40)

    if solve_part2:
        res = solver.solve_part2()
        if res is not None: print(f"Part 02 solved : '{res}'")
        else: print(f"Part 02 has not been solved")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("exercise", help="Name of the exercise file (e.g., ex01)")
    parser.add_argument("input", help="The path of the input file")
    parser.add_argument("--disable-part1", help="Do not run part 1", action='store_true', default=False)
    parser.add_argument("--disable-part2", help="Do not run part 2", action='store_true', default=False)

    args = parser.parse_args()

    run_exercise(args.exercise, args.input, solve_part1=(not args.disable_part1), solve_part2=(not args.disable_part2))
