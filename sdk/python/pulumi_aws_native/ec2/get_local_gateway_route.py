# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetLocalGatewayRouteResult',
    'AwaitableGetLocalGatewayRouteResult',
    'get_local_gateway_route',
    'get_local_gateway_route_output',
]

@pulumi.output_type
class GetLocalGatewayRouteResult:
    def __init__(__self__, local_gateway_virtual_interface_group_id=None, network_interface_id=None, state=None, type=None):
        if local_gateway_virtual_interface_group_id and not isinstance(local_gateway_virtual_interface_group_id, str):
            raise TypeError("Expected argument 'local_gateway_virtual_interface_group_id' to be a str")
        pulumi.set(__self__, "local_gateway_virtual_interface_group_id", local_gateway_virtual_interface_group_id)
        if network_interface_id and not isinstance(network_interface_id, str):
            raise TypeError("Expected argument 'network_interface_id' to be a str")
        pulumi.set(__self__, "network_interface_id", network_interface_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="localGatewayVirtualInterfaceGroupId")
    def local_gateway_virtual_interface_group_id(self) -> Optional[str]:
        """
        The ID of the virtual interface group.
        """
        return pulumi.get(self, "local_gateway_virtual_interface_group_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[str]:
        """
        The ID of the network interface.
        """
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the route.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The route type.
        """
        return pulumi.get(self, "type")


class AwaitableGetLocalGatewayRouteResult(GetLocalGatewayRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalGatewayRouteResult(
            local_gateway_virtual_interface_group_id=self.local_gateway_virtual_interface_group_id,
            network_interface_id=self.network_interface_id,
            state=self.state,
            type=self.type)


def get_local_gateway_route(destination_cidr_block: Optional[str] = None,
                            local_gateway_route_table_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalGatewayRouteResult:
    """
    Describes a route for a local gateway route table.


    :param str destination_cidr_block: The CIDR block used for destination matches.
    :param str local_gateway_route_table_id: The ID of the local gateway route table.
    """
    __args__ = dict()
    __args__['destinationCidrBlock'] = destination_cidr_block
    __args__['localGatewayRouteTableId'] = local_gateway_route_table_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getLocalGatewayRoute', __args__, opts=opts, typ=GetLocalGatewayRouteResult).value

    return AwaitableGetLocalGatewayRouteResult(
        local_gateway_virtual_interface_group_id=__ret__.local_gateway_virtual_interface_group_id,
        network_interface_id=__ret__.network_interface_id,
        state=__ret__.state,
        type=__ret__.type)


@_utilities.lift_output_func(get_local_gateway_route)
def get_local_gateway_route_output(destination_cidr_block: Optional[pulumi.Input[str]] = None,
                                   local_gateway_route_table_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalGatewayRouteResult]:
    """
    Describes a route for a local gateway route table.


    :param str destination_cidr_block: The CIDR block used for destination matches.
    :param str local_gateway_route_table_id: The ID of the local gateway route table.
    """
    ...
