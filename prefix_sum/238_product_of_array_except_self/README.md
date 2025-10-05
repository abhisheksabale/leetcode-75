# 238. Product of Array Except Self

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/product-of-array-except-self)

---

## 🧠 Brute Force Approach
**Idea:**  
- Looped through array twice to calculate product causing O(n^2) time and time exceed error

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n^2)
- **Space:** O(n)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Understood prefix sum, looked at a solution
- We find a prefix product array and a suffix product array, then multiply both for answer

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Prefix sum
- **When to Use:** quickly calculate the sum of elements in a subarray or range multiple times.
- **Mistakes I Made:**
  - Didn't know about prefix sum logic
  - Had to take help from solutions