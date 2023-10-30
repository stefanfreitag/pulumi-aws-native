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
from ._inputs import *

__all__ = ['DeviceProfileArgs', 'DeviceProfile']

@pulumi.input_type
class DeviceProfileArgs:
    def __init__(__self__, *,
                 lo_ra_wan: Optional[pulumi.Input['DeviceProfileLoRaWanDeviceProfileArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceProfileTagArgs']]]] = None):
        """
        The set of arguments for constructing a DeviceProfile resource.
        :param pulumi.Input['DeviceProfileLoRaWanDeviceProfileArgs'] lo_ra_wan: LoRaWANDeviceProfile supports all LoRa specific attributes for service profile for CreateDeviceProfile operation
        :param pulumi.Input[str] name: Name of service profile
        :param pulumi.Input[Sequence[pulumi.Input['DeviceProfileTagArgs']]] tags: A list of key-value pairs that contain metadata for the device profile.
        """
        if lo_ra_wan is not None:
            pulumi.set(__self__, "lo_ra_wan", lo_ra_wan)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="loRaWan")
    def lo_ra_wan(self) -> Optional[pulumi.Input['DeviceProfileLoRaWanDeviceProfileArgs']]:
        """
        LoRaWANDeviceProfile supports all LoRa specific attributes for service profile for CreateDeviceProfile operation
        """
        return pulumi.get(self, "lo_ra_wan")

    @lo_ra_wan.setter
    def lo_ra_wan(self, value: Optional[pulumi.Input['DeviceProfileLoRaWanDeviceProfileArgs']]):
        pulumi.set(self, "lo_ra_wan", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of service profile
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeviceProfileTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the device profile.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceProfileTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DeviceProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['DeviceProfileLoRaWanDeviceProfileArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceProfileTagArgs']]]]] = None,
                 __props__=None):
        """
        Device Profile's resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DeviceProfileLoRaWanDeviceProfileArgs']] lo_ra_wan: LoRaWANDeviceProfile supports all LoRa specific attributes for service profile for CreateDeviceProfile operation
        :param pulumi.Input[str] name: Name of service profile
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceProfileTagArgs']]]] tags: A list of key-value pairs that contain metadata for the device profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DeviceProfileArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Device Profile's resource schema demonstrating some basic constructs and validation rules.

        :param str resource_name: The name of the resource.
        :param DeviceProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['DeviceProfileLoRaWanDeviceProfileArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceProfileTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceProfileArgs.__new__(DeviceProfileArgs)

            __props__.__dict__["lo_ra_wan"] = lo_ra_wan
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(DeviceProfile, __self__).__init__(
            'aws-native:iotwireless:DeviceProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeviceProfile':
        """
        Get an existing DeviceProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeviceProfileArgs.__new__(DeviceProfileArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["lo_ra_wan"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return DeviceProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Service profile Arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="loRaWan")
    def lo_ra_wan(self) -> pulumi.Output[Optional['outputs.DeviceProfileLoRaWanDeviceProfile']]:
        """
        LoRaWANDeviceProfile supports all LoRa specific attributes for service profile for CreateDeviceProfile operation
        """
        return pulumi.get(self, "lo_ra_wan")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of service profile
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DeviceProfileTag']]]:
        """
        A list of key-value pairs that contain metadata for the device profile.
        """
        return pulumi.get(self, "tags")

