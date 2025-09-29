# 1768. Merge Strings Alternately

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/merge-strings-alternately)

---

## 🧠 Brute Force Approach
**Idea:**  
- First calculate which word has max length.
- Then loop over the length and insert character into list if it exists. 
- Return by converting list into string.

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(Max(N,M))
- **Space:** O(N+M)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Find minimum length between two strings
- Loop over minimum length and add words alternatively
- After loop, check if first or second string has some characters left to fill
- Add those characters and convert list to string

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(N+M)
- **Space:** O(N+M)

---

## 📝 Key Takeaways
- **Pattern:** One Pointer
- **When to Use:** When same operation is required to be done on both data types
- **Mistakes I Made:**
  - Looped over max length
  - Optimized version avoids looping and if condition inside loop
