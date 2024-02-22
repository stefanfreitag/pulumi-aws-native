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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str],
                 application_type: pulumi.Input['ApplicationType'],
                 credentials: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationCredentialArgs']]]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sap_instance_number: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags of a SystemsManagerSAP application.
        """
        pulumi.set(__self__, "application_id", application_id)
        pulumi.set(__self__, "application_type", application_type)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if instances is not None:
            pulumi.set(__self__, "instances", instances)
        if sap_instance_number is not None:
            pulumi.set(__self__, "sap_instance_number", sap_instance_number)
        if sid is not None:
            pulumi.set(__self__, "sid", sid)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> pulumi.Input['ApplicationType']:
        return pulumi.get(self, "application_type")

    @application_type.setter
    def application_type(self, value: pulumi.Input['ApplicationType']):
        pulumi.set(self, "application_type", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationCredentialArgs']]]]:
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationCredentialArgs']]]]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter
    def instances(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "instances")

    @instances.setter
    def instances(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instances", value)

    @property
    @pulumi.getter(name="sapInstanceNumber")
    def sap_instance_number(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sap_instance_number")

    @sap_instance_number.setter
    def sap_instance_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sap_instance_number", value)

    @property
    @pulumi.getter
    def sid(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sid")

    @sid.setter
    def sid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sid", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags of a SystemsManagerSAP application.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 application_type: Optional[pulumi.Input['ApplicationType']] = None,
                 credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationCredentialArgs']]]]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sap_instance_number: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::SystemsManagerSAP::Application

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The tags of a SystemsManagerSAP application.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::SystemsManagerSAP::Application

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 application_type: Optional[pulumi.Input['ApplicationType']] = None,
                 credentials: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationCredentialArgs']]]]] = None,
                 instances: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sap_instance_number: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            if application_id is None and not opts.urn:
                raise TypeError("Missing required property 'application_id'")
            __props__.__dict__["application_id"] = application_id
            if application_type is None and not opts.urn:
                raise TypeError("Missing required property 'application_type'")
            __props__.__dict__["application_type"] = application_type
            __props__.__dict__["credentials"] = credentials
            __props__.__dict__["instances"] = instances
            __props__.__dict__["sap_instance_number"] = sap_instance_number
            __props__.__dict__["sid"] = sid
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["credentials[*]", "instances[*]", "sap_instance_number", "sid"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Application, __self__).__init__(
            'aws-native:systemsmanagersap:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationArgs.__new__(ApplicationArgs)

        __props__.__dict__["application_id"] = None
        __props__.__dict__["application_type"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["credentials"] = None
        __props__.__dict__["instances"] = None
        __props__.__dict__["sap_instance_number"] = None
        __props__.__dict__["sid"] = None
        __props__.__dict__["tags"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="applicationType")
    def application_type(self) -> pulumi.Output['ApplicationType']:
        return pulumi.get(self, "application_type")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Helix application
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationCredential']]]:
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="sapInstanceNumber")
    def sap_instance_number(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sap_instance_number")

    @property
    @pulumi.getter
    def sid(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags of a SystemsManagerSAP application.
        """
        return pulumi.get(self, "tags")

