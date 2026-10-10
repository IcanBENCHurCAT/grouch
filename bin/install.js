#!/usr/bin/env node
// Installs the grouch skill into an agent skills directory.
//   npx grouch-skill              -> ~/.claude/skills/grouch (user level)
//   npx grouch-skill --project    -> ./.claude/skills/grouch (current project)
//   npx grouch-skill --dir <path> -> <path>/grouch
//   npx grouch-skill --uninstall [--project] [--dir <path>]
// Zero dependencies. Re-running overwrites with the latest copy.

const fs = require("fs");
const os = require("os");
const path = require("path");

function usage() {
  console.log("Usage: npx grouch-skill [--project] [--dir <path>]");
  console.log("       npx grouch-skill --uninstall [--project] [--dir <path>]");
  process.exit(1);
}

const args = process.argv.slice(2);
let destBase;
let uninstall = false;
for (let i = 0; i < args.length; i++) {
  if (args[i] === "--uninstall") {
    uninstall = true;
  } else if (args[i] === "--project") {
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

// Only ever touch the grouch subdirectory of the resolved skills dir.
const dest = path.resolve(destBase, "grouch");

if (uninstall) {
  if (fs.existsSync(dest)) {
    fs.rmSync(dest, { recursive: true });
    console.log("grouch removed from " + dest);
  } else {
    console.log("grouch is not installed at " + dest + " (nothing to remove)");
  }
  process.exit(0);
}

const src = path.join(__dirname, "..", "skills", "grouch");

if (!fs.existsSync(path.join(src, "SKILL.md"))) {
  console.error("grouch-skill: skill files not found in package (" + src + ")");
  process.exit(1);
}

fs.mkdirSync(destBase, { recursive: true });
fs.cpSync(src, dest, { recursive: true });

console.log("grouch installed -> " + dest);
console.log('Trigger it with "grouch mode", "/grouch", "/grouch high", or "/grouch oscar". Say "stop grouch" to revert.');
