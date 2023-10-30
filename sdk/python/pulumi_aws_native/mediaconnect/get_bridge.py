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
from ._enums import *

__all__ = [
    'GetBridgeResult',
    'AwaitableGetBridgeResult',
    'get_bridge',
    'get_bridge_output',
]

@pulumi.output_type
class GetBridgeResult:
    def __init__(__self__, bridge_arn=None, bridge_state=None, egress_gateway_bridge=None, ingress_gateway_bridge=None, name=None, outputs=None, placement_arn=None, source_failover_config=None, sources=None):
        if bridge_arn and not isinstance(bridge_arn, str):
            raise TypeError("Expected argument 'bridge_arn' to be a str")
        pulumi.set(__self__, "bridge_arn", bridge_arn)
        if bridge_state and not isinstance(bridge_state, str):
            raise TypeError("Expected argument 'bridge_state' to be a str")
        pulumi.set(__self__, "bridge_state", bridge_state)
        if egress_gateway_bridge and not isinstance(egress_gateway_bridge, dict):
            raise TypeError("Expected argument 'egress_gateway_bridge' to be a dict")
        pulumi.set(__self__, "egress_gateway_bridge", egress_gateway_bridge)
        if ingress_gateway_bridge and not isinstance(ingress_gateway_bridge, dict):
            raise TypeError("Expected argument 'ingress_gateway_bridge' to be a dict")
        pulumi.set(__self__, "ingress_gateway_bridge", ingress_gateway_bridge)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outputs and not isinstance(outputs, list):
            raise TypeError("Expected argument 'outputs' to be a list")
        pulumi.set(__self__, "outputs", outputs)
        if placement_arn and not isinstance(placement_arn, str):
            raise TypeError("Expected argument 'placement_arn' to be a str")
        pulumi.set(__self__, "placement_arn", placement_arn)
        if source_failover_config and not isinstance(source_failover_config, dict):
            raise TypeError("Expected argument 'source_failover_config' to be a dict")
        pulumi.set(__self__, "source_failover_config", source_failover_config)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)

    @property
    @pulumi.getter(name="bridgeArn")
    def bridge_arn(self) -> Optional[str]:
        """
        The Amazon Resource Number (ARN) of the bridge.
        """
        return pulumi.get(self, "bridge_arn")

    @property
    @pulumi.getter(name="bridgeState")
    def bridge_state(self) -> Optional['BridgeStateEnum']:
        return pulumi.get(self, "bridge_state")

    @property
    @pulumi.getter(name="egressGatewayBridge")
    def egress_gateway_bridge(self) -> Optional['outputs.BridgeEgressGatewayBridge']:
        return pulumi.get(self, "egress_gateway_bridge")

    @property
    @pulumi.getter(name="ingressGatewayBridge")
    def ingress_gateway_bridge(self) -> Optional['outputs.BridgeIngressGatewayBridge']:
        return pulumi.get(self, "ingress_gateway_bridge")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the bridge.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> Optional[Sequence['outputs.BridgeOutput']]:
        """
        The outputs on this bridge.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="placementArn")
    def placement_arn(self) -> Optional[str]:
        """
        The placement Amazon Resource Number (ARN) of the bridge.
        """
        return pulumi.get(self, "placement_arn")

    @property
    @pulumi.getter(name="sourceFailoverConfig")
    def source_failover_config(self) -> Optional['outputs.BridgeFailoverConfig']:
        return pulumi.get(self, "source_failover_config")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.BridgeSource']]:
        """
        The sources on this bridge.
        """
        return pulumi.get(self, "sources")


class AwaitableGetBridgeResult(GetBridgeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBridgeResult(
            bridge_arn=self.bridge_arn,
            bridge_state=self.bridge_state,
            egress_gateway_bridge=self.egress_gateway_bridge,
            ingress_gateway_bridge=self.ingress_gateway_bridge,
            name=self.name,
            outputs=self.outputs,
            placement_arn=self.placement_arn,
            source_failover_config=self.source_failover_config,
            sources=self.sources)


def get_bridge(bridge_arn: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBridgeResult:
    """
    Resource schema for AWS::MediaConnect::Bridge


    :param str bridge_arn: The Amazon Resource Number (ARN) of the bridge.
    """
    __args__ = dict()
    __args__['bridgeArn'] = bridge_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediaconnect:getBridge', __args__, opts=opts, typ=GetBridgeResult).value

    return AwaitableGetBridgeResult(
        bridge_arn=pulumi.get(__ret__, 'bridge_arn'),
        bridge_state=pulumi.get(__ret__, 'bridge_state'),
        egress_gateway_bridge=pulumi.get(__ret__, 'egress_gateway_bridge'),
        ingress_gateway_bridge=pulumi.get(__ret__, 'ingress_gateway_bridge'),
        name=pulumi.get(__ret__, 'name'),
        outputs=pulumi.get(__ret__, 'outputs'),
        placement_arn=pulumi.get(__ret__, 'placement_arn'),
        source_failover_config=pulumi.get(__ret__, 'source_failover_config'),
        sources=pulumi.get(__ret__, 'sources'))


@_utilities.lift_output_func(get_bridge)
def get_bridge_output(bridge_arn: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBridgeResult]:
    """
    Resource schema for AWS::MediaConnect::Bridge


    :param str bridge_arn: The Amazon Resource Number (ARN) of the bridge.
    """
    ...
