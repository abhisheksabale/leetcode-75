# 283. Move Zeroes

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/move-zeroes)

---

## 🧠 Brute Force Approach
**Idea:**  
- Init last zero found at variable at 0
- Loop over length of list and if field is non-zero then shift it to last zero found index and increment it
- At last loop over the remaining indexes till end of length of list and add zeros there

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
  - Couldn't find solution in required time, looked in editorial for help