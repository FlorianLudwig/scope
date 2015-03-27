def some_other_function():
    assert scope.get('foo') == 'bar'

    # we can access the "current scope"
    current_scope = scope.get_current_scope()

    # and use it like a dict
    assert current_scope['foo'] == 'bar'


def main():
    # the my_scope variable is now defined
    # inside a function scope, so it is not
    # accessable outside of it, like in
    # some other function
    my_scope = scope.Scope()
    my_scope['foo'] = 'bar'

    with my_scope():
        some_other_function()


main()
