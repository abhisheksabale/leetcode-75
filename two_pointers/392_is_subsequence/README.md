# 392. Is Subsequence

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/is-subsequence)

---

## 🧠 Brute Force Approach
**Idea:**  
- Keep two pointers. One for first string and other for another
- keep looping till pointers exceed strings len
- Increment pointer 1 if word found and always increment pointer 2
- If pointer 1 value is same as len of first string return True
**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Same

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Two pointers
- **When to Use:** Use when two points can be traversed to fix the issue
- **Mistakes I Made:**
  - Could have avoided if else in return statement