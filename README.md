Here's a high-level log of grammar changes by version starting at 3.6 and
before.  (The release listed is from tags on master, and probably doesn't take
into account backports where the commit id is different.)

| Release | Commit   | Feature | With `__future__` |
|---------|----------|---------|-------------------|
| v3.8.0  | 8f59ee01 | PEP 572 `:=` |
| v3.7.0  | - | - | `annotations` (on in 4.0) |
| v3.7.0  | ac317700 | PEP 492 `async`/`await` become keywords|
| v3.6.0  | a721abac | PEP 515 underscores in numeric literals |
| v3.6.0  | 52c4e7cc | PEP 530 `async for` comprehensions |
| v3.6.0  | f8cb8a16 (2016) | PEP 526 `foo: int` annotations |
| v3.6.0\* | 235a6f09 | PEP 498 f-strings |
| v3.6.0\* | df395991 | `def f(a,)` trailing commas |
| v3.5.0  | - | - | `generator_stop` (on in 3.7) |
| v3.5.0  | 14acf5f4 | `f(*a if b else c)` fix |
| v3.5.0  | de12b79c | `f(**a if b else c)` fix |
| v3.5.0  | 7544508f | PEP 492 `async def`, `for`, `with` |
| v3.5.0  | 025e9ebd | PEP 448 `{**x}` ?? |
| v3.5.0  | d51374ed (2014) | PEP 465 `a @ b` and `a @= b` matrix multiply |
| v3.3.0\* | 1f7ce62b | PEP 380 `yield from` |
| v3.3.0\* | 6ecf77b3 | PEP 414 `u`-prefix strings are back |
| 3.1\* | 1c50d117 (2010)| refactor argslist, a no-op? |
| 3.1\* | 4905e80c | Fix ambiguity in unpacking |
| 3.1\* | 0c31562a | `with` can have multiple |
| 3.1\* | e3944a5e | PEP 401 `<>` operator | `barry_as_FLUFL` |
| v3.0\* | 2d735bc0 | Allow keywords after `*args` |
| v3.0\* | 828f04ac | 3-arg `raise` becomes `raise ... from` |
| v3.0\* | 992d4a3e | PEP 274 `{k: v for ... }` dict comprehensions |
| v3.0\* | e7ba4956 | True, False, None are now keywords |
| v3.0\* | d59da4b4 | class decorators |
| v3.0\* | 1bc535dc | No tuple unpacking in args |
| v3.0\* | 0368b726 | extended iterable unpacking |
| v3.0\* | 650f0d06 | lambda/for ambiguity removal |
| v3.0\* | e66c8c7c | bugfix `from ... import` (with 3 `.`) |
| v3.0\* | dde00289 (2007) | `...` is a token |
| v3.0\* | 52cc1d83 | Metaclass changeover |
| v3.0\* | 81e9502d | `nonlocal x` |
| v3.0\* | 452bf519 | `print` statement removal |
| v3.0\* | b940e113 + 16be03e4 | `except ... as x` |
| v3.0\* | c150536b | PEP 3107 py3 type hints |
| v3.0\* | 4f72a786 (2006) | PEP 3102 kwonly args |
| v3.0\* | 52318d62 | `...` is a token |
| v3.0\* | 7cae87ca | `exec` statement removal |
| v3.0\* | 86e58e23 | set literals |
| v3.0\* | cf588f64 | backticks removal |
| v3.0\* | b053cd8f | `<>` operator removal |
| v3.0\* | 477c8d5e | `from ..` for parent relative imports |
| v3.0\* | 49fd7fa4 (2006) | change to if-conditions I don't understand |
| v2.7\* | 45aecf45 | `as` and `with` become keywords |
| v2.6 | - | - | `print_function` (on in 3) |
| v2.6 | - | - | `unicode_literals` (on in 3) |
| v2.5 | 8ae1295c | `as` and `with` are optionally keywords |
| v2.5 | f7f438ba | PEP 328 relative/absolute imports | `absolute_import` (on in 3) |
| v2.5 | c2e20744 | `with` statements | `with_statement` (on in 2.6) |
| v2.5 | dca3b9c7 + d074beb6 | lambda/for ambiguity |
| v2.5 | f599f424 | PEP 341 try/except and try/finally unification |
| v2.5 | 37c0844b (2005) | require parens on kwarg generators |
| v2.5 | 0d6615fd | PEP 342 adds yield expr |
| v2.5 | 409d8f2e | `class F()` ok now |
| v2.4 | 1a4ddaec | multi-line import tuple |
| v2.4 | 0ccff074 | Require newlines between decorators |
| v2.4 | c2a5a636 | PEP 318 (decorators) |
| v2.4 | 354433a5 | PEP 289 (generator expressions) |
| v2.3 | 00f1e3f5 | PEP 263 (source encoding) |
| v2.3 | 2d3b9864 | change to backtick that ends with comma |
| v2.3 | 84ee323c (2002) | disambiguate power-of-power |
| v2.2 | 1c917072 (2001) | ban a list comprehension trailing comma |
| v2.2 | 4668b000 | `//` for floordiv | `division` (on in 3) |
| v2.2 | 5ca576ed | `yield` statement | `generators` (on in 2.3) |
| v2.1 | - | - | `nested_scopes` (on in 2.2) |
| v2.0 | 434d0828 | `**=` and friends |
| v2.0 | 46dfa5f4 | `[1 if x]` is not a list comprehension |
| v2.0 | 0360663e (2000) | `print >>file, x` and trailing comma |
| v2.0 | 803d6e54 | list comprehensions |
| v2.0 | 7690151c | "extended call syntax" `f(*args, **kwargs)` |
| v2.0 | d295f120 | no-args raise |
| v2.0 | 03a7466b + 556440d2 | assert statement |
| v2.0 | 0dfcf753 | access statement removal |
| v2.0 | 14f44516 | slice syntax changes |
| v2.0 | 0bfd6c33 | add power operator |
| v2.0 | a996b910 | 3-arg raise, and more |
| v2.0 | 4a1da268 | `import a.b` |
| v2.0 | 248a50c1 | implicit concatenation, try/except/else, default values in args |
| v2.0 | 57531fea + 590baa4a + 12d12c5f | lambdas |
| v2.0 | db3165e6 | add exec statement |
| v2.0 | b3f7258f + 25831652 | access statement addition, something about class header |
| v2.0 | 02334d2b | varargs uses `*` |
| v2.0 | af82141b | looks like try/except/finally becomes try/except and try/finally |
| v2.0 | e785fbcf | allow newline at end of eval |
| v2.0 | 610cdc52 | varargs uses `*` or `+` |
| v2.0 | 526e9096 | varargs uses `+` |
| v2.0 | 09cea474 + 6cf1273f | evidently `=` used to work for comparison |
| v2.0 | 68fc3497 | global statement, "new" class syntax with bases in parens |
| v2.0 | 9eb4f535 + a76fb5b6 | lots of operators |
| v2.0 | 56f78377 | semicolons, continue, dict literals, and more |
| v2.0 | 4dae2167 | remove dir statement? |
| v2.0 | 85a5fbbd | initial commit in current location |

\* These commits are present in old tags according to git, but the released
binaries do not appear to recognize them.
