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

__all__ = ['CertificateProviderArgs', 'CertificateProvider']

@pulumi.input_type
class CertificateProviderArgs:
    def __init__(__self__, *,
                 account_default_for_operations: pulumi.Input[Sequence[pulumi.Input['CertificateProviderOperation']]],
                 lambda_function_arn: pulumi.Input[str],
                 certificate_provider_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a CertificateProvider resource.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "account_default_for_operations", account_default_for_operations)
        pulumi.set(__self__, "lambda_function_arn", lambda_function_arn)
        if certificate_provider_name is not None:
            pulumi.set(__self__, "certificate_provider_name", certificate_provider_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accountDefaultForOperations")
    def account_default_for_operations(self) -> pulumi.Input[Sequence[pulumi.Input['CertificateProviderOperation']]]:
        return pulumi.get(self, "account_default_for_operations")

    @account_default_for_operations.setter
    def account_default_for_operations(self, value: pulumi.Input[Sequence[pulumi.Input['CertificateProviderOperation']]]):
        pulumi.set(self, "account_default_for_operations", value)

    @property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "lambda_function_arn")

    @lambda_function_arn.setter
    def lambda_function_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "lambda_function_arn", value)

    @property
    @pulumi.getter(name="certificateProviderName")
    def certificate_provider_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate_provider_name")

    @certificate_provider_name.setter
    def certificate_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_provider_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class CertificateProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_default_for_operations: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateProviderOperation']]]] = None,
                 certificate_provider_name: Optional[pulumi.Input[str]] = None,
                 lambda_function_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.

        :param str resource_name: The name of the resource.
        :param CertificateProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_default_for_operations: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateProviderOperation']]]] = None,
                 certificate_provider_name: Optional[pulumi.Input[str]] = None,
                 lambda_function_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateProviderArgs.__new__(CertificateProviderArgs)

            if account_default_for_operations is None and not opts.urn:
                raise TypeError("Missing required property 'account_default_for_operations'")
            __props__.__dict__["account_default_for_operations"] = account_default_for_operations
            __props__.__dict__["certificate_provider_name"] = certificate_provider_name
            if lambda_function_arn is None and not opts.urn:
                raise TypeError("Missing required property 'lambda_function_arn'")
            __props__.__dict__["lambda_function_arn"] = lambda_function_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["certificate_provider_name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CertificateProvider, __self__).__init__(
            'aws-native:iot:CertificateProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CertificateProvider':
        """
        Get an existing CertificateProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateProviderArgs.__new__(CertificateProviderArgs)

        __props__.__dict__["account_default_for_operations"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["certificate_provider_name"] = None
        __props__.__dict__["lambda_function_arn"] = None
        __props__.__dict__["tags"] = None
        return CertificateProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountDefaultForOperations")
    def account_default_for_operations(self) -> pulumi.Output[Sequence['CertificateProviderOperation']]:
        return pulumi.get(self, "account_default_for_operations")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="certificateProviderName")
    def certificate_provider_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "certificate_provider_name")

    @property
    @pulumi.getter(name="lambdaFunctionArn")
    def lambda_function_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "lambda_function_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

