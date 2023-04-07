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

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 engine_type: pulumi.Input['EnvironmentEngineType'],
                 instance_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 high_availability_config: Optional[pulumi.Input['EnvironmentHighAvailabilityConfigArgs']] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentStorageConfigurationArgs']]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input['EnvironmentTagMapArgs']] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] instance_type: The type of instance underlying the environment.
        :param pulumi.Input[str] description: The description of the environment.
        :param pulumi.Input[str] engine_version: The version of the runtime engine for the environment.
        :param pulumi.Input[str] kms_key_id: The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input[str] preferred_maintenance_window: Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.
        :param pulumi.Input[bool] publicly_accessible: Specifies whether the environment is publicly accessible.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The list of security groups for the VPC associated with this environment.
        :param pulumi.Input[Sequence[pulumi.Input['EnvironmentStorageConfigurationArgs']]] storage_configurations: The storage configurations defined for the runtime environment.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The unique identifiers of the subnets assigned to this runtime environment.
        :param pulumi.Input['EnvironmentTagMapArgs'] tags: Tags associated to this environment.
        """
        pulumi.set(__self__, "engine_type", engine_type)
        pulumi.set(__self__, "instance_type", instance_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if engine_version is not None:
            pulumi.set(__self__, "engine_version", engine_version)
        if high_availability_config is not None:
            pulumi.set(__self__, "high_availability_config", high_availability_config)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if preferred_maintenance_window is not None:
            pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if publicly_accessible is not None:
            pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if storage_configurations is not None:
            pulumi.set(__self__, "storage_configurations", storage_configurations)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Input['EnvironmentEngineType']:
        return pulumi.get(self, "engine_type")

    @engine_type.setter
    def engine_type(self, value: pulumi.Input['EnvironmentEngineType']):
        pulumi.set(self, "engine_type", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        The type of instance underlying the environment.
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the runtime engine for the environment.
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="highAvailabilityConfig")
    def high_availability_config(self) -> Optional[pulumi.Input['EnvironmentHighAvailabilityConfigArgs']]:
        return pulumi.get(self, "high_availability_config")

    @high_availability_config.setter
    def high_availability_config(self, value: Optional[pulumi.Input['EnvironmentHighAvailabilityConfigArgs']]):
        pulumi.set(self, "high_availability_config", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[str]]:
        """
        Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_maintenance_window", value)

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether the environment is publicly accessible.
        """
        return pulumi.get(self, "publicly_accessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publicly_accessible", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of security groups for the VPC associated with this environment.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="storageConfigurations")
    def storage_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentStorageConfigurationArgs']]]]:
        """
        The storage configurations defined for the runtime environment.
        """
        return pulumi.get(self, "storage_configurations")

    @storage_configurations.setter
    def storage_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EnvironmentStorageConfigurationArgs']]]]):
        pulumi.set(self, "storage_configurations", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The unique identifiers of the subnets assigned to this runtime environment.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['EnvironmentTagMapArgs']]:
        """
        Tags associated to this environment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['EnvironmentTagMapArgs']]):
        pulumi.set(self, "tags", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine_type: Optional[pulumi.Input['EnvironmentEngineType']] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 high_availability_config: Optional[pulumi.Input[pulumi.InputType['EnvironmentHighAvailabilityConfigArgs']]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentStorageConfigurationArgs']]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['EnvironmentTagMapArgs']]] = None,
                 __props__=None):
        """
        Represents a runtime environment that can run migrated mainframe applications.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the environment.
        :param pulumi.Input[str] engine_version: The version of the runtime engine for the environment.
        :param pulumi.Input[str] instance_type: The type of instance underlying the environment.
        :param pulumi.Input[str] kms_key_id: The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.
        :param pulumi.Input[str] name: The name of the environment.
        :param pulumi.Input[str] preferred_maintenance_window: Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.
        :param pulumi.Input[bool] publicly_accessible: Specifies whether the environment is publicly accessible.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The list of security groups for the VPC associated with this environment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentStorageConfigurationArgs']]]] storage_configurations: The storage configurations defined for the runtime environment.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: The unique identifiers of the subnets assigned to this runtime environment.
        :param pulumi.Input[pulumi.InputType['EnvironmentTagMapArgs']] tags: Tags associated to this environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a runtime environment that can run migrated mainframe applications.

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 engine_type: Optional[pulumi.Input['EnvironmentEngineType']] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 high_availability_config: Optional[pulumi.Input[pulumi.InputType['EnvironmentHighAvailabilityConfigArgs']]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 preferred_maintenance_window: Optional[pulumi.Input[str]] = None,
                 publicly_accessible: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 storage_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EnvironmentStorageConfigurationArgs']]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[pulumi.InputType['EnvironmentTagMapArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["description"] = description
            if engine_type is None and not opts.urn:
                raise TypeError("Missing required property 'engine_type'")
            __props__.__dict__["engine_type"] = engine_type
            __props__.__dict__["engine_version"] = engine_version
            __props__.__dict__["high_availability_config"] = high_availability_config
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["kms_key_id"] = kms_key_id
            __props__.__dict__["name"] = name
            __props__.__dict__["preferred_maintenance_window"] = preferred_maintenance_window
            __props__.__dict__["publicly_accessible"] = publicly_accessible
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["storage_configurations"] = storage_configurations
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["environment_arn"] = None
            __props__.__dict__["environment_id"] = None
        super(Environment, __self__).__init__(
            'aws-native:m2:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["engine_type"] = None
        __props__.__dict__["engine_version"] = None
        __props__.__dict__["environment_arn"] = None
        __props__.__dict__["environment_id"] = None
        __props__.__dict__["high_availability_config"] = None
        __props__.__dict__["instance_type"] = None
        __props__.__dict__["kms_key_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["preferred_maintenance_window"] = None
        __props__.__dict__["publicly_accessible"] = None
        __props__.__dict__["security_group_ids"] = None
        __props__.__dict__["storage_configurations"] = None
        __props__.__dict__["subnet_ids"] = None
        __props__.__dict__["tags"] = None
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> pulumi.Output['EnvironmentEngineType']:
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the runtime engine for the environment.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="environmentArn")
    def environment_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the runtime environment.
        """
        return pulumi.get(self, "environment_arn")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[str]:
        """
        The unique identifier of the environment.
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="highAvailabilityConfig")
    def high_availability_config(self) -> pulumi.Output[Optional['outputs.EnvironmentHighAvailabilityConfig']]:
        return pulumi.get(self, "high_availability_config")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        """
        The type of instance underlying the environment.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID or the Amazon Resource Name (ARN) of the customer managed KMS Key used for encrypting environment-related resources.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[Optional[str]]:
        """
        Configures a desired maintenance window for the environment. If you do not provide a value, a random system-generated value will be assigned.
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether the environment is publicly accessible.
        """
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of security groups for the VPC associated with this environment.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="storageConfigurations")
    def storage_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.EnvironmentStorageConfiguration']]]:
        """
        The storage configurations defined for the runtime environment.
        """
        return pulumi.get(self, "storage_configurations")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The unique identifiers of the subnets assigned to this runtime environment.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional['outputs.EnvironmentTagMap']]:
        """
        Tags associated to this environment.
        """
        return pulumi.get(self, "tags")

