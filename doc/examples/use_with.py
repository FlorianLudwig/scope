my_scope = scope.Scope()
my_scope['foo'] = 'bar'

with my_scope():
    # the global module scope's .get
    # knows we are insude "my_scope"
    assert scope.get('foo') == 'bar'

