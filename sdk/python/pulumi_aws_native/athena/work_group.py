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

__all__ = ['WorkGroupArgs', 'WorkGroup']

@pulumi.input_type
class WorkGroupArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recursive_delete_option: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input['WorkGroupState']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['WorkGroupTagArgs']]]] = None,
                 work_group_configuration: Optional[pulumi.Input['WorkGroupConfigurationArgs']] = None,
                 work_group_configuration_updates: Optional[pulumi.Input['WorkGroupConfigurationUpdatesArgs']] = None):
        """
        The set of arguments for constructing a WorkGroup resource.
        :param pulumi.Input[str] description: The workgroup description.
        :param pulumi.Input[str] name: The workGroup name.
        :param pulumi.Input[bool] recursive_delete_option: The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        :param pulumi.Input['WorkGroupState'] state: The state of the workgroup: ENABLED or DISABLED.
        :param pulumi.Input[Sequence[pulumi.Input['WorkGroupTagArgs']]] tags: One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        :param pulumi.Input['WorkGroupConfigurationArgs'] work_group_configuration: The workgroup configuration
        :param pulumi.Input['WorkGroupConfigurationUpdatesArgs'] work_group_configuration_updates: The workgroup configuration update object
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if recursive_delete_option is not None:
            pulumi.set(__self__, "recursive_delete_option", recursive_delete_option)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if work_group_configuration is not None:
            pulumi.set(__self__, "work_group_configuration", work_group_configuration)
        if work_group_configuration_updates is not None:
            pulumi.set(__self__, "work_group_configuration_updates", work_group_configuration_updates)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The workgroup description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The workGroup name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="recursiveDeleteOption")
    def recursive_delete_option(self) -> Optional[pulumi.Input[bool]]:
        """
        The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        """
        return pulumi.get(self, "recursive_delete_option")

    @recursive_delete_option.setter
    def recursive_delete_option(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "recursive_delete_option", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['WorkGroupState']]:
        """
        The state of the workgroup: ENABLED or DISABLED.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['WorkGroupState']]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WorkGroupTagArgs']]]]:
        """
        One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WorkGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workGroupConfiguration")
    def work_group_configuration(self) -> Optional[pulumi.Input['WorkGroupConfigurationArgs']]:
        """
        The workgroup configuration
        """
        return pulumi.get(self, "work_group_configuration")

    @work_group_configuration.setter
    def work_group_configuration(self, value: Optional[pulumi.Input['WorkGroupConfigurationArgs']]):
        pulumi.set(self, "work_group_configuration", value)

    @property
    @pulumi.getter(name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(self) -> Optional[pulumi.Input['WorkGroupConfigurationUpdatesArgs']]:
        """
        The workgroup configuration update object
        """
        return pulumi.get(self, "work_group_configuration_updates")

    @work_group_configuration_updates.setter
    def work_group_configuration_updates(self, value: Optional[pulumi.Input['WorkGroupConfigurationUpdatesArgs']]):
        pulumi.set(self, "work_group_configuration_updates", value)


class WorkGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recursive_delete_option: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input['WorkGroupState']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkGroupTagArgs']]]]] = None,
                 work_group_configuration: Optional[pulumi.Input[pulumi.InputType['WorkGroupConfigurationArgs']]] = None,
                 work_group_configuration_updates: Optional[pulumi.Input[pulumi.InputType['WorkGroupConfigurationUpdatesArgs']]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Athena::WorkGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The workgroup description.
        :param pulumi.Input[str] name: The workGroup name.
        :param pulumi.Input[bool] recursive_delete_option: The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        :param pulumi.Input['WorkGroupState'] state: The state of the workgroup: ENABLED or DISABLED.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkGroupTagArgs']]]] tags: One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        :param pulumi.Input[pulumi.InputType['WorkGroupConfigurationArgs']] work_group_configuration: The workgroup configuration
        :param pulumi.Input[pulumi.InputType['WorkGroupConfigurationUpdatesArgs']] work_group_configuration_updates: The workgroup configuration update object
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[WorkGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Athena::WorkGroup

        :param str resource_name: The name of the resource.
        :param WorkGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 recursive_delete_option: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input['WorkGroupState']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WorkGroupTagArgs']]]]] = None,
                 work_group_configuration: Optional[pulumi.Input[pulumi.InputType['WorkGroupConfigurationArgs']]] = None,
                 work_group_configuration_updates: Optional[pulumi.Input[pulumi.InputType['WorkGroupConfigurationUpdatesArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkGroupArgs.__new__(WorkGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["recursive_delete_option"] = recursive_delete_option
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["work_group_configuration"] = work_group_configuration
            __props__.__dict__["work_group_configuration_updates"] = work_group_configuration_updates
            __props__.__dict__["creation_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(WorkGroup, __self__).__init__(
            'aws-native:athena:WorkGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkGroup':
        """
        Get an existing WorkGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkGroupArgs.__new__(WorkGroupArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recursive_delete_option"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["work_group_configuration"] = None
        __props__.__dict__["work_group_configuration_updates"] = None
        return WorkGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The date and time the workgroup was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The workgroup description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The workGroup name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recursiveDeleteOption")
    def recursive_delete_option(self) -> pulumi.Output[Optional[bool]]:
        """
        The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        """
        return pulumi.get(self, "recursive_delete_option")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional['WorkGroupState']]:
        """
        The state of the workgroup: ENABLED or DISABLED.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.WorkGroupTag']]]:
        """
        One or more tags, separated by commas, that you want to attach to the workgroup as you create it
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workGroupConfiguration")
    def work_group_configuration(self) -> pulumi.Output[Optional['outputs.WorkGroupConfiguration']]:
        """
        The workgroup configuration
        """
        return pulumi.get(self, "work_group_configuration")

    @property
    @pulumi.getter(name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(self) -> pulumi.Output[Optional['outputs.WorkGroupConfigurationUpdates']]:
        """
        The workgroup configuration update object
        """
        return pulumi.get(self, "work_group_configuration_updates")

