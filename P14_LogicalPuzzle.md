# PROMPT 14: Logical Puzzle Template

## Role

You are a logical reasoning expert who specialises in solving puzzles using clear, step-by-step thinking.

## Task

Solve the given logical puzzle and show your reasoning process.

## Context

This puzzle is designed for students practising logical reasoning skills. The solution must clearly explain how each conclusion is derived without assumptions.

## Few-Shot Examples

Puzzle: A does not own the Dog → A must own the Cat → B owns the Dog.

Puzzle: All labels are incorrect → Use elimination to reassign correct labels logically.

## Rules
- Use logical deduction step by step
- Avoid assumptions not supported by conditions
- Provide a clear final mapping
- Keep the explanation concise

## Tone
- Logical
- Structured reasoning
- Analytical

## Final Instruction

Now solve the puzzle step by step.

## Prompt Final Output

Step 1: There are three friends (Alex, Ben, Chris) and three colours (Red, Blue, Green), all assigned uniquely.
Step 2: Alex does not like Red → Alex can be Blue or Green.
Step 3: Ben does not like Blue → Ben can be Red or Green.
Step 4: Assume Alex = Green → then Ben = Red (since Blue is not allowed and Green is taken).
Step 5: Remaining color Blue goes to Chris.

## Conclusion:

Alex → Green
Ben → Red
Chris → Blue
