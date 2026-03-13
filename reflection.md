# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

#1 - The first bug I noticed was that the hints were backwards. If the guess was too high it would give you the hint to guess even higher. So that needed to be fixed. 
#2 - The second bug I noticed was that on the left sidebar it would say I have 8 attempts allowed, but on the main screen it would only show 7 attempts left. 
#3 - The last bug I noticed was that if you changed a game mode to easy the range in the sidebar would change from 1-20 but the actual game mode would still be 1-100. 

---

## 2. How did you use AI as a teammate?

I utilized Claude Code and specifically Haiku to observe these errors because I wanted to be careful with my token usage. 

The AI made a lot of correct suggestions such as suggestion to change the hint for Go Higher to Go Lower. 

One incorrect suggestion the AI made was that the secret was exposed in the debug info which "could be considered a cheat". While this may be a helpful suggestion I think the AI lacked the context and true understanding that it is OK the debug console was there. 

---

## 3. Debugging and testing your fixes

did functional testing to see after I changed the code if the hint was to guess lower after you guessed too high of a number. Basically testing the app out myself for edge cases. 

I wrote tests using pytest and one of the tests it came up with was: 

The AI designed the pytests tests and also gave explanatations of each test. 

---

## 4. What did you learn about Streamlit and state?






- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits


I think learning good prompts to ask Claude so it can get to the bottom of an issue quicker is a good learning. One thing could be to metaprompt or ask the AI what a good prompt for the project could be.

I would spend more time playing around with the code next time. 

This made me more aware of how powerful AI generated code is. 

