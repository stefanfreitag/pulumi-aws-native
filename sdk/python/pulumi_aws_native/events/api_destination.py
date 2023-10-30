# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['ApiDestinationArgs', 'ApiDestination']

@pulumi.input_type
class ApiDestinationArgs:
    def __init__(__self__, *,
                 connection_arn: pulumi.Input[str],
                 http_method: pulumi.Input['ApiDestinationHttpMethod'],
                 invocation_endpoint: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 invocation_rate_limit_per_second: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiDestination resource.
        :param pulumi.Input[str] connection_arn: The arn of the connection.
        :param pulumi.Input[str] invocation_endpoint: Url endpoint to invoke.
        :param pulumi.Input[str] name: Name of the apiDestination.
        """
        pulumi.set(__self__, "connection_arn", connection_arn)
        pulumi.set(__self__, "http_method", http_method)
        pulumi.set(__self__, "invocation_endpoint", invocation_endpoint)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if invocation_rate_limit_per_second is not None:
            pulumi.set(__self__, "invocation_rate_limit_per_second", invocation_rate_limit_per_second)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Input[str]:
        """
        The arn of the connection.
        """
        return pulumi.get(self, "connection_arn")

    @connection_arn.setter
    def connection_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_arn", value)

    @property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Input['ApiDestinationHttpMethod']:
        return pulumi.get(self, "http_method")

    @http_method.setter
    def http_method(self, value: pulumi.Input['ApiDestinationHttpMethod']):
        pulumi.set(self, "http_method", value)

    @property
    @pulumi.getter(name="invocationEndpoint")
    def invocation_endpoint(self) -> pulumi.Input[str]:
        """
        Url endpoint to invoke.
        """
        return pulumi.get(self, "invocation_endpoint")

    @invocation_endpoint.setter
    def invocation_endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "invocation_endpoint", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="invocationRateLimitPerSecond")
    def invocation_rate_limit_per_second(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "invocation_rate_limit_per_second")

    @invocation_rate_limit_per_second.setter
    def invocation_rate_limit_per_second(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "invocation_rate_limit_per_second", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the apiDestination.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ApiDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 http_method: Optional[pulumi.Input['ApiDestinationHttpMethod']] = None,
                 invocation_endpoint: Optional[pulumi.Input[str]] = None,
                 invocation_rate_limit_per_second: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Events::ApiDestination.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_arn: The arn of the connection.
        :param pulumi.Input[str] invocation_endpoint: Url endpoint to invoke.
        :param pulumi.Input[str] name: Name of the apiDestination.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiDestinationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Events::ApiDestination.

        :param str resource_name: The name of the resource.
        :param ApiDestinationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiDestinationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 http_method: Optional[pulumi.Input['ApiDestinationHttpMethod']] = None,
                 invocation_endpoint: Optional[pulumi.Input[str]] = None,
                 invocation_rate_limit_per_second: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiDestinationArgs.__new__(ApiDestinationArgs)

            if connection_arn is None and not opts.urn:
                raise TypeError("Missing required property 'connection_arn'")
            __props__.__dict__["connection_arn"] = connection_arn
            __props__.__dict__["description"] = description
            if http_method is None and not opts.urn:
                raise TypeError("Missing required property 'http_method'")
            __props__.__dict__["http_method"] = http_method
            if invocation_endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'invocation_endpoint'")
            __props__.__dict__["invocation_endpoint"] = invocation_endpoint
            __props__.__dict__["invocation_rate_limit_per_second"] = invocation_rate_limit_per_second
            __props__.__dict__["name"] = name
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ApiDestination, __self__).__init__(
            'aws-native:events:ApiDestination',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiDestination':
        """
        Get an existing ApiDestination resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiDestinationArgs.__new__(ApiDestinationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["connection_arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["http_method"] = None
        __props__.__dict__["invocation_endpoint"] = None
        __props__.__dict__["invocation_rate_limit_per_second"] = None
        __props__.__dict__["name"] = None
        return ApiDestination(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The arn of the api destination.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Output[str]:
        """
        The arn of the connection.
        """
        return pulumi.get(self, "connection_arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> pulumi.Output['ApiDestinationHttpMethod']:
        return pulumi.get(self, "http_method")

    @property
    @pulumi.getter(name="invocationEndpoint")
    def invocation_endpoint(self) -> pulumi.Output[str]:
        """
        Url endpoint to invoke.
        """
        return pulumi.get(self, "invocation_endpoint")

    @property
    @pulumi.getter(name="invocationRateLimitPerSecond")
    def invocation_rate_limit_per_second(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "invocation_rate_limit_per_second")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the apiDestination.
        """
        return pulumi.get(self, "name")

