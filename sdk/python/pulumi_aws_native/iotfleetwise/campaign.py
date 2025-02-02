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

__all__ = ['CampaignArgs', 'Campaign']

@pulumi.input_type
class CampaignArgs:
    def __init__(__self__, *,
                 action: pulumi.Input['CampaignUpdateCampaignAction'],
                 collection_scheme: pulumi.Input[Union['CampaignCollectionScheme0PropertiesArgs', 'CampaignCollectionScheme1PropertiesArgs']],
                 signal_catalog_arn: pulumi.Input[str],
                 target_arn: pulumi.Input[str],
                 compression: Optional[pulumi.Input['CampaignCompression']] = None,
                 data_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CampaignDataDestinationConfig0PropertiesArgs', 'CampaignDataDestinationConfig1PropertiesArgs']]]]] = None,
                 data_extra_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 diagnostics_mode: Optional[pulumi.Input['CampaignDiagnosticsMode']] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_trigger_collection_duration: Optional[pulumi.Input[float]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 signals_to_collect: Optional[pulumi.Input[Sequence[pulumi.Input['CampaignSignalInformationArgs']]]] = None,
                 spooling_mode: Optional[pulumi.Input['CampaignSpoolingMode']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Campaign resource.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "collection_scheme", collection_scheme)
        pulumi.set(__self__, "signal_catalog_arn", signal_catalog_arn)
        pulumi.set(__self__, "target_arn", target_arn)
        if compression is not None:
            pulumi.set(__self__, "compression", compression)
        if data_destination_configs is not None:
            pulumi.set(__self__, "data_destination_configs", data_destination_configs)
        if data_extra_dimensions is not None:
            pulumi.set(__self__, "data_extra_dimensions", data_extra_dimensions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if diagnostics_mode is not None:
            pulumi.set(__self__, "diagnostics_mode", diagnostics_mode)
        if expiry_time is not None:
            pulumi.set(__self__, "expiry_time", expiry_time)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if post_trigger_collection_duration is not None:
            pulumi.set(__self__, "post_trigger_collection_duration", post_trigger_collection_duration)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if signals_to_collect is not None:
            pulumi.set(__self__, "signals_to_collect", signals_to_collect)
        if spooling_mode is not None:
            pulumi.set(__self__, "spooling_mode", spooling_mode)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input['CampaignUpdateCampaignAction']:
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input['CampaignUpdateCampaignAction']):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="collectionScheme")
    def collection_scheme(self) -> pulumi.Input[Union['CampaignCollectionScheme0PropertiesArgs', 'CampaignCollectionScheme1PropertiesArgs']]:
        return pulumi.get(self, "collection_scheme")

    @collection_scheme.setter
    def collection_scheme(self, value: pulumi.Input[Union['CampaignCollectionScheme0PropertiesArgs', 'CampaignCollectionScheme1PropertiesArgs']]):
        pulumi.set(self, "collection_scheme", value)

    @property
    @pulumi.getter(name="signalCatalogArn")
    def signal_catalog_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "signal_catalog_arn")

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "signal_catalog_arn", value)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_arn")

    @target_arn.setter
    def target_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_arn", value)

    @property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input['CampaignCompression']]:
        return pulumi.get(self, "compression")

    @compression.setter
    def compression(self, value: Optional[pulumi.Input['CampaignCompression']]):
        pulumi.set(self, "compression", value)

    @property
    @pulumi.getter(name="dataDestinationConfigs")
    def data_destination_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['CampaignDataDestinationConfig0PropertiesArgs', 'CampaignDataDestinationConfig1PropertiesArgs']]]]]:
        return pulumi.get(self, "data_destination_configs")

    @data_destination_configs.setter
    def data_destination_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['CampaignDataDestinationConfig0PropertiesArgs', 'CampaignDataDestinationConfig1PropertiesArgs']]]]]):
        pulumi.set(self, "data_destination_configs", value)

    @property
    @pulumi.getter(name="dataExtraDimensions")
    def data_extra_dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "data_extra_dimensions")

    @data_extra_dimensions.setter
    def data_extra_dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "data_extra_dimensions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="diagnosticsMode")
    def diagnostics_mode(self) -> Optional[pulumi.Input['CampaignDiagnosticsMode']]:
        return pulumi.get(self, "diagnostics_mode")

    @diagnostics_mode.setter
    def diagnostics_mode(self, value: Optional[pulumi.Input['CampaignDiagnosticsMode']]):
        pulumi.set(self, "diagnostics_mode", value)

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiry_time")

    @expiry_time.setter
    def expiry_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_time", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="postTriggerCollectionDuration")
    def post_trigger_collection_duration(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "post_trigger_collection_duration")

    @post_trigger_collection_duration.setter
    def post_trigger_collection_duration(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "post_trigger_collection_duration", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="signalsToCollect")
    def signals_to_collect(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CampaignSignalInformationArgs']]]]:
        return pulumi.get(self, "signals_to_collect")

    @signals_to_collect.setter
    def signals_to_collect(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CampaignSignalInformationArgs']]]]):
        pulumi.set(self, "signals_to_collect", value)

    @property
    @pulumi.getter(name="spoolingMode")
    def spooling_mode(self) -> Optional[pulumi.Input['CampaignSpoolingMode']]:
        return pulumi.get(self, "spooling_mode")

    @spooling_mode.setter
    def spooling_mode(self, value: Optional[pulumi.Input['CampaignSpoolingMode']]):
        pulumi.set(self, "spooling_mode", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Campaign(pulumi.CustomResource):
    warnings.warn("""Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input['CampaignUpdateCampaignAction']] = None,
                 collection_scheme: Optional[pulumi.Input[Union[pulumi.InputType['CampaignCollectionScheme0PropertiesArgs'], pulumi.InputType['CampaignCollectionScheme1PropertiesArgs']]]] = None,
                 compression: Optional[pulumi.Input['CampaignCompression']] = None,
                 data_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['CampaignDataDestinationConfig0PropertiesArgs'], pulumi.InputType['CampaignDataDestinationConfig1PropertiesArgs']]]]]] = None,
                 data_extra_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 diagnostics_mode: Optional[pulumi.Input['CampaignDiagnosticsMode']] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_trigger_collection_duration: Optional[pulumi.Input[float]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 signal_catalog_arn: Optional[pulumi.Input[str]] = None,
                 signals_to_collect: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CampaignSignalInformationArgs']]]]] = None,
                 spooling_mode: Optional[pulumi.Input['CampaignSpoolingMode']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of AWS::IoTFleetWise::Campaign Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CampaignArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::IoTFleetWise::Campaign Resource Type

        :param str resource_name: The name of the resource.
        :param CampaignArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CampaignArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input['CampaignUpdateCampaignAction']] = None,
                 collection_scheme: Optional[pulumi.Input[Union[pulumi.InputType['CampaignCollectionScheme0PropertiesArgs'], pulumi.InputType['CampaignCollectionScheme1PropertiesArgs']]]] = None,
                 compression: Optional[pulumi.Input['CampaignCompression']] = None,
                 data_destination_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['CampaignDataDestinationConfig0PropertiesArgs'], pulumi.InputType['CampaignDataDestinationConfig1PropertiesArgs']]]]]] = None,
                 data_extra_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 diagnostics_mode: Optional[pulumi.Input['CampaignDiagnosticsMode']] = None,
                 expiry_time: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_trigger_collection_duration: Optional[pulumi.Input[float]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 signal_catalog_arn: Optional[pulumi.Input[str]] = None,
                 signals_to_collect: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CampaignSignalInformationArgs']]]]] = None,
                 spooling_mode: Optional[pulumi.Input['CampaignSpoolingMode']] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Campaign is deprecated: Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CampaignArgs.__new__(CampaignArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if collection_scheme is None and not opts.urn:
                raise TypeError("Missing required property 'collection_scheme'")
            __props__.__dict__["collection_scheme"] = collection_scheme
            __props__.__dict__["compression"] = compression
            __props__.__dict__["data_destination_configs"] = data_destination_configs
            __props__.__dict__["data_extra_dimensions"] = data_extra_dimensions
            __props__.__dict__["description"] = description
            __props__.__dict__["diagnostics_mode"] = diagnostics_mode
            __props__.__dict__["expiry_time"] = expiry_time
            __props__.__dict__["name"] = name
            __props__.__dict__["post_trigger_collection_duration"] = post_trigger_collection_duration
            __props__.__dict__["priority"] = priority
            if signal_catalog_arn is None and not opts.urn:
                raise TypeError("Missing required property 'signal_catalog_arn'")
            __props__.__dict__["signal_catalog_arn"] = signal_catalog_arn
            __props__.__dict__["signals_to_collect"] = signals_to_collect
            __props__.__dict__["spooling_mode"] = spooling_mode
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["tags"] = tags
            if target_arn is None and not opts.urn:
                raise TypeError("Missing required property 'target_arn'")
            __props__.__dict__["target_arn"] = target_arn
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modification_time"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["collection_scheme", "compression", "diagnostics_mode", "expiry_time", "name", "post_trigger_collection_duration", "priority", "signal_catalog_arn", "spooling_mode", "start_time", "target_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Campaign, __self__).__init__(
            'aws-native:iotfleetwise:Campaign',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Campaign':
        """
        Get an existing Campaign resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CampaignArgs.__new__(CampaignArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["collection_scheme"] = None
        __props__.__dict__["compression"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["data_destination_configs"] = None
        __props__.__dict__["data_extra_dimensions"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["diagnostics_mode"] = None
        __props__.__dict__["expiry_time"] = None
        __props__.__dict__["last_modification_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["post_trigger_collection_duration"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["signal_catalog_arn"] = None
        __props__.__dict__["signals_to_collect"] = None
        __props__.__dict__["spooling_mode"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_arn"] = None
        return Campaign(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output['CampaignUpdateCampaignAction']:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="collectionScheme")
    def collection_scheme(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "collection_scheme")

    @property
    @pulumi.getter
    def compression(self) -> pulumi.Output[Optional['CampaignCompression']]:
        return pulumi.get(self, "compression")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="dataDestinationConfigs")
    def data_destination_configs(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        return pulumi.get(self, "data_destination_configs")

    @property
    @pulumi.getter(name="dataExtraDimensions")
    def data_extra_dimensions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "data_extra_dimensions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diagnosticsMode")
    def diagnostics_mode(self) -> pulumi.Output[Optional['CampaignDiagnosticsMode']]:
        return pulumi.get(self, "diagnostics_mode")

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter(name="lastModificationTime")
    def last_modification_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modification_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postTriggerCollectionDuration")
    def post_trigger_collection_duration(self) -> pulumi.Output[Optional[float]]:
        return pulumi.get(self, "post_trigger_collection_duration")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="signalCatalogArn")
    def signal_catalog_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "signal_catalog_arn")

    @property
    @pulumi.getter(name="signalsToCollect")
    def signals_to_collect(self) -> pulumi.Output[Optional[Sequence['outputs.CampaignSignalInformation']]]:
        return pulumi.get(self, "signals_to_collect")

    @property
    @pulumi.getter(name="spoolingMode")
    def spooling_mode(self) -> pulumi.Output[Optional['CampaignSpoolingMode']]:
        return pulumi.get(self, "spooling_mode")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['CampaignStatus']:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "target_arn")

