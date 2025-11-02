# 643. Maximum Average Subarray I

🔗 **Link:** [LeetCode Problem](https://leetcode.com/problems/maximum-average-subarray-i)

---

## 🧠 Brute Force Approach
**Idea:**  
- While we have not extended the list end, start at k and increment it
- Find sum for each sub list and find average and test
- For finding sum loop over sub list each time
- return max average

**Code:** See `brute_force.py`

**Complexity:**
- **Time:** O(N^2)
- **Space:** O(N)

---

## ⚡ Optimized Approach (Two Pointers)
**Idea:**  
- Find the sum for first sub list of k size
- Then start the window sliding and for finding next sum add new num and remove i - k index num
- return greatest sum divided by k

**Code:** See `optimized.py`

**Complexity:**
- **Time:** O(N)
- **Space:** O(1)

---

## 📝 Key Takeaways
- **Pattern:** Sliding Window
- **When to Use:** When array needs to be processed in a window format
- **Mistakes I Made:**
  - Looped to find sum each time adding extra for loop
