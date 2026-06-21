# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game looked normal to me, the instructions and player input was simple to follow and interact with. I could understand that this is a guessing game and my range was between 1 to 100.

The hints did appear backwards during every input and it claimed I had no more attempts when I had a few left to go. The game also allowed me to choose 0 as an input when it claimed range options are between 1 to 100.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 0 | "Not allowed" | "Go lower" | N/A |
| -1 | "Not allowed" | "Go lower" | N/A |
| 500 | "Not allowed" | "Go lower" | N/A |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude for this project.

One example of AI suggestion is that I needed to know why my game's attempts field left me with one less attempt than it stated on my very first game. The issue came with the variable not starting off with the correct value on the first game, but all other games are correct. So through Claude's callout of that logic, it reccomended using the value 0 and not 1, and through testing that option, I decided to stick with that advice. I tested this option by replaying the game, and using all my attemps. I was able to see that I could finally correctly get locked out of the game after all attempts were used.

A second example of AI suggestion that was incorrect was when I needed to fix the game's range input verification. The AI suggestion was fine and it worked as I tested it myself by reloading the page. I could correctly guess where the issue was and there were only two line fixes within the function. The issues came when I needed to create a test for this specific function and its changes.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
For the attempt related bug:
I tested this option by replaying the game, and using all my attemps. I was able to see that I could finally correctly get locked out of the game after all attempts were used.

For the range bug:
Creating a test file was difficult as I don't normally use test files at work.
I tried to follow the directions and used pytest but Claude's tests ran fine and the other tests errored. AI was not very helpful as I did not have a point of view of how to fix this issue.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit is a way for the website to run and play the game we created.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I need to AI to fully explain its reasoning and steps, especially when it comes to testing. I have coded for a long time and have a perspective on how things are built, but that is not true for test files. I could not correct as well as I could for normal code. To help me learn and for the AI to slow down, is to use the AI to explain itself step by step. It should not edit without my permission first.