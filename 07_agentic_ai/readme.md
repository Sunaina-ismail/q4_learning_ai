##  1. Why is the `Agent` class defined as a `dataclass`?

**What's a dataclass:**
A dataclass in Python is used when your class mainly stores data ,like properties. It saves us from writing boring code like `__init__`, `__repr__`, etc.

The `Agent` class stores things like:

* Agent name
* Instructions (system prompt)
* Tools it can use
* The model (e.g. GPT-4)
* Other configs

Since all of this is just data storage, using `@dataclass` makes the code cleaner, shorter, and easier.

**For Example:**
Think of an agent like a profile card of a team member. If you were creating cards for your project teammates, you’d just write:

```python
@dataclass
class Teammate:
    name: str
    role: str
    skills: List[str]
```

You wouldn’t want to write the full class manually. That’s what `@dataclass` does it fills in the boring parts so you can focus on logic.

---

## 2a.  The system prompt is contained in the Agent class as instructions? Why you can also set it as callable?

**Instructions:**
The instructions are the system prompt ,they define the agent’s role or behavior.

Example:

```python
instructions = "You are a helpful shopping assistant who suggests products."
```

This can be just plain text or it can be a function (callable) so it changes based on the situation:

```python
def dynamic_instructions(ctx):
    return f"You are helping {ctx['user_name']} to order lunch."
```

This makes the agent more flexible and context-aware.

**For Example:**
Let’s say you run a restaurant, and your waiter (agent) needs instructions.

* **Static:** “Serve pizza to everyone.”
* **Dynamic:** “Serve a vegetarian pizza to Ali, and a chicken burger to Sara.”

By making instructions a function, the agent can adjust what to do based on who it’s helping.

---

#  2b. But the user prompt is passed as parameter in the run method of Runner and the method is a classmethod

The user prompt is the message or task we want the agent to respond to — like “Find me a recipe” or “Book a flight to Lahore.”
We pass this prompt to `Runner.run()` because the `Runner` is in charge of starting and managing the whole process. The agent doesn’t just respond once — it might:

- Think step-by-step
- Use tools if needed
- Keep track of progress
- Finally give the answer

That entire loop is handled by `Runner.run()` — and that’s why the prompt goes there.

Now, why is `run()` a **classmethod**?

Because we don’t need to create a separate `Runner` object each time.  
We can just call it directly using the class:

```python
Runner.run(agent, prompt="Help me find a hotel in Murree")
```

**For Example:**
Imagine the agent is a robot assistant.
You’ve already set up the robot with tools and instructions.

Now you want to say:
* “Go clean the living room.” *

That’s your prompt.
You don’t rebuild the robot or its software each time. You just press a button (→ Runner.run()), and it starts working.

And that button can be pressed directly — no need to create a new button object each time.
That’s why it's a classmethod.


## 3. What is the purpose of the `Runner` class?

**Runner:**
`Runner` is like the manager that controls the full lifecycle of an agent’s task.

It:

* Takes the agent and the user prompt
* Starts the agent's reasoning loop
* Tracks steps, calls tools, updates messages, and checks if the job is complete
* Stops the loop once the final answer is ready

Without `Runner`, the `Agent` is just sitting idle. `Runner` brings it to life.

**For Example:**
If the `Agent` is a chef, then the `Runner` is the kitchen manager.
You give the manager (Runner) a task: “Make a pizza.”

* He tells the chef (Agent), who:

  * Reads the recipe
  * Uses tools (oven, knife)
  * Tries steps again if something fails
  * Serves the final dish

The `Runner` makes sure everything runs smoothly from start to finish.

---

## 4. What are `Generics` in Python? Why we use it for `TContext`?

**Generics:**
Generics in Python (from `typing`) are like templates. They let us say:
“I don’t know the type yet, but I’ll tell you later.”

So instead of hardcoding a type, you use a placeholder like `TContext`.

`TContext` is used for context — the info the agent gets about the situation.

Different agents may need different context types, like:

* A shopping agent might need: Cart, UserName, Address
* A coding agent might need: ProjectName, FilesList

Using generics lets us reuse the same agent logic  but with different types of context.

```python
TContext = TypeVar("TContext")
```

**For Example:**
It’s like a template form. You leave blanks like:

* Name: ___
* Age: ___
* Favorite Color: ___

Now, any user can fill it with their own values. You’re not locking it for one person only.
In the same way, `TContext` lets each agent work with customized data.

---


