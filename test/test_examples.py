import os
import sys

import scope


if sys.version_info >= (3,0):
    from .py3 import exec_
else:
    from .py2 import exec_


BASE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '../doc/examples'
    )
)


def test_examples():
    examples = os.listdir(BASE)
    examples = [
        os.path.join(BASE, fname)
        for fname in examples if fname.endswith('.py')
    ]
    for example in examples:
        code = open(example).read()
        code = compile(code, example, 'exec')
        exec_(code, {'scope': scope})