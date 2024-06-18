# Playbooks

Machine Setup and Configuration via Ansible

## Introduction

I have a problem: I hate the amount of shit that builds up on my machines over time, and the longer
I use a machine, the more shit I seem to accumulate. A few examples:

1. I run an installer for a one-off tool that installs god knows what god knows where
2. Something I use creates a ton of temporary files and never deletes them (even when uninstalled)
3. I simply forget to remove things I don't need anymore

Besides the obvious things like high disk space usage and general slowdowns, I can admit that this
"problem" is only an issue because I'm a really weird dude who likes to know what's happening on
every one of my machines at any given time. The two obvious things above aren't real issues, as
storage is cheap and modern operating systems are super fast. Regardless, I still needed I way to
solve this problem if for nothing more than to prevent myself from going insane. The brilliant
solution I created to a problem that isn't real is: **wiping and reinstalling my system every 👏
single 👏 fucking 👏 year**.

This solution definitely solves my problem, but man, reinstalling every single one of my favorite
tools and tweaking my configuration to make sure it's juuuuuuuuust right gets super annoying when
one does it every year. Luckily for me, my good friend and former co-worker
[Gabe](https://github.com/wrightgabriel0220) pointed me to Ansible, so I did the thing any
totally sane engineer would do: I created an Ansible playbook to set up my personal devices.

## Are You Okay?

No 😊

## Setup

If you're still reading this that means one of two things:

1. You're me because you forgot how to run your own tools (hi future James!)
2. You're just as unhinged as I am and want to see how this whole thing works (hi there!)

Regardless of why you're here, welcome! In order to get started, there's a couple things we
need to take care of first. Luckily for us, all of these things are in a convenient setup script!

Each script has comments for every step that include complete breakdowns of what each step does and
why the step matters for the context of setting up this repo on a new machine. Right now only MacOS
is supported here, but I plan on adding support for Windows 11 (ew, I know), Fedora (a linux
distribution that Gabe introduced me to that I've been meaning to try), and Alpine (my preferred
lightweight linux distribution for use on servers in my HomeLab).

To get this thing set up, clone the repo and run one of following commands (depending on your OS):

```bash
# MacOS
./setup/macos.sh
```

```powershell
# Windows
.\setup\windows.bat
```

```bash
# Fedora
./setup/fedora.sh
```

```bash
# Alpine
./setup/alpine.sh
```

Wow, that was super easy! Don't you love not having to think about anything when setting up a
machine?
