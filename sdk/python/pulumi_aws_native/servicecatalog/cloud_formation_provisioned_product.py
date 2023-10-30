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

__all__ = ['CloudFormationProvisionedProductArgs', 'CloudFormationProvisionedProduct']

@pulumi.input_type
class CloudFormationProvisionedProductArgs:
    def __init__(__self__, *,
                 accept_language: Optional[pulumi.Input['CloudFormationProvisionedProductAcceptLanguage']] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 path_id: Optional[pulumi.Input[str]] = None,
                 path_name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 provisioned_product_name: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_id: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_name: Optional[pulumi.Input[str]] = None,
                 provisioning_parameters: Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProvisionedProductProvisioningParameterArgs']]]] = None,
                 provisioning_preferences: Optional[pulumi.Input['CloudFormationProvisionedProductProvisioningPreferencesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProvisionedProductTagArgs']]]] = None):
        """
        The set of arguments for constructing a CloudFormationProvisionedProduct resource.
        """
        if accept_language is not None:
            pulumi.set(__self__, "accept_language", accept_language)
        if notification_arns is not None:
            pulumi.set(__self__, "notification_arns", notification_arns)
        if path_id is not None:
            pulumi.set(__self__, "path_id", path_id)
        if path_name is not None:
            pulumi.set(__self__, "path_name", path_name)
        if product_id is not None:
            pulumi.set(__self__, "product_id", product_id)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)
        if provisioned_product_name is not None:
            pulumi.set(__self__, "provisioned_product_name", provisioned_product_name)
        if provisioning_artifact_id is not None:
            pulumi.set(__self__, "provisioning_artifact_id", provisioning_artifact_id)
        if provisioning_artifact_name is not None:
            pulumi.set(__self__, "provisioning_artifact_name", provisioning_artifact_name)
        if provisioning_parameters is not None:
            pulumi.set(__self__, "provisioning_parameters", provisioning_parameters)
        if provisioning_preferences is not None:
            pulumi.set(__self__, "provisioning_preferences", provisioning_preferences)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input['CloudFormationProvisionedProductAcceptLanguage']]:
        return pulumi.get(self, "accept_language")

    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input['CloudFormationProvisionedProductAcceptLanguage']]):
        pulumi.set(self, "accept_language", value)

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "notification_arns")

    @notification_arns.setter
    def notification_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_arns", value)

    @property
    @pulumi.getter(name="pathId")
    def path_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "path_id")

    @path_id.setter
    def path_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path_id", value)

    @property
    @pulumi.getter(name="pathName")
    def path_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "path_name")

    @path_name.setter
    def path_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path_name", value)

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "product_id")

    @product_id.setter
    def product_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_id", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_name", value)

    @property
    @pulumi.getter(name="provisionedProductName")
    def provisioned_product_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provisioned_product_name")

    @provisioned_product_name.setter
    def provisioned_product_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioned_product_name", value)

    @property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provisioning_artifact_id")

    @provisioning_artifact_id.setter
    def provisioning_artifact_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_artifact_id", value)

    @property
    @pulumi.getter(name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provisioning_artifact_name")

    @provisioning_artifact_name.setter
    def provisioning_artifact_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_artifact_name", value)

    @property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProvisionedProductProvisioningParameterArgs']]]]:
        return pulumi.get(self, "provisioning_parameters")

    @provisioning_parameters.setter
    def provisioning_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProvisionedProductProvisioningParameterArgs']]]]):
        pulumi.set(self, "provisioning_parameters", value)

    @property
    @pulumi.getter(name="provisioningPreferences")
    def provisioning_preferences(self) -> Optional[pulumi.Input['CloudFormationProvisionedProductProvisioningPreferencesArgs']]:
        return pulumi.get(self, "provisioning_preferences")

    @provisioning_preferences.setter
    def provisioning_preferences(self, value: Optional[pulumi.Input['CloudFormationProvisionedProductProvisioningPreferencesArgs']]):
        pulumi.set(self, "provisioning_preferences", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProvisionedProductTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CloudFormationProvisionedProductTagArgs']]]]):
        pulumi.set(self, "tags", value)


class CloudFormationProvisionedProduct(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input['CloudFormationProvisionedProductAcceptLanguage']] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 path_id: Optional[pulumi.Input[str]] = None,
                 path_name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 provisioned_product_name: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_id: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_name: Optional[pulumi.Input[str]] = None,
                 provisioning_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProvisionedProductProvisioningParameterArgs']]]]] = None,
                 provisioning_preferences: Optional[pulumi.Input[pulumi.InputType['CloudFormationProvisionedProductProvisioningPreferencesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProvisionedProductTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CloudFormationProvisionedProductArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct

        :param str resource_name: The name of the resource.
        :param CloudFormationProvisionedProductArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CloudFormationProvisionedProductArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accept_language: Optional[pulumi.Input['CloudFormationProvisionedProductAcceptLanguage']] = None,
                 notification_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 path_id: Optional[pulumi.Input[str]] = None,
                 path_name: Optional[pulumi.Input[str]] = None,
                 product_id: Optional[pulumi.Input[str]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 provisioned_product_name: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_id: Optional[pulumi.Input[str]] = None,
                 provisioning_artifact_name: Optional[pulumi.Input[str]] = None,
                 provisioning_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProvisionedProductProvisioningParameterArgs']]]]] = None,
                 provisioning_preferences: Optional[pulumi.Input[pulumi.InputType['CloudFormationProvisionedProductProvisioningPreferencesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CloudFormationProvisionedProductTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CloudFormationProvisionedProductArgs.__new__(CloudFormationProvisionedProductArgs)

            __props__.__dict__["accept_language"] = accept_language
            __props__.__dict__["notification_arns"] = notification_arns
            __props__.__dict__["path_id"] = path_id
            __props__.__dict__["path_name"] = path_name
            __props__.__dict__["product_id"] = product_id
            __props__.__dict__["product_name"] = product_name
            __props__.__dict__["provisioned_product_name"] = provisioned_product_name
            __props__.__dict__["provisioning_artifact_id"] = provisioning_artifact_id
            __props__.__dict__["provisioning_artifact_name"] = provisioning_artifact_name
            __props__.__dict__["provisioning_parameters"] = provisioning_parameters
            __props__.__dict__["provisioning_preferences"] = provisioning_preferences
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cloudformation_stack_arn"] = None
            __props__.__dict__["outputs"] = None
            __props__.__dict__["provisioned_product_id"] = None
            __props__.__dict__["record_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["notification_arns[*]", "provisioned_product_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CloudFormationProvisionedProduct, __self__).__init__(
            'aws-native:servicecatalog:CloudFormationProvisionedProduct',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CloudFormationProvisionedProduct':
        """
        Get an existing CloudFormationProvisionedProduct resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CloudFormationProvisionedProductArgs.__new__(CloudFormationProvisionedProductArgs)

        __props__.__dict__["accept_language"] = None
        __props__.__dict__["cloudformation_stack_arn"] = None
        __props__.__dict__["notification_arns"] = None
        __props__.__dict__["outputs"] = None
        __props__.__dict__["path_id"] = None
        __props__.__dict__["path_name"] = None
        __props__.__dict__["product_id"] = None
        __props__.__dict__["product_name"] = None
        __props__.__dict__["provisioned_product_id"] = None
        __props__.__dict__["provisioned_product_name"] = None
        __props__.__dict__["provisioning_artifact_id"] = None
        __props__.__dict__["provisioning_artifact_name"] = None
        __props__.__dict__["provisioning_parameters"] = None
        __props__.__dict__["provisioning_preferences"] = None
        __props__.__dict__["record_id"] = None
        __props__.__dict__["tags"] = None
        return CloudFormationProvisionedProduct(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional['CloudFormationProvisionedProductAcceptLanguage']]:
        return pulumi.get(self, "accept_language")

    @property
    @pulumi.getter(name="cloudformationStackArn")
    def cloudformation_stack_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cloudformation_stack_arn")

    @property
    @pulumi.getter(name="notificationArns")
    def notification_arns(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "notification_arns")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Any]:
        """
        List of key-value pair outputs.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="pathId")
    def path_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "path_id")

    @property
    @pulumi.getter(name="pathName")
    def path_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "path_name")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="provisionedProductId")
    def provisioned_product_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioned_product_id")

    @property
    @pulumi.getter(name="provisionedProductName")
    def provisioned_product_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "provisioned_product_name")

    @property
    @pulumi.getter(name="provisioningArtifactId")
    def provisioning_artifact_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "provisioning_artifact_id")

    @property
    @pulumi.getter(name="provisioningArtifactName")
    def provisioning_artifact_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "provisioning_artifact_name")

    @property
    @pulumi.getter(name="provisioningParameters")
    def provisioning_parameters(self) -> pulumi.Output[Optional[Sequence['outputs.CloudFormationProvisionedProductProvisioningParameter']]]:
        return pulumi.get(self, "provisioning_parameters")

    @property
    @pulumi.getter(name="provisioningPreferences")
    def provisioning_preferences(self) -> pulumi.Output[Optional['outputs.CloudFormationProvisionedProductProvisioningPreferences']]:
        return pulumi.get(self, "provisioning_preferences")

    @property
    @pulumi.getter(name="recordId")
    def record_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "record_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CloudFormationProvisionedProductTag']]]:
        return pulumi.get(self, "tags")

