def print_numbers(numbas):
    for i in range(1, numbas):
        print(i)

# --------------------------------------------------

def test(numbas):
    print(f"Using input numbas: {numbas}")
    print(f"Printing numbas from 1 to {numbas - 1}:")
    print_numbers(numbas)
    print("======== *space* ==============")

# --------------------------------------------------

def main():
    test(201)
    test(77)
    test(11)
main()
