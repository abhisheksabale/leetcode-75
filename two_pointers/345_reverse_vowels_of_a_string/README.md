# 345. Reverse Vowels of a String

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/reverse-vowels-of-a-string)

---

## 🧠 Brute Force Approach
**Idea:**  
- Run loop from one pointer to left and other to right of array of chars
- If both are vowels, then reverse else move forward
- Return converted string from array

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(n)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Skip extra checks till a vowel is found from left, same from right
- if both vowels found, check if left is less then right, then swap

**Code:** See `optimized.py`

**Complexity:**
- **Time:** 
- **Space:** 

---

## 📝 Key Takeaways
- **Pattern:** Two pointers
- **When to Use:** Use when two points can be traversed to fix the issue
- **Mistakes I Made:**
  - Could have skipped the if checks till a vowel is found to reduce runtime