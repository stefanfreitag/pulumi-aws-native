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

__all__ = [
    'DetectorCfnDataSourceConfigurations',
    'DetectorCfnFeatureAdditionalConfiguration',
    'DetectorCfnFeatureConfiguration',
    'DetectorCfnKubernetesAuditLogsConfiguration',
    'DetectorCfnKubernetesConfiguration',
    'DetectorCfnMalwareProtectionConfiguration',
    'DetectorCfnScanEc2InstanceWithFindingsConfiguration',
    'DetectorCfns3LogsConfiguration',
    'DetectorTagItem',
    'FilterCondition',
    'FilterFindingCriteria',
    'FilterTag',
    'IpSetTag',
    'ThreatIntelSetTag',
]

@pulumi.output_type
class DetectorCfnDataSourceConfigurations(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "malwareProtection":
            suggest = "malware_protection"
        elif key == "s3Logs":
            suggest = "s3_logs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DetectorCfnDataSourceConfigurations. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DetectorCfnDataSourceConfigurations.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DetectorCfnDataSourceConfigurations.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 kubernetes: Optional['outputs.DetectorCfnKubernetesConfiguration'] = None,
                 malware_protection: Optional['outputs.DetectorCfnMalwareProtectionConfiguration'] = None,
                 s3_logs: Optional['outputs.DetectorCfns3LogsConfiguration'] = None):
        DetectorCfnDataSourceConfigurations._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kubernetes=kubernetes,
            malware_protection=malware_protection,
            s3_logs=s3_logs,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kubernetes: Optional['outputs.DetectorCfnKubernetesConfiguration'] = None,
             malware_protection: Optional['outputs.DetectorCfnMalwareProtectionConfiguration'] = None,
             s3_logs: Optional['outputs.DetectorCfns3LogsConfiguration'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if kubernetes is not None:
            _setter("kubernetes", kubernetes)
        if malware_protection is not None:
            _setter("malware_protection", malware_protection)
        if s3_logs is not None:
            _setter("s3_logs", s3_logs)

    @property
    @pulumi.getter
    def kubernetes(self) -> Optional['outputs.DetectorCfnKubernetesConfiguration']:
        return pulumi.get(self, "kubernetes")

    @property
    @pulumi.getter(name="malwareProtection")
    def malware_protection(self) -> Optional['outputs.DetectorCfnMalwareProtectionConfiguration']:
        return pulumi.get(self, "malware_protection")

    @property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional['outputs.DetectorCfns3LogsConfiguration']:
        return pulumi.get(self, "s3_logs")


@pulumi.output_type
class DetectorCfnFeatureAdditionalConfiguration(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        DetectorCfnFeatureAdditionalConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


@pulumi.output_type
class DetectorCfnFeatureConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalConfiguration":
            suggest = "additional_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DetectorCfnFeatureConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DetectorCfnFeatureConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DetectorCfnFeatureConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: 'DetectorCfnFeatureConfigurationName',
                 status: 'DetectorCfnFeatureConfigurationStatus',
                 additional_configuration: Optional[Sequence['outputs.DetectorCfnFeatureAdditionalConfiguration']] = None):
        DetectorCfnFeatureConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            status=status,
            additional_configuration=additional_configuration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: 'DetectorCfnFeatureConfigurationName',
             status: 'DetectorCfnFeatureConfigurationStatus',
             additional_configuration: Optional[Sequence['outputs.DetectorCfnFeatureAdditionalConfiguration']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("status", status)
        if additional_configuration is not None:
            _setter("additional_configuration", additional_configuration)

    @property
    @pulumi.getter
    def name(self) -> 'DetectorCfnFeatureConfigurationName':
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> 'DetectorCfnFeatureConfigurationStatus':
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[Sequence['outputs.DetectorCfnFeatureAdditionalConfiguration']]:
        return pulumi.get(self, "additional_configuration")


@pulumi.output_type
class DetectorCfnKubernetesAuditLogsConfiguration(dict):
    def __init__(__self__, *,
                 enable: bool):
        DetectorCfnKubernetesAuditLogsConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable=enable,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable: bool,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enable", enable)

    @property
    @pulumi.getter
    def enable(self) -> bool:
        return pulumi.get(self, "enable")


@pulumi.output_type
class DetectorCfnKubernetesConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "auditLogs":
            suggest = "audit_logs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DetectorCfnKubernetesConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DetectorCfnKubernetesConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DetectorCfnKubernetesConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 audit_logs: 'outputs.DetectorCfnKubernetesAuditLogsConfiguration'):
        DetectorCfnKubernetesConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            audit_logs=audit_logs,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             audit_logs: 'outputs.DetectorCfnKubernetesAuditLogsConfiguration',
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("audit_logs", audit_logs)

    @property
    @pulumi.getter(name="auditLogs")
    def audit_logs(self) -> 'outputs.DetectorCfnKubernetesAuditLogsConfiguration':
        return pulumi.get(self, "audit_logs")


@pulumi.output_type
class DetectorCfnMalwareProtectionConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scanEc2InstanceWithFindings":
            suggest = "scan_ec2_instance_with_findings"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DetectorCfnMalwareProtectionConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DetectorCfnMalwareProtectionConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DetectorCfnMalwareProtectionConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 scan_ec2_instance_with_findings: Optional['outputs.DetectorCfnScanEc2InstanceWithFindingsConfiguration'] = None):
        DetectorCfnMalwareProtectionConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            scan_ec2_instance_with_findings=scan_ec2_instance_with_findings,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             scan_ec2_instance_with_findings: Optional['outputs.DetectorCfnScanEc2InstanceWithFindingsConfiguration'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if scan_ec2_instance_with_findings is not None:
            _setter("scan_ec2_instance_with_findings", scan_ec2_instance_with_findings)

    @property
    @pulumi.getter(name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(self) -> Optional['outputs.DetectorCfnScanEc2InstanceWithFindingsConfiguration']:
        return pulumi.get(self, "scan_ec2_instance_with_findings")


@pulumi.output_type
class DetectorCfnScanEc2InstanceWithFindingsConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ebsVolumes":
            suggest = "ebs_volumes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DetectorCfnScanEc2InstanceWithFindingsConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DetectorCfnScanEc2InstanceWithFindingsConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DetectorCfnScanEc2InstanceWithFindingsConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ebs_volumes: Optional[bool] = None):
        DetectorCfnScanEc2InstanceWithFindingsConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ebs_volumes=ebs_volumes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ebs_volumes: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if ebs_volumes is not None:
            _setter("ebs_volumes", ebs_volumes)

    @property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(self) -> Optional[bool]:
        return pulumi.get(self, "ebs_volumes")


@pulumi.output_type
class DetectorCfns3LogsConfiguration(dict):
    def __init__(__self__, *,
                 enable: bool):
        DetectorCfns3LogsConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable=enable,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable: bool,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enable", enable)

    @property
    @pulumi.getter
    def enable(self) -> bool:
        return pulumi.get(self, "enable")


@pulumi.output_type
class DetectorTagItem(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        DetectorTagItem._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class FilterCondition(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "greaterThan":
            suggest = "greater_than"
        elif key == "greaterThanOrEqual":
            suggest = "greater_than_or_equal"
        elif key == "lessThan":
            suggest = "less_than"
        elif key == "lessThanOrEqual":
            suggest = "less_than_or_equal"
        elif key == "notEquals":
            suggest = "not_equals"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FilterCondition. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FilterCondition.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FilterCondition.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 eq: Optional[Sequence[str]] = None,
                 equals: Optional[Sequence[str]] = None,
                 greater_than: Optional[int] = None,
                 greater_than_or_equal: Optional[int] = None,
                 gt: Optional[int] = None,
                 gte: Optional[int] = None,
                 less_than: Optional[int] = None,
                 less_than_or_equal: Optional[int] = None,
                 lt: Optional[int] = None,
                 lte: Optional[int] = None,
                 neq: Optional[Sequence[str]] = None,
                 not_equals: Optional[Sequence[str]] = None):
        FilterCondition._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            eq=eq,
            equals=equals,
            greater_than=greater_than,
            greater_than_or_equal=greater_than_or_equal,
            gt=gt,
            gte=gte,
            less_than=less_than,
            less_than_or_equal=less_than_or_equal,
            lt=lt,
            lte=lte,
            neq=neq,
            not_equals=not_equals,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             eq: Optional[Sequence[str]] = None,
             equals: Optional[Sequence[str]] = None,
             greater_than: Optional[int] = None,
             greater_than_or_equal: Optional[int] = None,
             gt: Optional[int] = None,
             gte: Optional[int] = None,
             less_than: Optional[int] = None,
             less_than_or_equal: Optional[int] = None,
             lt: Optional[int] = None,
             lte: Optional[int] = None,
             neq: Optional[Sequence[str]] = None,
             not_equals: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if eq is not None:
            _setter("eq", eq)
        if equals is not None:
            _setter("equals", equals)
        if greater_than is not None:
            _setter("greater_than", greater_than)
        if greater_than_or_equal is not None:
            _setter("greater_than_or_equal", greater_than_or_equal)
        if gt is not None:
            _setter("gt", gt)
        if gte is not None:
            _setter("gte", gte)
        if less_than is not None:
            _setter("less_than", less_than)
        if less_than_or_equal is not None:
            _setter("less_than_or_equal", less_than_or_equal)
        if lt is not None:
            _setter("lt", lt)
        if lte is not None:
            _setter("lte", lte)
        if neq is not None:
            _setter("neq", neq)
        if not_equals is not None:
            _setter("not_equals", not_equals)

    @property
    @pulumi.getter
    def eq(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "eq")

    @property
    @pulumi.getter
    def equals(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "equals")

    @property
    @pulumi.getter(name="greaterThan")
    def greater_than(self) -> Optional[int]:
        return pulumi.get(self, "greater_than")

    @property
    @pulumi.getter(name="greaterThanOrEqual")
    def greater_than_or_equal(self) -> Optional[int]:
        return pulumi.get(self, "greater_than_or_equal")

    @property
    @pulumi.getter
    def gt(self) -> Optional[int]:
        return pulumi.get(self, "gt")

    @property
    @pulumi.getter
    def gte(self) -> Optional[int]:
        return pulumi.get(self, "gte")

    @property
    @pulumi.getter(name="lessThan")
    def less_than(self) -> Optional[int]:
        return pulumi.get(self, "less_than")

    @property
    @pulumi.getter(name="lessThanOrEqual")
    def less_than_or_equal(self) -> Optional[int]:
        return pulumi.get(self, "less_than_or_equal")

    @property
    @pulumi.getter
    def lt(self) -> Optional[int]:
        return pulumi.get(self, "lt")

    @property
    @pulumi.getter
    def lte(self) -> Optional[int]:
        return pulumi.get(self, "lte")

    @property
    @pulumi.getter
    def neq(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "neq")

    @property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "not_equals")


@pulumi.output_type
class FilterFindingCriteria(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "itemType":
            suggest = "item_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FilterFindingCriteria. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FilterFindingCriteria.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FilterFindingCriteria.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 criterion: Optional[Any] = None,
                 item_type: Optional['outputs.FilterCondition'] = None):
        FilterFindingCriteria._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            criterion=criterion,
            item_type=item_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             criterion: Optional[Any] = None,
             item_type: Optional['outputs.FilterCondition'] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if criterion is not None:
            _setter("criterion", criterion)
        if item_type is not None:
            _setter("item_type", item_type)

    @property
    @pulumi.getter
    def criterion(self) -> Optional[Any]:
        return pulumi.get(self, "criterion")

    @property
    @pulumi.getter(name="itemType")
    def item_type(self) -> Optional['outputs.FilterCondition']:
        return pulumi.get(self, "item_type")


@pulumi.output_type
class FilterTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        FilterTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class IpSetTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        IpSetTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class ThreatIntelSetTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        ThreatIntelSetTag._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: str,
             value: str,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


