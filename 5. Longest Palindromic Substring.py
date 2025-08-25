def longestPalindrome(s):
    n=len(s)

    lengtheist=""
    for i in range(n):
        for j in range(i+1,n+1):
            subString=s[i:j]

            if (subString == subString[::-1]) and len(subString) >len(lengtheist):
                lengtheist=subString

    return lengtheist     
