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

__all__ = [
    'CampaignAgentlessDialerConfig',
    'CampaignAnswerMachineDetectionConfig',
    'CampaignDialerConfig',
    'CampaignOutboundCallConfig',
    'CampaignPredictiveDialerConfig',
    'CampaignProgressiveDialerConfig',
    'CampaignTag',
]

@pulumi.output_type
class CampaignAgentlessDialerConfig(dict):
    """
    Agentless Dialer config
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dialingCapacity":
            suggest = "dialing_capacity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CampaignAgentlessDialerConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CampaignAgentlessDialerConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CampaignAgentlessDialerConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dialing_capacity: Optional[float] = None):
        """
        Agentless Dialer config
        :param float dialing_capacity: Allocates dialing capacity for this campaign between multiple active campaigns.
        """
        if dialing_capacity is not None:
            pulumi.set(__self__, "dialing_capacity", dialing_capacity)

    @property
    @pulumi.getter(name="dialingCapacity")
    def dialing_capacity(self) -> Optional[float]:
        """
        Allocates dialing capacity for this campaign between multiple active campaigns.
        """
        return pulumi.get(self, "dialing_capacity")


@pulumi.output_type
class CampaignAnswerMachineDetectionConfig(dict):
    """
    The configuration used for answering machine detection during outbound calls
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enableAnswerMachineDetection":
            suggest = "enable_answer_machine_detection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CampaignAnswerMachineDetectionConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CampaignAnswerMachineDetectionConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CampaignAnswerMachineDetectionConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enable_answer_machine_detection: bool):
        """
        The configuration used for answering machine detection during outbound calls
        :param bool enable_answer_machine_detection: Flag to decided whether outbound calls should have answering machine detection enabled or not
        """
        pulumi.set(__self__, "enable_answer_machine_detection", enable_answer_machine_detection)

    @property
    @pulumi.getter(name="enableAnswerMachineDetection")
    def enable_answer_machine_detection(self) -> bool:
        """
        Flag to decided whether outbound calls should have answering machine detection enabled or not
        """
        return pulumi.get(self, "enable_answer_machine_detection")


@pulumi.output_type
class CampaignDialerConfig(dict):
    """
    The possible types of dialer config parameters
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "agentlessDialerConfig":
            suggest = "agentless_dialer_config"
        elif key == "predictiveDialerConfig":
            suggest = "predictive_dialer_config"
        elif key == "progressiveDialerConfig":
            suggest = "progressive_dialer_config"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CampaignDialerConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CampaignDialerConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CampaignDialerConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 agentless_dialer_config: Optional['outputs.CampaignAgentlessDialerConfig'] = None,
                 predictive_dialer_config: Optional['outputs.CampaignPredictiveDialerConfig'] = None,
                 progressive_dialer_config: Optional['outputs.CampaignProgressiveDialerConfig'] = None):
        """
        The possible types of dialer config parameters
        """
        if agentless_dialer_config is not None:
            pulumi.set(__self__, "agentless_dialer_config", agentless_dialer_config)
        if predictive_dialer_config is not None:
            pulumi.set(__self__, "predictive_dialer_config", predictive_dialer_config)
        if progressive_dialer_config is not None:
            pulumi.set(__self__, "progressive_dialer_config", progressive_dialer_config)

    @property
    @pulumi.getter(name="agentlessDialerConfig")
    def agentless_dialer_config(self) -> Optional['outputs.CampaignAgentlessDialerConfig']:
        return pulumi.get(self, "agentless_dialer_config")

    @property
    @pulumi.getter(name="predictiveDialerConfig")
    def predictive_dialer_config(self) -> Optional['outputs.CampaignPredictiveDialerConfig']:
        return pulumi.get(self, "predictive_dialer_config")

    @property
    @pulumi.getter(name="progressiveDialerConfig")
    def progressive_dialer_config(self) -> Optional['outputs.CampaignProgressiveDialerConfig']:
        return pulumi.get(self, "progressive_dialer_config")


@pulumi.output_type
class CampaignOutboundCallConfig(dict):
    """
    The configuration used for outbound calls.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "connectContactFlowArn":
            suggest = "connect_contact_flow_arn"
        elif key == "answerMachineDetectionConfig":
            suggest = "answer_machine_detection_config"
        elif key == "connectQueueArn":
            suggest = "connect_queue_arn"
        elif key == "connectSourcePhoneNumber":
            suggest = "connect_source_phone_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CampaignOutboundCallConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CampaignOutboundCallConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CampaignOutboundCallConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 connect_contact_flow_arn: str,
                 answer_machine_detection_config: Optional['outputs.CampaignAnswerMachineDetectionConfig'] = None,
                 connect_queue_arn: Optional[str] = None,
                 connect_source_phone_number: Optional[str] = None):
        """
        The configuration used for outbound calls.
        :param str connect_contact_flow_arn: The identifier of the contact flow for the outbound call.
        :param str connect_queue_arn: The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number.
        :param str connect_source_phone_number: The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.
        """
        pulumi.set(__self__, "connect_contact_flow_arn", connect_contact_flow_arn)
        if answer_machine_detection_config is not None:
            pulumi.set(__self__, "answer_machine_detection_config", answer_machine_detection_config)
        if connect_queue_arn is not None:
            pulumi.set(__self__, "connect_queue_arn", connect_queue_arn)
        if connect_source_phone_number is not None:
            pulumi.set(__self__, "connect_source_phone_number", connect_source_phone_number)

    @property
    @pulumi.getter(name="connectContactFlowArn")
    def connect_contact_flow_arn(self) -> str:
        """
        The identifier of the contact flow for the outbound call.
        """
        return pulumi.get(self, "connect_contact_flow_arn")

    @property
    @pulumi.getter(name="answerMachineDetectionConfig")
    def answer_machine_detection_config(self) -> Optional['outputs.CampaignAnswerMachineDetectionConfig']:
        return pulumi.get(self, "answer_machine_detection_config")

    @property
    @pulumi.getter(name="connectQueueArn")
    def connect_queue_arn(self) -> Optional[str]:
        """
        The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the contact flow is used. If you do not specify a queue, you must specify a source phone number.
        """
        return pulumi.get(self, "connect_queue_arn")

    @property
    @pulumi.getter(name="connectSourcePhoneNumber")
    def connect_source_phone_number(self) -> Optional[str]:
        """
        The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.
        """
        return pulumi.get(self, "connect_source_phone_number")


@pulumi.output_type
class CampaignPredictiveDialerConfig(dict):
    """
    Predictive Dialer config
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bandwidthAllocation":
            suggest = "bandwidth_allocation"
        elif key == "dialingCapacity":
            suggest = "dialing_capacity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CampaignPredictiveDialerConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CampaignPredictiveDialerConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CampaignPredictiveDialerConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bandwidth_allocation: float,
                 dialing_capacity: Optional[float] = None):
        """
        Predictive Dialer config
        :param float bandwidth_allocation: The bandwidth allocation of a queue resource.
        :param float dialing_capacity: Allocates dialing capacity for this campaign between multiple active campaigns.
        """
        pulumi.set(__self__, "bandwidth_allocation", bandwidth_allocation)
        if dialing_capacity is not None:
            pulumi.set(__self__, "dialing_capacity", dialing_capacity)

    @property
    @pulumi.getter(name="bandwidthAllocation")
    def bandwidth_allocation(self) -> float:
        """
        The bandwidth allocation of a queue resource.
        """
        return pulumi.get(self, "bandwidth_allocation")

    @property
    @pulumi.getter(name="dialingCapacity")
    def dialing_capacity(self) -> Optional[float]:
        """
        Allocates dialing capacity for this campaign between multiple active campaigns.
        """
        return pulumi.get(self, "dialing_capacity")


@pulumi.output_type
class CampaignProgressiveDialerConfig(dict):
    """
    Progressive Dialer config
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bandwidthAllocation":
            suggest = "bandwidth_allocation"
        elif key == "dialingCapacity":
            suggest = "dialing_capacity"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CampaignProgressiveDialerConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CampaignProgressiveDialerConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CampaignProgressiveDialerConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bandwidth_allocation: float,
                 dialing_capacity: Optional[float] = None):
        """
        Progressive Dialer config
        :param float bandwidth_allocation: The bandwidth allocation of a queue resource.
        :param float dialing_capacity: Allocates dialing capacity for this campaign between multiple active campaigns.
        """
        pulumi.set(__self__, "bandwidth_allocation", bandwidth_allocation)
        if dialing_capacity is not None:
            pulumi.set(__self__, "dialing_capacity", dialing_capacity)

    @property
    @pulumi.getter(name="bandwidthAllocation")
    def bandwidth_allocation(self) -> float:
        """
        The bandwidth allocation of a queue resource.
        """
        return pulumi.get(self, "bandwidth_allocation")

    @property
    @pulumi.getter(name="dialingCapacity")
    def dialing_capacity(self) -> Optional[float]:
        """
        Allocates dialing capacity for this campaign between multiple active campaigns.
        """
        return pulumi.get(self, "dialing_capacity")


@pulumi.output_type
class CampaignTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        :param str value: The value for the tag. You can specify a value that's 1 to 256 characters in length.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. 
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag. You can specify a value that's 1 to 256 characters in length.
        """
        return pulumi.get(self, "value")


