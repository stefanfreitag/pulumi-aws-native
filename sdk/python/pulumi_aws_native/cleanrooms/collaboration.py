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

__all__ = ['CollaborationArgs', 'Collaboration']

@pulumi.input_type
class CollaborationArgs:
    def __init__(__self__, *,
                 creator_display_name: pulumi.Input[str],
                 creator_member_abilities: pulumi.Input[Sequence[pulumi.Input['CollaborationMemberAbility']]],
                 description: pulumi.Input[str],
                 members: pulumi.Input[Sequence[pulumi.Input['CollaborationMemberSpecificationArgs']]],
                 query_log_status: pulumi.Input['CollaborationQueryLogStatus'],
                 data_encryption_metadata: Optional[pulumi.Input['CollaborationDataEncryptionMetadataArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CollaborationTagArgs']]]] = None):
        """
        The set of arguments for constructing a Collaboration resource.
        :param pulumi.Input[Sequence[pulumi.Input['CollaborationTagArgs']]] tags: An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        pulumi.set(__self__, "creator_display_name", creator_display_name)
        pulumi.set(__self__, "creator_member_abilities", creator_member_abilities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "members", members)
        pulumi.set(__self__, "query_log_status", query_log_status)
        if data_encryption_metadata is not None:
            pulumi.set(__self__, "data_encryption_metadata", data_encryption_metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="creatorDisplayName")
    def creator_display_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "creator_display_name")

    @creator_display_name.setter
    def creator_display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "creator_display_name", value)

    @property
    @pulumi.getter(name="creatorMemberAbilities")
    def creator_member_abilities(self) -> pulumi.Input[Sequence[pulumi.Input['CollaborationMemberAbility']]]:
        return pulumi.get(self, "creator_member_abilities")

    @creator_member_abilities.setter
    def creator_member_abilities(self, value: pulumi.Input[Sequence[pulumi.Input['CollaborationMemberAbility']]]):
        pulumi.set(self, "creator_member_abilities", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input['CollaborationMemberSpecificationArgs']]]:
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input['CollaborationMemberSpecificationArgs']]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> pulumi.Input['CollaborationQueryLogStatus']:
        return pulumi.get(self, "query_log_status")

    @query_log_status.setter
    def query_log_status(self, value: pulumi.Input['CollaborationQueryLogStatus']):
        pulumi.set(self, "query_log_status", value)

    @property
    @pulumi.getter(name="dataEncryptionMetadata")
    def data_encryption_metadata(self) -> Optional[pulumi.Input['CollaborationDataEncryptionMetadataArgs']]:
        return pulumi.get(self, "data_encryption_metadata")

    @data_encryption_metadata.setter
    def data_encryption_metadata(self, value: Optional[pulumi.Input['CollaborationDataEncryptionMetadataArgs']]):
        pulumi.set(self, "data_encryption_metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CollaborationTagArgs']]]]:
        """
        An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CollaborationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Collaboration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creator_display_name: Optional[pulumi.Input[str]] = None,
                 creator_member_abilities: Optional[pulumi.Input[Sequence[pulumi.Input['CollaborationMemberAbility']]]] = None,
                 data_encryption_metadata: Optional[pulumi.Input[pulumi.InputType['CollaborationDataEncryptionMetadataArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollaborationMemberSpecificationArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_log_status: Optional[pulumi.Input['CollaborationQueryLogStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollaborationTagArgs']]]]] = None,
                 __props__=None):
        """
        Represents a collaboration between AWS accounts that allows for secure data collaboration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollaborationTagArgs']]]] tags: An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CollaborationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a collaboration between AWS accounts that allows for secure data collaboration

        :param str resource_name: The name of the resource.
        :param CollaborationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CollaborationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creator_display_name: Optional[pulumi.Input[str]] = None,
                 creator_member_abilities: Optional[pulumi.Input[Sequence[pulumi.Input['CollaborationMemberAbility']]]] = None,
                 data_encryption_metadata: Optional[pulumi.Input[pulumi.InputType['CollaborationDataEncryptionMetadataArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollaborationMemberSpecificationArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query_log_status: Optional[pulumi.Input['CollaborationQueryLogStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CollaborationTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CollaborationArgs.__new__(CollaborationArgs)

            if creator_display_name is None and not opts.urn:
                raise TypeError("Missing required property 'creator_display_name'")
            __props__.__dict__["creator_display_name"] = creator_display_name
            if creator_member_abilities is None and not opts.urn:
                raise TypeError("Missing required property 'creator_member_abilities'")
            __props__.__dict__["creator_member_abilities"] = creator_member_abilities
            __props__.__dict__["data_encryption_metadata"] = data_encryption_metadata
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__.__dict__["members"] = members
            __props__.__dict__["name"] = name
            if query_log_status is None and not opts.urn:
                raise TypeError("Missing required property 'query_log_status'")
            __props__.__dict__["query_log_status"] = query_log_status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["collaboration_identifier"] = None
        super(Collaboration, __self__).__init__(
            'aws-native:cleanrooms:Collaboration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Collaboration':
        """
        Get an existing Collaboration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CollaborationArgs.__new__(CollaborationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["collaboration_identifier"] = None
        __props__.__dict__["creator_display_name"] = None
        __props__.__dict__["creator_member_abilities"] = None
        __props__.__dict__["data_encryption_metadata"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["members"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["query_log_status"] = None
        __props__.__dict__["tags"] = None
        return Collaboration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="collaborationIdentifier")
    def collaboration_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "collaboration_identifier")

    @property
    @pulumi.getter(name="creatorDisplayName")
    def creator_display_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creator_display_name")

    @property
    @pulumi.getter(name="creatorMemberAbilities")
    def creator_member_abilities(self) -> pulumi.Output[Sequence['CollaborationMemberAbility']]:
        return pulumi.get(self, "creator_member_abilities")

    @property
    @pulumi.getter(name="dataEncryptionMetadata")
    def data_encryption_metadata(self) -> pulumi.Output[Optional['outputs.CollaborationDataEncryptionMetadata']]:
        return pulumi.get(self, "data_encryption_metadata")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence['outputs.CollaborationMemberSpecification']]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queryLogStatus")
    def query_log_status(self) -> pulumi.Output['CollaborationQueryLogStatus']:
        return pulumi.get(self, "query_log_status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CollaborationTag']]]:
        """
        An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        """
        return pulumi.get(self, "tags")

