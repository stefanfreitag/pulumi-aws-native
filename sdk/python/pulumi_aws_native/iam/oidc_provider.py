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

__all__ = ['OidcProviderArgs', 'OidcProvider']

@pulumi.input_type
class OidcProviderArgs:
    def __init__(__self__, *,
                 thumbprint_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 client_id_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['OidcProviderTagArgs']]]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OidcProvider resource.
        """
        OidcProviderArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            thumbprint_list=thumbprint_list,
            client_id_list=client_id_list,
            tags=tags,
            url=url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             thumbprint_list: pulumi.Input[Sequence[pulumi.Input[str]]],
             client_id_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['OidcProviderTagArgs']]]] = None,
             url: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("thumbprint_list", thumbprint_list)
        if client_id_list is not None:
            _setter("client_id_list", client_id_list)
        if tags is not None:
            _setter("tags", tags)
        if url is not None:
            _setter("url", url)

    @property
    @pulumi.getter(name="thumbprintList")
    def thumbprint_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "thumbprint_list")

    @thumbprint_list.setter
    def thumbprint_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "thumbprint_list", value)

    @property
    @pulumi.getter(name="clientIdList")
    def client_id_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "client_id_list")

    @client_id_list.setter
    def client_id_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "client_id_list", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OidcProviderTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OidcProviderTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class OidcProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OidcProviderTagArgs']]]]] = None,
                 thumbprint_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IAM::OIDCProvider

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OidcProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IAM::OIDCProvider

        :param str resource_name: The name of the resource.
        :param OidcProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OidcProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            OidcProviderArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OidcProviderTagArgs']]]]] = None,
                 thumbprint_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OidcProviderArgs.__new__(OidcProviderArgs)

            __props__.__dict__["client_id_list"] = client_id_list
            __props__.__dict__["tags"] = tags
            if thumbprint_list is None and not opts.urn:
                raise TypeError("Missing required property 'thumbprint_list'")
            __props__.__dict__["thumbprint_list"] = thumbprint_list
            __props__.__dict__["url"] = url
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["url"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(OidcProvider, __self__).__init__(
            'aws-native:iam:OidcProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OidcProvider':
        """
        Get an existing OidcProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OidcProviderArgs.__new__(OidcProviderArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["client_id_list"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["thumbprint_list"] = None
        __props__.__dict__["url"] = None
        return OidcProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the OIDC provider
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clientIdList")
    def client_id_list(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "client_id_list")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.OidcProviderTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="thumbprintList")
    def thumbprint_list(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "thumbprint_list")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "url")

