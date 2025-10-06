# 334. Increasing Triplet Subsequence

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/increasing-triplet-subsequence)

---

## 🧠 Brute Force Approach
**Idea:**  
- Brute forced by applying 3 for loops and check if condition matches
- Failed due to time complexity

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(n^3)
- **Space:** O(n)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Loop through nums once
- Check if current is smallest if yes then store it as smallest and continue
- If not smallest then check if it is second smallest, if yes then store and continue
- If its not smallest and not second smallest then we have found triplets, break and return true
- Here, we keep smallest and second smallest as max integer

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(n)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Greedy
- **When to Use:** Trying to find solution at the earliest
- **Mistakes I Made:**
  - Didn't know how to reduce time complexity, had to check the solutions
