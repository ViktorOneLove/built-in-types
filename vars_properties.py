import sys


def print_vars():
    try:
        frame = sys._getframe()
    except ValueError:
        print(f"Value error")
        return

    prev_frame = frame.f_back
    if prev_frame is not None:
        local_vars = prev_frame.f_locals
        for local_name, local_val in local_vars.items():
            print(f"{local_name}: {type(local_val).__module__ == 'builtins'}")
