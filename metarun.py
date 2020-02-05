import sys
import subprocess

import libcst as cst

VERSIONS = [
    "python2.3",
    "python2.4",
    "python2.5",
    "python2.6",
    "python2.7",
    "python3.0",
    "python3.1",
    "python3.2",
    "python3.3",
    "python3.4",
    "python3.5",
    "python3.6",
    "python3.7",
    "python3.8",
]

LIBCST_VERSIONS = [
    "2.3",
    "2.4",
    "2.6",
    "2.7",
    "3.0",
    "3.1",
    "3.3",
    "3.5",
    "3.6",
    "3.7",
    "3.8",
]


def main():
    # dict[filename][version]
    results = {}
    for v in VERSIONS:
        # TODO as there get to be many more of these, should run them in
        # parallel, or at least streaming.
        output = subprocess.check_output([v, "run.py"], encoding="utf-8")
        for line in output.splitlines():
            filename, result = line.split()
            results.setdefault(filename, {})[v] = result == "YES"

    # Now print a pretty table.  TODO should write json or something consumable
    # as well.
    max_filename = max(len(f) for f in results)

    # TODO mark versions that will be libcst-checked too
    buf = [" " * max_filename]
    for v in VERSIONS:
        short_version = v[-3:]
        if short_version in LIBCST_VERSIONS:
            buf.append(f" \x1b[32m{short_version.replace('.', '')}\x1b[0m")
        else:
            buf.append(f" {short_version.replace('.', '')}")
    print("".join(buf))

    for f in sorted(results):
        sys.stdout.write(f.ljust(max_filename + 1))
        for v in VERSIONS:
            libcst_result = None
            if v[-3:] in LIBCST_VERSIONS:
                try:
                    with open(f) as fo:
                        data = fo.read()
                    cst.parse_module(
                        data, cst.PartialParserConfig(python_version=v[-3:])
                    )
                    libcst_result = True
                except cst.ParserSyntaxError:
                    libcst_result = False
            if libcst_result is not None and results[f][v] != libcst_result:
                if results[f][v]:
                    sys.stdout.write(" \x1b[31mO\x1b[0m ")
                else:
                    sys.stdout.write(" \x1b[31mX\x1b[0m ")
            else:
                sys.stdout.write(" o " if results[f][v] else " . ")
        sys.stdout.write("\n")

    print("Legend:")
    print(" green header means will test with libcst")
    print(" o   legal")
    print(" .   illegal")
    print(" \x1b[31mO\x1b[0m   legal, but libcst fails")
    print(" \x1b[31mX\x1b[0m   illegal, but libcst succeeds")


if __name__ == "__main__":
    main()
