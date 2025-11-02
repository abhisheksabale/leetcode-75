# 1679. Max Number of K-Sum Pairs

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/max-number-of-k-sum-pairs)

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Keep dict for count
- Loop over num and check if k - num is available
- If yes then dont add num count and reduce k-num count and increment pairs count
- Return pairs

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(N)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Hashmap
- **When to Use:** Store key value pairs and process logic on them
- **Mistakes I Made:**
  - Considered only given test cases and missed the edge cases
