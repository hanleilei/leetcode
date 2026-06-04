# Parse Lisp Expression

You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
(An integer could be positive or negative.)
A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.

Example 1:

Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.
Example 2:

Input: expression = "(let x 3 x 2 x)"
Output: 2
Explanation: Assignment in let statements is processed sequentially.
Example 3:

Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Constraints:

1 <= expression.length <= 2000
There are no leading or trailing spaces in expression.
All tokens are separated by a single space in expression.
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
The expression is guaranteed to be legal and evaluate to an integer.

这个题目，算是224/227的升级版了，增加了变量和作用域的概念。解法也有两种：递归解析和状态机。

## 递归解析

```python
class Solution:
    def evaluate(self, expression: str) -> int:
        i, n = 0, len(expression)

        def parseVar() -> str:
            nonlocal i
            i0 = i
            while i < n and expression[i] != ' ' and expression[i] != ')':
                i += 1
            return expression[i0:i]

        def parseInt() -> int:
            nonlocal i
            sign, x = 1, 0
            if expression[i] == '-':
                sign = -1
                i += 1
            while i < n and expression[i].isdigit():
                x = x * 10 + int(expression[i])
                i += 1
            return sign * x

        scope = defaultdict(list)

        def innerEvaluate() -> int:
            nonlocal i
            if expression[i] != '(':  # 非表达式，可能为：整数或变量
                if expression[i].islower():  # 变量
                    return scope[parseVar()][-1]
                return parseInt()  # 整数
            i += 1  # 移除左括号
            if expression[i] == 'l':  # "let" 表达式
                i += 4  # 移除 "let "
                vars = []
                while True:
                    if not expression[i].islower():
                        ret = innerEvaluate()  # let 表达式的最后一个 expr 表达式的值
                        break
                    var = parseVar()
                    if expression[i] == ')':
                        ret = scope[var][-1]  # let 表达式的最后一个 expr 表达式的值
                        break
                    vars.append(var)
                    i += 1  # 移除空格
                    scope[var].append(innerEvaluate())
                    i += 1  # 移除空格
                for var in vars:
                    scope[var].pop()  # 清除当前作用域的变量
            elif expression[i] == 'a':  # "add" 表达式
                i += 4  # 移除 "add "
                e1 = innerEvaluate()
                i += 1  # 移除空格
                e2 = innerEvaluate()
                ret = e1 + e2
            else:  # "mult" 表达式
                i += 5  # 移除 "mult "
                e1 = innerEvaluate()
                i += 1  # 移除空格
                e2 = innerEvaluate()
                ret = e1 * e2
            i += 1  # 移除右括号
            return ret

        return innerEvaluate()
```

## 状态机

```python
from enum import Enum, auto

class ExprStatus(Enum):
    VALUE = auto()  # 初始状态
    NONE  = auto()  # 表达式类型未知
    LET   = auto()  # let 表达式
    LET1  = auto()  # let 表达式已经解析了 vi 变量
    LET2  = auto()  # let 表达式已经解析了最后一个表达式 expr
    ADD   = auto()  # add 表达式
    ADD1  = auto()  # add 表达式已经解析了 e1 表达式
    ADD2  = auto()  # add 表达式已经解析了 e2 表达式
    MULT  = auto()  # mult 表达式
    MULT1 = auto()  # mult 表达式已经解析了 e1 表达式
    MULT2 = auto()  # mult 表达式已经解析了 e2 表达式
    DONE  = auto()  # 解析完成

class Expr:
    __slots__ = 'status', 'var', 'value', 'e1', 'e2'

    def __init__(self, status):
        self.status = status
        self.var = ''  # let 的变量 vi
        self.value = 0  # VALUE 状态的数值，或者 LET2 状态最后一个表达式的数值
        self.e1 = self.e2 = 0  # add 或 mult 表达式的两个表达式 e1 和 e2 的数值

class Solution:
    def evaluate(self, expression: str) -> int:
        scope = defaultdict(list)

        def calculateToken(token: str) -> int:
            return scope[token][-1] if token[0].islower() else int(token)

        vars = []
        s = []
        cur = Expr(ExprStatus.VALUE)
        i, n = 0, len(expression)
        while i < n:
            if expression[i] == ' ':
                i += 1  # 去掉空格
                continue
            if expression[i] == '(':
                i += 1  # 去掉左括号
                s.append(cur)
                cur = Expr(ExprStatus.NONE)
                continue
            if expression[i] == ')':  # 本质上是把表达式转成一个 token
                i += 1  # 去掉右括号
                if cur.status is ExprStatus.LET2:
                    token = str(cur.value)
                    for var in vars[-1]:
                        scope[var].pop()  # 清除作用域
                    vars.pop()
                elif cur.status is ExprStatus.ADD2:
                    token = str(cur.e1 + cur.e2)
                else:
                    token = str(cur.e1 * cur.e2)
                cur = s.pop()  # 获取上层状态
            else:
                i0 = i
                while i < n and expression[i] != ' ' and expression[i] != ')':
                    i += 1
                token = expression[i0:i]

            if cur.status is ExprStatus.VALUE:
                cur.value = int(token)
                cur.status = ExprStatus.DONE
            elif cur.status is ExprStatus.NONE:
                if token == "let":
                    cur.status = ExprStatus.LET
                    vars.append([])  # 记录该层作用域的所有变量, 方便后续的清除
                elif token == "add":
                    cur.status = ExprStatus.ADD
                elif token == "mult":
                    cur.status = ExprStatus.MULT
            elif cur.status is ExprStatus.LET:
                if expression[i] == ')':  # let 表达式的最后一个 expr 表达式
                    cur.value = calculateToken(token)
                    cur.status = ExprStatus.LET2
                else:
                    cur.var = token
                    vars[-1].append(token)  # 记录该层作用域的所有变量, 方便后续的清除
                    cur.status = ExprStatus.LET1
            elif cur.status is ExprStatus.LET1:
                scope[cur.var].append(calculateToken(token))
                cur.status = ExprStatus.LET
            elif cur.status is ExprStatus.ADD:
                cur.e1 = calculateToken(token)
                cur.status = ExprStatus.ADD1
            elif cur.status is ExprStatus.ADD1:
                cur.e2 = calculateToken(token)
                cur.status = ExprStatus.ADD2
            elif cur.status is ExprStatus.MULT:
                cur.e1 = calculateToken(token)
                cur.status = ExprStatus.MULT1
            elif cur.status is ExprStatus.MULT1:
                cur.e2 = calculateToken(token)
                cur.status = ExprStatus.MULT2
        return cur.value
```

```rust
impl Solution {
    pub fn evaluate(expression: String) -> i32 {
        parse(&expression).evaluate(&mut Env::new())
    }
}
use std::collections::HashMap;

/// 一个变量和值的Binding
type Bindings = HashMap<String, i32>;

/// 记录变量绑定的环境
struct Env(Vec<Bindings>);

/// 实现一些栈操作
impl Env {
    /// 创建一个空栈
    fn new() -> Self {
        Env(Vec::new())
    }

    /// 从后向前逐帧查找一个变量
    fn find(&self, name: &str) -> Option<i32> {
        self.0.iter().rev().find_map(|map| map.get(name).copied())
    }

    /// 给栈增加新的帧
    fn add_frame(&mut self) {
        self.0.push(HashMap::new());
    }

    /// 从栈顶弹出一个帧
    fn pop(&mut self) -> Option<Bindings> {
        self.0.pop()
    }

    /// 向栈中当前帧添加一个变量
    fn insert(&mut self, k: String, v: i32) {
        self.0.last_mut().and_then(|bindings| bindings.insert(k, v));
    }
}

/// 语法树
#[derive(Debug)]
enum Expr {
    // List, Lisp的基本结构
    List(Vec<Expr>),
    // 数值
    Num(i32),
    // 符号
    Sym(String),
}

use Expr::*;

impl Expr {
    /// 表达式求值
    fn evaluate(&self, env: &mut Env) -> i32 {
        match self {
            // 对于数值，值即为它本身
            Num(n) => *n,
            // 对于符号，在栈中寻找对应的变量
            Sym(s) => env.find(s).unwrap(),
            // 对于列表，调用eval_list函数对其求值
            List(l) => Self::eval_list(l, env),
        }
    }

    /// 列表求值
    fn eval_list(list: &[Expr], env: &mut Env) -> i32 {
        // 对 let form 求值
        let eval_let = |l: &[Expr], env: &mut Env| {
            // 向栈中添加新帧
            env.add_frame();

            // 变量和值成对，单出来的是最终需要求值的表达式
            // 这syntax真烂啊
            let pairs = l.chunks_exact(2);
            let tail_expr = &pairs.remainder()[0];

            // 对于每对变量和值，对值表达式求值后加入环境
            pairs.for_each(|pair| if let [Sym(s), v] = pair {
                let val = v.evaluate(env);
                env.insert(s.clone(), val);
            });

            // 对tail求值
            let val = tail_expr.evaluate(env);

            // **离开let，从栈中pop出当前帧**
            env.pop();
            val
        };

        match list {
            // let form，调用eval_let
            [Sym(s), l @ ..] if s == "let" => eval_let(l, env),
            // add func，求值后求和
            [Sym(s), a, b] if s == "add" => a.evaluate(env) + b.evaluate(env),
            // mul func，求值后求积
            [Sym(s), a, b] if s == "mult" => a.evaluate(env) * b.evaluate(env),
            _ => unreachable!(),
        }
    }
}

/// 解析S表达式为语法树
fn parse(expr: &str) -> Expr {
    // 解析atom，能parse为数字就算数字……其他情况为符号
    let parse_atom = |atom: String| atom.parse().map_or(Sym(atom.to_string()), |n| Num(n));

    let mut stack = Vec::new();
    let mut list = Vec::new();
    let mut atom = String::new();

    for c in expr.chars() {
        match c {
            // 新的子表达式开始
            '(' => {
                // 将当前list暂存入stack
                stack.push(list);
                // 并新建一个stack
                list = Vec::new();
            }
            ' ' => if !atom.is_empty() {
                list.push(parse_atom(atom));
                atom = String::new();
            }
            // 当前表达式结束
            ')' => {
                // 若atom非空则将其加入list
                if !atom.is_empty() {
                    list.push(parse_atom(atom));
                    atom = String::new();
                }
                // 把当前的list作为元素加入上一层list
                let mut last_list = stack.pop().unwrap();
                last_list.push(List(list));
                // 并返回上一层
                list = last_list;
            }
            // 其他字符作为atom一部分
            _ => atom.push(c),
        }
    }

    if !atom.is_empty() {
        // 只有一个atom的情况
        parse_atom(atom)
    } else {
        // 否则list中唯一的项就是最终结果
        list.pop().unwrap()
    }
}
```
