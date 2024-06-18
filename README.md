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
[Gabriel](https://github.com/wrightgabriel0220) pointed me to Ansible, so I did the thing any
totally sane engineer would do: I created an Ansible playbook to set up my personal devices.
