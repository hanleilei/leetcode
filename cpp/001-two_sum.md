# Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2


```cpp
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        //Key is the number and value is its index in the vector.
        unordered_map<int, int> hash;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            hash[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            const int gap = target - nums[i];
            if (hash.find(gap) != hash.end() && hash[gap] > i){
                result.push_back(i);
                result.push_back(hash[gap]);
                break;
            }
        }

        return result;
    }
};
```

或者可以这样做：

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        //Key is the number and value is its index in the vector.
        unordered_map<int, int> hash;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            int numberToFind = target - nums[i];

                //if numberToFind is found in map, return them
            if (hash.find(numberToFind) != hash.end()) {
            //+1 because indices are NOT zero based
                result.push_back(hash[numberToFind]);
                result.push_back(i);			
                return result;
            }

                //number was not found. Put it in the map.
            hash[nums[i]] = i;
        }
        return result;
    }
};
```
