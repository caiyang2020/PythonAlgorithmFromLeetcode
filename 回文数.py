"""
    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

"""


def isPalindrome(self, x: int) -> bool:
    x = str(x)
    if x[0] == "-":
        return False
    else:
        if x == x[::-1]:
            x = int(x)
            return True if -2147483648 < x < 2147483647 else 0
        else:
            return False
