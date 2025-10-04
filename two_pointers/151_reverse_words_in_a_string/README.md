# 151. Reverse Words in a String

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/reverse-words-in-a-string)

---

## 🧠 Brute Force Approach
**Idea:**  
- First remove starting whitespaces
- Then remove ending whitespaces
- Then separate words when empty space occurs
- Then remove single space string from result
- Then reverse the result list
- Join reversed list by adding single empty space

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(n)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Not use any in-build funtions
- Perform multiple operations in single for loop
- Reuse reverse function

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(n)

---

## 📝 Key Takeaways
- **Pattern:** Two pointers
- **When to Use:** Use when two points can be traversed to fix the issue
- **Mistakes I Made:**
  - Could have avoided split and join inbuilt functions