# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AssessmentAWSAccountArgs',
    'AssessmentAWSServiceArgs',
    'AssessmentDelegationArgs',
    'AssessmentReportsDestinationArgs',
    'AssessmentRoleArgs',
    'AssessmentScopeArgs',
    'AssessmentTagArgs',
]

@pulumi.input_type
class AssessmentAWSAccountArgs:
    def __init__(__self__, *,
                 email_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The AWS account associated with the assessment.
        """
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class AssessmentAWSServiceArgs:
    def __init__(__self__, *,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        An AWS service such as Amazon S3, AWS CloudTrail, and so on.
        """
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)


@pulumi.input_type
class AssessmentDelegationArgs:
    def __init__(__self__, *,
                 assessment_id: Optional[pulumi.Input[str]] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 control_set_id: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[float]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[float]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input['AssessmentRoleType']] = None,
                 status: Optional[pulumi.Input['AssessmentDelegationStatus']] = None):
        """
        The assignment of a control set to a delegate for review.
        """
        if assessment_id is not None:
            pulumi.set(__self__, "assessment_id", assessment_id)
        if assessment_name is not None:
            pulumi.set(__self__, "assessment_name", assessment_name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if control_set_id is not None:
            pulumi.set(__self__, "control_set_id", control_set_id)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if role_type is not None:
            pulumi.set(__self__, "role_type", role_type)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="assessmentId")
    def assessment_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "assessment_id")

    @assessment_id.setter
    def assessment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_id", value)

    @property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "assessment_name")

    @assessment_name.setter
    def assessment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="controlSetId")
    def control_set_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "control_set_id")

    @control_set_id.setter
    def control_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "control_set_id", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[pulumi.Input['AssessmentRoleType']]:
        return pulumi.get(self, "role_type")

    @role_type.setter
    def role_type(self, value: Optional[pulumi.Input['AssessmentRoleType']]):
        pulumi.set(self, "role_type", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['AssessmentDelegationStatus']]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['AssessmentDelegationStatus']]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class AssessmentReportsDestinationArgs:
    def __init__(__self__, *,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input['AssessmentReportDestinationType']] = None):
        """
        The destination in which evidence reports are stored for the specified assessment.
        """
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if destination_type is not None:
            pulumi.set(__self__, "destination_type", destination_type)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[pulumi.Input['AssessmentReportDestinationType']]:
        return pulumi.get(self, "destination_type")

    @destination_type.setter
    def destination_type(self, value: Optional[pulumi.Input['AssessmentReportDestinationType']]):
        pulumi.set(self, "destination_type", value)


@pulumi.input_type
class AssessmentRoleArgs:
    def __init__(__self__, *,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input['AssessmentRoleType']] = None):
        """
        The wrapper that contains AWS Audit Manager role information, such as the role type and IAM ARN.
        """
        if role_arn is not None:
            pulumi.set(__self__, "role_arn", role_arn)
        if role_type is not None:
            pulumi.set(__self__, "role_type", role_type)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[pulumi.Input['AssessmentRoleType']]:
        return pulumi.get(self, "role_type")

    @role_type.setter
    def role_type(self, value: Optional[pulumi.Input['AssessmentRoleType']]):
        pulumi.set(self, "role_type", value)


@pulumi.input_type
class AssessmentScopeArgs:
    def __init__(__self__, *,
                 aws_accounts: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentAWSAccountArgs']]]] = None,
                 aws_services: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentAWSServiceArgs']]]] = None):
        """
        The wrapper that contains the AWS accounts and AWS services in scope for the assessment.
        :param pulumi.Input[Sequence[pulumi.Input['AssessmentAWSAccountArgs']]] aws_accounts: The AWS accounts included in scope.
        :param pulumi.Input[Sequence[pulumi.Input['AssessmentAWSServiceArgs']]] aws_services: The AWS services included in scope.
        """
        if aws_accounts is not None:
            pulumi.set(__self__, "aws_accounts", aws_accounts)
        if aws_services is not None:
            pulumi.set(__self__, "aws_services", aws_services)

    @property
    @pulumi.getter(name="awsAccounts")
    def aws_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentAWSAccountArgs']]]]:
        """
        The AWS accounts included in scope.
        """
        return pulumi.get(self, "aws_accounts")

    @aws_accounts.setter
    def aws_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentAWSAccountArgs']]]]):
        pulumi.set(self, "aws_accounts", value)

    @property
    @pulumi.getter(name="awsServices")
    def aws_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentAWSServiceArgs']]]]:
        """
        The AWS services included in scope.
        """
        return pulumi.get(self, "aws_services")

    @aws_services.setter
    def aws_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AssessmentAWSServiceArgs']]]]):
        pulumi.set(self, "aws_services", value)


@pulumi.input_type
class AssessmentTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[str] key: The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param pulumi.Input[str] value: The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


