Taiwan Image Transcreation
台灣文化圖像轉譯系統

Teach AI to see the world through Taiwanese cultural context.

Taiwan Image Transcreation is an interactive demo system that transforms generic image captions into Taiwan-culturally grounded visual prompts.
Instead of generating only literal or globally generic images, this project injects localized Taiwanese cultural knowledge into the generation pipeline, allowing AI to produce outputs that better reflect Taiwan’s food, architecture, traffic, festivals, and daily life.

Project Overview

Most text-to-image models can generate visually plausible images, but they often lack local cultural specificity.
For example, a simple prompt like “a bowl of noodles” may generate a generic noodle dish, but not necessarily Taiwanese beef noodles with suancai and dark broth.

This project addresses that gap through a 3-phase transcreation workflow:

Knowledge Retrieval
Retrieve relevant Taiwan cultural concepts from a local knowledge base.
LLM Transcreation
Rewrite the original generic caption into a culturally enriched prompt.
Diffusion Generation
Send the final transcreated prompt into an image generation model such as Flux/SDXL.

The system is designed as both a research demo and a human-centered interface prototype for localized AI generation.

Key Features
Interactive web-based demo UI
3-phase cultural transcreation pipeline
Taiwan-specific cultural taxonomy
Prompt enrichment based on local concepts
Image generation through diffusion model API
Simulated evaluation metrics:
CLIP Score for cultural relevance
DINO Score for structural consistency
Clean bilingual presentation style (English + Traditional Chinese)
System Pipeline
Phase 1 — Knowledge Retrieval

The system matches user input against a Taiwan concept database (taiwan_concepts.json style logic in the prototype).
Examples include:

Food: Beef noodles, bubble tea
Transport: Scooter waterfall, blue truck
Architecture: Temples, iron grilles
Festival: Ghost Festival, Mazu pilgrimage
Phase 2 — LLM Transcreation

A generic caption is transformed into a culturally meaningful prompt.

Example:

Input:
a bowl of noodles

Transcreated Prompt:
A close-up photo of a bowl of authentic Taiwanese beef noodles, rich dark brown broth, topped with chopped green pickled mustard greens (suancai) and braised beef chunks...

Phase 3 — Diffusion Generation

The enriched prompt is passed into a diffusion model pipeline to generate a culturally localized image result.

Example Inputs

Try prompts such as:

a bowl of noodles
busy city traffic
a building
people celebrating
drinking tea

These are mapped to localized Taiwanese concepts like:

Taiwanese Beef Noodles
Scooter Waterfall
Traditional Temple
Ghost Festival
Bubble Tea
Cultural Knowledge Taxonomy

The prototype currently organizes knowledge into 4 major categories:

Food
Beef Noodles
Lu Rou Fan
Bubble Tea
Transport
Scooter Waterfall
Blue Truck
Architecture
Temples
Iron Grilles
Festival
Ghost Festival
Mazu Pilgrimage

This taxonomy can be expanded in future versions with more categories such as markets, school life, convenience stores, mountain culture, indigenous culture, and urban-rural visual differences.

Evaluation Metrics

The interface includes two visualized evaluation indicators:

CLIP Score
Measures prompt-image semantic alignment and cultural relevance
DINO Score
Measures structural consistency and visual coherence

In the current demo, these values are simulated for UI presentation, but the framework can be extended to connect with real evaluation pipelines.

Tech Stack
Frontend: HTML, Tailwind CSS, JavaScript
UI Animation: GSAP
Icons: Font Awesome
Typography: Noto Sans TC, JetBrains Mono
Image Generation: Flux model via Pollinations API
Design Language: Taiwan-inspired red/blue interface palette
Project Structure
taiwan-image-transcreation/
│── index.html
│── data/
│   └── taiwan_concepts.json
│── assets/
│   └── demo-images/
│── README.md
How to Run

Because this is currently a frontend prototype, you can run it locally by simply opening the HTML file in a browser.

Option 1

Open index.html directly.

Option 2

Use a local server:

python -m http.server 8000

Then open:

http://localhost:8000
Research Motivation

This project explores an important question in generative AI:

Can image generation systems move beyond literal captioning and begin to perform cultural transcreation?

Rather than only translating text into images, the system attempts to reinterpret prompts through a Taiwanese cultural lens, making the outputs more locally meaningful, context-aware, and identity-sensitive.

This makes the project relevant to:

localized AI interfaces
culturally aware generative systems
digital humanities
HCI / UX research
prompt engineering and knowledge-grounded generation
Future Work
Replace keyword matching with semantic retrieval
Build a larger Taiwan cultural knowledge base
Integrate real LLM-based prompt rewriting
Use real CLIP / DINO evaluation instead of simulated metrics
Support multilingual input
Compare Taiwan-transcreated outputs against generic baseline generations
Add user study for perceived cultural authenticity
Demo Screenshot

You can place a screenshot here:

![Demo Screenshot](./assets/demo-screenshot.png)
License

This project is for research / educational / prototype demonstration purposes.
Please ensure that any third-party model APIs, datasets, or cultural assets are used in accordance with their respective licenses.

Acknowledgement

Inspired by the idea that AI should not only generate images, but also understand how culture shapes visual meaning.
