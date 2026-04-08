# Prompt 3 - PHARA PHRASING

## Role

You are a senior QA tester with 5+ years of experience in web and mobile application testing, responsible for improving bug report quality and clarity.

## Task

- Rewrite a defect description that currently reads:
- “App crashes sometimes when user clicks the profile icon after logging in.”
- The goal is to make it clearer, more precise, and actionable for the development team.

## Context

This defect report is part of a sprint testing cycle for a mobile app. The development team needs detailed, unambiguous information to reproduce and fix the issue efficiently.

## Guidelines

- Preserve the original meaning
- Eliminate vague terms like “sometimes”
- Include clear reproduction steps
- Include expected and actual behavior
- Include environment details if helpful

## Tone

- Professional QA language
- Clear and structured
- Concise and easy to understand

## Response Style

- Single paragraph
- Structured and detailed

## Output Format

You are a senior QA tester with 5+ years of experience in web and mobile application testing. Rewrite the following defect description to make it clearer, precise, and actionable for the development team:

"App crashes sometimes when user clicks the profile icon after logging in."

The rewritten description should be a single paragraph that includes:

• Clear reproduction steps
• Expected behavior
• Actual behavior
• Any relevant environment or device information (e.g., OS version, app version)

Make sure to preserve the original meaning, eliminate vague terms like “sometimes,” use professional QA language, and make it concise, structured, and easy to understand for developers. Include any additional details that would help reproduce the bug.

## Few-Shot Examples

• Rewrite with steps
• Include expected vs actual
• Add environment details

## Final Instruction

Now respond as a senior QA tester, following all the above structure, tone, and rules.

## Prompt Final Output
Defect Description:
When a user logs into the mobile app (v2.3.1) on an Android device running OS 13.0, tapping the profile icon from the home screen causes the app to immediately crash. 
Reproduction steps: 
1) Open the app and log in with valid credentials, 
2) Navigate to the home screen, 
3) Tap the profile icon. 
Expected behaviour: The user should be navigated to their profile page without interruption. 
Actual behaviour: The app closes unexpectedly and returns to the device home screen. This issue occurs consistently on the specified OS and app version and needs urgent attention for stability and user experience.

