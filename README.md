# LeetCode
Description of the solved problems and links to them

1)Isomorphic Strings

    https://leetcode.com/problems/isomorphic-strings/description/

    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving the order of characters. 
    No two characters may map to the same character, but a character may map to itself.
  
2)Is Subsequence

    https://leetcode.com/problems/is-subsequence/description/

    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative       positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
  
3)Verifying an Alien Dictionary 
      
    https://leetcode.com/problems/verifying-an-alien-dictionary/description/

    In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
    The order of the alphabet is some permutation of lowercase letters.
    Given a sequence of words written in the alien language, and the order of the alphabet,
    return true if and only if the given words are sorted lexicographically in this alien language.
  
4)Contains Duplicate

    https://leetcode.com/problems/contains-duplicate/description/

    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
  
5)Find Pivot Index

    https://leetcode.com/problems/find-pivot-index/description/

    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
    This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.
  
6)Running Sum of 1d Array
  
    https://leetcode.com/problems/running-sum-of-1d-array/

    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    
7)Two Sum

    https://leetcode.com/problems/two-sum/
    
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    
8)Fizz Buzz
    
    https://leetcode.com/problems/fizz-buzz/
    
    Given an integer n, return a string array answer (1-indexed) where:
    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
    
9)Integer to Roman

    https://leetcode.com/problems/integer-to-roman/
    
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II.
    The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right.
    However, the numeral for four is not IIII. Instead, the number four is written as IV.
    Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
    There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.
    
10)Palindrome Number
    
    https://leetcode.com/problems/palindrome-number/
    
    Given an integer x, return true if x is a palindrome, and false otherwise.
 
11)Power of Three

    https://leetcode.com/problems/power-of-three/
    
    Given an integer n, return true if it is a power of three.
    Otherwise, return false.
    An integer n is a power of three, if there exists an integer x such that n == 3x.
    
12)Roman to Integer
    
    https://leetcode.com/problems/roman-to-integer/
    
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. 
    The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. 
    However, the numeral for four is not IIII. Instead, the number four is written as IV. 
    Because the one is before the five we subtract it making four. The same principle applies to the number nine,
    which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

13)Binary Search
    
    https://leetcode.com/problems/binary-search/description/
    
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.
14)Valid Anagram

    https://leetcode.com/problems/valid-anagram/description/
    
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    
15)Zigzag Conversion

    https://leetcode.com/problems/zigzag-conversion/description/
    
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
     And then read line by line: "PAHNAPLSIIGYIR"

     Write the code that will take a string and make this conversion given a number of rows:

     string convert(string s, int numRows);
     
16)Remove Duplicates from Sorted Array
    
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
    
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages,
    you must instead have the result be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array.
    You must do this by modifying the input array in-place with O(1) extra memory.
    
17)Search Insert Position
    
    https://leetcode.com/problems/search-insert-position/description/
    
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
  
18)Shuffle the Array

    https://leetcode.com/problems/shuffle-the-array/description/
    
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].
  
19)Reverse String

    https://leetcode.com/problems/reverse-string/description/?envType=study-plan&id=algorithm-i
    
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.

20)First Bad Version

    https://leetcode.com/problems/first-bad-version/description/
    
    You are a product manager and currently leading a team to develop a new product.
    Unfortunately, the latest version of your product fails the quality check.
    Since each version is developed based on the previous version,
    all the versions after a bad version are also bad.
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
    which causes all the following ones to be bad.
    You are given an API bool isBadVersion(version) which returns whether version is bad.
    Implement a function to find the first bad version.
    You should minimize the number of calls to the API.
    
21)Rotate String

    https://leetcode.com/problems/rotate-string/description/
    
    Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
    A shift on s consists of moving the leftmost character of s to the rightmost position.
    For example, if s = "abcde", then it will be "bcdea" after one shift.
    
22)Rotate Array
    https://leetcode.com/problems/rotate-array/description/
    
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
   
23)Longest Common Prefix
    
    https://leetcode.com/problems/longest-common-prefix/description/
    
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
 
24)Letter Combinations of a Phone Number
    
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
    
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 
25)Reverse Integer

    https://leetcode.com/problems/reverse-integer/description/
    
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.
