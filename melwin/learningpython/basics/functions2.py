def main():
    main2()

# main2() <= this would fail

def main2():
    print("hey")
  
# This solves the problem of that
# occurs when main2() is called before
# its definition  
if __name__ == "__main__":
    main()