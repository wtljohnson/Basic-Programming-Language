import basic

while True:
    output = input("basic > ")
    result, error = basic.run("<stdin>", output)

    if error:
        print(error)
    elif result:
        print(result)
