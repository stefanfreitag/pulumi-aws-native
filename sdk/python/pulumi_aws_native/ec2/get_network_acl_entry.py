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
    'GetNetworkAclEntryResult',
    'AwaitableGetNetworkAclEntryResult',
    'get_network_acl_entry',
    'get_network_acl_entry_output',
]

@pulumi.output_type
class GetNetworkAclEntryResult:
    def __init__(__self__, cidr_block=None, icmp=None, id=None, ipv6_cidr_block=None, port_range=None, protocol=None, rule_action=None):
        if cidr_block and not isinstance(cidr_block, str):
            raise TypeError("Expected argument 'cidr_block' to be a str")
        pulumi.set(__self__, "cidr_block", cidr_block)
        if icmp and not isinstance(icmp, dict):
            raise TypeError("Expected argument 'icmp' to be a dict")
        pulumi.set(__self__, "icmp", icmp)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6_cidr_block and not isinstance(ipv6_cidr_block, str):
            raise TypeError("Expected argument 'ipv6_cidr_block' to be a str")
        pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        if port_range and not isinstance(port_range, dict):
            raise TypeError("Expected argument 'port_range' to be a dict")
        pulumi.set(__self__, "port_range", port_range)
        if protocol and not isinstance(protocol, int):
            raise TypeError("Expected argument 'protocol' to be a int")
        pulumi.set(__self__, "protocol", protocol)
        if rule_action and not isinstance(rule_action, str):
            raise TypeError("Expected argument 'rule_action' to be a str")
        pulumi.set(__self__, "rule_action", rule_action)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[str]:
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter
    def icmp(self) -> Optional['outputs.NetworkAclEntryIcmp']:
        return pulumi.get(self, "icmp")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[str]:
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional['outputs.NetworkAclEntryPortRange']:
        return pulumi.get(self, "port_range")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[int]:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[str]:
        return pulumi.get(self, "rule_action")


class AwaitableGetNetworkAclEntryResult(GetNetworkAclEntryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkAclEntryResult(
            cidr_block=self.cidr_block,
            icmp=self.icmp,
            id=self.id,
            ipv6_cidr_block=self.ipv6_cidr_block,
            port_range=self.port_range,
            protocol=self.protocol,
            rule_action=self.rule_action)


def get_network_acl_entry(id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkAclEntryResult:
    """
    Resource Type definition for AWS::EC2::NetworkAclEntry
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkAclEntry', __args__, opts=opts, typ=GetNetworkAclEntryResult).value

    return AwaitableGetNetworkAclEntryResult(
        cidr_block=pulumi.get(__ret__, 'cidr_block'),
        icmp=pulumi.get(__ret__, 'icmp'),
        id=pulumi.get(__ret__, 'id'),
        ipv6_cidr_block=pulumi.get(__ret__, 'ipv6_cidr_block'),
        port_range=pulumi.get(__ret__, 'port_range'),
        protocol=pulumi.get(__ret__, 'protocol'),
        rule_action=pulumi.get(__ret__, 'rule_action'))


@_utilities.lift_output_func(get_network_acl_entry)
def get_network_acl_entry_output(id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkAclEntryResult]:
    """
    Resource Type definition for AWS::EC2::NetworkAclEntry
    """
    ...
