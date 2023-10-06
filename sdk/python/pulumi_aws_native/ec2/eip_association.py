# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EipAssociationArgs', 'EipAssociation']

@pulumi.input_type
class EipAssociationArgs:
    def __init__(__self__, *,
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 eip: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EipAssociation resource.
        :param pulumi.Input[str] allocation_id: The allocation ID. This is required for EC2-VPC.
        :param pulumi.Input[str] eip: The Elastic IP address to associate with the instance.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] network_interface_id: The ID of the network interface.
        :param pulumi.Input[str] private_ip_address: The primary or secondary private IP address to associate with the Elastic IP address.
        """
        EipAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allocation_id=allocation_id,
            eip=eip,
            instance_id=instance_id,
            network_interface_id=network_interface_id,
            private_ip_address=private_ip_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allocation_id: Optional[pulumi.Input[str]] = None,
             eip: Optional[pulumi.Input[str]] = None,
             instance_id: Optional[pulumi.Input[str]] = None,
             network_interface_id: Optional[pulumi.Input[str]] = None,
             private_ip_address: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if allocation_id is not None:
            _setter("allocation_id", allocation_id)
        if eip is not None:
            _setter("eip", eip)
        if instance_id is not None:
            _setter("instance_id", instance_id)
        if network_interface_id is not None:
            _setter("network_interface_id", network_interface_id)
        if private_ip_address is not None:
            _setter("private_ip_address", private_ip_address)

    @property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[str]]:
        """
        The allocation ID. This is required for EC2-VPC.
        """
        return pulumi.get(self, "allocation_id")

    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocation_id", value)

    @property
    @pulumi.getter
    def eip(self) -> Optional[pulumi.Input[str]]:
        """
        The Elastic IP address to associate with the instance.
        """
        return pulumi.get(self, "eip")

    @eip.setter
    def eip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eip", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the network interface.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The primary or secondary private IP address to associate with the Elastic IP address.
        """
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)


class EipAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 eip: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for EC2 EIP association.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocation_id: The allocation ID. This is required for EC2-VPC.
        :param pulumi.Input[str] eip: The Elastic IP address to associate with the instance.
        :param pulumi.Input[str] instance_id: The ID of the instance.
        :param pulumi.Input[str] network_interface_id: The ID of the network interface.
        :param pulumi.Input[str] private_ip_address: The primary or secondary private IP address to associate with the Elastic IP address.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[EipAssociationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for EC2 EIP association.

        :param str resource_name: The name of the resource.
        :param EipAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EipAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EipAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_id: Optional[pulumi.Input[str]] = None,
                 eip: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EipAssociationArgs.__new__(EipAssociationArgs)

            __props__.__dict__["allocation_id"] = allocation_id
            __props__.__dict__["eip"] = eip
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["network_interface_id"] = network_interface_id
            __props__.__dict__["private_ip_address"] = private_ip_address
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["allocation_id", "eip", "instance_id", "network_interface_id", "private_ip_address"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(EipAssociation, __self__).__init__(
            'aws-native:ec2:EipAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EipAssociation':
        """
        Get an existing EipAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EipAssociationArgs.__new__(EipAssociationArgs)

        __props__.__dict__["allocation_id"] = None
        __props__.__dict__["eip"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["network_interface_id"] = None
        __props__.__dict__["private_ip_address"] = None
        return EipAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[Optional[str]]:
        """
        The allocation ID. This is required for EC2-VPC.
        """
        return pulumi.get(self, "allocation_id")

    @property
    @pulumi.getter
    def eip(self) -> pulumi.Output[Optional[str]]:
        """
        The Elastic IP address to associate with the instance.
        """
        return pulumi.get(self, "eip")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the network interface.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> pulumi.Output[Optional[str]]:
        """
        The primary or secondary private IP address to associate with the Elastic IP address.
        """
        return pulumi.get(self, "private_ip_address")

