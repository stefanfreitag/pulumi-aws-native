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

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 release_label: pulumi.Input[str],
                 type: pulumi.Input[str],
                 architecture: Optional[pulumi.Input['ApplicationArchitecture']] = None,
                 auto_start_configuration: Optional[pulumi.Input['ApplicationAutoStartConfigurationArgs']] = None,
                 auto_stop_configuration: Optional[pulumi.Input['ApplicationAutoStopConfigurationArgs']] = None,
                 image_configuration: Optional[pulumi.Input['ApplicationImageConfigurationInputArgs']] = None,
                 initial_capacity: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationInitialCapacityConfigKeyValuePairArgs']]]] = None,
                 maximum_capacity: Optional[pulumi.Input['ApplicationMaximumAllowedResourcesArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input['ApplicationNetworkConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]] = None,
                 worker_type_specifications: Optional[pulumi.Input['ApplicationWorkerTypeSpecificationInputMapArgs']] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[str] release_label: EMR release label.
        :param pulumi.Input[str] type: The type of the application
        :param pulumi.Input['ApplicationAutoStartConfigurationArgs'] auto_start_configuration: Configuration for Auto Start of Application.
        :param pulumi.Input['ApplicationAutoStopConfigurationArgs'] auto_stop_configuration: Configuration for Auto Stop of Application.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationInitialCapacityConfigKeyValuePairArgs']]] initial_capacity: Initial capacity initialized when an Application is started.
        :param pulumi.Input['ApplicationMaximumAllowedResourcesArgs'] maximum_capacity: Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
        :param pulumi.Input[str] name: User friendly Application name.
        :param pulumi.Input['ApplicationNetworkConfigurationArgs'] network_configuration: Network Configuration for customer VPC connectivity.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]] tags: Tag map with key and value
        :param pulumi.Input['ApplicationWorkerTypeSpecificationInputMapArgs'] worker_type_specifications: The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
        """
        pulumi.set(__self__, "release_label", release_label)
        pulumi.set(__self__, "type", type)
        if architecture is not None:
            pulumi.set(__self__, "architecture", architecture)
        if auto_start_configuration is not None:
            pulumi.set(__self__, "auto_start_configuration", auto_start_configuration)
        if auto_stop_configuration is not None:
            pulumi.set(__self__, "auto_stop_configuration", auto_stop_configuration)
        if image_configuration is not None:
            pulumi.set(__self__, "image_configuration", image_configuration)
        if initial_capacity is not None:
            pulumi.set(__self__, "initial_capacity", initial_capacity)
        if maximum_capacity is not None:
            pulumi.set(__self__, "maximum_capacity", maximum_capacity)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network_configuration is not None:
            pulumi.set(__self__, "network_configuration", network_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if worker_type_specifications is not None:
            pulumi.set(__self__, "worker_type_specifications", worker_type_specifications)

    @property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Input[str]:
        """
        EMR release label.
        """
        return pulumi.get(self, "release_label")

    @release_label.setter
    def release_label(self, value: pulumi.Input[str]):
        pulumi.set(self, "release_label", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the application
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input['ApplicationArchitecture']]:
        return pulumi.get(self, "architecture")

    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input['ApplicationArchitecture']]):
        pulumi.set(self, "architecture", value)

    @property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(self) -> Optional[pulumi.Input['ApplicationAutoStartConfigurationArgs']]:
        """
        Configuration for Auto Start of Application.
        """
        return pulumi.get(self, "auto_start_configuration")

    @auto_start_configuration.setter
    def auto_start_configuration(self, value: Optional[pulumi.Input['ApplicationAutoStartConfigurationArgs']]):
        pulumi.set(self, "auto_start_configuration", value)

    @property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(self) -> Optional[pulumi.Input['ApplicationAutoStopConfigurationArgs']]:
        """
        Configuration for Auto Stop of Application.
        """
        return pulumi.get(self, "auto_stop_configuration")

    @auto_stop_configuration.setter
    def auto_stop_configuration(self, value: Optional[pulumi.Input['ApplicationAutoStopConfigurationArgs']]):
        pulumi.set(self, "auto_stop_configuration", value)

    @property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(self) -> Optional[pulumi.Input['ApplicationImageConfigurationInputArgs']]:
        return pulumi.get(self, "image_configuration")

    @image_configuration.setter
    def image_configuration(self, value: Optional[pulumi.Input['ApplicationImageConfigurationInputArgs']]):
        pulumi.set(self, "image_configuration", value)

    @property
    @pulumi.getter(name="initialCapacity")
    def initial_capacity(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationInitialCapacityConfigKeyValuePairArgs']]]]:
        """
        Initial capacity initialized when an Application is started.
        """
        return pulumi.get(self, "initial_capacity")

    @initial_capacity.setter
    def initial_capacity(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationInitialCapacityConfigKeyValuePairArgs']]]]):
        pulumi.set(self, "initial_capacity", value)

    @property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(self) -> Optional[pulumi.Input['ApplicationMaximumAllowedResourcesArgs']]:
        """
        Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
        """
        return pulumi.get(self, "maximum_capacity")

    @maximum_capacity.setter
    def maximum_capacity(self, value: Optional[pulumi.Input['ApplicationMaximumAllowedResourcesArgs']]):
        pulumi.set(self, "maximum_capacity", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        User friendly Application name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input['ApplicationNetworkConfigurationArgs']]:
        """
        Network Configuration for customer VPC connectivity.
        """
        return pulumi.get(self, "network_configuration")

    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input['ApplicationNetworkConfigurationArgs']]):
        pulumi.set(self, "network_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]:
        """
        Tag map with key and value
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workerTypeSpecifications")
    def worker_type_specifications(self) -> Optional[pulumi.Input['ApplicationWorkerTypeSpecificationInputMapArgs']]:
        """
        The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
        """
        return pulumi.get(self, "worker_type_specifications")

    @worker_type_specifications.setter
    def worker_type_specifications(self, value: Optional[pulumi.Input['ApplicationWorkerTypeSpecificationInputMapArgs']]):
        pulumi.set(self, "worker_type_specifications", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input['ApplicationArchitecture']] = None,
                 auto_start_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationAutoStartConfigurationArgs']]] = None,
                 auto_stop_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationAutoStopConfigurationArgs']]] = None,
                 image_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationImageConfigurationInputArgs']]] = None,
                 initial_capacity: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationInitialCapacityConfigKeyValuePairArgs']]]]] = None,
                 maximum_capacity: Optional[pulumi.Input[pulumi.InputType['ApplicationMaximumAllowedResourcesArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationNetworkConfigurationArgs']]] = None,
                 release_label: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 worker_type_specifications: Optional[pulumi.Input[pulumi.InputType['ApplicationWorkerTypeSpecificationInputMapArgs']]] = None,
                 __props__=None):
        """
        Resource schema for AWS::EMRServerless::Application Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ApplicationAutoStartConfigurationArgs']] auto_start_configuration: Configuration for Auto Start of Application.
        :param pulumi.Input[pulumi.InputType['ApplicationAutoStopConfigurationArgs']] auto_stop_configuration: Configuration for Auto Stop of Application.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationInitialCapacityConfigKeyValuePairArgs']]]] initial_capacity: Initial capacity initialized when an Application is started.
        :param pulumi.Input[pulumi.InputType['ApplicationMaximumAllowedResourcesArgs']] maximum_capacity: Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
        :param pulumi.Input[str] name: User friendly Application name.
        :param pulumi.Input[pulumi.InputType['ApplicationNetworkConfigurationArgs']] network_configuration: Network Configuration for customer VPC connectivity.
        :param pulumi.Input[str] release_label: EMR release label.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]] tags: Tag map with key and value
        :param pulumi.Input[str] type: The type of the application
        :param pulumi.Input[pulumi.InputType['ApplicationWorkerTypeSpecificationInputMapArgs']] worker_type_specifications: The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::EMRServerless::Application Type

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
                 architecture: Optional[pulumi.Input['ApplicationArchitecture']] = None,
                 auto_start_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationAutoStartConfigurationArgs']]] = None,
                 auto_stop_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationAutoStopConfigurationArgs']]] = None,
                 image_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationImageConfigurationInputArgs']]] = None,
                 initial_capacity: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationInitialCapacityConfigKeyValuePairArgs']]]]] = None,
                 maximum_capacity: Optional[pulumi.Input[pulumi.InputType['ApplicationMaximumAllowedResourcesArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_configuration: Optional[pulumi.Input[pulumi.InputType['ApplicationNetworkConfigurationArgs']]] = None,
                 release_label: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationTagArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 worker_type_specifications: Optional[pulumi.Input[pulumi.InputType['ApplicationWorkerTypeSpecificationInputMapArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            __props__.__dict__["architecture"] = architecture
            __props__.__dict__["auto_start_configuration"] = auto_start_configuration
            __props__.__dict__["auto_stop_configuration"] = auto_stop_configuration
            __props__.__dict__["image_configuration"] = image_configuration
            __props__.__dict__["initial_capacity"] = initial_capacity
            __props__.__dict__["maximum_capacity"] = maximum_capacity
            __props__.__dict__["name"] = name
            __props__.__dict__["network_configuration"] = network_configuration
            if release_label is None and not opts.urn:
                raise TypeError("Missing required property 'release_label'")
            __props__.__dict__["release_label"] = release_label
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["worker_type_specifications"] = worker_type_specifications
            __props__.__dict__["application_id"] = None
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name", "type"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Application, __self__).__init__(
            'aws-native:emrserverless:Application',
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
        __props__.__dict__["architecture"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["auto_start_configuration"] = None
        __props__.__dict__["auto_stop_configuration"] = None
        __props__.__dict__["image_configuration"] = None
        __props__.__dict__["initial_capacity"] = None
        __props__.__dict__["maximum_capacity"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_configuration"] = None
        __props__.__dict__["release_label"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["worker_type_specifications"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Output[str]:
        """
        The ID of the EMR Serverless Application.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional['ApplicationArchitecture']]:
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the EMR Serverless Application.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoStartConfiguration")
    def auto_start_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationAutoStartConfiguration']]:
        """
        Configuration for Auto Start of Application.
        """
        return pulumi.get(self, "auto_start_configuration")

    @property
    @pulumi.getter(name="autoStopConfiguration")
    def auto_stop_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationAutoStopConfiguration']]:
        """
        Configuration for Auto Stop of Application.
        """
        return pulumi.get(self, "auto_stop_configuration")

    @property
    @pulumi.getter(name="imageConfiguration")
    def image_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationImageConfigurationInput']]:
        return pulumi.get(self, "image_configuration")

    @property
    @pulumi.getter(name="initialCapacity")
    def initial_capacity(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationInitialCapacityConfigKeyValuePair']]]:
        """
        Initial capacity initialized when an Application is started.
        """
        return pulumi.get(self, "initial_capacity")

    @property
    @pulumi.getter(name="maximumCapacity")
    def maximum_capacity(self) -> pulumi.Output[Optional['outputs.ApplicationMaximumAllowedResources']]:
        """
        Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.
        """
        return pulumi.get(self, "maximum_capacity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        User friendly Application name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> pulumi.Output[Optional['outputs.ApplicationNetworkConfiguration']]:
        """
        Network Configuration for customer VPC connectivity.
        """
        return pulumi.get(self, "network_configuration")

    @property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Output[str]:
        """
        EMR release label.
        """
        return pulumi.get(self, "release_label")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationTag']]]:
        """
        Tag map with key and value
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the application
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workerTypeSpecifications")
    def worker_type_specifications(self) -> pulumi.Output[Optional['outputs.ApplicationWorkerTypeSpecificationInputMap']]:
        """
        The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.
        """
        return pulumi.get(self, "worker_type_specifications")

