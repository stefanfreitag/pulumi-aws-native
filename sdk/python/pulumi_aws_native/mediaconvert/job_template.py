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
from ._inputs import *

__all__ = ['JobTemplateArgs', 'JobTemplate']

@pulumi.input_type
class JobTemplateArgs:
    def __init__(__self__, *,
                 settings_json: Any,
                 acceleration_settings: Optional[pulumi.Input['JobTemplateAccelerationSettingsArgs']] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hop_destinations: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateHopDestinationArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 status_update_interval: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a JobTemplate resource.
        """
        JobTemplateArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            settings_json=settings_json,
            acceleration_settings=acceleration_settings,
            category=category,
            description=description,
            hop_destinations=hop_destinations,
            name=name,
            priority=priority,
            queue=queue,
            status_update_interval=status_update_interval,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             settings_json: Any,
             acceleration_settings: Optional[pulumi.Input['JobTemplateAccelerationSettingsArgs']] = None,
             category: Optional[pulumi.Input[str]] = None,
             description: Optional[pulumi.Input[str]] = None,
             hop_destinations: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateHopDestinationArgs']]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             queue: Optional[pulumi.Input[str]] = None,
             status_update_interval: Optional[pulumi.Input[str]] = None,
             tags: Optional[Any] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("settings_json", settings_json)
        if acceleration_settings is not None:
            _setter("acceleration_settings", acceleration_settings)
        if category is not None:
            _setter("category", category)
        if description is not None:
            _setter("description", description)
        if hop_destinations is not None:
            _setter("hop_destinations", hop_destinations)
        if name is not None:
            _setter("name", name)
        if priority is not None:
            _setter("priority", priority)
        if queue is not None:
            _setter("queue", queue)
        if status_update_interval is not None:
            _setter("status_update_interval", status_update_interval)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter(name="settingsJson")
    def settings_json(self) -> Any:
        return pulumi.get(self, "settings_json")

    @settings_json.setter
    def settings_json(self, value: Any):
        pulumi.set(self, "settings_json", value)

    @property
    @pulumi.getter(name="accelerationSettings")
    def acceleration_settings(self) -> Optional[pulumi.Input['JobTemplateAccelerationSettingsArgs']]:
        return pulumi.get(self, "acceleration_settings")

    @acceleration_settings.setter
    def acceleration_settings(self, value: Optional[pulumi.Input['JobTemplateAccelerationSettingsArgs']]):
        pulumi.set(self, "acceleration_settings", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="hopDestinations")
    def hop_destinations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateHopDestinationArgs']]]]:
        return pulumi.get(self, "hop_destinations")

    @hop_destinations.setter
    def hop_destinations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['JobTemplateHopDestinationArgs']]]]):
        pulumi.set(self, "hop_destinations", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def queue(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "queue")

    @queue.setter
    def queue(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue", value)

    @property
    @pulumi.getter(name="statusUpdateInterval")
    def status_update_interval(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status_update_interval")

    @status_update_interval.setter
    def status_update_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status_update_interval", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


warnings.warn("""JobTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class JobTemplate(pulumi.CustomResource):
    warnings.warn("""JobTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acceleration_settings: Optional[pulumi.Input[pulumi.InputType['JobTemplateAccelerationSettingsArgs']]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hop_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateHopDestinationArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 settings_json: Optional[Any] = None,
                 status_update_interval: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::MediaConvert::JobTemplate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::MediaConvert::JobTemplate

        :param str resource_name: The name of the resource.
        :param JobTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            JobTemplateArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acceleration_settings: Optional[pulumi.Input[pulumi.InputType['JobTemplateAccelerationSettingsArgs']]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hop_destinations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['JobTemplateHopDestinationArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 settings_json: Optional[Any] = None,
                 status_update_interval: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        pulumi.log.warn("""JobTemplate is deprecated: JobTemplate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobTemplateArgs.__new__(JobTemplateArgs)

            if acceleration_settings is not None and not isinstance(acceleration_settings, JobTemplateAccelerationSettingsArgs):
                acceleration_settings = acceleration_settings or {}
                def _setter(key, value):
                    acceleration_settings[key] = value
                JobTemplateAccelerationSettingsArgs._configure(_setter, **acceleration_settings)
            __props__.__dict__["acceleration_settings"] = acceleration_settings
            __props__.__dict__["category"] = category
            __props__.__dict__["description"] = description
            __props__.__dict__["hop_destinations"] = hop_destinations
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["queue"] = queue
            if settings_json is None and not opts.urn:
                raise TypeError("Missing required property 'settings_json'")
            __props__.__dict__["settings_json"] = settings_json
            __props__.__dict__["status_update_interval"] = status_update_interval
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(JobTemplate, __self__).__init__(
            'aws-native:mediaconvert:JobTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobTemplate':
        """
        Get an existing JobTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobTemplateArgs.__new__(JobTemplateArgs)

        __props__.__dict__["acceleration_settings"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["hop_destinations"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["queue"] = None
        __props__.__dict__["settings_json"] = None
        __props__.__dict__["status_update_interval"] = None
        __props__.__dict__["tags"] = None
        return JobTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accelerationSettings")
    def acceleration_settings(self) -> pulumi.Output[Optional['outputs.JobTemplateAccelerationSettings']]:
        return pulumi.get(self, "acceleration_settings")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hopDestinations")
    def hop_destinations(self) -> pulumi.Output[Optional[Sequence['outputs.JobTemplateHopDestination']]]:
        return pulumi.get(self, "hop_destinations")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def queue(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "queue")

    @property
    @pulumi.getter(name="settingsJson")
    def settings_json(self) -> pulumi.Output[Any]:
        return pulumi.get(self, "settings_json")

    @property
    @pulumi.getter(name="statusUpdateInterval")
    def status_update_interval(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "status_update_interval")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "tags")

