
import sasila.utils.tt as tt


def y_hi():
    yield tt.t_yield()

def hi():
    print(y_hi())
    print(y_hi())
    print(y_hi())
    print(y_hi())
    print(y_hi())

if __name__ == '__main__':
    hi()

