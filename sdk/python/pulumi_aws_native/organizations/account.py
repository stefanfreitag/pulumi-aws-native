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
from ._enums import *

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 parent_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] email: The email address of the owner to assign to the new member account.
        :param pulumi.Input[str] account_name: The friendly name of the member account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] parent_ids: List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.
        :param pulumi.Input[str] role_name: The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.
        """
        pulumi.set(__self__, "email", email)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if parent_ids is not None:
            pulumi.set(__self__, "parent_ids", parent_ids)
        if role_name is not None:
            pulumi.set(__self__, "role_name", role_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        The email address of the owner to assign to the new member account.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly name of the member account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="parentIds")
    def parent_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.
        """
        return pulumi.get(self, "parent_ids")

    @parent_ids.setter
    def parent_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "parent_ids", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 parent_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        You can use AWS::Organizations::Account to manage accounts in organization.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The friendly name of the member account.
        :param pulumi.Input[str] email: The email address of the owner to assign to the new member account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] parent_ids: List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.
        :param pulumi.Input[str] role_name: The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        You can use AWS::Organizations::Account to manage accounts in organization.

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 parent_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_name"] = account_name
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["parent_ids"] = parent_ids
            __props__.__dict__["role_name"] = role_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["account_id"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["joined_method"] = None
            __props__.__dict__["joined_timestamp"] = None
            __props__.__dict__["status"] = None
        super(Account, __self__).__init__(
            'aws-native:organizations:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccountArgs.__new__(AccountArgs)

        __props__.__dict__["account_id"] = None
        __props__.__dict__["account_name"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["email"] = None
        __props__.__dict__["joined_method"] = None
        __props__.__dict__["joined_timestamp"] = None
        __props__.__dict__["parent_ids"] = None
        __props__.__dict__["role_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        If the account was created successfully, the unique identifier (ID) of the new account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        The friendly name of the member account.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The email address of the owner to assign to the new member account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> pulumi.Output['AccountJoinedMethod']:
        """
        The method by which the account joined the organization.
        """
        return pulumi.get(self, "joined_method")

    @property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> pulumi.Output[str]:
        """
        The date the account became a part of the organization.
        """
        return pulumi.get(self, "joined_timestamp")

    @property
    @pulumi.getter(name="parentIds")
    def parent_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.
        """
        return pulumi.get(self, "parent_ids")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['AccountStatus']:
        """
        The status of the account in the organization.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.
        """
        return pulumi.get(self, "tags")

