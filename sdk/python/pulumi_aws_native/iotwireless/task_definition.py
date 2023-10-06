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

__all__ = ['TaskDefinitionArgs', 'TaskDefinition']

@pulumi.input_type
class TaskDefinitionArgs:
    def __init__(__self__, *,
                 auto_create_tasks: pulumi.Input[bool],
                 lo_ra_wan_update_gateway_task_entry: Optional[pulumi.Input['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]] = None,
                 task_definition_type: Optional[pulumi.Input['TaskDefinitionType']] = None,
                 update: Optional[pulumi.Input['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']] = None):
        """
        The set of arguments for constructing a TaskDefinition resource.
        :param pulumi.Input[bool] auto_create_tasks: Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.
        :param pulumi.Input['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs'] lo_ra_wan_update_gateway_task_entry: The list of task definitions.
        :param pulumi.Input[str] name: The name of the new resource.
        :param pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]] tags: A list of key-value pairs that contain metadata for the destination.
        :param pulumi.Input['TaskDefinitionType'] task_definition_type: A filter to list only the wireless gateway task definitions that use this task definition type
        :param pulumi.Input['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs'] update: Information about the gateways to update.
        """
        TaskDefinitionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            auto_create_tasks=auto_create_tasks,
            lo_ra_wan_update_gateway_task_entry=lo_ra_wan_update_gateway_task_entry,
            name=name,
            tags=tags,
            task_definition_type=task_definition_type,
            update=update,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             auto_create_tasks: pulumi.Input[bool],
             lo_ra_wan_update_gateway_task_entry: Optional[pulumi.Input['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']] = None,
             name: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]] = None,
             task_definition_type: Optional[pulumi.Input['TaskDefinitionType']] = None,
             update: Optional[pulumi.Input['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("auto_create_tasks", auto_create_tasks)
        if lo_ra_wan_update_gateway_task_entry is not None:
            _setter("lo_ra_wan_update_gateway_task_entry", lo_ra_wan_update_gateway_task_entry)
        if name is not None:
            _setter("name", name)
        if tags is not None:
            _setter("tags", tags)
        if task_definition_type is not None:
            _setter("task_definition_type", task_definition_type)
        if update is not None:
            _setter("update", update)

    @property
    @pulumi.getter(name="autoCreateTasks")
    def auto_create_tasks(self) -> pulumi.Input[bool]:
        """
        Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.
        """
        return pulumi.get(self, "auto_create_tasks")

    @auto_create_tasks.setter
    def auto_create_tasks(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auto_create_tasks", value)

    @property
    @pulumi.getter(name="loRaWanUpdateGatewayTaskEntry")
    def lo_ra_wan_update_gateway_task_entry(self) -> Optional[pulumi.Input['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']]:
        """
        The list of task definitions.
        """
        return pulumi.get(self, "lo_ra_wan_update_gateway_task_entry")

    @lo_ra_wan_update_gateway_task_entry.setter
    def lo_ra_wan_update_gateway_task_entry(self, value: Optional[pulumi.Input['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']]):
        pulumi.set(self, "lo_ra_wan_update_gateway_task_entry", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the new resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TaskDefinitionTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="taskDefinitionType")
    def task_definition_type(self) -> Optional[pulumi.Input['TaskDefinitionType']]:
        """
        A filter to list only the wireless gateway task definitions that use this task definition type
        """
        return pulumi.get(self, "task_definition_type")

    @task_definition_type.setter
    def task_definition_type(self, value: Optional[pulumi.Input['TaskDefinitionType']]):
        pulumi.set(self, "task_definition_type", value)

    @property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']]:
        """
        Information about the gateways to update.
        """
        return pulumi.get(self, "update")

    @update.setter
    def update(self, value: Optional[pulumi.Input['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']]):
        pulumi.set(self, "update", value)


class TaskDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_create_tasks: Optional[pulumi.Input[bool]] = None,
                 lo_ra_wan_update_gateway_task_entry: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionTagArgs']]]]] = None,
                 task_definition_type: Optional[pulumi.Input['TaskDefinitionType']] = None,
                 update: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']]] = None,
                 __props__=None):
        """
        Creates a gateway task definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_create_tasks: Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.
        :param pulumi.Input[pulumi.InputType['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']] lo_ra_wan_update_gateway_task_entry: The list of task definitions.
        :param pulumi.Input[str] name: The name of the new resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionTagArgs']]]] tags: A list of key-value pairs that contain metadata for the destination.
        :param pulumi.Input['TaskDefinitionType'] task_definition_type: A filter to list only the wireless gateway task definitions that use this task definition type
        :param pulumi.Input[pulumi.InputType['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']] update: Information about the gateways to update.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TaskDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a gateway task definition.

        :param str resource_name: The name of the resource.
        :param TaskDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TaskDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TaskDefinitionArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_create_tasks: Optional[pulumi.Input[bool]] = None,
                 lo_ra_wan_update_gateway_task_entry: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TaskDefinitionTagArgs']]]]] = None,
                 task_definition_type: Optional[pulumi.Input['TaskDefinitionType']] = None,
                 update: Optional[pulumi.Input[pulumi.InputType['TaskDefinitionUpdateWirelessGatewayTaskCreateArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TaskDefinitionArgs.__new__(TaskDefinitionArgs)

            if auto_create_tasks is None and not opts.urn:
                raise TypeError("Missing required property 'auto_create_tasks'")
            __props__.__dict__["auto_create_tasks"] = auto_create_tasks
            if lo_ra_wan_update_gateway_task_entry is not None and not isinstance(lo_ra_wan_update_gateway_task_entry, TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs):
                lo_ra_wan_update_gateway_task_entry = lo_ra_wan_update_gateway_task_entry or {}
                def _setter(key, value):
                    lo_ra_wan_update_gateway_task_entry[key] = value
                TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs._configure(_setter, **lo_ra_wan_update_gateway_task_entry)
            __props__.__dict__["lo_ra_wan_update_gateway_task_entry"] = lo_ra_wan_update_gateway_task_entry
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["task_definition_type"] = task_definition_type
            if update is not None and not isinstance(update, TaskDefinitionUpdateWirelessGatewayTaskCreateArgs):
                update = update or {}
                def _setter(key, value):
                    update[key] = value
                TaskDefinitionUpdateWirelessGatewayTaskCreateArgs._configure(_setter, **update)
            __props__.__dict__["update"] = update
            __props__.__dict__["arn"] = None
        super(TaskDefinition, __self__).__init__(
            'aws-native:iotwireless:TaskDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TaskDefinition':
        """
        Get an existing TaskDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TaskDefinitionArgs.__new__(TaskDefinitionArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["auto_create_tasks"] = None
        __props__.__dict__["lo_ra_wan_update_gateway_task_entry"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["task_definition_type"] = None
        __props__.__dict__["update"] = None
        return TaskDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        TaskDefinition arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoCreateTasks")
    def auto_create_tasks(self) -> pulumi.Output[bool]:
        """
        Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.
        """
        return pulumi.get(self, "auto_create_tasks")

    @property
    @pulumi.getter(name="loRaWanUpdateGatewayTaskEntry")
    def lo_ra_wan_update_gateway_task_entry(self) -> pulumi.Output[Optional['outputs.TaskDefinitionLoRaWanUpdateGatewayTaskEntry']]:
        """
        The list of task definitions.
        """
        return pulumi.get(self, "lo_ra_wan_update_gateway_task_entry")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the new resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.TaskDefinitionTag']]]:
        """
        A list of key-value pairs that contain metadata for the destination.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskDefinitionType")
    def task_definition_type(self) -> pulumi.Output[Optional['TaskDefinitionType']]:
        """
        A filter to list only the wireless gateway task definitions that use this task definition type
        """
        return pulumi.get(self, "task_definition_type")

    @property
    @pulumi.getter
    def update(self) -> pulumi.Output[Optional['outputs.TaskDefinitionUpdateWirelessGatewayTaskCreate']]:
        """
        Information about the gateways to update.
        """
        return pulumi.get(self, "update")

