'''
Try the following example in the editor below.

You are given a string S. Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Output Format

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.

In the second line, print True if S has any alphabetical characters. Otherwise, print False.

In the third line, print True if S has any digits. Otherwise, print False.

In the fourth line, print True if S has any lowercase characters. Otherwise, print False.

In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
'''

def main():
    S = input()
    #Your code goes here
    alnum_flag = False
    alpha_flag = False
    digit_flag = False
    lower_flag = False
    upper_flag = False
    for i in range(len(S)):
        if S[i].isalnum():
            alnum_flag = True
        if S[i].isalpha():
            alpha_flag = True
        if S[i].isdigit():
            digit_flag = True
        if S[i].islower():
            lower_flag = True
        if S[i].isupper():
            upper_flag = True
        else:
            continue
    print("True") if alnum_flag == True else print("False")
    print("True") if alpha_flag == True else print("False")
    print("True") if digit_flag == True else print("False")   
    print("True") if lower_flag == True else print("False")
    print("True") if upper_flag == True else print("False")

            

if __name__ == '__main__':
    main()
