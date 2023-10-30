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

__all__ = ['DeviceArgs', 'Device']

@pulumi.input_type
class DeviceArgs:
    def __init__(__self__, *,
                 global_network_id: pulumi.Input[str],
                 aws_location: Optional[pulumi.Input['DeviceAwsLocationArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input['DeviceLocationArgs']] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceTagArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Device resource.
        :param pulumi.Input[str] global_network_id: The ID of the global network.
        :param pulumi.Input['DeviceAwsLocationArgs'] aws_location: The Amazon Web Services location of the device, if applicable.
        :param pulumi.Input[str] description: The description of the device.
        :param pulumi.Input['DeviceLocationArgs'] location: The site location.
        :param pulumi.Input[str] model: The device model
        :param pulumi.Input[str] serial_number: The device serial number.
        :param pulumi.Input[str] site_id: The site ID.
        :param pulumi.Input[Sequence[pulumi.Input['DeviceTagArgs']]] tags: The tags for the device.
        :param pulumi.Input[str] type: The device type.
        :param pulumi.Input[str] vendor: The device vendor.
        """
        pulumi.set(__self__, "global_network_id", global_network_id)
        if aws_location is not None:
            pulumi.set(__self__, "aws_location", aws_location)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if serial_number is not None:
            pulumi.set(__self__, "serial_number", serial_number)
        if site_id is not None:
            pulumi.set(__self__, "site_id", site_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vendor is not None:
            pulumi.set(__self__, "vendor", vendor)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[str]:
        """
        The ID of the global network.
        """
        return pulumi.get(self, "global_network_id")

    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "global_network_id", value)

    @property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> Optional[pulumi.Input['DeviceAwsLocationArgs']]:
        """
        The Amazon Web Services location of the device, if applicable.
        """
        return pulumi.get(self, "aws_location")

    @aws_location.setter
    def aws_location(self, value: Optional[pulumi.Input['DeviceAwsLocationArgs']]):
        pulumi.set(self, "aws_location", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the device.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input['DeviceLocationArgs']]:
        """
        The site location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input['DeviceLocationArgs']]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        The device model
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[str]]:
        """
        The device serial number.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[str]]:
        """
        The site ID.
        """
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DeviceTagArgs']]]]:
        """
        The tags for the device.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DeviceTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The device type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[str]]:
        """
        The device vendor.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vendor", value)


class Device(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_location: Optional[pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['DeviceLocationArgs']]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::NetworkManager::Device type describes a device.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']] aws_location: The Amazon Web Services location of the device, if applicable.
        :param pulumi.Input[str] description: The description of the device.
        :param pulumi.Input[str] global_network_id: The ID of the global network.
        :param pulumi.Input[pulumi.InputType['DeviceLocationArgs']] location: The site location.
        :param pulumi.Input[str] model: The device model
        :param pulumi.Input[str] serial_number: The device serial number.
        :param pulumi.Input[str] site_id: The site ID.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceTagArgs']]]] tags: The tags for the device.
        :param pulumi.Input[str] type: The device type.
        :param pulumi.Input[str] vendor: The device vendor.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::NetworkManager::Device type describes a device.

        :param str resource_name: The name of the resource.
        :param DeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_location: Optional[pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['DeviceLocationArgs']]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DeviceTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceArgs.__new__(DeviceArgs)

            __props__.__dict__["aws_location"] = aws_location
            __props__.__dict__["description"] = description
            if global_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'global_network_id'")
            __props__.__dict__["global_network_id"] = global_network_id
            __props__.__dict__["location"] = location
            __props__.__dict__["model"] = model
            __props__.__dict__["serial_number"] = serial_number
            __props__.__dict__["site_id"] = site_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["vendor"] = vendor
            __props__.__dict__["created_at"] = None
            __props__.__dict__["device_arn"] = None
            __props__.__dict__["device_id"] = None
            __props__.__dict__["state"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["global_network_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Device, __self__).__init__(
            'aws-native:networkmanager:Device',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Device':
        """
        Get an existing Device resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeviceArgs.__new__(DeviceArgs)

        __props__.__dict__["aws_location"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["device_arn"] = None
        __props__.__dict__["device_id"] = None
        __props__.__dict__["global_network_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["model"] = None
        __props__.__dict__["serial_number"] = None
        __props__.__dict__["site_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vendor"] = None
        return Device(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> pulumi.Output[Optional['outputs.DeviceAwsLocation']]:
        """
        The Amazon Web Services location of the device, if applicable.
        """
        return pulumi.get(self, "aws_location")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date and time that the device was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the device.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceArn")
    def device_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the device.
        """
        return pulumi.get(self, "device_arn")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[str]:
        """
        The ID of the device.
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[str]:
        """
        The ID of the global network.
        """
        return pulumi.get(self, "global_network_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional['outputs.DeviceLocation']]:
        """
        The site location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def model(self) -> pulumi.Output[Optional[str]]:
        """
        The device model
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[Optional[str]]:
        """
        The device serial number.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[str]]:
        """
        The site ID.
        """
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the device.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DeviceTag']]]:
        """
        The tags for the device.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The device type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[str]]:
        """
        The device vendor.
        """
        return pulumi.get(self, "vendor")

