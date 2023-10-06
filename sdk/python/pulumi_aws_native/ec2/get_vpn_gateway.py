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
    'GetVpnGatewayResult',
    'AwaitableGetVpnGatewayResult',
    'get_vpn_gateway',
    'get_vpn_gateway_output',
]

@pulumi.output_type
class GetVpnGatewayResult:
    def __init__(__self__, tags=None, vpn_gateway_id=None):
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if vpn_gateway_id and not isinstance(vpn_gateway_id, str):
            raise TypeError("Expected argument 'vpn_gateway_id' to be a str")
        pulumi.set(__self__, "vpn_gateway_id", vpn_gateway_id)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.VpnGatewayTag']]:
        """
        Any tags assigned to the virtual private gateway.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpnGatewayId")
    def vpn_gateway_id(self) -> Optional[str]:
        """
        VPN Gateway ID generated by service
        """
        return pulumi.get(self, "vpn_gateway_id")


class AwaitableGetVpnGatewayResult(GetVpnGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnGatewayResult(
            tags=self.tags,
            vpn_gateway_id=self.vpn_gateway_id)


def get_vpn_gateway(vpn_gateway_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnGatewayResult:
    """
    Schema for EC2 VPN Gateway


    :param str vpn_gateway_id: VPN Gateway ID generated by service
    """
    __args__ = dict()
    __args__['vpnGatewayId'] = vpn_gateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getVpnGateway', __args__, opts=opts, typ=GetVpnGatewayResult).value

    return AwaitableGetVpnGatewayResult(
        tags=pulumi.get(__ret__, 'tags'),
        vpn_gateway_id=pulumi.get(__ret__, 'vpn_gateway_id'))


@_utilities.lift_output_func(get_vpn_gateway)
def get_vpn_gateway_output(vpn_gateway_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpnGatewayResult]:
    """
    Schema for EC2 VPN Gateway


    :param str vpn_gateway_id: VPN Gateway ID generated by service
    """
    ...
