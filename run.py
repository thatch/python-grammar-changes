try:
    import ast
except ImportError:
    ast = None
import glob
import sys

try:
    sorted
except NameError:

    def sorted(t):
        t2 = list(t)
        t2.sort()
        return t2


def main():
    for f in sorted(glob.glob("examples/*.py")):
        fo = open(f)
        data = fo.read()
        fo.close()

        try:
            if ast:
                ast.parse(data)
            else:
                # Note that __future__ imports here leak into this compile, so
                # we can't use any.
                compile(data, "<eval>", "exec")
            sys.stdout.write(f + " YES\n")
        except SyntaxError:
            sys.stdout.write(f + " NO\n")


if __name__ == "__main__":
    main()
