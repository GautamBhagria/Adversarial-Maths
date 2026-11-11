# Adversarial Infrastructure Security Portfolio

This showcases discrete mathematics, machine learning and offensive engineering in one frame. I have used **Streamlit** to evaluate edge-case security failures under semi-realistic threat vectors.

Project Details

## Project 1: Adversarial Defense Randomized Smoothing Engine
* **Core Objective:** Optimize machine learning classification safety boundaries against malicious input manips.
* Introduces controlled isotropic noise during training to enforce mathematically certifiable defense spaces.
* ** Hackers tweak inputs (like adding invisible pixels to an image) to trick an AI into making errors. This tool injects a protective "blur" (controlled noise) around the data so small tweaks cannot derail the AI.

## Project 2: Spectral Graph Laplacian Side-Channel Defect Analyzer
* **Core Objective:** Map software execution traces into complex topological networks to capture timing and power variations.
* Constructs an unnormalized Graph Laplacian Matrix (L = D - A) from a program's state interactions.
* Uses Spectral Bisection thresholds to automatically flag boundary anomalies; any drop below λ₂ < 0.8 highlights a physical data leak.
* ** Even if software code is secure, a chip can leak secret keys through tiny changes in how much power it draws or how long it takes to compute. This tool converts processing timelines into a interconnected network chart; if a secret data leak is present, a mathematical cut splits the network map and triggers a bright red alarm highlighting the exact leak location.


## Project 3: Multi-Vector OWASP & GenAI Adversarial Security Tester
* **Core Objective:** Emulate active attacker fuzzing behavior to validate application boundaries and validation filters.
* Features an automated mutation engine applying Hex/URL encoding to simulate Web Application Firewall (WAF) bypasses. Traditional input boundaries susceptible to structural code injections (SQLi, XSS). Modern **OWASP LLM Top 10** risks including administrative Prompt Injection (LLM01) and Context Window Leaks (LLM07).
* **Functions as a hacking simulator. It lets you test your web app defense filters by firing classic database exploits alongside modern AI prompt exploits (like trying to trick an AI into ignoring its rules). It includes an "evasion" toggle that disguises the malicious commands as web-safe scrambled text to prove that if your app doesn't sanitize data carefully, an attacker can slip past your outer firewall.
<img width="1867" height="883" alt="Project 1" src="https://github.com/user-attachments/assets/53b0e03a-18e9-4cf2-810f-e6fa4fb74b41" />
<img width="1877" height="943" alt="Project 2" src="https://github.com/user-attachments/assets/81a1577c-a57e-4f4d-8f31-b15e8773daba" />
<img width="1892" height="802" alt="project 3" src="https://github.com/user-attachments/assets/845bb79f-36a0-461f-9fcb-502e67c6dbf6" />

