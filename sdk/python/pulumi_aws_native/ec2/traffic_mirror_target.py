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

__all__ = ['TrafficMirrorTargetArgs', 'TrafficMirrorTarget']

@pulumi.input_type
class TrafficMirrorTargetArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_load_balancer_endpoint_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a TrafficMirrorTarget resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gateway_load_balancer_endpoint_id is not None:
            pulumi.set(__self__, "gateway_load_balancer_endpoint_id", gateway_load_balancer_endpoint_id)
        if network_interface_id is not None:
            pulumi.set(__self__, "network_interface_id", network_interface_id)
        if network_load_balancer_arn is not None:
            pulumi.set(__self__, "network_load_balancer_arn", network_load_balancer_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gatewayLoadBalancerEndpointId")
    def gateway_load_balancer_endpoint_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gateway_load_balancer_endpoint_id")

    @gateway_load_balancer_endpoint_id.setter
    def gateway_load_balancer_endpoint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_load_balancer_endpoint_id", value)

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_interface_id")

    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_interface_id", value)

    @property
    @pulumi.getter(name="networkLoadBalancerArn")
    def network_load_balancer_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "network_load_balancer_arn")

    @network_load_balancer_arn.setter
    def network_load_balancer_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_load_balancer_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""TrafficMirrorTarget is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class TrafficMirrorTarget(pulumi.CustomResource):
    warnings.warn("""TrafficMirrorTarget is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_load_balancer_endpoint_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::TrafficMirrorTarget

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TrafficMirrorTargetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::TrafficMirrorTarget

        :param str resource_name: The name of the resource.
        :param TrafficMirrorTargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TrafficMirrorTargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_load_balancer_endpoint_id: Optional[pulumi.Input[str]] = None,
                 network_interface_id: Optional[pulumi.Input[str]] = None,
                 network_load_balancer_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""TrafficMirrorTarget is deprecated: TrafficMirrorTarget is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TrafficMirrorTargetArgs.__new__(TrafficMirrorTargetArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["gateway_load_balancer_endpoint_id"] = gateway_load_balancer_endpoint_id
            __props__.__dict__["network_interface_id"] = network_interface_id
            __props__.__dict__["network_load_balancer_arn"] = network_load_balancer_arn
            __props__.__dict__["tags"] = tags
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["description", "gateway_load_balancer_endpoint_id", "network_interface_id", "network_load_balancer_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(TrafficMirrorTarget, __self__).__init__(
            'aws-native:ec2:TrafficMirrorTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TrafficMirrorTarget':
        """
        Get an existing TrafficMirrorTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TrafficMirrorTargetArgs.__new__(TrafficMirrorTargetArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["gateway_load_balancer_endpoint_id"] = None
        __props__.__dict__["network_interface_id"] = None
        __props__.__dict__["network_load_balancer_arn"] = None
        __props__.__dict__["tags"] = None
        return TrafficMirrorTarget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gatewayLoadBalancerEndpointId")
    def gateway_load_balancer_endpoint_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "gateway_load_balancer_endpoint_id")

    @property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "network_interface_id")

    @property
    @pulumi.getter(name="networkLoadBalancerArn")
    def network_load_balancer_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "network_load_balancer_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

