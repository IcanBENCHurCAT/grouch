#!/usr/bin/env node
// Installs the grouch skill into an agent skills directory.
//   npx grouch-skill              -> ~/.claude/skills/grouch (user level)
//   npx grouch-skill --project    -> ./.claude/skills/grouch (current project)
//   npx grouch-skill --dir <path> -> <path>/grouch
// Zero dependencies. Re-running overwrites with the latest copy.

const fs = require("fs");
const os = require("os");
const path = require("path");

function usage() {
  console.log("Usage: npx grouch-skill [--project] [--dir <path>]");
  process.exit(1);
}

const args = process.argv.slice(2);
let destBase;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--project") {
    destBase = path.join(process.cwd(), ".claude", "skills");
  } else if (args[i] === "--dir") {
    const p = args[++i];
    if (!p) usage();
    destBase = p;
  } else {
    usage();
  }
}
if (!destBase) destBase = path.join(os.homedir(), ".claude", "skills");

const src = path.join(__dirname, "..", "skills", "grouch");
const dest = path.join(destBase, "grouch");

if (!fs.existsSync(path.join(src, "SKILL.md"))) {
  console.error("grouch-skill: skill files not found in package (" + src + ")");
  process.exit(1);
}

fs.mkdirSync(destBase, { recursive: true });
fs.cpSync(src, dest, { recursive: true });

console.log("grouch installed -> " + dest);
console.log('Trigger it with "grouch mode", "/grouch", "/grouch high", or "/grouch oscar". Say "stop grouch" to revert.');
