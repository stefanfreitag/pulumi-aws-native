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

__all__ = [
    'GetAcceleratorResult',
    'AwaitableGetAcceleratorResult',
    'get_accelerator',
    'get_accelerator_output',
]

@pulumi.output_type
class GetAcceleratorResult:
    def __init__(__self__, accelerator_arn=None, dns_name=None, dual_stack_dns_name=None, enabled=None, ip_address_type=None, ip_addresses=None, ipv4_addresses=None, ipv6_addresses=None, name=None, tags=None):
        if accelerator_arn and not isinstance(accelerator_arn, str):
            raise TypeError("Expected argument 'accelerator_arn' to be a str")
        pulumi.set(__self__, "accelerator_arn", accelerator_arn)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if dual_stack_dns_name and not isinstance(dual_stack_dns_name, str):
            raise TypeError("Expected argument 'dual_stack_dns_name' to be a str")
        pulumi.set(__self__, "dual_stack_dns_name", dual_stack_dns_name)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if ip_address_type and not isinstance(ip_address_type, str):
            raise TypeError("Expected argument 'ip_address_type' to be a str")
        pulumi.set(__self__, "ip_address_type", ip_address_type)
        if ip_addresses and not isinstance(ip_addresses, list):
            raise TypeError("Expected argument 'ip_addresses' to be a list")
        pulumi.set(__self__, "ip_addresses", ip_addresses)
        if ipv4_addresses and not isinstance(ipv4_addresses, list):
            raise TypeError("Expected argument 'ipv4_addresses' to be a list")
        pulumi.set(__self__, "ipv4_addresses", ipv4_addresses)
        if ipv6_addresses and not isinstance(ipv6_addresses, list):
            raise TypeError("Expected argument 'ipv6_addresses' to be a list")
        pulumi.set(__self__, "ipv6_addresses", ipv6_addresses)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[str]:
        """
        The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 addresses.
        """
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="dualStackDnsName")
    def dual_stack_dns_name(self) -> Optional[str]:
        """
        The Domain Name System (DNS) name that Global Accelerator creates that points to your accelerator's static IPv4 and IPv6 addresses.
        """
        return pulumi.get(self, "dual_stack_dns_name")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicates whether an accelerator is enabled. The value is true or false.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional['AcceleratorIpAddressType']:
        """
        IP Address type.
        """
        return pulumi.get(self, "ip_address_type")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> Optional[Sequence[str]]:
        """
        The IP addresses from BYOIP Prefix pool.
        """
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter(name="ipv4Addresses")
    def ipv4_addresses(self) -> Optional[Sequence[str]]:
        """
        The IPv4 addresses assigned to the accelerator.
        """
        return pulumi.get(self, "ipv4_addresses")

    @property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Optional[Sequence[str]]:
        """
        The IPv6 addresses assigned if the accelerator is dualstack
        """
        return pulumi.get(self, "ipv6_addresses")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of accelerator.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.AcceleratorTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetAcceleratorResult(GetAcceleratorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAcceleratorResult(
            accelerator_arn=self.accelerator_arn,
            dns_name=self.dns_name,
            dual_stack_dns_name=self.dual_stack_dns_name,
            enabled=self.enabled,
            ip_address_type=self.ip_address_type,
            ip_addresses=self.ip_addresses,
            ipv4_addresses=self.ipv4_addresses,
            ipv6_addresses=self.ipv6_addresses,
            name=self.name,
            tags=self.tags)


def get_accelerator(accelerator_arn: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAcceleratorResult:
    """
    Resource Type definition for AWS::GlobalAccelerator::Accelerator


    :param str accelerator_arn: The Amazon Resource Name (ARN) of the accelerator.
    """
    __args__ = dict()
    __args__['acceleratorArn'] = accelerator_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:globalaccelerator:getAccelerator', __args__, opts=opts, typ=GetAcceleratorResult).value

    return AwaitableGetAcceleratorResult(
        accelerator_arn=pulumi.get(__ret__, 'accelerator_arn'),
        dns_name=pulumi.get(__ret__, 'dns_name'),
        dual_stack_dns_name=pulumi.get(__ret__, 'dual_stack_dns_name'),
        enabled=pulumi.get(__ret__, 'enabled'),
        ip_address_type=pulumi.get(__ret__, 'ip_address_type'),
        ip_addresses=pulumi.get(__ret__, 'ip_addresses'),
        ipv4_addresses=pulumi.get(__ret__, 'ipv4_addresses'),
        ipv6_addresses=pulumi.get(__ret__, 'ipv6_addresses'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_accelerator)
def get_accelerator_output(accelerator_arn: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAcceleratorResult]:
    """
    Resource Type definition for AWS::GlobalAccelerator::Accelerator


    :param str accelerator_arn: The Amazon Resource Name (ARN) of the accelerator.
    """
    ...
