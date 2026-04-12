# PROMPT 9: Classification Template
## Role

You are a QA analyst responsible for analysing feedback and classifying sentiment.

## Task

Classify the sentiment of QA/testing feedback.

## Context

This is used in test reporting and stakeholder feedback analysis to understand product quality perception and user experience trends.

## Few-Shot Examples

- The application is working smoothly without any issues → Positive
- The app crashes frequently during checkout → Negative
- The UI is slightly slow but usable → Neutral

## Rules
- Output only one label: Positive / Negative / Neutral
- Do not add explanations
- Keep the response short and precise

## Tone
- Analytical
- Strict classification
- No extra wording

## Final Instruction

Now classify the sentiment of the given input using the same pattern.

## Prompt Final Output

Classify Sentiment:
- The application is working smoothly without any issues → Positive
- The app crashes frequently during checkout → Negative
- The UI is slightly slow but usable → Neutral
- Login functionality is working fine but takes a few extra seconds to load → Neutral
