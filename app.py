import sys
import os
import importlib

sys.path.insert(0, os.path.dirname(__file__) or os.getcwd())


def _call_time_to_milliseconds(arg: str) -> int:
    module = importlib.import_module("time_utils.time_to_milliseconds")
    return module.convert_time_to_milliseconds(arg)

def _call_milliseconds_to_time(arg: str) -> str:
    module = importlib.import_module("time_utils.milliseconds_to_time")
    return module.milliseconds_to_time(int(arg))

def main():
    if len(sys.argv) < 3:
        print("Usage: python app.py <command> <arg>")
        sys.exit(1)
    cmd = sys.argv[1]
    arg = sys.argv[2]
    if cmd == "time_to_milliseconds":
        ms = _call_time_to_milliseconds(arg)
        print(ms)
    elif cmd == "milliseconds_to_time":
        time_str = _call_milliseconds_to_time(arg)
        print(time_str)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(2)


if __name__ == "__main__":
    sys.path.insert(0, os.getcwd())
    main()
