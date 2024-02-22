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

__all__ = ['AgreementArgs', 'Agreement']

@pulumi.input_type
class AgreementArgs:
    def __init__(__self__, *,
                 access_role: pulumi.Input[str],
                 base_directory: pulumi.Input[str],
                 local_profile_id: pulumi.Input[str],
                 partner_profile_id: pulumi.Input[str],
                 server_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['AgreementStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Agreement resource.
        :param pulumi.Input[str] access_role: Specifies the access role for the agreement.
        :param pulumi.Input[str] base_directory: Specifies the base directory for the agreement.
        :param pulumi.Input[str] local_profile_id: A unique identifier for the local profile.
        :param pulumi.Input[str] partner_profile_id: A unique identifier for the partner profile.
        :param pulumi.Input[str] server_id: A unique identifier for the server.
        :param pulumi.Input[str] description: A textual description for the agreement.
        :param pulumi.Input['AgreementStatus'] status: Specifies the status of the agreement.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
        """
        pulumi.set(__self__, "access_role", access_role)
        pulumi.set(__self__, "base_directory", base_directory)
        pulumi.set(__self__, "local_profile_id", local_profile_id)
        pulumi.set(__self__, "partner_profile_id", partner_profile_id)
        pulumi.set(__self__, "server_id", server_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Input[str]:
        """
        Specifies the access role for the agreement.
        """
        return pulumi.get(self, "access_role")

    @access_role.setter
    def access_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_role", value)

    @property
    @pulumi.getter(name="baseDirectory")
    def base_directory(self) -> pulumi.Input[str]:
        """
        Specifies the base directory for the agreement.
        """
        return pulumi.get(self, "base_directory")

    @base_directory.setter
    def base_directory(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_directory", value)

    @property
    @pulumi.getter(name="localProfileId")
    def local_profile_id(self) -> pulumi.Input[str]:
        """
        A unique identifier for the local profile.
        """
        return pulumi.get(self, "local_profile_id")

    @local_profile_id.setter
    def local_profile_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "local_profile_id", value)

    @property
    @pulumi.getter(name="partnerProfileId")
    def partner_profile_id(self) -> pulumi.Input[str]:
        """
        A unique identifier for the partner profile.
        """
        return pulumi.get(self, "partner_profile_id")

    @partner_profile_id.setter
    def partner_profile_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "partner_profile_id", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        A unique identifier for the server.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A textual description for the agreement.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['AgreementStatus']]:
        """
        Specifies the status of the agreement.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['AgreementStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Agreement(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_role: Optional[pulumi.Input[str]] = None,
                 base_directory: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 local_profile_id: Optional[pulumi.Input[str]] = None,
                 partner_profile_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['AgreementStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Transfer::Agreement

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_role: Specifies the access role for the agreement.
        :param pulumi.Input[str] base_directory: Specifies the base directory for the agreement.
        :param pulumi.Input[str] description: A textual description for the agreement.
        :param pulumi.Input[str] local_profile_id: A unique identifier for the local profile.
        :param pulumi.Input[str] partner_profile_id: A unique identifier for the partner profile.
        :param pulumi.Input[str] server_id: A unique identifier for the server.
        :param pulumi.Input['AgreementStatus'] status: Specifies the status of the agreement.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgreementArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Transfer::Agreement

        :param str resource_name: The name of the resource.
        :param AgreementArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgreementArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_role: Optional[pulumi.Input[str]] = None,
                 base_directory: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 local_profile_id: Optional[pulumi.Input[str]] = None,
                 partner_profile_id: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['AgreementStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgreementArgs.__new__(AgreementArgs)

            if access_role is None and not opts.urn:
                raise TypeError("Missing required property 'access_role'")
            __props__.__dict__["access_role"] = access_role
            if base_directory is None and not opts.urn:
                raise TypeError("Missing required property 'base_directory'")
            __props__.__dict__["base_directory"] = base_directory
            __props__.__dict__["description"] = description
            if local_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'local_profile_id'")
            __props__.__dict__["local_profile_id"] = local_profile_id
            if partner_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'partner_profile_id'")
            __props__.__dict__["partner_profile_id"] = partner_profile_id
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["agreement_id"] = None
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["server_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Agreement, __self__).__init__(
            'aws-native:transfer:Agreement',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Agreement':
        """
        Get an existing Agreement resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgreementArgs.__new__(AgreementArgs)

        __props__.__dict__["access_role"] = None
        __props__.__dict__["agreement_id"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["base_directory"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["local_profile_id"] = None
        __props__.__dict__["partner_profile_id"] = None
        __props__.__dict__["server_id"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return Agreement(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessRole")
    def access_role(self) -> pulumi.Output[str]:
        """
        Specifies the access role for the agreement.
        """
        return pulumi.get(self, "access_role")

    @property
    @pulumi.getter(name="agreementId")
    def agreement_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the agreement.
        """
        return pulumi.get(self, "agreement_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Specifies the unique Amazon Resource Name (ARN) for the agreement.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="baseDirectory")
    def base_directory(self) -> pulumi.Output[str]:
        """
        Specifies the base directory for the agreement.
        """
        return pulumi.get(self, "base_directory")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A textual description for the agreement.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="localProfileId")
    def local_profile_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the local profile.
        """
        return pulumi.get(self, "local_profile_id")

    @property
    @pulumi.getter(name="partnerProfileId")
    def partner_profile_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the partner profile.
        """
        return pulumi.get(self, "partner_profile_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the server.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['AgreementStatus']]:
        """
        Specifies the status of the agreement.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
        """
        return pulumi.get(self, "tags")

