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

__all__ = ['ConnectorProfileArgs', 'ConnectorProfile']

@pulumi.input_type
class ConnectorProfileArgs:
    def __init__(__self__, *,
                 connection_mode: pulumi.Input['ConnectorProfileConnectionMode'],
                 connector_type: pulumi.Input['ConnectorProfileConnectorType'],
                 connector_label: Optional[pulumi.Input[str]] = None,
                 connector_profile_config: Optional[pulumi.Input['ConnectorProfileConfigArgs']] = None,
                 connector_profile_name: Optional[pulumi.Input[str]] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ConnectorProfile resource.
        :param pulumi.Input['ConnectorProfileConnectionMode'] connection_mode: Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular
        :param pulumi.Input['ConnectorProfileConnectorType'] connector_type: List of Saas providers that need connector profile to be created
        :param pulumi.Input[str] connector_label: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
        :param pulumi.Input['ConnectorProfileConfigArgs'] connector_profile_config: Connector specific configurations needed to create connector profile
        :param pulumi.Input[str] connector_profile_name: The maximum number of items to retrieve in a single batch.
        :param pulumi.Input[str] kms_arn: The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        """
        pulumi.set(__self__, "connection_mode", connection_mode)
        pulumi.set(__self__, "connector_type", connector_type)
        if connector_label is not None:
            pulumi.set(__self__, "connector_label", connector_label)
        if connector_profile_config is not None:
            pulumi.set(__self__, "connector_profile_config", connector_profile_config)
        if connector_profile_name is not None:
            pulumi.set(__self__, "connector_profile_name", connector_profile_name)
        if kms_arn is not None:
            pulumi.set(__self__, "kms_arn", kms_arn)

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Input['ConnectorProfileConnectionMode']:
        """
        Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular
        """
        return pulumi.get(self, "connection_mode")

    @connection_mode.setter
    def connection_mode(self, value: pulumi.Input['ConnectorProfileConnectionMode']):
        pulumi.set(self, "connection_mode", value)

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input['ConnectorProfileConnectorType']:
        """
        List of Saas providers that need connector profile to be created
        """
        return pulumi.get(self, "connector_type")

    @connector_type.setter
    def connector_type(self, value: pulumi.Input['ConnectorProfileConnectorType']):
        pulumi.set(self, "connector_type", value)

    @property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> Optional[pulumi.Input[str]]:
        """
        The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
        """
        return pulumi.get(self, "connector_label")

    @connector_label.setter
    def connector_label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_label", value)

    @property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> Optional[pulumi.Input['ConnectorProfileConfigArgs']]:
        """
        Connector specific configurations needed to create connector profile
        """
        return pulumi.get(self, "connector_profile_config")

    @connector_profile_config.setter
    def connector_profile_config(self, value: Optional[pulumi.Input['ConnectorProfileConfigArgs']]):
        pulumi.set(self, "connector_profile_config", value)

    @property
    @pulumi.getter(name="connectorProfileName")
    def connector_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The maximum number of items to retrieve in a single batch.
        """
        return pulumi.get(self, "connector_profile_name")

    @connector_profile_name.setter
    def connector_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_profile_name", value)

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        """
        return pulumi.get(self, "kms_arn")

    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_arn", value)


class ConnectorProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_mode: Optional[pulumi.Input['ConnectorProfileConnectionMode']] = None,
                 connector_label: Optional[pulumi.Input[str]] = None,
                 connector_profile_config: Optional[pulumi.Input[pulumi.InputType['ConnectorProfileConfigArgs']]] = None,
                 connector_profile_name: Optional[pulumi.Input[str]] = None,
                 connector_type: Optional[pulumi.Input['ConnectorProfileConnectorType']] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppFlow::ConnectorProfile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ConnectorProfileConnectionMode'] connection_mode: Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular
        :param pulumi.Input[str] connector_label: The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
        :param pulumi.Input[pulumi.InputType['ConnectorProfileConfigArgs']] connector_profile_config: Connector specific configurations needed to create connector profile
        :param pulumi.Input[str] connector_profile_name: The maximum number of items to retrieve in a single batch.
        :param pulumi.Input['ConnectorProfileConnectorType'] connector_type: List of Saas providers that need connector profile to be created
        :param pulumi.Input[str] kms_arn: The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppFlow::ConnectorProfile

        :param str resource_name: The name of the resource.
        :param ConnectorProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_mode: Optional[pulumi.Input['ConnectorProfileConnectionMode']] = None,
                 connector_label: Optional[pulumi.Input[str]] = None,
                 connector_profile_config: Optional[pulumi.Input[pulumi.InputType['ConnectorProfileConfigArgs']]] = None,
                 connector_profile_name: Optional[pulumi.Input[str]] = None,
                 connector_type: Optional[pulumi.Input['ConnectorProfileConnectorType']] = None,
                 kms_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorProfileArgs.__new__(ConnectorProfileArgs)

            if connection_mode is None and not opts.urn:
                raise TypeError("Missing required property 'connection_mode'")
            __props__.__dict__["connection_mode"] = connection_mode
            __props__.__dict__["connector_label"] = connector_label
            __props__.__dict__["connector_profile_config"] = connector_profile_config
            __props__.__dict__["connector_profile_name"] = connector_profile_name
            if connector_type is None and not opts.urn:
                raise TypeError("Missing required property 'connector_type'")
            __props__.__dict__["connector_type"] = connector_type
            __props__.__dict__["kms_arn"] = kms_arn
            __props__.__dict__["connector_profile_arn"] = None
            __props__.__dict__["credentials_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["connector_label", "connector_profile_name", "connector_type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ConnectorProfile, __self__).__init__(
            'aws-native:appflow:ConnectorProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConnectorProfile':
        """
        Get an existing ConnectorProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorProfileArgs.__new__(ConnectorProfileArgs)

        __props__.__dict__["connection_mode"] = None
        __props__.__dict__["connector_label"] = None
        __props__.__dict__["connector_profile_arn"] = None
        __props__.__dict__["connector_profile_config"] = None
        __props__.__dict__["connector_profile_name"] = None
        __props__.__dict__["connector_type"] = None
        __props__.__dict__["credentials_arn"] = None
        __props__.__dict__["kms_arn"] = None
        return ConnectorProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionMode")
    def connection_mode(self) -> pulumi.Output['ConnectorProfileConnectionMode']:
        """
        Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular
        """
        return pulumi.get(self, "connection_mode")

    @property
    @pulumi.getter(name="connectorLabel")
    def connector_label(self) -> pulumi.Output[Optional[str]]:
        """
        The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type/.
        """
        return pulumi.get(self, "connector_label")

    @property
    @pulumi.getter(name="connectorProfileArn")
    def connector_profile_arn(self) -> pulumi.Output[str]:
        """
        Unique identifier for connector profile resources
        """
        return pulumi.get(self, "connector_profile_arn")

    @property
    @pulumi.getter(name="connectorProfileConfig")
    def connector_profile_config(self) -> pulumi.Output[Optional['outputs.ConnectorProfileConfig']]:
        """
        Connector specific configurations needed to create connector profile
        """
        return pulumi.get(self, "connector_profile_config")

    @property
    @pulumi.getter(name="connectorProfileName")
    def connector_profile_name(self) -> pulumi.Output[str]:
        """
        The maximum number of items to retrieve in a single batch.
        """
        return pulumi.get(self, "connector_profile_name")

    @property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output['ConnectorProfileConnectorType']:
        """
        List of Saas providers that need connector profile to be created
        """
        return pulumi.get(self, "connector_type")

    @property
    @pulumi.getter(name="credentialsArn")
    def credentials_arn(self) -> pulumi.Output[str]:
        """
        A unique Arn for Connector-Profile resource
        """
        return pulumi.get(self, "credentials_arn")

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.
        """
        return pulumi.get(self, "kms_arn")

