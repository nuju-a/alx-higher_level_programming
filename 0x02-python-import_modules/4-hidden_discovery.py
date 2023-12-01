#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    name = dir(hidden_4)
    sort_name = sorted(name)

    for name in sort_name:
        if not name.startswith("__"):
            print(name)
