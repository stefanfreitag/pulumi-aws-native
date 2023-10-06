# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetExtensionResult',
    'AwaitableGetExtensionResult',
    'get_extension',
    'get_extension_output',
]

@pulumi.output_type
class GetExtensionResult:
    def __init__(__self__, actions=None, arn=None, description=None, id=None, parameters=None, version_number=None):
        if actions and not isinstance(actions, dict):
            raise TypeError("Expected argument 'actions' to be a dict")
        pulumi.set(__self__, "actions", actions)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if version_number and not isinstance(version_number, int):
            raise TypeError("Expected argument 'version_number' to be a int")
        pulumi.set(__self__, "version_number", version_number)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Any]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the extension.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="versionNumber")
    def version_number(self) -> Optional[int]:
        return pulumi.get(self, "version_number")


class AwaitableGetExtensionResult(GetExtensionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtensionResult(
            actions=self.actions,
            arn=self.arn,
            description=self.description,
            id=self.id,
            parameters=self.parameters,
            version_number=self.version_number)


def get_extension(id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtensionResult:
    """
    Resource Type definition for AWS::AppConfig::Extension
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:appconfig:getExtension', __args__, opts=opts, typ=GetExtensionResult).value

    return AwaitableGetExtensionResult(
        actions=pulumi.get(__ret__, 'actions'),
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        parameters=pulumi.get(__ret__, 'parameters'),
        version_number=pulumi.get(__ret__, 'version_number'))


@_utilities.lift_output_func(get_extension)
def get_extension_output(id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExtensionResult]:
    """
    Resource Type definition for AWS::AppConfig::Extension
    """
    ...
