# 443. String Compression

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/string-compression)

---

## 🧠 Brute Force Approach
**Idea:**  
- Run a loop and create a compress string
- Then run another loop and update the input array with chars from string

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Same as brute

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Two pointers
- **When to Use:** Use when two points can be traversed to fix the issue
- **Mistakes I Made:**
  - Edge case missed for last element in array