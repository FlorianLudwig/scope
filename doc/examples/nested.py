app_scope = scope.Scope()
app_scope['db_password'] = 'foobar'
app_scope['user'] = 'anon'

nested_user_scope = scope.Scope()

def handle_user():
    current_scope = scope.get_current_scope()

    # now inside a user session we might want
    # to store some user data
    current_scope['user'] = 'admin'
    # and we still want to access the
    # app data
    assert current_scope.get('db_password') == 'foobar'

    # we can change the db_password
    current_scope['db_password'] = 'secret_admin_password'

    # and all our data is as expected:
    assert current_scope.get('db_password') == 'secret_admin_password'
    assert current_scope.get('user') == 'admin'


def main():
    with app_scope():
        # we are inside "some app" that
        # stores it "db_password" inside
        # a scope
        assert scope.get('db_password') == 'foobar'

        with nested_user_scope():
            handle_user()

        # the app scope is untouched
        assert scope.get('db_password') == 'foobar'
        assert scope.get('user') == 'anon'


main()