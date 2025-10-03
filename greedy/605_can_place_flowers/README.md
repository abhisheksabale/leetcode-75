# 605. Can Place Flowers

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/can-place-flowers)

---

## 🧠 Brute Force Approach
**Idea:**  
- Loop through flowerbed and skip 2 places forward if planted
- If not planted, then check if next is also empty or it is end of list
- return comparison

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Same as brute but end loop early by comparison

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Greedy
- **When to Use:** Trying to find solution at the earliest
- **Mistakes I Made:**
  - Edge cases took time to fix
  - End loop early
