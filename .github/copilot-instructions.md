# LeetCode Study Repository Copilot Instructions

## Repository Structure & Purpose

This is a comprehensive algorithm learning repository focused on LeetCode problem solutions across multiple programming languages. The repository follows a structured approach to algorithm mastery using a 5-round learning methodology.

## File Organization Patterns

### Language-Specific Solutions
- **`cpp/`**, **`python/`**, **`java/`**, **`golang/`**, **`rust/`**: Problem solutions by language
- **Naming Convention**: `{problem_number}_{problem_name}.md` (e.g., `001_two_sum.md`, `023-merge_k_sorted_lists.md`)
  - Note: Some use underscores (`_`), others use hyphens (`-`) - both are acceptable
- **File Format**: Markdown files containing problem description, multiple solution approaches, and complexity analysis

### Algorithm Topic Categorization
- **Topic Files**: Root-level `.md` files organized by pattern:
  - Data Structures: `hashtable.md`, `heap.md`, `stack.md`, `linkedlist.md`, `tree.md`, `unionfind.md`, `segmenttree.md`
  - Algorithm Patterns: `bfs.md`, `dfs.md`, `dp.md`, `greedy.md`, `binarysearch.md`, `2points.md`, `DivideConquer.md`, `recursion.md`, `bitManipulation.md`
  - Special Topics: `sliding window.md`, `interval overlapping.md`, `MonotonicStack.md`, `topology sort.md`, `prefixSum.md`
- **Purpose**: Quick reference for problems by algorithmic pattern
- **Content**: Links to related problems (often minimal - just problem numbers and links)

### Study Resources
- **`template/jiuzhang_template.md`**: Comprehensive algorithm templates from Jiuzhang (九章算法)
  - Contains standard patterns for Binary Search, Two Pointers, BFS, DFS, Dynamic Programming, etc.
  - Includes complexity analysis and use case conditions for each pattern
- **`ClassifyByCompany.md`**: Problems organized by tech companies (LinkedIn, Google, Facebook, etc.) for interview prep
- **`GrokkingTheCodingInterviewPatternInPython/`**: Additional pattern-based problem groupings
- **`CtCI/`**: Cracking the Coding Interview related content

## Solution File Format Standards

Each solution file follows this structure:
```markdown
# Problem Title

[[tag]] (e.g., [[hashtable]], [[dfs]], [[bfs]], [[2points]], etc.)

Problem description...

Example:
Input: ...
Output: ...

Time/Space complexity analysis...

```language
// Solution code with comments
```

Alternative approaches and optimizations...
```

### Complexity Analysis Requirements
- Always include both **Time Complexity** (e.g., O(n), O(logn)) and **Space Complexity** (e.g., O(1), O(n))
- Explain the reasoning behind complexity calculations
- Compare complexities when multiple approaches are presented

### Code Style
- Include inline comments for non-obvious logic
- For C++: Use STL containers (`unordered_map`, `vector`, etc.)
- For Python: Use Pythonic idioms and built-in functions
- Chinese comments are acceptable where appropriate (this is a bilingual repository)

## Key Development Patterns

### Problem Analysis Workflow (4-step process)
1. **Clarification (澄清)**: Understand problem requirements thoroughly
2. **Multiple Solutions (多个方法)**: Analyze different approaches with complexity trade-offs (compare time/space)
3. **Implementation (coding)**: Code the optimal solution
4. **Test Cases**: Validate with edge cases

### Learning Methodology (5-round system)
从 README.md 的学习方法论：
- **Round 1 (5分钟)**: Read problem, look at solutions, understand approaches, memorize patterns
- **Round 2 (马上)**: Write solution independently, submit to LeetCode, compare different approaches
- **Round 3 (24小时后)**: Redo the problem without looking at solutions
- **Round 4 (一周后)**: Specialized practice for specific patterns
- **Round 5 (面试前)**: Recovery practice before interviews

**职业训练 = 拆分知识点 + 刻意练习 + 反馈**

## Content Creation Guidelines

### When Adding New Solutions
1. Create file in appropriate language directory using naming convention
2. Start with `# Problem Title` and `[[tag]]` references
3. Include complete problem description with examples
4. Provide multiple solution approaches when applicable:
   - Brute force approach (if educational)
   - Optimized approach with explanation
   - Alternative approaches with trade-off analysis
5. Add detailed complexity analysis for each approach
6. Include clean, well-commented code
7. Add cross-references to relevant topic files

### Topic File Maintenance
- Topic files are intentionally minimal (just links to problems)
- When adding a new problem with a specific pattern, add its reference to the corresponding topic file
- Format: Problem number and link (follow existing format in each topic file)

### Cross-Language Consistency
- The same problem may have different implementations across languages
- Focus on idiomatic solutions for each language
- C++ solutions may differ in structure from Python solutions (this is expected and encouraged)

### Template Usage
- Reference `template/jiuzhang_template.md` for standard algorithm patterns
- Key templates include:
  - **Binary Search**: Three main types (finding position, first/last occurrence, answer space search)
  - **Two Pointers**: Opposite direction, same direction, sliding window
  - **BFS**: Level-order traversal template using queue
  - **DFS**: Recursion with backtracking
  - **Dynamic Programming**: State definition, transition equations, initialization
  - **Union Find**: Quick union with path compression

## Directory Structure Notes

- **`notes/`**: Additional study notes and references
- **`SQL/`**: SQL problem solutions
- **`shell/`**: Shell scripting problems
- **`2020Sep/`**: Time-based problem collection
- **Temporary files**: `t`, `t.cpp`, `t.py` - scratch files for quick testing (don't modify)

## Quick Reference

- **Find by Pattern**: Check topic files (`.md` files in root)
- **Find by Company**: Use `ClassifyByCompany.md`
- **Algorithm Templates**: Reference `template/jiuzhang_template.md`
- **Multi-language**: Solutions available in `cpp/`, `python/`, `java/`, `golang/`, `rust/`
- **Learning Method**: Follow the 5-round system described in README.md

## Working with This Repository

When helping with this repository:
1. **Prioritize code clarity** - Solutions should be educational
2. **Include complexity analysis** - This is non-negotiable for all solutions
3. **Maintain file organization** - Follow the established naming conventions
4. **Provide multiple approaches** - Compare and contrast different solutions
5. **Add cross-references** - Link related problems via `[[tag]]` notation
6. **Respect bilingual nature** - Both English and Chinese content are acceptable