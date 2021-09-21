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

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 role: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 user_name: pulumi.Input[str],
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['UserHomeDirectoryMapEntryArgs']]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input['UserPosixProfileArgs']] = None,
                 ssh_public_keys: Optional[pulumi.Input[Sequence[pulumi.Input['UserSshPublicKeyArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]]] = None):
        """
        The set of arguments for constructing a User resource.
        """
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "server_id", server_id)
        pulumi.set(__self__, "user_name", user_name)
        if home_directory is not None:
            pulumi.set(__self__, "home_directory", home_directory)
        if home_directory_mappings is not None:
            pulumi.set(__self__, "home_directory_mappings", home_directory_mappings)
        if home_directory_type is not None:
            pulumi.set(__self__, "home_directory_type", home_directory_type)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if posix_profile is not None:
            pulumi.set(__self__, "posix_profile", posix_profile)
        if ssh_public_keys is not None:
            pulumi.set(__self__, "ssh_public_keys", ssh_public_keys)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "home_directory")

    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory", value)

    @property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserHomeDirectoryMapEntryArgs']]]]:
        return pulumi.get(self, "home_directory_mappings")

    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserHomeDirectoryMapEntryArgs']]]]):
        pulumi.set(self, "home_directory_mappings", value)

    @property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "home_directory_type")

    @home_directory_type.setter
    def home_directory_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_directory_type", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> Optional[pulumi.Input['UserPosixProfileArgs']]:
        return pulumi.get(self, "posix_profile")

    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input['UserPosixProfileArgs']]):
        pulumi.set(self, "posix_profile", value)

    @property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserSshPublicKeyArgs']]]]:
        return pulumi.get(self, "ssh_public_keys")

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserSshPublicKeyArgs']]]]):
        pulumi.set(self, "ssh_public_keys", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""User is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class User(pulumi.CustomResource):
    warnings.warn("""User is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserHomeDirectoryMapEntryArgs']]]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input[pulumi.InputType['UserPosixProfileArgs']]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 ssh_public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserSshPublicKeyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserTagArgs']]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Transfer::User

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Transfer::User

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 home_directory: Optional[pulumi.Input[str]] = None,
                 home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserHomeDirectoryMapEntryArgs']]]]] = None,
                 home_directory_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 posix_profile: Optional[pulumi.Input[pulumi.InputType['UserPosixProfileArgs']]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 ssh_public_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserSshPublicKeyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserTagArgs']]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""User is deprecated: User is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["home_directory"] = home_directory
            __props__.__dict__["home_directory_mappings"] = home_directory_mappings
            __props__.__dict__["home_directory_type"] = home_directory_type
            __props__.__dict__["policy"] = policy
            __props__.__dict__["posix_profile"] = posix_profile
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            __props__.__dict__["ssh_public_keys"] = ssh_public_keys
            __props__.__dict__["tags"] = tags
            if user_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_name'")
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["arn"] = None
        super(User, __self__).__init__(
            'aws-native:transfer:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserArgs.__new__(UserArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["home_directory"] = None
        __props__.__dict__["home_directory_mappings"] = None
        __props__.__dict__["home_directory_type"] = None
        __props__.__dict__["policy"] = None
        __props__.__dict__["posix_profile"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["server_id"] = None
        __props__.__dict__["ssh_public_keys"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_name"] = None
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "home_directory")

    @property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> pulumi.Output[Optional[Sequence['outputs.UserHomeDirectoryMapEntry']]]:
        return pulumi.get(self, "home_directory_mappings")

    @property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "home_directory_type")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> pulumi.Output[Optional['outputs.UserPosixProfile']]:
        return pulumi.get(self, "posix_profile")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="sshPublicKeys")
    def ssh_public_keys(self) -> pulumi.Output[Optional[Sequence['outputs.UserSshPublicKey']]]:
        return pulumi.get(self, "ssh_public_keys")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.UserTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "user_name")

