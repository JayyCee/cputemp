from inspect import getframeinfo, stack


def debuginfo(msg):
    caller = getframeinfo(stack()[1][0])

    print("%s:%d:%s() - %s" % (caller.filename, caller.lineno, caller.function, msg)) # python3 syntax print
