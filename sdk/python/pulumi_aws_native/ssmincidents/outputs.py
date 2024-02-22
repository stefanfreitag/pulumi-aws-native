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

__all__ = [
    'ReplicationSetRegionConfiguration',
    'ReplicationSetReplicationRegion',
    'ResponsePlanAction',
    'ResponsePlanChatChannel',
    'ResponsePlanDynamicSsmParameter',
    'ResponsePlanDynamicSsmParameterValue',
    'ResponsePlanIncidentTemplate',
    'ResponsePlanIntegration',
    'ResponsePlanNotificationTargetItem',
    'ResponsePlanPagerDutyConfiguration',
    'ResponsePlanPagerDutyIncidentConfiguration',
    'ResponsePlanSsmAutomation',
    'ResponsePlanSsmParameter',
    'ResponsePlanTag',
]

@pulumi.output_type
class ReplicationSetRegionConfiguration(dict):
    """
    The ReplicationSet regional configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "sseKmsKeyId":
            suggest = "sse_kms_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReplicationSetRegionConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReplicationSetRegionConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReplicationSetRegionConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 sse_kms_key_id: str):
        """
        The ReplicationSet regional configuration.
        """
        pulumi.set(__self__, "sse_kms_key_id", sse_kms_key_id)

    @property
    @pulumi.getter(name="sseKmsKeyId")
    def sse_kms_key_id(self) -> str:
        return pulumi.get(self, "sse_kms_key_id")


@pulumi.output_type
class ReplicationSetReplicationRegion(dict):
    """
    The ReplicationSet regional configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "regionConfiguration":
            suggest = "region_configuration"
        elif key == "regionName":
            suggest = "region_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReplicationSetReplicationRegion. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReplicationSetReplicationRegion.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReplicationSetReplicationRegion.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 region_configuration: Optional['outputs.ReplicationSetRegionConfiguration'] = None,
                 region_name: Optional[str] = None):
        """
        The ReplicationSet regional configuration.
        """
        if region_configuration is not None:
            pulumi.set(__self__, "region_configuration", region_configuration)
        if region_name is not None:
            pulumi.set(__self__, "region_name", region_name)

    @property
    @pulumi.getter(name="regionConfiguration")
    def region_configuration(self) -> Optional['outputs.ReplicationSetRegionConfiguration']:
        return pulumi.get(self, "region_configuration")

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> Optional[str]:
        return pulumi.get(self, "region_name")


@pulumi.output_type
class ResponsePlanAction(dict):
    """
    The automation configuration to launch.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ssmAutomation":
            suggest = "ssm_automation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ssm_automation: Optional['outputs.ResponsePlanSsmAutomation'] = None):
        """
        The automation configuration to launch.
        """
        if ssm_automation is not None:
            pulumi.set(__self__, "ssm_automation", ssm_automation)

    @property
    @pulumi.getter(name="ssmAutomation")
    def ssm_automation(self) -> Optional['outputs.ResponsePlanSsmAutomation']:
        return pulumi.get(self, "ssm_automation")


@pulumi.output_type
class ResponsePlanChatChannel(dict):
    """
    The chat channel configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "chatbotSns":
            suggest = "chatbot_sns"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanChatChannel. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanChatChannel.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanChatChannel.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 chatbot_sns: Optional[Sequence[str]] = None):
        """
        The chat channel configuration.
        """
        if chatbot_sns is not None:
            pulumi.set(__self__, "chatbot_sns", chatbot_sns)

    @property
    @pulumi.getter(name="chatbotSns")
    def chatbot_sns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "chatbot_sns")


@pulumi.output_type
class ResponsePlanDynamicSsmParameter(dict):
    """
    A parameter with a dynamic value to set when starting the SSM automation document.
    """
    def __init__(__self__, *,
                 key: str,
                 value: 'outputs.ResponsePlanDynamicSsmParameterValue'):
        """
        A parameter with a dynamic value to set when starting the SSM automation document.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> 'outputs.ResponsePlanDynamicSsmParameterValue':
        return pulumi.get(self, "value")


@pulumi.output_type
class ResponsePlanDynamicSsmParameterValue(dict):
    """
    Value of the dynamic parameter to set when starting the SSM automation document.
    """
    def __init__(__self__, *,
                 variable: Optional['ResponsePlanVariableType'] = None):
        """
        Value of the dynamic parameter to set when starting the SSM automation document.
        """
        if variable is not None:
            pulumi.set(__self__, "variable", variable)

    @property
    @pulumi.getter
    def variable(self) -> Optional['ResponsePlanVariableType']:
        return pulumi.get(self, "variable")


@pulumi.output_type
class ResponsePlanIncidentTemplate(dict):
    """
    The incident template configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dedupeString":
            suggest = "dedupe_string"
        elif key == "incidentTags":
            suggest = "incident_tags"
        elif key == "notificationTargets":
            suggest = "notification_targets"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanIncidentTemplate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanIncidentTemplate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanIncidentTemplate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 impact: int,
                 title: str,
                 dedupe_string: Optional[str] = None,
                 incident_tags: Optional[Sequence['outputs.ResponsePlanTag']] = None,
                 notification_targets: Optional[Sequence['outputs.ResponsePlanNotificationTargetItem']] = None,
                 summary: Optional[str] = None):
        """
        The incident template configuration.
        :param int impact: The impact value.
        :param str title: The title string.
        :param str dedupe_string: The deduplication string.
        :param Sequence['ResponsePlanTag'] incident_tags: Tags that get applied to incidents created by the StartIncident API action.
        :param Sequence['ResponsePlanNotificationTargetItem'] notification_targets: The list of notification targets.
        :param str summary: The summary string.
        """
        pulumi.set(__self__, "impact", impact)
        pulumi.set(__self__, "title", title)
        if dedupe_string is not None:
            pulumi.set(__self__, "dedupe_string", dedupe_string)
        if incident_tags is not None:
            pulumi.set(__self__, "incident_tags", incident_tags)
        if notification_targets is not None:
            pulumi.set(__self__, "notification_targets", notification_targets)
        if summary is not None:
            pulumi.set(__self__, "summary", summary)

    @property
    @pulumi.getter
    def impact(self) -> int:
        """
        The impact value.
        """
        return pulumi.get(self, "impact")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        The title string.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="dedupeString")
    def dedupe_string(self) -> Optional[str]:
        """
        The deduplication string.
        """
        return pulumi.get(self, "dedupe_string")

    @property
    @pulumi.getter(name="incidentTags")
    def incident_tags(self) -> Optional[Sequence['outputs.ResponsePlanTag']]:
        """
        Tags that get applied to incidents created by the StartIncident API action.
        """
        return pulumi.get(self, "incident_tags")

    @property
    @pulumi.getter(name="notificationTargets")
    def notification_targets(self) -> Optional[Sequence['outputs.ResponsePlanNotificationTargetItem']]:
        """
        The list of notification targets.
        """
        return pulumi.get(self, "notification_targets")

    @property
    @pulumi.getter
    def summary(self) -> Optional[str]:
        """
        The summary string.
        """
        return pulumi.get(self, "summary")


@pulumi.output_type
class ResponsePlanIntegration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pagerDutyConfiguration":
            suggest = "pager_duty_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanIntegration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanIntegration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanIntegration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 pager_duty_configuration: Optional['outputs.ResponsePlanPagerDutyConfiguration'] = None):
        if pager_duty_configuration is not None:
            pulumi.set(__self__, "pager_duty_configuration", pager_duty_configuration)

    @property
    @pulumi.getter(name="pagerDutyConfiguration")
    def pager_duty_configuration(self) -> Optional['outputs.ResponsePlanPagerDutyConfiguration']:
        return pulumi.get(self, "pager_duty_configuration")


@pulumi.output_type
class ResponsePlanNotificationTargetItem(dict):
    """
    A notification target.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "snsTopicArn":
            suggest = "sns_topic_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanNotificationTargetItem. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanNotificationTargetItem.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanNotificationTargetItem.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 sns_topic_arn: Optional[str] = None):
        """
        A notification target.
        """
        if sns_topic_arn is not None:
            pulumi.set(__self__, "sns_topic_arn", sns_topic_arn)

    @property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[str]:
        return pulumi.get(self, "sns_topic_arn")


@pulumi.output_type
class ResponsePlanPagerDutyConfiguration(dict):
    """
    The pagerDuty configuration to use when starting the incident.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pagerDutyIncidentConfiguration":
            suggest = "pager_duty_incident_configuration"
        elif key == "secretId":
            suggest = "secret_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanPagerDutyConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanPagerDutyConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanPagerDutyConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 pager_duty_incident_configuration: 'outputs.ResponsePlanPagerDutyIncidentConfiguration',
                 secret_id: str):
        """
        The pagerDuty configuration to use when starting the incident.
        :param str name: The name of the pagerDuty configuration.
        :param str secret_id: The AWS secrets manager secretId storing the pagerDuty token.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "pager_duty_incident_configuration", pager_duty_incident_configuration)
        pulumi.set(__self__, "secret_id", secret_id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the pagerDuty configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pagerDutyIncidentConfiguration")
    def pager_duty_incident_configuration(self) -> 'outputs.ResponsePlanPagerDutyIncidentConfiguration':
        return pulumi.get(self, "pager_duty_incident_configuration")

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> str:
        """
        The AWS secrets manager secretId storing the pagerDuty token.
        """
        return pulumi.get(self, "secret_id")


@pulumi.output_type
class ResponsePlanPagerDutyIncidentConfiguration(dict):
    """
    The pagerDuty incident configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceId":
            suggest = "service_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanPagerDutyIncidentConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanPagerDutyIncidentConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanPagerDutyIncidentConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_id: str):
        """
        The pagerDuty incident configuration.
        :param str service_id: The pagerDuty serviceId.
        """
        pulumi.set(__self__, "service_id", service_id)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        """
        The pagerDuty serviceId.
        """
        return pulumi.get(self, "service_id")


@pulumi.output_type
class ResponsePlanSsmAutomation(dict):
    """
    The configuration to use when starting the SSM automation document.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "documentName":
            suggest = "document_name"
        elif key == "roleArn":
            suggest = "role_arn"
        elif key == "documentVersion":
            suggest = "document_version"
        elif key == "dynamicParameters":
            suggest = "dynamic_parameters"
        elif key == "targetAccount":
            suggest = "target_account"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResponsePlanSsmAutomation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResponsePlanSsmAutomation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResponsePlanSsmAutomation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 document_name: str,
                 role_arn: str,
                 document_version: Optional[str] = None,
                 dynamic_parameters: Optional[Sequence['outputs.ResponsePlanDynamicSsmParameter']] = None,
                 parameters: Optional[Sequence['outputs.ResponsePlanSsmParameter']] = None,
                 target_account: Optional['ResponsePlanSsmAutomationTargetAccount'] = None):
        """
        The configuration to use when starting the SSM automation document.
        :param str document_name: The document name to use when starting the SSM automation document.
        :param str role_arn: The role ARN to use when starting the SSM automation document.
        :param str document_version: The version of the document to use when starting the SSM automation document.
        :param Sequence['ResponsePlanDynamicSsmParameter'] dynamic_parameters: The parameters with dynamic values to set when starting the SSM automation document.
        :param Sequence['ResponsePlanSsmParameter'] parameters: The parameters to set when starting the SSM automation document.
        :param 'ResponsePlanSsmAutomationTargetAccount' target_account: The account type to use when starting the SSM automation document.
        """
        pulumi.set(__self__, "document_name", document_name)
        pulumi.set(__self__, "role_arn", role_arn)
        if document_version is not None:
            pulumi.set(__self__, "document_version", document_version)
        if dynamic_parameters is not None:
            pulumi.set(__self__, "dynamic_parameters", dynamic_parameters)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if target_account is not None:
            pulumi.set(__self__, "target_account", target_account)

    @property
    @pulumi.getter(name="documentName")
    def document_name(self) -> str:
        """
        The document name to use when starting the SSM automation document.
        """
        return pulumi.get(self, "document_name")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        The role ARN to use when starting the SSM automation document.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[str]:
        """
        The version of the document to use when starting the SSM automation document.
        """
        return pulumi.get(self, "document_version")

    @property
    @pulumi.getter(name="dynamicParameters")
    def dynamic_parameters(self) -> Optional[Sequence['outputs.ResponsePlanDynamicSsmParameter']]:
        """
        The parameters with dynamic values to set when starting the SSM automation document.
        """
        return pulumi.get(self, "dynamic_parameters")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence['outputs.ResponsePlanSsmParameter']]:
        """
        The parameters to set when starting the SSM automation document.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="targetAccount")
    def target_account(self) -> Optional['ResponsePlanSsmAutomationTargetAccount']:
        """
        The account type to use when starting the SSM automation document.
        """
        return pulumi.get(self, "target_account")


@pulumi.output_type
class ResponsePlanSsmParameter(dict):
    """
    A parameter to set when starting the SSM automation document.
    """
    def __init__(__self__, *,
                 key: str,
                 values: Sequence[str]):
        """
        A parameter to set when starting the SSM automation document.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")


@pulumi.output_type
class ResponsePlanTag(dict):
    """
    A key-value pair to tag a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to tag a resource.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


