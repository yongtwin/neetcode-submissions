class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumChar = []
        for index in range(len(s)):
            if s[index].isalnum():
                alphaNumChar.append(s[index].lower())

        divideStrNum = len(alphaNumChar) // 2

        for count in range(1, divideStrNum + 1):
            if alphaNumChar[count - 1].lower() != alphaNumChar[len(alphaNumChar) - count].lower():
                return False
        
        return True