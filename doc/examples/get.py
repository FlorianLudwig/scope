import pytest

my_scope = scope.Scope()

# using .get on a non existing key
# does NOT return None as a python
# dict but raises an IndexError.
with pytest.raises(IndexError):
    my_scope.get('foo')

# if you want to None for non existing
# values, do so explicitly:
assert my_scope.get('foo', None) is None