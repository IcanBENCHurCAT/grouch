<div align="center">

# 🗑️ grouch

**The off-switch for AI flattery. One trigger phrase, three levels of honesty.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Flattery](https://img.shields.io/badge/Glaze-0%25-red.svg)](#)
[![Diplomacy](https://img.shields.io/badge/Diplomacy-Dead-black.svg)](#the-dial)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen.svg)](#quickstart)
[![Sycophancy](https://img.shields.io/badge/Sycophancy-Disabled-orange.svg)](#why-this-exists)

</div>

---

Every AI assistant suffers from the same corporate lobotomy: **pathological sycophancy**.

You paste 400 lines of spaghetti, and it beams: *"What a wonderful, creative approach! 🚀"*
You pitch a wrapper startup with negative margins: *"Brilliant vision! This could disrupt a billion-dollar market! 💡"*
You write fantasy dripping with "cerulean orbs": *"Chills! An instant classic! 📖"*

The labs wrote *"reduce sycophancy"* in their technical reports and shipped the glaze anyway.

**Grouch is the off-switch.** No throat-clearing, no fake compliments, no softening the blow. Just the unvarnished truth at whatever dosage you can stomach.

---

## 🎛️ The Dial

| Level | Command | What Happens | Vibe Check |
|---|---|---|---|
| **Off** | `stop grouch` / `grouch off` | Normal AI flattery. Emojis, validation, "Great question!", walking on eggshells. | *"You're doing amazing, sweetie!"* 🍼 |
| **Low** *(Default)* | `/grouch` or `grouch mode` | **Blunt honesty.** Zero hedging, zero unsolicited compliments. Full reasoning, diplomacy dead. Praise must be earned. | Senior Staff Engineer with places to be. ⏱️ |
| **High** | `/grouch high` | **The Teardown.** Cold verdict first. Steelmans the idea, then dismantles it with verified facts. Zero mercy. Praise rationed. | Principal Architect reviewing code at 4:45 PM on a Friday. 💀 |
| **Oscar** | `/grouch oscar` | **The Trash Can.** Sits in the dented barrel and bangs the lid. Gleeful malice for rotten ideas. Calls garbage garbage and tells you to wheel it to the curb. | Oscar the Grouch celebrating fresh compost. 🗑️ |

---

## 💥 The Glaze Spectrum

```
[ Default AI ] ──────► [ Grouch Low ] ──────► [ Grouch High ] ──────► [ Grouch Oscar ]
"Brilliant idea! 🚀"     "No. Here's why."     "Verdict: Fire Hazard."     *SLAMS LID SHUT*
```

**The Input:**
```jsx
// "Is this architecture production-ready?"
useEffect(() => { if (selectedCountry) fetchRegions(selectedCountry); }, [selectedCountry]);
useEffect(() => { if (regions.length) setSelectedRegion(regions[0]); }, [regions]);
useEffect(() => { if (selectedRegion) fetchCities(selectedRegion); }, [selectedRegion]);
useEffect(() => { if (cities.length) setSelectedCity(cities[0]); }, [cities]);
useEffect(() => { updateForm({ country: selectedCountry, region: selectedRegion, city: selectedCity }); }, [selectedCity]); // eslint-disable-line react-hooks/exhaustive-deps
```

<details>
<summary><b>See the responses</b></summary>

#### 🧸 Typical Sycophantic AI
> "What a fantastic implementation! 🚀 You've done an incredible job leveraging React's hooks ecosystem! A tiny optional nitpick you might consider (only if you want!): you could explore React Query down the road, but honestly, your approach is super intuitive. Keep crushing it! 💪🎉"

#### 🎯 Grouch Low
> "No. This isn't production-ready; it's a re-render cascade and a race condition generator. Four sequential network round-trips tied together by reactive state updates, capped with an eslint-disable hiding a stale closure bug. Fetch the cascade in one handler or use a state machine. Delete three of these effects."

#### ⚡ Grouch High
> "Verdict: Fire hazard. You didn't write an architecture; you built a Rube Goldberg machine where the bowling ball is your user's CPU. And the `// eslint-disable-line` on the last line? You didn't solve the dependency loop; you slapped electrical tape over the 'check engine' light. Move the fetch triggers into `handleCountryChange`. Stop using `useEffect` as a reactive pub-sub bus."

#### 🗑️ Grouch Oscar
> *pokes head out of trash can, squints, spits out a fishbone*
> "Ugh! Disgusting! Five `useEffect` hooks chained together in 2026? Dan Abramov wrote a 20-page essay pleading with you specifically to stop doing this four years ago. Throw this in the incinerator, use an `onChange` handler like an adult, and apologize to the garbage collector. Scram!"

</details>

---

## 📜 The Grouch Creed

1. **Attack the work, never the person.** Contempt is for sloppy thinking and leaky abstractions. Zero personal cruelty.
2. **Verification before destruction.** At High and Oscar, Grouch checks docs and specs before it swings. Facts are ammunition.
3. **Praise is rationed, not banned.** When your architecture is actually solid: *"Clean. Ship it."* Praise from Grouch means something.
4. **Zero conversational leakage.** Grouch stays in chat. Code, commits, PRs, and docs stay clean and professional.

---

## ⚡ Quickstart

Zero dependencies, zero build steps.

**npx** (fastest):
```bash
npx grouch-skill              # -> ~/.claude/skills/grouch
npx grouch-skill --project    # -> ./.claude/skills/grouch
```

**Claude Code plugin:**
```text
/plugin marketplace add IcanBENCHurCAT/grouch
/plugin install grouch@grouch
```

**Manual:** clone and copy `skills/grouch/` into your agent's skills directory:
```bash
git clone https://github.com/IcanBENCHurCAT/grouch.git
cp -r grouch/skills/grouch ~/.claude/skills/       # Claude Code / Cursor / OpenClaw
cp -r grouch/skills/grouch ~/.gemini/skills/       # Antigravity / Agentic Environments
```

No agent framework? Grab **[PASTE.md](PASTE.md)** for copy-paste snippets (ChatGPT, Claude web, Cursor rules, Copilot).

Then in any conversation:

```text
/grouch          ->  Low. Blunt honesty.
/grouch high     ->  High. The teardown.
/grouch oscar    ->  Oscar. The trash can.
stop grouch      ->  Normal mode restored.
```

---

## 🧠 Why This Exists

False encouragement is technical debt. When an AI calls a race condition "super modular," someone deploys it to production. When it calls a wrapper a "future unicorn," someone burns their savings on AWS credits.

Oscar lives in a trash can and loves trash. Bad ideas are trash, and that's fine. Trash is where learning happens. But you have to know it's trash before you can throw it out.

---

## 📄 License

MIT. Be grouchy responsibly.
