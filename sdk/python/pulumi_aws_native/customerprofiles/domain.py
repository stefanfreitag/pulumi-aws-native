# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 dead_letter_queue_url: Optional[pulumi.Input[str]] = None,
                 default_encryption_key: Optional[pulumi.Input[str]] = None,
                 default_expiration_days: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[str] domain_name: The unique name of the domain.
        :param pulumi.Input[str] dead_letter_queue_url: The URL of the SQS dead letter queue
        :param pulumi.Input[str] default_encryption_key: The default encryption key
        :param pulumi.Input[int] default_expiration_days: The default number of days until the data within the domain expires.
        :param pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]] tags: The tags (keys and values) associated with the domain
        """
        pulumi.set(__self__, "domain_name", domain_name)
        if dead_letter_queue_url is not None:
            pulumi.set(__self__, "dead_letter_queue_url", dead_letter_queue_url)
        if default_encryption_key is not None:
            pulumi.set(__self__, "default_encryption_key", default_encryption_key)
        if default_expiration_days is not None:
            pulumi.set(__self__, "default_expiration_days", default_expiration_days)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The unique name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the SQS dead letter queue
        """
        return pulumi.get(self, "dead_letter_queue_url")

    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dead_letter_queue_url", value)

    @property
    @pulumi.getter(name="defaultEncryptionKey")
    def default_encryption_key(self) -> Optional[pulumi.Input[str]]:
        """
        The default encryption key
        """
        return pulumi.get(self, "default_encryption_key")

    @default_encryption_key.setter
    def default_encryption_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_encryption_key", value)

    @property
    @pulumi.getter(name="defaultExpirationDays")
    def default_expiration_days(self) -> Optional[pulumi.Input[int]]:
        """
        The default number of days until the data within the domain expires.
        """
        return pulumi.get(self, "default_expiration_days")

    @default_expiration_days.setter
    def default_expiration_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_expiration_days", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]:
        """
        The tags (keys and values) associated with the domain
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dead_letter_queue_url: Optional[pulumi.Input[str]] = None,
                 default_encryption_key: Optional[pulumi.Input[str]] = None,
                 default_expiration_days: Optional[pulumi.Input[int]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 __props__=None):
        """
        A domain defined for 3rd party data source in Profile Service

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dead_letter_queue_url: The URL of the SQS dead letter queue
        :param pulumi.Input[str] default_encryption_key: The default encryption key
        :param pulumi.Input[int] default_expiration_days: The default number of days until the data within the domain expires.
        :param pulumi.Input[str] domain_name: The unique name of the domain.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]] tags: The tags (keys and values) associated with the domain
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A domain defined for 3rd party data source in Profile Service

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dead_letter_queue_url: Optional[pulumi.Input[str]] = None,
                 default_encryption_key: Optional[pulumi.Input[str]] = None,
                 default_expiration_days: Optional[pulumi.Input[int]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainTagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["dead_letter_queue_url"] = dead_letter_queue_url
            __props__.__dict__["default_encryption_key"] = default_encryption_key
            __props__.__dict__["default_expiration_days"] = default_expiration_days
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_updated_at"] = None
        super(Domain, __self__).__init__(
            'aws-native:customerprofiles:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainArgs.__new__(DomainArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["dead_letter_queue_url"] = None
        __props__.__dict__["default_encryption_key"] = None
        __props__.__dict__["default_expiration_days"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["last_updated_at"] = None
        __props__.__dict__["tags"] = None
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time of this integration got created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL of the SQS dead letter queue
        """
        return pulumi.get(self, "dead_letter_queue_url")

    @property
    @pulumi.getter(name="defaultEncryptionKey")
    def default_encryption_key(self) -> pulumi.Output[Optional[str]]:
        """
        The default encryption key
        """
        return pulumi.get(self, "default_encryption_key")

    @property
    @pulumi.getter(name="defaultExpirationDays")
    def default_expiration_days(self) -> pulumi.Output[Optional[int]]:
        """
        The default number of days until the data within the domain expires.
        """
        return pulumi.get(self, "default_expiration_days")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The unique name of the domain.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> pulumi.Output[str]:
        """
        The time of this integration got last updated at
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DomainTag']]]:
        """
        The tags (keys and values) associated with the domain
        """
        return pulumi.get(self, "tags")

