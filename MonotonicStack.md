参考： https://leetcode.com/tag/monotonic-stack/

### Introduction

I've had my fair share of time dealing with problem related to monotonic stack. To be honest, some of the parts have been fairly confusing. Today, I decided to address it by writing a comprehensive resource that formulises when to use monotonic stack and which templates work in which cases.

### Problem

Monotonic stacks are generally used for solving questions of the type - next greater element, next smaller element, previous greater element and previous smaller element. We are going to create a template for each of the format, and then use them to solve variety of problems.

The template is slightly opinionated. To keep things simple, while traversing through an array, we always go from left to right. You might come across some implementations where they go from left to right for some problem and right to left for another, I feel it only adds to our confusion. Let's keep it simple.

### Assumptions and audience

I'm assuming that you are familiar with stack data structure. You might have used them to convert recursion into iteration, expression evaluation etc. In this article, we focus on building a special type of stack - monotonic stack.

If you have dealt with questions to find next greater, previous smaller elements in an array, then this article will give you some clarity of thought process.

### What is monotonic stack?

There could be four types of monotonic stacks. Please read them carefully, we'll refer to these types at multiple places in the sections below.

1. **Strictly increasing** - every element of the stack is strictly greater than the previous element. Example - `[1, 4, 5, 8, 9]`
2. **Non-decreasing** - every element of the stack is greater than or equal to the previous element. Example - `[1, 4, 5, 5, 8, 9, 9]`
3. **Strictly decreasing** - every element of the stack is strictly smaller than the previous element - `[9, 8, 5, 4, 1]`
4. **Non-increasing** - every element of the stack is smaller than or equal to the previous element. - `[9, 9, 8, 5, 5, 4, 1]`

We also assume that the right most element is at the top of the stack and left most element is at the bottom of the stack.

### A generic template

We can use the following template to build a stack that keep the monotonous property alive through the execution of the program. Don't worry if you don't understand it right now, we'll be using this template later on to work on some specific examples. That might be another opportunity to understand what is happening here.

```javascript
function buildMonoStack(arr) {
  // initialize an empty stack
  stack = [];
  
  // iterate through all the elements in the array
  for (i = 0 to arr.length - 1)) {
    while (stack is not empty && element represented by stack top `OPERATOR` arr[i]) {
      // if the previous condition is satisfied, we pop the top element
      let stackTop = stack.pop();
  
      // do something with stackTop here e.g.
      // nextGreater[stackTop] = i
    }
  
    if (stack.length) {
      // if stack has some elements left
      // do something with stack top here e.g.
      // previousGreater[i] = stack.at(-1)
    }

    // at the ened, we push the current index into the stack
     stack.push(i);
  }
  
  // At all points in time, the stack maintains its monotonic property
}
```



