# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetConnectionAliasResult',
    'AwaitableGetConnectionAliasResult',
    'get_connection_alias',
    'get_connection_alias_output',
]

@pulumi.output_type
class GetConnectionAliasResult:
    def __init__(__self__, alias_id=None, associations=None, connection_alias_state=None):
        if alias_id and not isinstance(alias_id, str):
            raise TypeError("Expected argument 'alias_id' to be a str")
        pulumi.set(__self__, "alias_id", alias_id)
        if associations and not isinstance(associations, list):
            raise TypeError("Expected argument 'associations' to be a list")
        pulumi.set(__self__, "associations", associations)
        if connection_alias_state and not isinstance(connection_alias_state, str):
            raise TypeError("Expected argument 'connection_alias_state' to be a str")
        pulumi.set(__self__, "connection_alias_state", connection_alias_state)

    @property
    @pulumi.getter(name="aliasId")
    def alias_id(self) -> Optional[str]:
        return pulumi.get(self, "alias_id")

    @property
    @pulumi.getter
    def associations(self) -> Optional[Sequence['outputs.ConnectionAliasAssociation']]:
        return pulumi.get(self, "associations")

    @property
    @pulumi.getter(name="connectionAliasState")
    def connection_alias_state(self) -> Optional['ConnectionAliasState']:
        return pulumi.get(self, "connection_alias_state")


class AwaitableGetConnectionAliasResult(GetConnectionAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectionAliasResult(
            alias_id=self.alias_id,
            associations=self.associations,
            connection_alias_state=self.connection_alias_state)


def get_connection_alias(alias_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectionAliasResult:
    """
    Resource Type definition for AWS::WorkSpaces::ConnectionAlias
    """
    __args__ = dict()
    __args__['aliasId'] = alias_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:workspaces:getConnectionAlias', __args__, opts=opts, typ=GetConnectionAliasResult).value

    return AwaitableGetConnectionAliasResult(
        alias_id=pulumi.get(__ret__, 'alias_id'),
        associations=pulumi.get(__ret__, 'associations'),
        connection_alias_state=pulumi.get(__ret__, 'connection_alias_state'))


@_utilities.lift_output_func(get_connection_alias)
def get_connection_alias_output(alias_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectionAliasResult]:
    """
    Resource Type definition for AWS::WorkSpaces::ConnectionAlias
    """
    ...
