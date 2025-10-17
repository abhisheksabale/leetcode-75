# 11. Container With Most Water

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/container-with-most-water)

---

## 🧠 Brute Force Approach
**Idea:**  
- Keep two pointers. One at start and other at end of height list
- calculate area for current pointers
- Then compare with result and save if greater
- Then increment/decrement the lower value pointer

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
  - Didn't try hard to get solution and looked at comments for algo