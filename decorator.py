def div(a,b):
    print(a/b)
def special(div):
    def inner(a,b):
        if a<b:
         a,b=b,a 
        return div(a,b)
    return inner
div=special(div)
div(2,4)