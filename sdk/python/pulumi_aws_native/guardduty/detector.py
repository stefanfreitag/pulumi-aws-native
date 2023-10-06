# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DetectorArgs', 'Detector']

@pulumi.input_type
class DetectorArgs:
    def __init__(__self__, *,
                 enable: pulumi.Input[bool],
                 data_sources: Optional[pulumi.Input['DetectorCfnDataSourceConfigurationsArgs']] = None,
                 features: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureConfigurationArgs']]]] = None,
                 finding_publishing_frequency: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagItemArgs']]]] = None):
        """
        The set of arguments for constructing a Detector resource.
        """
        DetectorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable=enable,
            data_sources=data_sources,
            features=features,
            finding_publishing_frequency=finding_publishing_frequency,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable: pulumi.Input[bool],
             data_sources: Optional[pulumi.Input['DetectorCfnDataSourceConfigurationsArgs']] = None,
             features: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureConfigurationArgs']]]] = None,
             finding_publishing_frequency: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagItemArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enable", enable)
        if data_sources is not None:
            _setter("data_sources", data_sources)
        if features is not None:
            _setter("features", features)
        if finding_publishing_frequency is not None:
            _setter("finding_publishing_frequency", finding_publishing_frequency)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[pulumi.Input['DetectorCfnDataSourceConfigurationsArgs']]:
        return pulumi.get(self, "data_sources")

    @data_sources.setter
    def data_sources(self, value: Optional[pulumi.Input['DetectorCfnDataSourceConfigurationsArgs']]):
        pulumi.set(self, "data_sources", value)

    @property
    @pulumi.getter
    def features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureConfigurationArgs']]]]:
        return pulumi.get(self, "features")

    @features.setter
    def features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureConfigurationArgs']]]]):
        pulumi.set(self, "features", value)

    @property
    @pulumi.getter(name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "finding_publishing_frequency")

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "finding_publishing_frequency", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagItemArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagItemArgs']]]]):
        pulumi.set(self, "tags", value)


class Detector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_sources: Optional[pulumi.Input[pulumi.InputType['DetectorCfnDataSourceConfigurationsArgs']]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 features: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorCfnFeatureConfigurationArgs']]]]] = None,
                 finding_publishing_frequency: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorTagItemArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::GuardDuty::Detector

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DetectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::GuardDuty::Detector

        :param str resource_name: The name of the resource.
        :param DetectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DetectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DetectorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_sources: Optional[pulumi.Input[pulumi.InputType['DetectorCfnDataSourceConfigurationsArgs']]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 features: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorCfnFeatureConfigurationArgs']]]]] = None,
                 finding_publishing_frequency: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorTagItemArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DetectorArgs.__new__(DetectorArgs)

            if data_sources is not None and not isinstance(data_sources, DetectorCfnDataSourceConfigurationsArgs):
                data_sources = data_sources or {}
                def _setter(key, value):
                    data_sources[key] = value
                DetectorCfnDataSourceConfigurationsArgs._configure(_setter, **data_sources)
            __props__.__dict__["data_sources"] = data_sources
            if enable is None and not opts.urn:
                raise TypeError("Missing required property 'enable'")
            __props__.__dict__["enable"] = enable
            __props__.__dict__["features"] = features
            __props__.__dict__["finding_publishing_frequency"] = finding_publishing_frequency
            __props__.__dict__["tags"] = tags
        super(Detector, __self__).__init__(
            'aws-native:guardduty:Detector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Detector':
        """
        Get an existing Detector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DetectorArgs.__new__(DetectorArgs)

        __props__.__dict__["data_sources"] = None
        __props__.__dict__["enable"] = None
        __props__.__dict__["features"] = None
        __props__.__dict__["finding_publishing_frequency"] = None
        __props__.__dict__["tags"] = None
        return Detector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> pulumi.Output[Optional['outputs.DetectorCfnDataSourceConfigurations']]:
        return pulumi.get(self, "data_sources")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def features(self) -> pulumi.Output[Optional[Sequence['outputs.DetectorCfnFeatureConfiguration']]]:
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "finding_publishing_frequency")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DetectorTagItem']]]:
        return pulumi.get(self, "tags")

