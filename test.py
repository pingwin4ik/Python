def arg_to_print(argument):
    print "Hello {}!".format(argument)


if __name__ == "__main__":
    arg = raw_input('Input argument: \n')
    arg_to_print(arg)