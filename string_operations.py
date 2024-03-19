def main():
    S = input()
    
    #Print length of the string S
    print(len(S))
    
    #Print the first occurence of the letter 'a' in S
    print(S.index('a'))
    #Note it is guaranteed that letter a is present in the string S
    
    #Print all the characters with even index in S
    print(S[0::2])
    return 0

if __name__ == '__main__':
    main()
