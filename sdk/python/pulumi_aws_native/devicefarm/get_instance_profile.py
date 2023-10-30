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

__all__ = [
    'GetInstanceProfileResult',
    'AwaitableGetInstanceProfileResult',
    'get_instance_profile',
    'get_instance_profile_output',
]

@pulumi.output_type
class GetInstanceProfileResult:
    def __init__(__self__, arn=None, description=None, exclude_app_packages_from_cleanup=None, name=None, package_cleanup=None, reboot_after_use=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if exclude_app_packages_from_cleanup and not isinstance(exclude_app_packages_from_cleanup, list):
            raise TypeError("Expected argument 'exclude_app_packages_from_cleanup' to be a list")
        pulumi.set(__self__, "exclude_app_packages_from_cleanup", exclude_app_packages_from_cleanup)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_cleanup and not isinstance(package_cleanup, bool):
            raise TypeError("Expected argument 'package_cleanup' to be a bool")
        pulumi.set(__self__, "package_cleanup", package_cleanup)
        if reboot_after_use and not isinstance(reboot_after_use, bool):
            raise TypeError("Expected argument 'reboot_after_use' to be a bool")
        pulumi.set(__self__, "reboot_after_use", reboot_after_use)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="excludeAppPackagesFromCleanup")
    def exclude_app_packages_from_cleanup(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "exclude_app_packages_from_cleanup")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageCleanup")
    def package_cleanup(self) -> Optional[bool]:
        return pulumi.get(self, "package_cleanup")

    @property
    @pulumi.getter(name="rebootAfterUse")
    def reboot_after_use(self) -> Optional[bool]:
        return pulumi.get(self, "reboot_after_use")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.InstanceProfileTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetInstanceProfileResult(GetInstanceProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstanceProfileResult(
            arn=self.arn,
            description=self.description,
            exclude_app_packages_from_cleanup=self.exclude_app_packages_from_cleanup,
            name=self.name,
            package_cleanup=self.package_cleanup,
            reboot_after_use=self.reboot_after_use,
            tags=self.tags)


def get_instance_profile(arn: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstanceProfileResult:
    """
    AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:devicefarm:getInstanceProfile', __args__, opts=opts, typ=GetInstanceProfileResult).value

    return AwaitableGetInstanceProfileResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        exclude_app_packages_from_cleanup=pulumi.get(__ret__, 'exclude_app_packages_from_cleanup'),
        name=pulumi.get(__ret__, 'name'),
        package_cleanup=pulumi.get(__ret__, 'package_cleanup'),
        reboot_after_use=pulumi.get(__ret__, 'reboot_after_use'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_instance_profile)
def get_instance_profile_output(arn: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstanceProfileResult]:
    """
    AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile
    """
    ...
