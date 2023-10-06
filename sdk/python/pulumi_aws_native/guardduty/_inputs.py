# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'DetectorCfnDataSourceConfigurationsArgs',
    'DetectorCfnFeatureAdditionalConfigurationArgs',
    'DetectorCfnFeatureConfigurationArgs',
    'DetectorCfnKubernetesAuditLogsConfigurationArgs',
    'DetectorCfnKubernetesConfigurationArgs',
    'DetectorCfnMalwareProtectionConfigurationArgs',
    'DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs',
    'DetectorCfns3LogsConfigurationArgs',
    'DetectorTagItemArgs',
    'FilterConditionArgs',
    'FilterFindingCriteriaArgs',
    'FilterTagArgs',
    'IpSetTagArgs',
    'ThreatIntelSetTagArgs',
]

@pulumi.input_type
class DetectorCfnDataSourceConfigurationsArgs:
    def __init__(__self__, *,
                 kubernetes: Optional[pulumi.Input['DetectorCfnKubernetesConfigurationArgs']] = None,
                 malware_protection: Optional[pulumi.Input['DetectorCfnMalwareProtectionConfigurationArgs']] = None,
                 s3_logs: Optional[pulumi.Input['DetectorCfns3LogsConfigurationArgs']] = None):
        DetectorCfnDataSourceConfigurationsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kubernetes=kubernetes,
            malware_protection=malware_protection,
            s3_logs=s3_logs,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kubernetes: Optional[pulumi.Input['DetectorCfnKubernetesConfigurationArgs']] = None,
             malware_protection: Optional[pulumi.Input['DetectorCfnMalwareProtectionConfigurationArgs']] = None,
             s3_logs: Optional[pulumi.Input['DetectorCfns3LogsConfigurationArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if kubernetes is not None:
            _setter("kubernetes", kubernetes)
        if malware_protection is not None:
            _setter("malware_protection", malware_protection)
        if s3_logs is not None:
            _setter("s3_logs", s3_logs)

    @property
    @pulumi.getter
    def kubernetes(self) -> Optional[pulumi.Input['DetectorCfnKubernetesConfigurationArgs']]:
        return pulumi.get(self, "kubernetes")

    @kubernetes.setter
    def kubernetes(self, value: Optional[pulumi.Input['DetectorCfnKubernetesConfigurationArgs']]):
        pulumi.set(self, "kubernetes", value)

    @property
    @pulumi.getter(name="malwareProtection")
    def malware_protection(self) -> Optional[pulumi.Input['DetectorCfnMalwareProtectionConfigurationArgs']]:
        return pulumi.get(self, "malware_protection")

    @malware_protection.setter
    def malware_protection(self, value: Optional[pulumi.Input['DetectorCfnMalwareProtectionConfigurationArgs']]):
        pulumi.set(self, "malware_protection", value)

    @property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional[pulumi.Input['DetectorCfns3LogsConfigurationArgs']]:
        return pulumi.get(self, "s3_logs")

    @s3_logs.setter
    def s3_logs(self, value: Optional[pulumi.Input['DetectorCfns3LogsConfigurationArgs']]):
        pulumi.set(self, "s3_logs", value)


@pulumi.input_type
class DetectorCfnFeatureAdditionalConfigurationArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        DetectorCfnFeatureAdditionalConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class DetectorCfnFeatureConfigurationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input['DetectorCfnFeatureConfigurationName'],
                 status: pulumi.Input['DetectorCfnFeatureConfigurationStatus'],
                 additional_configuration: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureAdditionalConfigurationArgs']]]] = None):
        DetectorCfnFeatureConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            status=status,
            additional_configuration=additional_configuration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: pulumi.Input['DetectorCfnFeatureConfigurationName'],
             status: pulumi.Input['DetectorCfnFeatureConfigurationStatus'],
             additional_configuration: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureAdditionalConfigurationArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("name", name)
        _setter("status", status)
        if additional_configuration is not None:
            _setter("additional_configuration", additional_configuration)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input['DetectorCfnFeatureConfigurationName']:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input['DetectorCfnFeatureConfigurationName']):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input['DetectorCfnFeatureConfigurationStatus']:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input['DetectorCfnFeatureConfigurationStatus']):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureAdditionalConfigurationArgs']]]]:
        return pulumi.get(self, "additional_configuration")

    @additional_configuration.setter
    def additional_configuration(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorCfnFeatureAdditionalConfigurationArgs']]]]):
        pulumi.set(self, "additional_configuration", value)


@pulumi.input_type
class DetectorCfnKubernetesAuditLogsConfigurationArgs:
    def __init__(__self__, *,
                 enable: pulumi.Input[bool]):
        DetectorCfnKubernetesAuditLogsConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable=enable,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable: pulumi.Input[bool],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enable", enable)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable", value)


@pulumi.input_type
class DetectorCfnKubernetesConfigurationArgs:
    def __init__(__self__, *,
                 audit_logs: pulumi.Input['DetectorCfnKubernetesAuditLogsConfigurationArgs']):
        DetectorCfnKubernetesConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            audit_logs=audit_logs,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             audit_logs: pulumi.Input['DetectorCfnKubernetesAuditLogsConfigurationArgs'],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("audit_logs", audit_logs)

    @property
    @pulumi.getter(name="auditLogs")
    def audit_logs(self) -> pulumi.Input['DetectorCfnKubernetesAuditLogsConfigurationArgs']:
        return pulumi.get(self, "audit_logs")

    @audit_logs.setter
    def audit_logs(self, value: pulumi.Input['DetectorCfnKubernetesAuditLogsConfigurationArgs']):
        pulumi.set(self, "audit_logs", value)


@pulumi.input_type
class DetectorCfnMalwareProtectionConfigurationArgs:
    def __init__(__self__, *,
                 scan_ec2_instance_with_findings: Optional[pulumi.Input['DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs']] = None):
        DetectorCfnMalwareProtectionConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            scan_ec2_instance_with_findings=scan_ec2_instance_with_findings,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             scan_ec2_instance_with_findings: Optional[pulumi.Input['DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if scan_ec2_instance_with_findings is not None:
            _setter("scan_ec2_instance_with_findings", scan_ec2_instance_with_findings)

    @property
    @pulumi.getter(name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(self) -> Optional[pulumi.Input['DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs']]:
        return pulumi.get(self, "scan_ec2_instance_with_findings")

    @scan_ec2_instance_with_findings.setter
    def scan_ec2_instance_with_findings(self, value: Optional[pulumi.Input['DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs']]):
        pulumi.set(self, "scan_ec2_instance_with_findings", value)


@pulumi.input_type
class DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs:
    def __init__(__self__, *,
                 ebs_volumes: Optional[pulumi.Input[bool]] = None):
        DetectorCfnScanEc2InstanceWithFindingsConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ebs_volumes=ebs_volumes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ebs_volumes: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if ebs_volumes is not None:
            _setter("ebs_volumes", ebs_volumes)

    @property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ebs_volumes")

    @ebs_volumes.setter
    def ebs_volumes(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ebs_volumes", value)


@pulumi.input_type
class DetectorCfns3LogsConfigurationArgs:
    def __init__(__self__, *,
                 enable: pulumi.Input[bool]):
        DetectorCfns3LogsConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enable=enable,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enable: pulumi.Input[bool],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enable", enable)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable", value)


@pulumi.input_type
class DetectorTagItemArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        DetectorTagItemArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class FilterConditionArgs:
    def __init__(__self__, *,
                 eq: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 greater_than: Optional[pulumi.Input[int]] = None,
                 greater_than_or_equal: Optional[pulumi.Input[int]] = None,
                 gt: Optional[pulumi.Input[int]] = None,
                 gte: Optional[pulumi.Input[int]] = None,
                 less_than: Optional[pulumi.Input[int]] = None,
                 less_than_or_equal: Optional[pulumi.Input[int]] = None,
                 lt: Optional[pulumi.Input[int]] = None,
                 lte: Optional[pulumi.Input[int]] = None,
                 neq: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        FilterConditionArgs._configure(
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
             eq: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             greater_than: Optional[pulumi.Input[int]] = None,
             greater_than_or_equal: Optional[pulumi.Input[int]] = None,
             gt: Optional[pulumi.Input[int]] = None,
             gte: Optional[pulumi.Input[int]] = None,
             less_than: Optional[pulumi.Input[int]] = None,
             less_than_or_equal: Optional[pulumi.Input[int]] = None,
             lt: Optional[pulumi.Input[int]] = None,
             lte: Optional[pulumi.Input[int]] = None,
             neq: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
    def eq(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "eq")

    @eq.setter
    def eq(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "eq", value)

    @property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "equals")

    @equals.setter
    def equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "equals", value)

    @property
    @pulumi.getter(name="greaterThan")
    def greater_than(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "greater_than")

    @greater_than.setter
    def greater_than(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "greater_than", value)

    @property
    @pulumi.getter(name="greaterThanOrEqual")
    def greater_than_or_equal(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "greater_than_or_equal")

    @greater_than_or_equal.setter
    def greater_than_or_equal(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "greater_than_or_equal", value)

    @property
    @pulumi.getter
    def gt(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "gt")

    @gt.setter
    def gt(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "gt", value)

    @property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "gte")

    @gte.setter
    def gte(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "gte", value)

    @property
    @pulumi.getter(name="lessThan")
    def less_than(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "less_than")

    @less_than.setter
    def less_than(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "less_than", value)

    @property
    @pulumi.getter(name="lessThanOrEqual")
    def less_than_or_equal(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "less_than_or_equal")

    @less_than_or_equal.setter
    def less_than_or_equal(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "less_than_or_equal", value)

    @property
    @pulumi.getter
    def lt(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "lt")

    @lt.setter
    def lt(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lt", value)

    @property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "lte")

    @lte.setter
    def lte(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "lte", value)

    @property
    @pulumi.getter
    def neq(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "neq")

    @neq.setter
    def neq(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "neq", value)

    @property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "not_equals")

    @not_equals.setter
    def not_equals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "not_equals", value)


@pulumi.input_type
class FilterFindingCriteriaArgs:
    def __init__(__self__, *,
                 criterion: Optional[Any] = None,
                 item_type: Optional[pulumi.Input['FilterConditionArgs']] = None):
        FilterFindingCriteriaArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            criterion=criterion,
            item_type=item_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             criterion: Optional[Any] = None,
             item_type: Optional[pulumi.Input['FilterConditionArgs']] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if criterion is not None:
            _setter("criterion", criterion)
        if item_type is not None:
            _setter("item_type", item_type)

    @property
    @pulumi.getter
    def criterion(self) -> Optional[Any]:
        return pulumi.get(self, "criterion")

    @criterion.setter
    def criterion(self, value: Optional[Any]):
        pulumi.set(self, "criterion", value)

    @property
    @pulumi.getter(name="itemType")
    def item_type(self) -> Optional[pulumi.Input['FilterConditionArgs']]:
        return pulumi.get(self, "item_type")

    @item_type.setter
    def item_type(self, value: Optional[pulumi.Input['FilterConditionArgs']]):
        pulumi.set(self, "item_type", value)


@pulumi.input_type
class FilterTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        FilterTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class IpSetTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        IpSetTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ThreatIntelSetTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        ThreatIntelSetTagArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             value: pulumi.Input[str],
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


