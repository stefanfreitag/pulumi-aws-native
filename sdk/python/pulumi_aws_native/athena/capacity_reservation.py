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

__all__ = ['CapacityReservationArgs', 'CapacityReservation']

@pulumi.input_type
class CapacityReservationArgs:
    def __init__(__self__, *,
                 target_dpus: pulumi.Input[int],
                 capacity_assignment_configuration: Optional[pulumi.Input['CapacityReservationCapacityAssignmentConfigurationArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationTagArgs']]]] = None):
        """
        The set of arguments for constructing a CapacityReservation resource.
        :param pulumi.Input[int] target_dpus: The number of DPUs to request to be allocated to the reservation.
        :param pulumi.Input[str] name: The reservation name.
        :param pulumi.Input[Sequence[pulumi.Input['CapacityReservationTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "target_dpus", target_dpus)
        if capacity_assignment_configuration is not None:
            pulumi.set(__self__, "capacity_assignment_configuration", capacity_assignment_configuration)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="targetDpus")
    def target_dpus(self) -> pulumi.Input[int]:
        """
        The number of DPUs to request to be allocated to the reservation.
        """
        return pulumi.get(self, "target_dpus")

    @target_dpus.setter
    def target_dpus(self, value: pulumi.Input[int]):
        pulumi.set(self, "target_dpus", value)

    @property
    @pulumi.getter(name="capacityAssignmentConfiguration")
    def capacity_assignment_configuration(self) -> Optional[pulumi.Input['CapacityReservationCapacityAssignmentConfigurationArgs']]:
        return pulumi.get(self, "capacity_assignment_configuration")

    @capacity_assignment_configuration.setter
    def capacity_assignment_configuration(self, value: Optional[pulumi.Input['CapacityReservationCapacityAssignmentConfigurationArgs']]):
        pulumi.set(self, "capacity_assignment_configuration", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The reservation name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationTagArgs']]]]):
        pulumi.set(self, "tags", value)


class CapacityReservation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_assignment_configuration: Optional[pulumi.Input[pulumi.InputType['CapacityReservationCapacityAssignmentConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationTagArgs']]]]] = None,
                 target_dpus: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource schema for AWS::Athena::CapacityReservation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The reservation name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[int] target_dpus: The number of DPUs to request to be allocated to the reservation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CapacityReservationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::Athena::CapacityReservation

        :param str resource_name: The name of the resource.
        :param CapacityReservationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityReservationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_assignment_configuration: Optional[pulumi.Input[pulumi.InputType['CapacityReservationCapacityAssignmentConfigurationArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationTagArgs']]]]] = None,
                 target_dpus: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapacityReservationArgs.__new__(CapacityReservationArgs)

            __props__.__dict__["capacity_assignment_configuration"] = capacity_assignment_configuration
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if target_dpus is None and not opts.urn:
                raise TypeError("Missing required property 'target_dpus'")
            __props__.__dict__["target_dpus"] = target_dpus
            __props__.__dict__["allocated_dpus"] = None
            __props__.__dict__["arn"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_successful_allocation_time"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CapacityReservation, __self__).__init__(
            'aws-native:athena:CapacityReservation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CapacityReservation':
        """
        Get an existing CapacityReservation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CapacityReservationArgs.__new__(CapacityReservationArgs)

        __props__.__dict__["allocated_dpus"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["capacity_assignment_configuration"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["last_successful_allocation_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_dpus"] = None
        return CapacityReservation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocatedDpus")
    def allocated_dpus(self) -> pulumi.Output[int]:
        """
        The number of DPUs Athena has provisioned and allocated for the reservation
        """
        return pulumi.get(self, "allocated_dpus")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="capacityAssignmentConfiguration")
    def capacity_assignment_configuration(self) -> pulumi.Output[Optional['outputs.CapacityReservationCapacityAssignmentConfiguration']]:
        return pulumi.get(self, "capacity_assignment_configuration")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The date and time the reservation was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="lastSuccessfulAllocationTime")
    def last_successful_allocation_time(self) -> pulumi.Output[str]:
        """
        The timestamp when the last successful allocated was made
        """
        return pulumi.get(self, "last_successful_allocation_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The reservation name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['CapacityReservationStatus']:
        """
        The status of the reservation.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.CapacityReservationTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetDpus")
    def target_dpus(self) -> pulumi.Output[int]:
        """
        The number of DPUs to request to be allocated to the reservation.
        """
        return pulumi.get(self, "target_dpus")

