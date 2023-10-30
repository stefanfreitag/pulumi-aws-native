# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetModuleVersionResult',
    'AwaitableGetModuleVersionResult',
    'get_module_version',
    'get_module_version_output',
]

@pulumi.output_type
class GetModuleVersionResult:
    def __init__(__self__, arn=None, description=None, documentation_url=None, is_default_version=None, schema=None, time_created=None, version_id=None, visibility=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if documentation_url and not isinstance(documentation_url, str):
            raise TypeError("Expected argument 'documentation_url' to be a str")
        pulumi.set(__self__, "documentation_url", documentation_url)
        if is_default_version and not isinstance(is_default_version, bool):
            raise TypeError("Expected argument 'is_default_version' to be a bool")
        pulumi.set(__self__, "is_default_version", is_default_version)
        if schema and not isinstance(schema, str):
            raise TypeError("Expected argument 'schema' to be a str")
        pulumi.set(__self__, "schema", schema)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        pulumi.set(__self__, "version_id", version_id)
        if visibility and not isinstance(visibility, str):
            raise TypeError("Expected argument 'visibility' to be a str")
        pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the module.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the registered module.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentationUrl")
    def documentation_url(self) -> Optional[str]:
        """
        The URL of a page providing detailed documentation for this module.
        """
        return pulumi.get(self, "documentation_url")

    @property
    @pulumi.getter(name="isDefaultVersion")
    def is_default_version(self) -> Optional[bool]:
        """
        Indicator of whether this module version is the current default version
        """
        return pulumi.get(self, "is_default_version")

    @property
    @pulumi.getter
    def schema(self) -> Optional[str]:
        """
        The schema defining input parameters to and resources generated by the module.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[str]:
        """
        The time that the specified module version was registered.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> Optional[str]:
        """
        The version ID of the module represented by this module instance.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter
    def visibility(self) -> Optional['ModuleVersionVisibility']:
        """
        The scope at which the type is visible and usable in CloudFormation operations.

        The only allowed value at present is:

        PRIVATE: The type is only visible and usable within the account in which it is registered. Currently, AWS CloudFormation marks any types you register as PRIVATE.
        """
        return pulumi.get(self, "visibility")


class AwaitableGetModuleVersionResult(GetModuleVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetModuleVersionResult(
            arn=self.arn,
            description=self.description,
            documentation_url=self.documentation_url,
            is_default_version=self.is_default_version,
            schema=self.schema,
            time_created=self.time_created,
            version_id=self.version_id,
            visibility=self.visibility)


def get_module_version(arn: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetModuleVersionResult:
    """
    A module that has been registered in the CloudFormation registry.


    :param str arn: The Amazon Resource Name (ARN) of the module.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudformation:getModuleVersion', __args__, opts=opts, typ=GetModuleVersionResult).value

    return AwaitableGetModuleVersionResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        documentation_url=pulumi.get(__ret__, 'documentation_url'),
        is_default_version=pulumi.get(__ret__, 'is_default_version'),
        schema=pulumi.get(__ret__, 'schema'),
        time_created=pulumi.get(__ret__, 'time_created'),
        version_id=pulumi.get(__ret__, 'version_id'),
        visibility=pulumi.get(__ret__, 'visibility'))


@_utilities.lift_output_func(get_module_version)
def get_module_version_output(arn: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetModuleVersionResult]:
    """
    A module that has been registered in the CloudFormation registry.


    :param str arn: The Amazon Resource Name (ARN) of the module.
    """
    ...
