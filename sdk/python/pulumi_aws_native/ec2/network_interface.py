# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']

@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 group_set: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interface_type: Optional[pulumi.Input[str]] = None,
                 ipv6_address_count: Optional[pulumi.Input[int]] = None,
                 ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceInstanceIpv6AddressArgs']]]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfacePrivateIpAddressSpecificationArgs']]]] = None,
                 secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
                 source_dest_check: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTagArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkInterface resource.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if group_set is not None:
            pulumi.set(__self__, "group_set", group_set)
        if interface_type is not None:
            pulumi.set(__self__, "interface_type", interface_type)
        if ipv6_address_count is not None:
            pulumi.set(__self__, "ipv6_address_count", ipv6_address_count)
        if ipv6_addresses is not None:
            pulumi.set(__self__, "ipv6_addresses", ipv6_addresses)
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if private_ip_addresses is not None:
            pulumi.set(__self__, "private_ip_addresses", private_ip_addresses)
        if secondary_private_ip_address_count is not None:
            pulumi.set(__self__, "secondary_private_ip_address_count", secondary_private_ip_address_count)
        if source_dest_check is not None:
            pulumi.set(__self__, "source_dest_check", source_dest_check)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="groupSet")
    def group_set(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "group_set")

    @group_set.setter
    def group_set(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_set", value)

    @property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "interface_type")

    @interface_type.setter
    def interface_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_type", value)

    @property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "ipv6_address_count")

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ipv6_address_count", value)

    @property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceInstanceIpv6AddressArgs']]]]:
        return pulumi.get(self, "ipv6_addresses")

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceInstanceIpv6AddressArgs']]]]):
        pulumi.set(self, "ipv6_addresses", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfacePrivateIpAddressSpecificationArgs']]]]:
        return pulumi.get(self, "private_ip_addresses")

    @private_ip_addresses.setter
    def private_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfacePrivateIpAddressSpecificationArgs']]]]):
        pulumi.set(self, "private_ip_addresses", value)

    @property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "secondary_private_ip_address_count")

    @secondary_private_ip_address_count.setter
    def secondary_private_ip_address_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "secondary_private_ip_address_count", value)

    @property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "source_dest_check")

    @source_dest_check.setter
    def source_dest_check(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "source_dest_check", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NetworkInterfaceTagArgs']]]]):
        pulumi.set(self, "tags", value)


class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 group_set: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interface_type: Optional[pulumi.Input[str]] = None,
                 ipv6_address_count: Optional[pulumi.Input[int]] = None,
                 ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceInstanceIpv6AddressArgs']]]]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfacePrivateIpAddressSpecificationArgs']]]]] = None,
                 secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
                 source_dest_check: Optional[pulumi.Input[bool]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::NetworkInterface

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkInterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::NetworkInterface

        :param str resource_name: The name of the resource.
        :param NetworkInterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkInterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 group_set: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 interface_type: Optional[pulumi.Input[str]] = None,
                 ipv6_address_count: Optional[pulumi.Input[int]] = None,
                 ipv6_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceInstanceIpv6AddressArgs']]]]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 private_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfacePrivateIpAddressSpecificationArgs']]]]] = None,
                 secondary_private_ip_address_count: Optional[pulumi.Input[int]] = None,
                 source_dest_check: Optional[pulumi.Input[bool]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkInterfaceTagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["group_set"] = group_set
            __props__.__dict__["interface_type"] = interface_type
            __props__.__dict__["ipv6_address_count"] = ipv6_address_count
            __props__.__dict__["ipv6_addresses"] = ipv6_addresses
            __props__.__dict__["private_ip_address"] = private_ip_address
            __props__.__dict__["private_ip_addresses"] = private_ip_addresses
            __props__.__dict__["secondary_private_ip_address_count"] = secondary_private_ip_address_count
            __props__.__dict__["source_dest_check"] = source_dest_check
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["primary_private_ip_address"] = None
            __props__.__dict__["secondary_private_ip_addresses"] = None
        super(NetworkInterface, __self__).__init__(
            'aws-native:ec2:NetworkInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkInterface':
        """
        Get an existing NetworkInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkInterfaceArgs.__new__(NetworkInterfaceArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["group_set"] = None
        __props__.__dict__["interface_type"] = None
        __props__.__dict__["ipv6_address_count"] = None
        __props__.__dict__["ipv6_addresses"] = None
        __props__.__dict__["primary_private_ip_address"] = None
        __props__.__dict__["private_ip_address"] = None
        __props__.__dict__["private_ip_addresses"] = None
        __props__.__dict__["secondary_private_ip_address_count"] = None
        __props__.__dict__["secondary_private_ip_addresses"] = None
        __props__.__dict__["source_dest_check"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["tags"] = None
        return NetworkInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="groupSet")
    def group_set(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "group_set")

    @property
    @pulumi.getter(name="interfaceType")
    def interface_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "interface_type")

    @property
    @pulumi.getter(name="ipv6AddressCount")
    def ipv6_address_count(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "ipv6_address_count")

    @property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInterfaceInstanceIpv6Address']]]:
        return pulumi.get(self, "ipv6_addresses")

    @property
    @pulumi.getter(name="primaryPrivateIpAddress")
    def primary_private_ip_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "primary_private_ip_address")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="privateIpAddresses")
    def private_ip_addresses(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInterfacePrivateIpAddressSpecification']]]:
        return pulumi.get(self, "private_ip_addresses")

    @property
    @pulumi.getter(name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "secondary_private_ip_address_count")

    @property
    @pulumi.getter(name="secondaryPrivateIpAddresses")
    def secondary_private_ip_addresses(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "secondary_private_ip_addresses")

    @property
    @pulumi.getter(name="sourceDestCheck")
    def source_dest_check(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "source_dest_check")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkInterfaceTag']]]:
        return pulumi.get(self, "tags")

