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

__all__ = ['AssessmentArgs', 'Assessment']

@pulumi.input_type
class AssessmentArgs:
    def __init__(__self__, *,
                 assessment_reports_destination: Optional[pulumi.Input['AssessmentReportsDestinationArgs']] = None,
                 aws_account: Optional[pulumi.Input['AssessmentAwsAccountArgs']] = None,
                 delegations: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentDelegationArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 framework_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentRoleArgs']]]] = None,
                 scope: Optional[pulumi.Input['AssessmentScopeArgs']] = None,
                 status: Optional[pulumi.Input['AssessmentStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentTagArgs']]]] = None):
        """
        The set of arguments for constructing a Assessment resource.
        :param pulumi.Input[Sequence[pulumi.Input['AssessmentDelegationArgs']]] delegations: The list of delegations.
        :param pulumi.Input[Sequence[pulumi.Input['AssessmentRoleArgs']]] roles: The list of roles for the specified assessment.
        :param pulumi.Input[Sequence[pulumi.Input['AssessmentTagArgs']]] tags: The tags associated with the assessment.
        """
        if assessment_reports_destination is not None:
            pulumi.set(__self__, "assessment_reports_destination", assessment_reports_destination)
        if aws_account is not None:
            pulumi.set(__self__, "aws_account", aws_account)
        if delegations is not None:
            pulumi.set(__self__, "delegations", delegations)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if framework_id is not None:
            pulumi.set(__self__, "framework_id", framework_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="assessmentReportsDestination")
    def assessment_reports_destination(self) -> Optional[pulumi.Input['AssessmentReportsDestinationArgs']]:
        return pulumi.get(self, "assessment_reports_destination")

    @assessment_reports_destination.setter
    def assessment_reports_destination(self, value: Optional[pulumi.Input['AssessmentReportsDestinationArgs']]):
        pulumi.set(self, "assessment_reports_destination", value)

    @property
    @pulumi.getter(name="awsAccount")
    def aws_account(self) -> Optional[pulumi.Input['AssessmentAwsAccountArgs']]:
        return pulumi.get(self, "aws_account")

    @aws_account.setter
    def aws_account(self, value: Optional[pulumi.Input['AssessmentAwsAccountArgs']]):
        pulumi.set(self, "aws_account", value)

    @property
    @pulumi.getter
    def delegations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentDelegationArgs']]]]:
        """
        The list of delegations.
        """
        return pulumi.get(self, "delegations")

    @delegations.setter
    def delegations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentDelegationArgs']]]]):
        pulumi.set(self, "delegations", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "framework_id")

    @framework_id.setter
    def framework_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "framework_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentRoleArgs']]]]:
        """
        The list of roles for the specified assessment.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentRoleArgs']]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input['AssessmentScopeArgs']]:
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input['AssessmentScopeArgs']]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['AssessmentStatus']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['AssessmentStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentTagArgs']]]]:
        """
        The tags associated with the assessment.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Assessment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_reports_destination: Optional[pulumi.Input[pulumi.InputType['AssessmentReportsDestinationArgs']]] = None,
                 aws_account: Optional[pulumi.Input[pulumi.InputType['AssessmentAwsAccountArgs']]] = None,
                 delegations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentDelegationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 framework_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentRoleArgs']]]]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['AssessmentScopeArgs']]] = None,
                 status: Optional[pulumi.Input['AssessmentStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentTagArgs']]]]] = None,
                 __props__=None):
        """
        An entity that defines the scope of audit evidence collected by AWS Audit Manager.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentDelegationArgs']]]] delegations: The list of delegations.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentRoleArgs']]]] roles: The list of roles for the specified assessment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentTagArgs']]]] tags: The tags associated with the assessment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AssessmentArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An entity that defines the scope of audit evidence collected by AWS Audit Manager.

        :param str resource_name: The name of the resource.
        :param AssessmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssessmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_reports_destination: Optional[pulumi.Input[pulumi.InputType['AssessmentReportsDestinationArgs']]] = None,
                 aws_account: Optional[pulumi.Input[pulumi.InputType['AssessmentAwsAccountArgs']]] = None,
                 delegations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentDelegationArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 framework_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentRoleArgs']]]]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['AssessmentScopeArgs']]] = None,
                 status: Optional[pulumi.Input['AssessmentStatus']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AssessmentTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssessmentArgs.__new__(AssessmentArgs)

            __props__.__dict__["assessment_reports_destination"] = assessment_reports_destination
            __props__.__dict__["aws_account"] = aws_account
            __props__.__dict__["delegations"] = delegations
            __props__.__dict__["description"] = description
            __props__.__dict__["framework_id"] = framework_id
            __props__.__dict__["name"] = name
            __props__.__dict__["roles"] = roles
            __props__.__dict__["scope"] = scope
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["assessment_id"] = None
            __props__.__dict__["creation_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["aws_account", "framework_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Assessment, __self__).__init__(
            'aws-native:auditmanager:Assessment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Assessment':
        """
        Get an existing Assessment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssessmentArgs.__new__(AssessmentArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["assessment_id"] = None
        __props__.__dict__["assessment_reports_destination"] = None
        __props__.__dict__["aws_account"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["delegations"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["framework_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["roles"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return Assessment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assessmentId")
    def assessment_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "assessment_id")

    @property
    @pulumi.getter(name="assessmentReportsDestination")
    def assessment_reports_destination(self) -> pulumi.Output[Optional['outputs.AssessmentReportsDestination']]:
        return pulumi.get(self, "assessment_reports_destination")

    @property
    @pulumi.getter(name="awsAccount")
    def aws_account(self) -> pulumi.Output[Optional['outputs.AssessmentAwsAccount']]:
        return pulumi.get(self, "aws_account")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[float]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def delegations(self) -> pulumi.Output[Optional[Sequence['outputs.AssessmentDelegation']]]:
        """
        The list of delegations.
        """
        return pulumi.get(self, "delegations")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "framework_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence['outputs.AssessmentRole']]]:
        """
        The list of roles for the specified assessment.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional['outputs.AssessmentScope']]:
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional['AssessmentStatus']]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.AssessmentTag']]]:
        """
        The tags associated with the assessment.
        """
        return pulumi.get(self, "tags")

