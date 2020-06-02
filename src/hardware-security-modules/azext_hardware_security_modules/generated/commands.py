# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_hardware_security_modules.generated._client_factory import cf_dedicated_hsm
    hardwaresecuritymodules_dedicated_hsm = CliCommandType(
        operations_tmpl='azext_hardware_security_modules.vendored_sdks.hardwaresecuritymodules.operations._dedicated_hsm_'
        'operations#DedicatedHsmOperations.{}',
        client_factory=cf_dedicated_hsm)
    with self.command_group('dedicated-hsm', hardwaresecuritymodules_dedicated_hsm,
                            client_factory=cf_dedicated_hsm, is_experimental=True) as g:
        g.custom_command('list', 'hardwaresecuritymodules_dedicated_hsm_list')
        g.custom_show_command(
            'show', 'hardwaresecuritymodules_dedicated_hsm_show')
        g.custom_command(
            'create', 'hardwaresecuritymodules_dedicated_hsm_create', supports_no_wait=True)
        g.custom_command(
            'update', 'hardwaresecuritymodules_dedicated_hsm_update', supports_no_wait=True)
        g.custom_command('delete', 'hardwaresecuritymodules_dedicated_hsm_delete',
                         supports_no_wait=True, confirmation=True)
        g.wait_command('wait')