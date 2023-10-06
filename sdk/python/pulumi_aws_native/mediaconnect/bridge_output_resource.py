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
from ._inputs import *

__all__ = ['BridgeOutputResourceArgs', 'BridgeOutputResource']

@pulumi.input_type
class BridgeOutputResourceArgs:
    def __init__(__self__, *,
                 bridge_arn: pulumi.Input[str],
                 network_output: pulumi.Input['BridgeOutputResourceBridgeNetworkOutputArgs'],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BridgeOutputResource resource.
        :param pulumi.Input[str] bridge_arn: The Amazon Resource Number (ARN) of the bridge.
        :param pulumi.Input['BridgeOutputResourceBridgeNetworkOutputArgs'] network_output: The output of the bridge.
        :param pulumi.Input[str] name: The network output name.
        """
        BridgeOutputResourceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bridge_arn=bridge_arn,
            network_output=network_output,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bridge_arn: pulumi.Input[str],
             network_output: pulumi.Input['BridgeOutputResourceBridgeNetworkOutputArgs'],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("bridge_arn", bridge_arn)
        _setter("network_output", network_output)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter(name="bridgeArn")
    def bridge_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Number (ARN) of the bridge.
        """
        return pulumi.get(self, "bridge_arn")

    @bridge_arn.setter
    def bridge_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "bridge_arn", value)

    @property
    @pulumi.getter(name="networkOutput")
    def network_output(self) -> pulumi.Input['BridgeOutputResourceBridgeNetworkOutputArgs']:
        """
        The output of the bridge.
        """
        return pulumi.get(self, "network_output")

    @network_output.setter
    def network_output(self, value: pulumi.Input['BridgeOutputResourceBridgeNetworkOutputArgs']):
        pulumi.set(self, "network_output", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The network output name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class BridgeOutputResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_output: Optional[pulumi.Input[pulumi.InputType['BridgeOutputResourceBridgeNetworkOutputArgs']]] = None,
                 __props__=None):
        """
        Resource schema for AWS::MediaConnect::BridgeOutput

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bridge_arn: The Amazon Resource Number (ARN) of the bridge.
        :param pulumi.Input[str] name: The network output name.
        :param pulumi.Input[pulumi.InputType['BridgeOutputResourceBridgeNetworkOutputArgs']] network_output: The output of the bridge.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BridgeOutputResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::MediaConnect::BridgeOutput

        :param str resource_name: The name of the resource.
        :param BridgeOutputResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BridgeOutputResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BridgeOutputResourceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bridge_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_output: Optional[pulumi.Input[pulumi.InputType['BridgeOutputResourceBridgeNetworkOutputArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BridgeOutputResourceArgs.__new__(BridgeOutputResourceArgs)

            if bridge_arn is None and not opts.urn:
                raise TypeError("Missing required property 'bridge_arn'")
            __props__.__dict__["bridge_arn"] = bridge_arn
            __props__.__dict__["name"] = name
            if network_output is not None and not isinstance(network_output, BridgeOutputResourceBridgeNetworkOutputArgs):
                network_output = network_output or {}
                def _setter(key, value):
                    network_output[key] = value
                BridgeOutputResourceBridgeNetworkOutputArgs._configure(_setter, **network_output)
            if network_output is None and not opts.urn:
                raise TypeError("Missing required property 'network_output'")
            __props__.__dict__["network_output"] = network_output
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["bridge_arn", "name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(BridgeOutputResource, __self__).__init__(
            'aws-native:mediaconnect:BridgeOutputResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BridgeOutputResource':
        """
        Get an existing BridgeOutputResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BridgeOutputResourceArgs.__new__(BridgeOutputResourceArgs)

        __props__.__dict__["bridge_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_output"] = None
        return BridgeOutputResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bridgeArn")
    def bridge_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Number (ARN) of the bridge.
        """
        return pulumi.get(self, "bridge_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The network output name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkOutput")
    def network_output(self) -> pulumi.Output['outputs.BridgeOutputResourceBridgeNetworkOutput']:
        """
        The output of the bridge.
        """
        return pulumi.get(self, "network_output")

