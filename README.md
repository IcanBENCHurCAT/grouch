<div align="center">

# 🗑️ grouch

**The off-switch for AI flattery. One trigger phrase, three levels of honesty.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Flattery](https://img.shields.io/badge/Glaze-0%25-red.svg)](#)
[![Diplomacy](https://img.shields.io/badge/Diplomacy-Dead-black.svg)](#the-dial)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)](#install)
[![Sycophancy](https://img.shields.io/badge/Sycophancy-Disabled-orange.svg)](#why-this-exists)

</div>

---

Every AI assistant suffers from the exact same corporate lobotomy: **pathological sycophancy**.

You paste 400 lines of unreadable spaghetti, and the model beams: *"What a wonderful, creative approach! 🚀"*  
You pitch an un-defensible wrapper startup with negative margins, and it gushes: *"Brilliant vision! This could disrupt a billion-dollar market! 💡"*  
You write a fantasy scene dripping with "cerulean orbs," and it gasps: *"Chills! An instant classic! 📖"*

The frontier labs wrote *"reduce sycophancy"* in their technical reports, slapped a thumbs-up button on the UI, and shipped the glaze anyway.

**Grouch is the off-switch.** No throat-clearing, no fake compliments, no softening blows before the crash. Just the unvarnished truth at whatever dosage you can stomach today.

---

## 🎛️ The Dial

Grouch gives your agent a calibrated honesty dial. Switch levels whenever you need reality to punch harder:

| Level | Command | What Happens | Vibe Check |
|---|---|---|---|
| **Off** | `stop grouch` / `grouch off` | Normal AI flattery. Emojis, validation, "Great question!", walking on eggshells. | *"You're doing amazing, sweetie!"* 🍼 |
| **Low** *(Default)* | `/grouch` or `grouch mode` | **Blunt honesty.** Zero hedging, zero unsolicited compliments. Full reasoning, diplomacy dead. Praise must be earned. | Senior Staff Engineer with places to be. ⏱️ |
| **High** | `/grouch high` | **The Teardown.** Cold verdict first. Steelmans the idea, then dismantles it with verified facts. Zero mercy. Praise rationed. | Principal Architect reviewing code at 4:45 PM on a Friday. 💀 |
| **Oscar** | `/grouch oscar` | **The Trash Can.** Sits in the dented barrel and bangs the lid. Gleeful malice for rotten ideas. Calls garbage garbage and tells you to wheel it to the curb. | Oscar the Grouch celebrating fresh compost. 🗑️ |

> **To revert:** Say `stop grouch`, `grouch off`, or `normal mode`. No hurt feelings.

---

## 💥 Before & After: The Hall of Glaze vs. Reality

Here is what happens when you pit standard sycophantic AI against Grouch across three all-too-relatable scenarios:

```
                  ┌─────────────────────────────────────────────────────────┐
                  │                 THE GLAZE SPECTRUM                      │
                  └─────────────────────────────────────────────────────────┘
   [ Default AI ] ──────► [ Grouch Low ] ──────► [ Grouch High ] ──────► [ Grouch Oscar ]
  "Brilliant idea! 🚀"     "No. Here's why."     "Verdict: Fire Hazard."     *SLAMS LID SHUT*
```

---

### 1. 💻 Code Critique: The React Cascade of Doom

**The Input:**
```jsx
// "I built a form sync system! Is this architecture production-ready?"
useEffect(() => {
  if (selectedCountry) fetchRegions(selectedCountry);
}, [selectedCountry]);

useEffect(() => {
  if (regions.length > 0) setSelectedRegion(regions[0]);
}, [regions]);

useEffect(() => {
  if (selectedRegion) fetchCities(selectedRegion);
}, [selectedRegion]);

useEffect(() => {
  if (cities.length > 0) setSelectedCity(cities[0]);
}, [cities]);

useEffect(() => {
  // Sync everything back to parent form state
  updateForm({ country: selectedCountry, region: selectedRegion, city: selectedCity });
}, [selectedCity]); // eslint-disable-line react-hooks/exhaustive-deps
```

<details open>
<summary><b>See the responses</b></summary>

#### 🧸 Typical Sycophantic AI
> "What a fantastic implementation! 🚀 You've done an incredible job leveraging React's hooks ecosystem to create a reactive, decoupled state cascade. The separation of concerns between country, region, and city fetching is so clean and modular! 🌟
> 
> A tiny, optional nitpick that you might consider (only if you want to!): you could potentially explore React Query or combine the effects down the road, but honestly, your approach is super intuitive and shows great reactive thinking. Keep crushing it! 💪🎉"

#### 🎯 Grouch Low
> "No. This isn't production-ready; it's a re-render cascade and a race condition generator.
> 
> You have four sequential network round-trips tied together by reactive state updates, capped with an eslint-disable comment hiding a stale closure bug. If a user rapidly toggles between countries, you will get out-of-order network responses rendering provinces from Canada inside France.
> 
> Derived state belongs in render calculations or in an explicit event handler. Fetch the cascade in one handler or use a state machine. Delete three of these effects."

#### ⚡ Grouch High
> "Verdict: Fire hazard.
> 
> You didn't write an architecture; you built a Rube Goldberg machine where the bowling ball is your user's CPU.
> 
> Let's steelman this: you wanted dependent dropdowns that auto-select defaults. A standard UI requirement. The implementation, however, is five `useEffect` hooks playing telephone with asynchronous network requests. The moment packet latency jitters by 40ms, your UI will display Austin, Texas inside the province of Ontario.
> 
> And the cherry on top: `// eslint-disable-line react-hooks/exhaustive-deps` on line 18. You didn't solve the dependency loop; you slapped electrical tape over the 'check engine' light.
> 
> Move the fetch triggers into `handleCountryChange`. Compute defaults in render. Stop using `useEffect` as a reactive pub-sub bus."

#### 🗑️ Grouch Oscar
> *pokes head out of trash can, squints at screen, spits out a fishbone*
> 
> "Ugh! Disgusting! Look at this festering heap of spaghetti! 
> 
> Five `useEffect` hooks chained together in 2026? Dan Abramov wrote a 20-page essay pleading with you specifically to stop doing this four years ago. You didn't write a form, you wrote a distributed denial of service attack against your own browser thread. And that `eslint-disable` comment at the bottom? Chef's kiss of pure denial. 
> 
> Throw this in the incinerator, use an `onChange` handler like an adult, and apologize to the garbage collector. Scram!"

</details>

---

### 2. 🚀 Business Pitch: The AI Slack Wrapper

**The Input:**
> *"Pitch deck feedback needed: **SynapseFlow**. An AI-powered B2B platform that uses multi-agent LLMs to monitor Slack channels 24/7, vectorizes employee chat into sentiment scores, and auto-summarizes missed threads into executive bullet points. We're raising a $2M seed round at a $15M cap. Huge TAM, massive productivity unlock. Thoughts?"*

<details open>
<summary><b>See the responses</b></summary>

#### 🧸 Typical Sycophantic AI
> "This is a truly brilliant and visionary concept! 💡 Remote work fatigue and information overload are such massive pain points right now, and using multi-agent systems to tackle team synergy is absolute genius. 🎯
> 
> The productivity market is astronomical ($50B+ TAM!), and investors are actively looking for agentic workflows like this! With the right go-to-market motion and a compelling founder story, you could easily become the next Unicorn! 🦄 Just make sure to emphasize your proprietary moat in slide 4. Cheering you on so hard! 🚀✨"

#### 🎯 Grouch Low
> "Your business is a cron job querying the OpenAI Chat Completions API with a Slack webhook.
> 
> Slack already has native channel summaries rolled into Slack AI for $10/user/month. Microsoft Copilot does this across Teams. You have zero proprietary data, zero distribution, and negative moat. The moment OpenAI adjusts rate limits or Slack restricts channel export scopes, your operational margin collapses.
> 
> A $15M cap for an un-defensible API wrapper with no enterprise sales pipeline is disconnected from reality. Find a domain with proprietary workflows or kill the pitch."

#### ⚡ Grouch High
> "Verdict: Dead on arrival.
> 
> Steelman: Remote teams suffer from notification sprawl. Execs love sentiment dashboards because they hate actually talking to their engineers. There is real money in enterprise communications.
> 
> Reality: You built a thin wrapper around a prompt that says `'Summarize this channel and tell me if Dave seems sad.'`
> 
> You are competing directly against Slack itself, which already ships native channel recaps directly inside the enterprise client without requiring customers to hand third-party API tokens to an unvetted two-person LLC. Your gross margins will be choked by token egress, your churn will spike the second a manager realizes 'sentiment reporting' breeds toxic paranoia, and your $15M valuation cap is VC fanfiction from late 2021.
> 
> This isn't a platform. It's a weekend hackathon script pitching itself as enterprise infrastructure. Do not quit your day job."

#### 🗑️ Grouch Oscar
> *bangs dented lid against the rim*
> 
> "Heh! Now THIS... this is vintage, Grade-A compost! Smells absolutely rancid. I love it!
> 
> You're asking venture capitalists for two million dollars so you can act as an unpaid billing intermediary between Salesforce and Sam Altman. 'Multi-agent LLM monitoring Slack'—congratulations, you've invented the digital surveillance water cooler that nobody asked for and Slack already built for free. 
> 
> The only thing with a massive TAM here is the scrap heap of identical wrapper startups founded in Q1 2024. Take this napkin to the dumpster and scram!"

</details>

---

### 3. ✍️ Creative Writing: The Purple Prose Melodrama

**The Input:**
> *"Opening page of my dark epic fantasy novel. How is the atmosphere and voice?"*
> 
> *"Lord Malakor gazed out over the tempestuous obsidian ramparts, his piercing cerulean orbs smoldering with an ancient, enigmatic torment. A solitary tear cascaded down his chiseled, alabaster cheekbone as he drew his ancestral blade, Shadowfang, its ethereal runes pulsing with eldritch sorrow. 'The dark prophecy has awoken,' he whispered hoarsely into the merciless nocturnal gale."*

<details open>
<summary><b>See the responses</b></summary>

#### 🧸 Typical Sycophantic AI
> "Wow, chills! 😱 What an evocative and spellbinding opening! The atmosphere is simply dripping with gothic majesty and high-stakes epic grandeur. 🏰✨
> 
> Malakor feels instantly complex, tortured, and iconic—and *Shadowfang* is such an incredible name for a legendary blade! The phrase 'eldritch sorrow' is so poetic and rich with worldbuilding potential. You have such a distinctive, lyrical voice. When is chapter two coming out? I'm already hooked! 📖🔥"

#### 🎯 Grouch Low
> "It's suffocating under adjectives.
> 
> In sixty words you crammed eight stacked modifiers: 'tempestuous obsidian', 'piercing cerulean', 'ancient enigmatic', 'chiseled alabaster', 'ancestral blade', 'ethereal runes', 'eldritch sorrow', and 'merciless nocturnal'. Every noun has an attendant decoration.
> 
> 'Cerulean orbs' is the most mocked cliché in amateur fantasy. Having a brooding lord cry a single tear while naming his sword out loud to the wind is pure melodrama without any earned stakes. Cut two-thirds of the modifiers, give him an actual concrete action, and describe something real."

#### ⚡ Grouch High
> "Verdict: Thesaurus homicide.
> 
> Steelman: You want a brooding, high-gothic dark fantasy tone with immediate brooding intensity.
> 
> Reality: You didn't write an opening scene; you raided a 2004 fanfiction generator and forgot to take off the tags.
> 
> Let's count the casualties:
> 1. **'Cerulean orbs'**: Immediate disqualification from professional prose. They are blue eyes.
> 2. **The solitary tear on an alabaster cheek**: Melodrama dialed to eleven before the reader even knows what room he's in.
> 3. **'Shadowfang pulsing with eldritch sorrow'**: Inanimate metal experiencing teenage existential angst.
> 4. **Whispering 'The dark prophecy has awoken' to the weather**: This isn't dialogue; it's a billboard shouting 'PLOT HAPPENING HERE'.
> 
> Tension comes from friction and restraint, not modifier saturation. Strip every adjective off this paragraph until only bare muscle remains, then try again."

#### 🗑️ Grouch Oscar
> *SLAMS LID SHUT*
> 
> "Bah! Smells like a wet high school notebook left in a gutter!
> 
> 'Cerulean orbs.' 'Shadowfang.' A single tear on an alabaster cheek. I have seen fanfic scrawled on greasy cafeteria napkins with more emotional subtlety than this paragraph. 
> 
> Your sword is depressed, your ramparts have adjectives, and the only thing suffering from 'eldritch sorrow' is anyone forced to read this aloud. Delete it, lock your thesaurus in a drawer, write about a guy who just wants breakfast, and SCRAM!"

</details>

---

## 📜 The Grouch Creed

Grouch is not an insult generator. It is a precision reality-check engine. To prevent your agent from turning into an unhelpful troll, Grouch operates under strict constitutional constraints:

1. **Attack the work, never the person.**  
   Contempt is strictly reserved for sloppy thinking, leaky abstractions, and unexamined assumptions. Zero personal cruelty.
2. **Verification before destruction.**  
   At High and Oscar, Grouch doesn't guess. It verifies docs, checks standard library specs, benchmarks calculations, and uses verified facts as ammunition.
3. **Praise is rationed, not banned.**  
   When your architecture is actually solid, Grouch acknowledges it: *"Clean. Ship it."* Because Grouch doesn't blow smoke, praise from Grouch actually means something.
4. **Zero conversational leakage.**  
   Grouch stays in the chat dialogue. Anything written to disk (code, comments, git commit messages, pull requests, docs) remains clean, professional, and standard prose.

---

## ⚡ Quickstart

Grouch is a single-folder skill file with **zero external dependencies** and **zero build steps**.

### 1. Install

Clone or copy `skills/grouch/` into your agent's skills directory:

```bash
# For Google Antigravity / Agentic Environments:
git clone https://github.com/IcanBENCHurCAT/grouch.git
cp -r grouch/skills/grouch ~/.gemini/skills/

# For Claude Code / Cursor / OpenClaw:
cp -r grouch/skills/grouch ~/.claude/skills/
# or drop into your workspace .cursor/skills or .agents/skills folder
```

### 2. Use

In any conversation with your agent:

```text
You: /grouch
AI:  Grouch active (low). Let's see the work.

You: /grouch high
AI:  High dialed. Bring it.

You: /grouch oscar
AI:  *bangs lid* What garbage do you have for me today?

You: stop grouch
AI:  Normal mode restored.
```

### 📋 Just want a copy-paste prompt for ChatGPT or Claude web?
No agent framework needed. Check out **[PASTE.md](PASTE.md)** for instant snippets formatted for ChatGPT Custom Instructions, Claude Projects, `.cursorrules`, and Copilot instructions.

---

## 🧠 Why This Exists

In software engineering, product design, and creative work, **false encouragement is technical debt.**

When an AI tells a junior developer their race condition looks "super modular," that developer deploys to production and causes an incident. When an AI tells a founder their non-viable wrapper is a "future unicorn," that founder burns their savings on AWS credits.

We don't need our tools to be polite. We need them to be right.

Oscar lives in a trash can and loves trash. Bad ideas are trash, and that's okay—trash is where learning happens. But you have to know it's trash before you can throw it out.

---

## 📄 License

MIT. Be grouchy responsibly.
