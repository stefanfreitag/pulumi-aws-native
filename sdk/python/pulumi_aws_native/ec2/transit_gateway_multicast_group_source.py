# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TransitGatewayMulticastGroupSourceArgs', 'TransitGatewayMulticastGroupSource']

@pulumi.input_type
class TransitGatewayMulticastGroupSourceArgs:
    def __init__(__self__, *,
                 group_ip_address: pulumi.Input[str],
                 network_interface_id: pulumi.Input[str],
                 transit_gateway_multicast_domain_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a TransitGatewayMulticastGroupSource resource.
        :param pulumi.Input[str] group_ip_address: The IP address assigned to the transit gateway multicast group.
        :param pulumi.Input[str] network_interface_id: The ID of the transit gateway attachment.
        :param pulumi.Input[str] transit_gateway_multicast_domain_id: The ID of the transit gateway multicast domain.
        """
        pulumi.set(__self__, "group_ip_address", group_ip_address)
        pulumi.set(__self__, "network_interface_id", network_interface_id)
        pulumi.set(__self__, "transit_gateway_multicast_domain_id", transit_gateway_multicast_domain_id)

    @property
    @pulumi.getter(name="groupIpAddress")
    def group_ip_address(self) -> pulumi.Input[str]:
        """
        The IP address assigned to the transit gateway multicast group.
        """
        return pulumi.get(self, "group_ip_address")

    @group_ip_address.setter
    def group_ip_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_ip_address", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Input[str]:
        """
        The ID of the transit gateway attachment.
        """
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="transitGatewayMulticastDomainId")
    def transit_gateway_multicast_domain_id(self) -> pulumi.Input[str]:
        """
        The ID of the transit gateway multicast domain.
        """
        return pulumi.get(self, "transit_gateway_multicast_domain_id")

    @transit_gateway_multicast_domain_id.setter
    def transit_gateway_multicast_domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transit_gateway_multicast_domain_id", value)


class TransitGatewayMulticastGroupSource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_ip_address: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_multicast_domain_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::EC2::TransitGatewayMulticastGroupSource registers and deregisters members and sources (network interfaces) with the transit gateway multicast group

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_ip_address: The IP address assigned to the transit gateway multicast group.
        :param pulumi.Input[str] network_interface_id: The ID of the transit gateway attachment.
        :param pulumi.Input[str] transit_gateway_multicast_domain_id: The ID of the transit gateway multicast domain.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransitGatewayMulticastGroupSourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::TransitGatewayMulticastGroupSource registers and deregisters members and sources (network interfaces) with the transit gateway multicast group

        :param str resource_name: The name of the resource.
        :param TransitGatewayMulticastGroupSourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransitGatewayMulticastGroupSourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_ip_address: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 transit_gateway_multicast_domain_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TransitGatewayMulticastGroupSourceArgs.__new__(TransitGatewayMulticastGroupSourceArgs)

            if group_ip_address is None and not opts.urn:
                raise TypeError("Missing required property 'group_ip_address'")
            __props__.__dict__["group_ip_address"] = group_ip_address
            if network_interface_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_interface_id'")
            __props__.__dict__["network_interface_id"] = network_interface_id
            if transit_gateway_multicast_domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'transit_gateway_multicast_domain_id'")
            __props__.__dict__["transit_gateway_multicast_domain_id"] = transit_gateway_multicast_domain_id
            __props__.__dict__["group_member"] = None
            __props__.__dict__["group_source"] = None
            __props__.__dict__["member_type"] = None
            __props__.__dict__["resource_id"] = None
            __props__.__dict__["resource_type"] = None
            __props__.__dict__["source_type"] = None
            __props__.__dict__["subnet_id"] = None
            __props__.__dict__["transit_gateway_attachment_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["group_ip_address", "network_interface_id", "transit_gateway_multicast_domain_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(TransitGatewayMulticastGroupSource, __self__).__init__(
            'aws-native:ec2:TransitGatewayMulticastGroupSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TransitGatewayMulticastGroupSource':
        """
        Get an existing TransitGatewayMulticastGroupSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TransitGatewayMulticastGroupSourceArgs.__new__(TransitGatewayMulticastGroupSourceArgs)

        __props__.__dict__["group_ip_address"] = None
        __props__.__dict__["group_member"] = None
        __props__.__dict__["group_source"] = None
        __props__.__dict__["member_type"] = None
        __props__.__dict__["network_interface_id"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["source_type"] = None
        __props__.__dict__["subnet_id"] = None
        __props__.__dict__["transit_gateway_attachment_id"] = None
        __props__.__dict__["transit_gateway_multicast_domain_id"] = None
        return TransitGatewayMulticastGroupSource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupIpAddress")
    def group_ip_address(self) -> pulumi.Output[str]:
        """
        The IP address assigned to the transit gateway multicast group.
        """
        return pulumi.get(self, "group_ip_address")

    @property
    @pulumi.getter(name="groupMember")
    def group_member(self) -> pulumi.Output[bool]:
        """
        Indicates that the resource is a transit gateway multicast group member.
        """
        return pulumi.get(self, "group_member")

    @property
    @pulumi.getter(name="groupSource")
    def group_source(self) -> pulumi.Output[bool]:
        """
        Indicates that the resource is a transit gateway multicast group member.
        """
        return pulumi.get(self, "group_source")

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> pulumi.Output[str]:
        """
        The member type (for example, static).
        """
        return pulumi.get(self, "member_type")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway attachment.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        The type of resource, for example a VPC attachment.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[str]:
        """
        The source type.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        """
        The ID of the subnet.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway attachment.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayMulticastDomainId")
    def transit_gateway_multicast_domain_id(self) -> pulumi.Output[str]:
        """
        The ID of the transit gateway multicast domain.
        """
        return pulumi.get(self, "transit_gateway_multicast_domain_id")

