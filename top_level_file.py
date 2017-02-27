from submodule.foo import A
import submodule.bar as bar
import submodule.foo as foo
print(A, id(A))

try:
    # foo.throw()
    bar.throw()
except A:
    print('it worked')
except Exception as z:
    print(z, id(z))
