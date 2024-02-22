# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['VpnGatewayArgs', 'VpnGateway']

@pulumi.input_type
class VpnGatewayArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 amazon_side_asn: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a VpnGateway resource.
        :param pulumi.Input[str] type: The type of VPN connection the virtual private gateway supports.
        :param pulumi.Input[int] amazon_side_asn: The private Autonomous System Number (ASN) for the Amazon side of a BGP session.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Any tags assigned to the virtual private gateway.
        """
        pulumi.set(__self__, "type", type)
        if amazon_side_asn is not None:
            pulumi.set(__self__, "amazon_side_asn", amazon_side_asn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of VPN connection the virtual private gateway supports.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> Optional[pulumi.Input[int]]:
        """
        The private Autonomous System Number (ASN) for the Amazon side of a BGP session.
        """
        return pulumi.get(self, "amazon_side_asn")

    @amazon_side_asn.setter
    def amazon_side_asn(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "amazon_side_asn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Any tags assigned to the virtual private gateway.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class VpnGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amazon_side_asn: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Schema for EC2 VPN Gateway

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] amazon_side_asn: The private Autonomous System Number (ASN) for the Amazon side of a BGP session.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Any tags assigned to the virtual private gateway.
        :param pulumi.Input[str] type: The type of VPN connection the virtual private gateway supports.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for EC2 VPN Gateway

        :param str resource_name: The name of the resource.
        :param VpnGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amazon_side_asn: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VpnGatewayArgs.__new__(VpnGatewayArgs)

            __props__.__dict__["amazon_side_asn"] = amazon_side_asn
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["vpn_gateway_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["amazon_side_asn", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VpnGateway, __self__).__init__(
            'aws-native:ec2:VpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpnGateway':
        """
        Get an existing VpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpnGatewayArgs.__new__(VpnGatewayArgs)

        __props__.__dict__["amazon_side_asn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vpn_gateway_id"] = None
        return VpnGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="amazonSideAsn")
    def amazon_side_asn(self) -> pulumi.Output[Optional[int]]:
        """
        The private Autonomous System Number (ASN) for the Amazon side of a BGP session.
        """
        return pulumi.get(self, "amazon_side_asn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Any tags assigned to the virtual private gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of VPN connection the virtual private gateway supports.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> pulumi.Output[str]:
        """
        VPN Gateway ID generated by service
        """
        return pulumi.get(self, "vpn_gateway_id")

