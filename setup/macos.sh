# This script installs all of the prerequisites for running Ansible on MacOS. This script has been
# tested exclusively on MacOS Sonoma 14.5, and I have no guarauntee that it works anywhere else.
# This script is laid out like so:
#
# 1. An echo letting you know what step is about to run
# 2. A comment explaining what the step does and why it's needed
# 3. The script to actually run the step
#
# With all that in mind, enjoy the sheer beauty of automatic setup!

echo "Installing Xcode Select (This may take awhile)"
# Xcode Select is a collection of CLI-based development tooling for MacOS and is actually a
# completely independent tool from Xcode itself. Xcode is Apple's official IDE for writing native
# MacOS software, iOS apps, etc. It incluides way more tools than we need for running simple Ansible
# playbooks. It's also like 40GB and requires an Apple developer account to use, which is annoying.
# Xcode Select includes far too many tools to list in this comment (roughly 1.2 GB iirc), but the
# tools it installs that we need to use Ansible are Python3 and Git. For a full list of everything
# Xcode Select installs, check out https://mac.install.guide/commandlinetools/8
xcode-select --install

echo "Installing Ansible with Pip3"
# Now for the fun part, installing Ansible! Ansible is unfortunately written in Python (booooo) so
# it has to be installed via Pip. I personally hate Pip with a passion, and I hate how it installs
# everything globally even more, but this is the only way that I know of to install Ansible, so
# that's what we're gonna do!
pip install ansible
