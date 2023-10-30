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

__all__ = ['UserPoolResourceServerArgs', 'UserPoolResourceServer']

@pulumi.input_type
class UserPoolResourceServerArgs:
    def __init__(__self__, *,
                 identifier: pulumi.Input[str],
                 user_pool_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input['UserPoolResourceServerResourceServerScopeTypeArgs']]]] = None):
        """
        The set of arguments for constructing a UserPoolResourceServer resource.
        """
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "user_pool_id", user_pool_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identifier")

    @identifier.setter
    def identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "identifier", value)

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_pool_id")

    @user_pool_id.setter
    def user_pool_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_pool_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserPoolResourceServerResourceServerScopeTypeArgs']]]]:
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserPoolResourceServerResourceServerScopeTypeArgs']]]]):
        pulumi.set(self, "scopes", value)


warnings.warn("""UserPoolResourceServer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class UserPoolResourceServer(pulumi.CustomResource):
    warnings.warn("""UserPoolResourceServer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserPoolResourceServerResourceServerScopeTypeArgs']]]]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Cognito::UserPoolResourceServer

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserPoolResourceServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Cognito::UserPoolResourceServer

        :param str resource_name: The name of the resource.
        :param UserPoolResourceServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserPoolResourceServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identifier: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserPoolResourceServerResourceServerScopeTypeArgs']]]]] = None,
                 user_pool_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""UserPoolResourceServer is deprecated: UserPoolResourceServer is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserPoolResourceServerArgs.__new__(UserPoolResourceServerArgs)

            if identifier is None and not opts.urn:
                raise TypeError("Missing required property 'identifier'")
            __props__.__dict__["identifier"] = identifier
            __props__.__dict__["name"] = name
            __props__.__dict__["scopes"] = scopes
            if user_pool_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_pool_id'")
            __props__.__dict__["user_pool_id"] = user_pool_id
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["identifier", "user_pool_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(UserPoolResourceServer, __self__).__init__(
            'aws-native:cognito:UserPoolResourceServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserPoolResourceServer':
        """
        Get an existing UserPoolResourceServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserPoolResourceServerArgs.__new__(UserPoolResourceServerArgs)

        __props__.__dict__["identifier"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["user_pool_id"] = None
        return UserPoolResourceServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence['outputs.UserPoolResourceServerResourceServerScopeType']]]:
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter(name="userPoolId")
    def user_pool_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_pool_id")

