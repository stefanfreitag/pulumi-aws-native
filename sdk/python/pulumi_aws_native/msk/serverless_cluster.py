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
from ._inputs import *

__all__ = ['ServerlessClusterArgs', 'ServerlessCluster']

@pulumi.input_type
class ServerlessClusterArgs:
    def __init__(__self__, *,
                 client_authentication: pulumi.Input['ServerlessClusterClientAuthenticationArgs'],
                 cluster_name: pulumi.Input[str],
                 vpc_configs: pulumi.Input[Sequence[pulumi.Input['ServerlessClusterVpcConfigArgs']]],
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a ServerlessCluster resource.
        :param Any tags: A key-value pair to associate with a resource.
        """
        ServerlessClusterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            client_authentication=client_authentication,
            cluster_name=cluster_name,
            vpc_configs=vpc_configs,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             client_authentication: pulumi.Input['ServerlessClusterClientAuthenticationArgs'],
             cluster_name: pulumi.Input[str],
             vpc_configs: pulumi.Input[Sequence[pulumi.Input['ServerlessClusterVpcConfigArgs']]],
             tags: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("client_authentication", client_authentication)
        _setter("cluster_name", cluster_name)
        _setter("vpc_configs", vpc_configs)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> pulumi.Input['ServerlessClusterClientAuthenticationArgs']:
        return pulumi.get(self, "client_authentication")

    @client_authentication.setter
    def client_authentication(self, value: pulumi.Input['ServerlessClusterClientAuthenticationArgs']):
        pulumi.set(self, "client_authentication", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(self) -> pulumi.Input[Sequence[pulumi.Input['ServerlessClusterVpcConfigArgs']]]:
        return pulumi.get(self, "vpc_configs")

    @vpc_configs.setter
    def vpc_configs(self, value: pulumi.Input[Sequence[pulumi.Input['ServerlessClusterVpcConfigArgs']]]):
        pulumi.set(self, "vpc_configs", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class ServerlessCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_authentication: Optional[pulumi.Input[pulumi.InputType['ServerlessClusterClientAuthenticationArgs']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 vpc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerlessClusterVpcConfigArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::MSK::ServerlessCluster

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any tags: A key-value pair to associate with a resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerlessClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::MSK::ServerlessCluster

        :param str resource_name: The name of the resource.
        :param ServerlessClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerlessClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ServerlessClusterArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_authentication: Optional[pulumi.Input[pulumi.InputType['ServerlessClusterClientAuthenticationArgs']]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 vpc_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerlessClusterVpcConfigArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerlessClusterArgs.__new__(ServerlessClusterArgs)

            if client_authentication is not None and not isinstance(client_authentication, ServerlessClusterClientAuthenticationArgs):
                client_authentication = client_authentication or {}
                def _setter(key, value):
                    client_authentication[key] = value
                ServerlessClusterClientAuthenticationArgs._configure(_setter, **client_authentication)
            if client_authentication is None and not opts.urn:
                raise TypeError("Missing required property 'client_authentication'")
            __props__.__dict__["client_authentication"] = client_authentication
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["tags"] = tags
            if vpc_configs is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_configs'")
            __props__.__dict__["vpc_configs"] = vpc_configs
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["client_authentication", "cluster_name", "tags", "vpc_configs[*]"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ServerlessCluster, __self__).__init__(
            'aws-native:msk:ServerlessCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerlessCluster':
        """
        Get an existing ServerlessCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerlessClusterArgs.__new__(ServerlessClusterArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["client_authentication"] = None
        __props__.__dict__["cluster_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["vpc_configs"] = None
        return ServerlessCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> pulumi.Output['outputs.ServerlessClusterClientAuthentication']:
        return pulumi.get(self, "client_authentication")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        A key-value pair to associate with a resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcConfigs")
    def vpc_configs(self) -> pulumi.Output[Sequence['outputs.ServerlessClusterVpcConfig']]:
        return pulumi.get(self, "vpc_configs")

