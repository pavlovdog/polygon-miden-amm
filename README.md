# AMM pool implementation on Polygon miden

Stack based, contains initial state and list of operations to emulate.
Each operation is specified with two numbers - operation identifier and amount.

Operation identifiers:

- `1`, swap left to right
- `2`, swap right to left
- `3`, add liquidity to left, right increased correspondingly
- `4`, add liquidity to right, left increased correspondingly

## Usage

`$ miden run --assembly amm.masm --input input.json`

## Example

Input:

```json
{
  "operand_stack": [
    "1000",
    "2",
    "10000",
    "20000"
  ],
  "advice_stack": ["0"]
}
```

Output:

```
Output: [18181, 11000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## Benchmarks

Execution for 1000 operations takes 1.5s on Mac Pro.

## TODO

- Support remove liquidity operation
