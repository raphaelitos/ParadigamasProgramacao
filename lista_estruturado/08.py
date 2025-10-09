def CtoF(c):
    return c * 1.8 + 32

def CtoK(c):
    return c + 273

def main():
    temp = float(input())
    print("to Kelvin: ", CtoK(temp))
    print("to Fahrenheit: ", CtoF(temp))

main()