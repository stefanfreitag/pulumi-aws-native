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

__all__ = [
    'GetConnectPeerResult',
    'AwaitableGetConnectPeerResult',
    'get_connect_peer',
    'get_connect_peer_output',
]

@pulumi.output_type
class GetConnectPeerResult:
    def __init__(__self__, configuration=None, connect_peer_id=None, core_network_id=None, created_at=None, edge_location=None, state=None, tags=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if connect_peer_id and not isinstance(connect_peer_id, str):
            raise TypeError("Expected argument 'connect_peer_id' to be a str")
        pulumi.set(__self__, "connect_peer_id", connect_peer_id)
        if core_network_id and not isinstance(core_network_id, str):
            raise TypeError("Expected argument 'core_network_id' to be a str")
        pulumi.set(__self__, "core_network_id", core_network_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if edge_location and not isinstance(edge_location, str):
            raise TypeError("Expected argument 'edge_location' to be a str")
        pulumi.set(__self__, "edge_location", edge_location)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def configuration(self) -> Optional['outputs.ConnectPeerConfiguration']:
        """
        Configuration of the connect peer.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="connectPeerId")
    def connect_peer_id(self) -> Optional[str]:
        """
        The ID of the Connect peer.
        """
        return pulumi.get(self, "connect_peer_id")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[str]:
        """
        The ID of the core network.
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        Connect peer creation time.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="edgeLocation")
    def edge_location(self) -> Optional[str]:
        """
        The Connect peer Regions where edges are located.
        """
        return pulumi.get(self, "edge_location")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        State of the connect peer.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ConnectPeerTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetConnectPeerResult(GetConnectPeerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectPeerResult(
            configuration=self.configuration,
            connect_peer_id=self.connect_peer_id,
            core_network_id=self.core_network_id,
            created_at=self.created_at,
            edge_location=self.edge_location,
            state=self.state,
            tags=self.tags)


def get_connect_peer(connect_peer_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectPeerResult:
    """
    AWS::NetworkManager::ConnectPeer Resource Type Definition.


    :param str connect_peer_id: The ID of the Connect peer.
    """
    __args__ = dict()
    __args__['connectPeerId'] = connect_peer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:networkmanager:getConnectPeer', __args__, opts=opts, typ=GetConnectPeerResult).value

    return AwaitableGetConnectPeerResult(
        configuration=pulumi.get(__ret__, 'configuration'),
        connect_peer_id=pulumi.get(__ret__, 'connect_peer_id'),
        core_network_id=pulumi.get(__ret__, 'core_network_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        edge_location=pulumi.get(__ret__, 'edge_location'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_connect_peer)
def get_connect_peer_output(connect_peer_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectPeerResult]:
    """
    AWS::NetworkManager::ConnectPeer Resource Type Definition.


    :param str connect_peer_id: The ID of the Connect peer.
    """
    ...
