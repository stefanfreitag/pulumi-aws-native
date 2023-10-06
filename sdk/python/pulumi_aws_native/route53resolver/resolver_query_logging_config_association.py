# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['ResolverQueryLoggingConfigAssociationArgs', 'ResolverQueryLoggingConfigAssociation']

@pulumi.input_type
class ResolverQueryLoggingConfigAssociationArgs:
    def __init__(__self__, *,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResolverQueryLoggingConfigAssociation resource.
        :param pulumi.Input[str] resolver_query_log_config_id: ResolverQueryLogConfigId
        :param pulumi.Input[str] resource_id: ResourceId
        """
        ResolverQueryLoggingConfigAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resolver_query_log_config_id=resolver_query_log_config_id,
            resource_id=resource_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
             resource_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if resolver_query_log_config_id is not None:
            _setter("resolver_query_log_config_id", resolver_query_log_config_id)
        if resource_id is not None:
            _setter("resource_id", resource_id)

    @property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> Optional[pulumi.Input[str]]:
        """
        ResolverQueryLogConfigId
        """
        return pulumi.get(self, "resolver_query_log_config_id")

    @resolver_query_log_config_id.setter
    def resolver_query_log_config_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolver_query_log_config_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ResourceId
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


class ResolverQueryLoggingConfigAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resolver_query_log_config_id: ResolverQueryLogConfigId
        :param pulumi.Input[str] resource_id: ResourceId
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ResolverQueryLoggingConfigAssociationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.

        :param str resource_name: The name of the resource.
        :param ResolverQueryLoggingConfigAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverQueryLoggingConfigAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResolverQueryLoggingConfigAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverQueryLoggingConfigAssociationArgs.__new__(ResolverQueryLoggingConfigAssociationArgs)

            __props__.__dict__["resolver_query_log_config_id"] = resolver_query_log_config_id
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["error_message"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["resolver_query_log_config_id", "resource_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ResolverQueryLoggingConfigAssociation, __self__).__init__(
            'aws-native:route53resolver:ResolverQueryLoggingConfigAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResolverQueryLoggingConfigAssociation':
        """
        Get an existing ResolverQueryLoggingConfigAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResolverQueryLoggingConfigAssociationArgs.__new__(ResolverQueryLoggingConfigAssociationArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["error_message"] = None
        __props__.__dict__["resolver_query_log_config_id"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["status"] = None
        return ResolverQueryLoggingConfigAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output['ResolverQueryLoggingConfigAssociationError']:
        """
        ResolverQueryLogConfigAssociationError
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        ResolverQueryLogConfigAssociationErrorMessage
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> pulumi.Output[Optional[str]]:
        """
        ResolverQueryLogConfigId
        """
        return pulumi.get(self, "resolver_query_log_config_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        ResourceId
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['ResolverQueryLoggingConfigAssociationStatus']:
        """
        ResolverQueryLogConfigAssociationStatus
        """
        return pulumi.get(self, "status")

