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
from ._inputs import *

__all__ = ['FirewallDomainListArgs', 'FirewallDomainList']

@pulumi.input_type
class FirewallDomainListArgs:
    def __init__(__self__, *,
                 domain_file_url: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallDomainListTagArgs']]]] = None):
        """
        The set of arguments for constructing a FirewallDomainList resource.
        :param pulumi.Input[str] domain_file_url: S3 URL to import domains from.
        :param pulumi.Input[str] name: FirewallDomainListName
        :param pulumi.Input[Sequence[pulumi.Input['FirewallDomainListTagArgs']]] tags: Tags
        """
        if domain_file_url is not None:
            pulumi.set(__self__, "domain_file_url", domain_file_url)
        if domains is not None:
            pulumi.set(__self__, "domains", domains)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainFileUrl")
    def domain_file_url(self) -> Optional[pulumi.Input[str]]:
        """
        S3 URL to import domains from.
        """
        return pulumi.get(self, "domain_file_url")

    @domain_file_url.setter
    def domain_file_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_file_url", value)

    @property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        FirewallDomainListName
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallDomainListTagArgs']]]]:
        """
        Tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallDomainListTagArgs']]]]):
        pulumi.set(self, "tags", value)


class FirewallDomainList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_file_url: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallDomainListTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Route53Resolver::FirewallDomainList.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_file_url: S3 URL to import domains from.
        :param pulumi.Input[str] name: FirewallDomainListName
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallDomainListTagArgs']]]] tags: Tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[FirewallDomainListArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Route53Resolver::FirewallDomainList.

        :param str resource_name: The name of the resource.
        :param FirewallDomainListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirewallDomainListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_file_url: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallDomainListTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirewallDomainListArgs.__new__(FirewallDomainListArgs)

            __props__.__dict__["domain_file_url"] = domain_file_url
            __props__.__dict__["domains"] = domains
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["creator_request_id"] = None
            __props__.__dict__["domain_count"] = None
            __props__.__dict__["managed_owner_name"] = None
            __props__.__dict__["modification_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_message"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(FirewallDomainList, __self__).__init__(
            'aws-native:route53resolver:FirewallDomainList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FirewallDomainList':
        """
        Get an existing FirewallDomainList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirewallDomainListArgs.__new__(FirewallDomainListArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["creator_request_id"] = None
        __props__.__dict__["domain_count"] = None
        __props__.__dict__["domain_file_url"] = None
        __props__.__dict__["domains"] = None
        __props__.__dict__["managed_owner_name"] = None
        __props__.__dict__["modification_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_message"] = None
        __props__.__dict__["tags"] = None
        return FirewallDomainList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Arn
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="creatorRequestId")
    def creator_request_id(self) -> pulumi.Output[str]:
        """
        The id of the creator request.
        """
        return pulumi.get(self, "creator_request_id")

    @property
    @pulumi.getter(name="domainCount")
    def domain_count(self) -> pulumi.Output[int]:
        """
        Count
        """
        return pulumi.get(self, "domain_count")

    @property
    @pulumi.getter(name="domainFileUrl")
    def domain_file_url(self) -> pulumi.Output[Optional[str]]:
        """
        S3 URL to import domains from.
        """
        return pulumi.get(self, "domain_file_url")

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter(name="managedOwnerName")
    def managed_owner_name(self) -> pulumi.Output[str]:
        """
        ServicePrincipal
        """
        return pulumi.get(self, "managed_owner_name")

    @property
    @pulumi.getter(name="modificationTime")
    def modification_time(self) -> pulumi.Output[str]:
        """
        Rfc3339TimeString
        """
        return pulumi.get(self, "modification_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        FirewallDomainListName
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['FirewallDomainListStatus']:
        """
        ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[str]:
        """
        FirewallDomainListAssociationStatus
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallDomainListTag']]]:
        """
        Tags
        """
        return pulumi.get(self, "tags")

