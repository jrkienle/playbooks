#!/usr/bin/python

# Copyright: (c) 2024, James Kienle and Fenn Kienle Holdings LLC
# MIT License (see LICENSE or https://opensource.org/license/mit)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: install_package_manager

short_description: Installs preferred OS package manager for jrkienle/playbooks

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Installs Chocolaty on Windows and MacPorts on MacOS

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - James Kienle (@jrkienle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Install Package Manager
  local.jrkienle.install_package_manager
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
import platform


def run_module():
    module_args = dict()

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = {
        'changed': False,
        'command': [],
        'os': ''
    }

    os = platform.system()
    result['os'] = os;

    if module.check_mode:
        module.exit_json(**result)

    if os == 'Darwin':
        # I probably shouldn't trust this random script, but yolo amiright?
        command = [
          'sh', '-c',
          '"$(curl -fsSL https://gist.githubusercontent.com/dive/c4a51179aa96d229a32dd3492e5fdc2d/raw/install_macports.sh)"'
        ]
    else:
        module.fail_json({ 'msg': 'Unsupported Operating System: ' + os })

        foo = 1

    rc, out, err = module.run_command(command)
    if rc != 0:
        module.fail_json({ 'msg': 'MacPorts installation failed with exit code: ' + str(rc) })

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()