# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetWalWorkspaceResult',
    'AwaitableGetWalWorkspaceResult',
    'get_wal_workspace',
    'get_wal_workspace_output',
]

@pulumi.output_type
class GetWalWorkspaceResult:
    def __init__(__self__, tags=None):
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.WalWorkspaceTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetWalWorkspaceResult(GetWalWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWalWorkspaceResult(
            tags=self.tags)


def get_wal_workspace(wal_workspace_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWalWorkspaceResult:
    """
    Resource schema for AWS::EMR::WALWorkspace Type


    :param str wal_workspace_name: The name of the emrwal container
    """
    __args__ = dict()
    __args__['walWorkspaceName'] = wal_workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:emr:getWalWorkspace', __args__, opts=opts, typ=GetWalWorkspaceResult).value

    return AwaitableGetWalWorkspaceResult(
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_wal_workspace)
def get_wal_workspace_output(wal_workspace_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWalWorkspaceResult]:
    """
    Resource schema for AWS::EMR::WALWorkspace Type


    :param str wal_workspace_name: The name of the emrwal container
    """
    ...
