import argparse
import logging

def remove_others(exp):
    ret = ""
    for c in exp:
        if c == "(":
            ret += "("
        elif c == ")":
            ret += ")"
    return ret

def find_pair_index(exp):
    ret = 1
    cnt = 0

    for i in range(len(exp)):
        if exp[i] == "(":
            cnt += 1
        elif exp[i] == ")":
            cnt -= 1

        if cnt == 0:
            ret = i
            break

    if cnt > 0:
        ret = -1

    return ret

# string -> bool
# The function checks if the expression contains the balanced parantheses.
# If it is, the function returns True; otherwise, it returns False
def is_balanced(exp):
    exp = remove_others(exp)
    if len(exp) == 0:
        return True
    elif len(exp) == 1:
        return False
    elif exp[0] == "(":
        if exp[1] == ")":
            rest = exp[2:]
            return is_balanced(rest)
        else:
            idx = find_pair_index(exp)
            rest1 = exp[1:idx]
            rest2 = exp[idx+1:]
            return is_balanced(rest1) and is_balanced(rest2)
    elif exp[-2] == "(" and exp[-1] == ")":
        rest = exp[:-2]
        return is_balanced(rest)
    else:
        return False

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exp", required=True, help="Expression", type=str)
    parser.add_argument("-l", "--log", help="Log level (DEBUG/INFO/WARNING/ERROR/CRITICAL)", type=str, default="INFO")

    args = parser.parse_args()
    return args

def main():
    args = command_line_args()
    logging.basicConfig(level=args.log)

    logging.info("Expression: {}".format(args.exp))
    logging.info("Result: {}".format(is_balanced(args.exp)))

if __name__ == "__main__":
    main()
