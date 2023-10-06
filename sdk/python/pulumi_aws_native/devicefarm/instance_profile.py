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
from ._inputs import *

__all__ = ['InstanceProfileArgs', 'InstanceProfile']

@pulumi.input_type
class InstanceProfileArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 exclude_app_packages_from_cleanup: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 package_cleanup: Optional[pulumi.Input[bool]] = None,
                 reboot_after_use: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]] = None):
        """
        The set of arguments for constructing a InstanceProfile resource.
        """
        InstanceProfileArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            exclude_app_packages_from_cleanup=exclude_app_packages_from_cleanup,
            name=name,
            package_cleanup=package_cleanup,
            reboot_after_use=reboot_after_use,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             exclude_app_packages_from_cleanup: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             package_cleanup: Optional[pulumi.Input[bool]] = None,
             reboot_after_use: Optional[pulumi.Input[bool]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if description is not None:
            _setter("description", description)
        if exclude_app_packages_from_cleanup is not None:
            _setter("exclude_app_packages_from_cleanup", exclude_app_packages_from_cleanup)
        if name is not None:
            _setter("name", name)
        if package_cleanup is not None:
            _setter("package_cleanup", package_cleanup)
        if reboot_after_use is not None:
            _setter("reboot_after_use", reboot_after_use)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="excludeAppPackagesFromCleanup")
    def exclude_app_packages_from_cleanup(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "exclude_app_packages_from_cleanup")

    @exclude_app_packages_from_cleanup.setter
    def exclude_app_packages_from_cleanup(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "exclude_app_packages_from_cleanup", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="packageCleanup")
    def package_cleanup(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "package_cleanup")

    @package_cleanup.setter
    def package_cleanup(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "package_cleanup", value)

    @property
    @pulumi.getter(name="rebootAfterUse")
    def reboot_after_use(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "reboot_after_use")

    @reboot_after_use.setter
    def reboot_after_use(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reboot_after_use", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceProfileTagArgs']]]]):
        pulumi.set(self, "tags", value)


class InstanceProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclude_app_packages_from_cleanup: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 package_cleanup: Optional[pulumi.Input[bool]] = None,
                 reboot_after_use: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceProfileTagArgs']]]]] = None,
                 __props__=None):
        """
        AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InstanceProfileArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile

        :param str resource_name: The name of the resource.
        :param InstanceProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            InstanceProfileArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 exclude_app_packages_from_cleanup: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 package_cleanup: Optional[pulumi.Input[bool]] = None,
                 reboot_after_use: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InstanceProfileTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceProfileArgs.__new__(InstanceProfileArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["exclude_app_packages_from_cleanup"] = exclude_app_packages_from_cleanup
            __props__.__dict__["name"] = name
            __props__.__dict__["package_cleanup"] = package_cleanup
            __props__.__dict__["reboot_after_use"] = reboot_after_use
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(InstanceProfile, __self__).__init__(
            'aws-native:devicefarm:InstanceProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InstanceProfile':
        """
        Get an existing InstanceProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InstanceProfileArgs.__new__(InstanceProfileArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["exclude_app_packages_from_cleanup"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["package_cleanup"] = None
        __props__.__dict__["reboot_after_use"] = None
        __props__.__dict__["tags"] = None
        return InstanceProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="excludeAppPackagesFromCleanup")
    def exclude_app_packages_from_cleanup(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "exclude_app_packages_from_cleanup")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageCleanup")
    def package_cleanup(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "package_cleanup")

    @property
    @pulumi.getter(name="rebootAfterUse")
    def reboot_after_use(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "reboot_after_use")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.InstanceProfileTag']]]:
        return pulumi.get(self, "tags")

