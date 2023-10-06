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
from ._enums import *
from ._inputs import *

__all__ = ['DevicePoolArgs', 'DevicePool']

@pulumi.input_type
class DevicePoolArgs:
    def __init__(__self__, *,
                 project_arn: pulumi.Input[str],
                 rules: pulumi.Input[Sequence[pulumi.Input['DevicePoolRuleArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 max_devices: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DevicePoolTagArgs']]]] = None):
        """
        The set of arguments for constructing a DevicePool resource.
        """
        DevicePoolArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            project_arn=project_arn,
            rules=rules,
            description=description,
            max_devices=max_devices,
            name=name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             project_arn: pulumi.Input[str],
             rules: pulumi.Input[Sequence[pulumi.Input['DevicePoolRuleArgs']]],
             description: Optional[pulumi.Input[str]] = None,
             max_devices: Optional[pulumi.Input[int]] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DevicePoolTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("project_arn", project_arn)
        _setter("rules", rules)
        if description is not None:
            _setter("description", description)
        if max_devices is not None:
            _setter("max_devices", max_devices)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project_arn")

    @project_arn.setter
    def project_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_arn", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['DevicePoolRuleArgs']]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['DevicePoolRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxDevices")
    def max_devices(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "max_devices")

    @max_devices.setter
    def max_devices(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_devices", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DevicePoolTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DevicePoolTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DevicePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_devices: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_arn: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DevicePoolRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DevicePoolTagArgs']]]]] = None,
                 __props__=None):
        """
        AWS::DeviceFarm::DevicePool creates a new Device Pool for a given DF Project

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DevicePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AWS::DeviceFarm::DevicePool creates a new Device Pool for a given DF Project

        :param str resource_name: The name of the resource.
        :param DevicePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DevicePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DevicePoolArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_devices: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_arn: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DevicePoolRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DevicePoolTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DevicePoolArgs.__new__(DevicePoolArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["max_devices"] = max_devices
            __props__.__dict__["name"] = name
            if project_arn is None and not opts.urn:
                raise TypeError("Missing required property 'project_arn'")
            __props__.__dict__["project_arn"] = project_arn
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DevicePool, __self__).__init__(
            'aws-native:devicefarm:DevicePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DevicePool':
        """
        Get an existing DevicePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DevicePoolArgs.__new__(DevicePoolArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["max_devices"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project_arn"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["tags"] = None
        return DevicePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="maxDevices")
    def max_devices(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "max_devices")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project_arn")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.DevicePoolRule']]:
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DevicePoolTag']]]:
        return pulumi.get(self, "tags")

