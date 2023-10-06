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

__all__ = ['PrefixListArgs', 'PrefixList']

@pulumi.input_type
class PrefixListArgs:
    def __init__(__self__, *,
                 address_family: pulumi.Input['PrefixListAddressFamily'],
                 max_entries: pulumi.Input[int],
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListTagArgs']]]] = None):
        """
        The set of arguments for constructing a PrefixList resource.
        :param pulumi.Input['PrefixListAddressFamily'] address_family: Ip Version of Prefix List.
        :param pulumi.Input[int] max_entries: Max Entries of Prefix List.
        :param pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]] entries: Entries of Prefix List.
        :param pulumi.Input[str] prefix_list_name: Name of Prefix List.
        :param pulumi.Input[Sequence[pulumi.Input['PrefixListTagArgs']]] tags: Tags for Prefix List
        """
        PrefixListArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_family=address_family,
            max_entries=max_entries,
            entries=entries,
            prefix_list_name=prefix_list_name,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_family: pulumi.Input['PrefixListAddressFamily'],
             max_entries: pulumi.Input[int],
             entries: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]] = None,
             prefix_list_name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListTagArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("address_family", address_family)
        _setter("max_entries", max_entries)
        if entries is not None:
            _setter("entries", entries)
        if prefix_list_name is not None:
            _setter("prefix_list_name", prefix_list_name)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Input['PrefixListAddressFamily']:
        """
        Ip Version of Prefix List.
        """
        return pulumi.get(self, "address_family")

    @address_family.setter
    def address_family(self, value: pulumi.Input['PrefixListAddressFamily']):
        pulumi.set(self, "address_family", value)

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> pulumi.Input[int]:
        """
        Max Entries of Prefix List.
        """
        return pulumi.get(self, "max_entries")

    @max_entries.setter
    def max_entries(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_entries", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]]:
        """
        Entries of Prefix List.
        """
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListEntryArgs']]]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter(name="prefixListName")
    def prefix_list_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Prefix List.
        """
        return pulumi.get(self, "prefix_list_name")

    @prefix_list_name.setter
    def prefix_list_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListTagArgs']]]]:
        """
        Tags for Prefix List
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrefixListTagArgs']]]]):
        pulumi.set(self, "tags", value)


class PrefixList(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_family: Optional[pulumi.Input['PrefixListAddressFamily']] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema of AWS::EC2::PrefixList Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['PrefixListAddressFamily'] address_family: Ip Version of Prefix List.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]] entries: Entries of Prefix List.
        :param pulumi.Input[int] max_entries: Max Entries of Prefix List.
        :param pulumi.Input[str] prefix_list_name: Name of Prefix List.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListTagArgs']]]] tags: Tags for Prefix List
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrefixListArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema of AWS::EC2::PrefixList Type

        :param str resource_name: The name of the resource.
        :param PrefixListArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrefixListArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            PrefixListArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_family: Optional[pulumi.Input['PrefixListAddressFamily']] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListEntryArgs']]]]] = None,
                 max_entries: Optional[pulumi.Input[int]] = None,
                 prefix_list_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrefixListTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrefixListArgs.__new__(PrefixListArgs)

            if address_family is None and not opts.urn:
                raise TypeError("Missing required property 'address_family'")
            __props__.__dict__["address_family"] = address_family
            __props__.__dict__["entries"] = entries
            if max_entries is None and not opts.urn:
                raise TypeError("Missing required property 'max_entries'")
            __props__.__dict__["max_entries"] = max_entries
            __props__.__dict__["prefix_list_name"] = prefix_list_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["owner_id"] = None
            __props__.__dict__["prefix_list_id"] = None
            __props__.__dict__["version"] = None
        super(PrefixList, __self__).__init__(
            'aws-native:ec2:PrefixList',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrefixList':
        """
        Get an existing PrefixList resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrefixListArgs.__new__(PrefixListArgs)

        __props__.__dict__["address_family"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["entries"] = None
        __props__.__dict__["max_entries"] = None
        __props__.__dict__["owner_id"] = None
        __props__.__dict__["prefix_list_id"] = None
        __props__.__dict__["prefix_list_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["version"] = None
        return PrefixList(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressFamily")
    def address_family(self) -> pulumi.Output['PrefixListAddressFamily']:
        """
        Ip Version of Prefix List.
        """
        return pulumi.get(self, "address_family")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Prefix List.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def entries(self) -> pulumi.Output[Optional[Sequence['outputs.PrefixListEntry']]]:
        """
        Entries of Prefix List.
        """
        return pulumi.get(self, "entries")

    @property
    @pulumi.getter(name="maxEntries")
    def max_entries(self) -> pulumi.Output[int]:
        """
        Max Entries of Prefix List.
        """
        return pulumi.get(self, "max_entries")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        Owner Id of Prefix List.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> pulumi.Output[str]:
        """
        Id of Prefix List.
        """
        return pulumi.get(self, "prefix_list_id")

    @property
    @pulumi.getter(name="prefixListName")
    def prefix_list_name(self) -> pulumi.Output[str]:
        """
        Name of Prefix List.
        """
        return pulumi.get(self, "prefix_list_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PrefixListTag']]]:
        """
        Tags for Prefix List
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        Version of Prefix List.
        """
        return pulumi.get(self, "version")

