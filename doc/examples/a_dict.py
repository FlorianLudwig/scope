import scope

my_scope = scope.Scope()
my_scope['foo'] = 'bar'
assert my_scope.get('foo') == 'bar'