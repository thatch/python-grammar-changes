# Usage: libcst_parse.py 2.7 somefile.py

import sys
import libcst as cst


def main(version, filename):
    with open(filename) as fo:
        data = fo.read()
    mod = cst.parse_module(data, cst.PartialParserConfig(python_version=version))
    print(mod)


if __name__ == "__main__":
    main(*sys.argv[1:])
