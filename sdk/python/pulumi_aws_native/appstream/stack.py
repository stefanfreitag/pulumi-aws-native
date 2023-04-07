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

__all__ = ['StackArgs', 'Stack']

@pulumi.input_type
class StackArgs:
    def __init__(__self__, *,
                 access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input['StackAccessEndpointArgs']]]] = None,
                 application_settings: Optional[pulumi.Input['StackApplicationSettingsArgs']] = None,
                 attributes_to_delete: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delete_storage_connectors: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feedback_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input['StackStorageConnectorArgs']]]] = None,
                 streaming_experience_settings: Optional[pulumi.Input['StackStreamingExperienceSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]] = None,
                 user_settings: Optional[pulumi.Input[Sequence[pulumi.Input['StackUserSettingArgs']]]] = None):
        """
        The set of arguments for constructing a Stack resource.
        """
        if access_endpoints is not None:
            pulumi.set(__self__, "access_endpoints", access_endpoints)
        if application_settings is not None:
            pulumi.set(__self__, "application_settings", application_settings)
        if attributes_to_delete is not None:
            pulumi.set(__self__, "attributes_to_delete", attributes_to_delete)
        if delete_storage_connectors is not None:
            pulumi.set(__self__, "delete_storage_connectors", delete_storage_connectors)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if embed_host_domains is not None:
            pulumi.set(__self__, "embed_host_domains", embed_host_domains)
        if feedback_url is not None:
            pulumi.set(__self__, "feedback_url", feedback_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if redirect_url is not None:
            pulumi.set(__self__, "redirect_url", redirect_url)
        if storage_connectors is not None:
            pulumi.set(__self__, "storage_connectors", storage_connectors)
        if streaming_experience_settings is not None:
            pulumi.set(__self__, "streaming_experience_settings", streaming_experience_settings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_settings is not None:
            pulumi.set(__self__, "user_settings", user_settings)

    @property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackAccessEndpointArgs']]]]:
        return pulumi.get(self, "access_endpoints")

    @access_endpoints.setter
    def access_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackAccessEndpointArgs']]]]):
        pulumi.set(self, "access_endpoints", value)

    @property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> Optional[pulumi.Input['StackApplicationSettingsArgs']]:
        return pulumi.get(self, "application_settings")

    @application_settings.setter
    def application_settings(self, value: Optional[pulumi.Input['StackApplicationSettingsArgs']]):
        pulumi.set(self, "application_settings", value)

    @property
    @pulumi.getter(name="attributesToDelete")
    def attributes_to_delete(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "attributes_to_delete")

    @attributes_to_delete.setter
    def attributes_to_delete(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "attributes_to_delete", value)

    @property
    @pulumi.getter(name="deleteStorageConnectors")
    def delete_storage_connectors(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "delete_storage_connectors")

    @delete_storage_connectors.setter
    def delete_storage_connectors(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_storage_connectors", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="embedHostDomains")
    def embed_host_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "embed_host_domains")

    @embed_host_domains.setter
    def embed_host_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "embed_host_domains", value)

    @property
    @pulumi.getter(name="feedbackURL")
    def feedback_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "feedback_url")

    @feedback_url.setter
    def feedback_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "feedback_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="redirectURL")
    def redirect_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "redirect_url")

    @redirect_url.setter
    def redirect_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_url", value)

    @property
    @pulumi.getter(name="storageConnectors")
    def storage_connectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackStorageConnectorArgs']]]]:
        return pulumi.get(self, "storage_connectors")

    @storage_connectors.setter
    def storage_connectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackStorageConnectorArgs']]]]):
        pulumi.set(self, "storage_connectors", value)

    @property
    @pulumi.getter(name="streamingExperienceSettings")
    def streaming_experience_settings(self) -> Optional[pulumi.Input['StackStreamingExperienceSettingsArgs']]:
        return pulumi.get(self, "streaming_experience_settings")

    @streaming_experience_settings.setter
    def streaming_experience_settings(self, value: Optional[pulumi.Input['StackStreamingExperienceSettingsArgs']]):
        pulumi.set(self, "streaming_experience_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StackUserSettingArgs']]]]:
        return pulumi.get(self, "user_settings")

    @user_settings.setter
    def user_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StackUserSettingArgs']]]]):
        pulumi.set(self, "user_settings", value)


warnings.warn("""Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Stack(pulumi.CustomResource):
    warnings.warn("""Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackAccessEndpointArgs']]]]] = None,
                 application_settings: Optional[pulumi.Input[pulumi.InputType['StackApplicationSettingsArgs']]] = None,
                 attributes_to_delete: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delete_storage_connectors: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feedback_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackStorageConnectorArgs']]]]] = None,
                 streaming_experience_settings: Optional[pulumi.Input[pulumi.InputType['StackStreamingExperienceSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackTagArgs']]]]] = None,
                 user_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackUserSettingArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppStream::Stack

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[StackArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppStream::Stack

        :param str resource_name: The name of the resource.
        :param StackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackAccessEndpointArgs']]]]] = None,
                 application_settings: Optional[pulumi.Input[pulumi.InputType['StackApplicationSettingsArgs']]] = None,
                 attributes_to_delete: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delete_storage_connectors: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 embed_host_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 feedback_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 redirect_url: Optional[pulumi.Input[str]] = None,
                 storage_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackStorageConnectorArgs']]]]] = None,
                 streaming_experience_settings: Optional[pulumi.Input[pulumi.InputType['StackStreamingExperienceSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackTagArgs']]]]] = None,
                 user_settings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackUserSettingArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Stack is deprecated: Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StackArgs.__new__(StackArgs)

            __props__.__dict__["access_endpoints"] = access_endpoints
            __props__.__dict__["application_settings"] = application_settings
            __props__.__dict__["attributes_to_delete"] = attributes_to_delete
            __props__.__dict__["delete_storage_connectors"] = delete_storage_connectors
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["embed_host_domains"] = embed_host_domains
            __props__.__dict__["feedback_url"] = feedback_url
            __props__.__dict__["name"] = name
            __props__.__dict__["redirect_url"] = redirect_url
            __props__.__dict__["storage_connectors"] = storage_connectors
            __props__.__dict__["streaming_experience_settings"] = streaming_experience_settings
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_settings"] = user_settings
        super(Stack, __self__).__init__(
            'aws-native:appstream:Stack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Stack':
        """
        Get an existing Stack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StackArgs.__new__(StackArgs)

        __props__.__dict__["access_endpoints"] = None
        __props__.__dict__["application_settings"] = None
        __props__.__dict__["attributes_to_delete"] = None
        __props__.__dict__["delete_storage_connectors"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["embed_host_domains"] = None
        __props__.__dict__["feedback_url"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["redirect_url"] = None
        __props__.__dict__["storage_connectors"] = None
        __props__.__dict__["streaming_experience_settings"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_settings"] = None
        return Stack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessEndpoints")
    def access_endpoints(self) -> pulumi.Output[Optional[Sequence['outputs.StackAccessEndpoint']]]:
        return pulumi.get(self, "access_endpoints")

    @property
    @pulumi.getter(name="applicationSettings")
    def application_settings(self) -> pulumi.Output[Optional['outputs.StackApplicationSettings']]:
        return pulumi.get(self, "application_settings")

    @property
    @pulumi.getter(name="attributesToDelete")
    def attributes_to_delete(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "attributes_to_delete")

    @property
    @pulumi.getter(name="deleteStorageConnectors")
    def delete_storage_connectors(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "delete_storage_connectors")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="embedHostDomains")
    def embed_host_domains(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "embed_host_domains")

    @property
    @pulumi.getter(name="feedbackURL")
    def feedback_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "feedback_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="redirectURL")
    def redirect_url(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "redirect_url")

    @property
    @pulumi.getter(name="storageConnectors")
    def storage_connectors(self) -> pulumi.Output[Optional[Sequence['outputs.StackStorageConnector']]]:
        return pulumi.get(self, "storage_connectors")

    @property
    @pulumi.getter(name="streamingExperienceSettings")
    def streaming_experience_settings(self) -> pulumi.Output[Optional['outputs.StackStreamingExperienceSettings']]:
        return pulumi.get(self, "streaming_experience_settings")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.StackTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> pulumi.Output[Optional[Sequence['outputs.StackUserSetting']]]:
        return pulumi.get(self, "user_settings")

