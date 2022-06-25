# TFLite

A Tiny Functional Language (lite).

## Declarations

Newlines and semicolons delimit. Leading characters name.

## ADTs

Uppercase names define ADTs. Bar denotes sums, juxtaposition products.

* `FA|BF|CFF` <=> `data F = A | B F | C F F`

## Functions

Lowercase names are functions. Numbers denote arity. An expression follows arguments.

* `k2xyx` <=> `k x y = x`

## Pattern matching

Argments are matched structurally. Uppercase destructures ADTs.
Lowercase binds. Underscore ignores. Bar delimits patterns.

* `BT|F;a2TTT|Txx|_TF` <=> `data B = T | F`; `a T T = T`; `a T x = x`; `a _ T = F`

## Expressions

Juxtaposition applies. Parentheses group. Brackets form anonymous functions.

* `[1Sxx|ZSZ](S(SZ))` is `(SZ)` is `SZ`

## Main

Caret denotes an entry point.

* `^1xx` <=> `main x = x`

## I/O

Input and output are shell standard. Both form expressions of ADTs. Newlines delimit inputs.
Output is singular. Equivalence is expressionwise rather than bytewise.

* `S(SZ)\nSZ` ~> `^2SxSy^xy|ZSxx|SxZx|ZZZ` ~> `SZ` is `S Z` is `S(Z)` is `(S)(Z)` is ...

## Whitespace

Spaces and tabs are insignificant. Empty declarations vanish.

* ` f    3g    x  y             gy  x ;  ;;;;` is `f3gxygyx`

## Legal

The rules disallow disallowing exploiting transpiler bugs. Exploits are discouraged.
All material is served as is. All rights are reserved.
