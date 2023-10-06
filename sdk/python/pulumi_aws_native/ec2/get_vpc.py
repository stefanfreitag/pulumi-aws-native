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

__all__ = [
    'GetVpcResult',
    'AwaitableGetVpcResult',
    'get_vpc',
    'get_vpc_output',
]

@pulumi.output_type
class GetVpcResult:
    def __init__(__self__, cidr_block_associations=None, default_network_acl=None, default_security_group=None, enable_dns_hostnames=None, enable_dns_support=None, instance_tenancy=None, ipv6_cidr_blocks=None, tags=None, vpc_id=None):
        if cidr_block_associations and not isinstance(cidr_block_associations, list):
            raise TypeError("Expected argument 'cidr_block_associations' to be a list")
        pulumi.set(__self__, "cidr_block_associations", cidr_block_associations)
        if default_network_acl and not isinstance(default_network_acl, str):
            raise TypeError("Expected argument 'default_network_acl' to be a str")
        pulumi.set(__self__, "default_network_acl", default_network_acl)
        if default_security_group and not isinstance(default_security_group, str):
            raise TypeError("Expected argument 'default_security_group' to be a str")
        pulumi.set(__self__, "default_security_group", default_security_group)
        if enable_dns_hostnames and not isinstance(enable_dns_hostnames, bool):
            raise TypeError("Expected argument 'enable_dns_hostnames' to be a bool")
        pulumi.set(__self__, "enable_dns_hostnames", enable_dns_hostnames)
        if enable_dns_support and not isinstance(enable_dns_support, bool):
            raise TypeError("Expected argument 'enable_dns_support' to be a bool")
        pulumi.set(__self__, "enable_dns_support", enable_dns_support)
        if instance_tenancy and not isinstance(instance_tenancy, str):
            raise TypeError("Expected argument 'instance_tenancy' to be a str")
        pulumi.set(__self__, "instance_tenancy", instance_tenancy)
        if ipv6_cidr_blocks and not isinstance(ipv6_cidr_blocks, list):
            raise TypeError("Expected argument 'ipv6_cidr_blocks' to be a list")
        pulumi.set(__self__, "ipv6_cidr_blocks", ipv6_cidr_blocks)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="cidrBlockAssociations")
    def cidr_block_associations(self) -> Optional[Sequence[str]]:
        """
        A list of IPv4 CIDR block association IDs for the VPC.
        """
        return pulumi.get(self, "cidr_block_associations")

    @property
    @pulumi.getter(name="defaultNetworkAcl")
    def default_network_acl(self) -> Optional[str]:
        """
        The default network ACL ID that is associated with the VPC.
        """
        return pulumi.get(self, "default_network_acl")

    @property
    @pulumi.getter(name="defaultSecurityGroup")
    def default_security_group(self) -> Optional[str]:
        """
        The default security group ID that is associated with the VPC.
        """
        return pulumi.get(self, "default_security_group")

    @property
    @pulumi.getter(name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> Optional[bool]:
        """
        Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs.
        """
        return pulumi.get(self, "enable_dns_hostnames")

    @property
    @pulumi.getter(name="enableDnsSupport")
    def enable_dns_support(self) -> Optional[bool]:
        """
        Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default.
        """
        return pulumi.get(self, "enable_dns_support")

    @property
    @pulumi.getter(name="instanceTenancy")
    def instance_tenancy(self) -> Optional[str]:
        """
        The allowed tenancy of instances launched into the VPC.

        "default": An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.

        "dedicated": An instance launched into the VPC is a Dedicated Instance by default, unless you explicitly specify a tenancy of host during instance launch. You cannot specify a tenancy of default during instance launch.

        Updating InstanceTenancy requires no replacement only if you are updating its value from "dedicated" to "default". Updating InstanceTenancy from "default" to "dedicated" requires replacement.
        """
        return pulumi.get(self, "instance_tenancy")

    @property
    @pulumi.getter(name="ipv6CidrBlocks")
    def ipv6_cidr_blocks(self) -> Optional[Sequence[str]]:
        """
        A list of IPv6 CIDR blocks that are associated with the VPC.
        """
        return pulumi.get(self, "ipv6_cidr_blocks")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VpcTag']]:
        """
        The tags for the VPC.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        """
        The Id for the model.
        """
        return pulumi.get(self, "vpc_id")


class AwaitableGetVpcResult(GetVpcResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcResult(
            cidr_block_associations=self.cidr_block_associations,
            default_network_acl=self.default_network_acl,
            default_security_group=self.default_security_group,
            enable_dns_hostnames=self.enable_dns_hostnames,
            enable_dns_support=self.enable_dns_support,
            instance_tenancy=self.instance_tenancy,
            ipv6_cidr_blocks=self.ipv6_cidr_blocks,
            tags=self.tags,
            vpc_id=self.vpc_id)


def get_vpc(vpc_id: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcResult:
    """
    Resource Type definition for AWS::EC2::VPC


    :param str vpc_id: The Id for the model.
    """
    __args__ = dict()
    __args__['vpcId'] = vpc_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVpc', __args__, opts=opts, typ=GetVpcResult).value

    return AwaitableGetVpcResult(
        cidr_block_associations=pulumi.get(__ret__, 'cidr_block_associations'),
        default_network_acl=pulumi.get(__ret__, 'default_network_acl'),
        default_security_group=pulumi.get(__ret__, 'default_security_group'),
        enable_dns_hostnames=pulumi.get(__ret__, 'enable_dns_hostnames'),
        enable_dns_support=pulumi.get(__ret__, 'enable_dns_support'),
        instance_tenancy=pulumi.get(__ret__, 'instance_tenancy'),
        ipv6_cidr_blocks=pulumi.get(__ret__, 'ipv6_cidr_blocks'),
        tags=pulumi.get(__ret__, 'tags'),
        vpc_id=pulumi.get(__ret__, 'vpc_id'))


@_utilities.lift_output_func(get_vpc)
def get_vpc_output(vpc_id: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcResult]:
    """
    Resource Type definition for AWS::EC2::VPC


    :param str vpc_id: The Id for the model.
    """
    ...
