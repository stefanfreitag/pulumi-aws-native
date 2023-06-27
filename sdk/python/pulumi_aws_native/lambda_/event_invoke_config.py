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
from ._inputs import *

__all__ = ['EventInvokeConfigArgs', 'EventInvokeConfig']

@pulumi.input_type
class EventInvokeConfigArgs:
    def __init__(__self__, *,
                 function_name: pulumi.Input[str],
                 qualifier: pulumi.Input[str],
                 destination_config: Optional[pulumi.Input['EventInvokeConfigDestinationConfigArgs']] = None,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a EventInvokeConfig resource.
        """
        pulumi.set(__self__, "function_name", function_name)
        pulumi.set(__self__, "qualifier", qualifier)
        if destination_config is not None:
            pulumi.set(__self__, "destination_config", destination_config)
        if maximum_event_age_in_seconds is not None:
            pulumi.set(__self__, "maximum_event_age_in_seconds", maximum_event_age_in_seconds)
        if maximum_retry_attempts is not None:
            pulumi.set(__self__, "maximum_retry_attempts", maximum_retry_attempts)

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "function_name")

    @function_name.setter
    def function_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "function_name", value)

    @property
    @pulumi.getter
    def qualifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "qualifier")

    @qualifier.setter
    def qualifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "qualifier", value)

    @property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional[pulumi.Input['EventInvokeConfigDestinationConfigArgs']]:
        return pulumi.get(self, "destination_config")

    @destination_config.setter
    def destination_config(self, value: Optional[pulumi.Input['EventInvokeConfigDestinationConfigArgs']]):
        pulumi.set(self, "destination_config", value)

    @property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "maximum_event_age_in_seconds")

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_event_age_in_seconds", value)

    @property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "maximum_retry_attempts")

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_retry_attempts", value)


class EventInvokeConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_config: Optional[pulumi.Input[pulumi.InputType['EventInvokeConfigDestinationConfigArgs']]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[int]] = None,
                 qualifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Lambda::EventInvokeConfig

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventInvokeConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Lambda::EventInvokeConfig

        :param str resource_name: The name of the resource.
        :param EventInvokeConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventInvokeConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_config: Optional[pulumi.Input[pulumi.InputType['EventInvokeConfigDestinationConfigArgs']]] = None,
                 function_name: Optional[pulumi.Input[str]] = None,
                 maximum_event_age_in_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_retry_attempts: Optional[pulumi.Input[int]] = None,
                 qualifier: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventInvokeConfigArgs.__new__(EventInvokeConfigArgs)

            __props__.__dict__["destination_config"] = destination_config
            if function_name is None and not opts.urn:
                raise TypeError("Missing required property 'function_name'")
            __props__.__dict__["function_name"] = function_name
            __props__.__dict__["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
            __props__.__dict__["maximum_retry_attempts"] = maximum_retry_attempts
            if qualifier is None and not opts.urn:
                raise TypeError("Missing required property 'qualifier'")
            __props__.__dict__["qualifier"] = qualifier
        super(EventInvokeConfig, __self__).__init__(
            'aws-native:lambda:EventInvokeConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventInvokeConfig':
        """
        Get an existing EventInvokeConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventInvokeConfigArgs.__new__(EventInvokeConfigArgs)

        __props__.__dict__["destination_config"] = None
        __props__.__dict__["function_name"] = None
        __props__.__dict__["maximum_event_age_in_seconds"] = None
        __props__.__dict__["maximum_retry_attempts"] = None
        __props__.__dict__["qualifier"] = None
        return EventInvokeConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> pulumi.Output[Optional['outputs.EventInvokeConfigDestinationConfig']]:
        return pulumi.get(self, "destination_config")

    @property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "function_name")

    @property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "maximum_event_age_in_seconds")

    @property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "maximum_retry_attempts")

    @property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "qualifier")

