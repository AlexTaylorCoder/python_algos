
def decimal_to_binary(num):
    assert int(num) == num, "Number must be an integer!"
    if num == 0:
        return 0
    return num % 2  + 10 * decimal_to_binary(int(num/2))





print(decimal_to_binary(-16))