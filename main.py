from package1.module_a import hello as hello_a
from package2.module_b import hello as hello_b
from package2.module_b import sixteen

# direct import from package1 and package2
if __name__ == "__main__":
    hello_a()
    hello_b()
    print(sixteen())