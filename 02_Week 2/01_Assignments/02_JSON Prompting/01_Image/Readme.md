# 📁 1. README — IMAGE GENERATION
# 🖼️ AI Image Generation using JSON Prompting
## 📌 Overview

This project demonstrates how structured JSON prompting improves the quality, consistency, and controllability of AI-generated images compared to traditional unstructured prompts.

The use case focuses on generating a horror-themed dinosaur creature using two approaches:

Normal text prompting

Structured JSON prompting

## 🎯 Objective

## To showcase:

- Differences between unstructured vs structured prompts
- Improved visual quality and realism
- Better feature control and repeatability

## 🧪 Test Scenario
- Test Case	Input Type	Description
- TC_01	Normal Prompt	Simple text input
- TC_02	JSON Prompt	Structured input with defined attributes

## 🔹 Normal Prompt Example
A terrifying mutated dinosaur demon with glowing cracks, multiple eyes, torn wings, standing in a dark swamp

## 🔹 JSON Prompt Example
{
  "subject": {
    "type": "creature",
    "description": "terrifying mutated dinosaur demon",
    "features": [
      "multiple glowing eyes",
      "torn bat wings",
      "decaying flesh",
      "glowing magma cracks"
    ]
  },
  "environment": {
    "location": "dark swamp",
    "details": [
      "dead trees",
      "thick fog",
      "burning ground"
    ]
  },
  "visual_style": {
    "style": "cinematic horror",
    "quality": "8K ultra realistic",
    "mood": "dark and terrifying",
    "lighting": "low key lighting with red glow"
  },
  "camera": {
    "angle": "low angle",
    "focus": "sharp focus on subject"
  },
  "effects": ["fog", "glow", "smoke"],
  "negative_prompt": ["cartoon", "blurry", "low detail"]
}

## 📊 Results Comparison

<img width="376" height="177" alt="image" src="https://github.com/user-attachments/assets/170c3934-0db3-41cc-b45c-b64f2ce92ed1" />

## 🛠️ Tools Used
- AI Image Generators (e.g., Stable Diffusion, Midjourney)
- Prompt Engineering Techniques

## 🧠 Key Learnings
- Structured prompts act like test cases
- JSON improves:
- Repeatability
- Accuracy
- Control over outputs

## 🚀 Future Enhancements
- Add automated prompt validation
- Integrate with test frameworks
- Expand to multi-scene storytelling
