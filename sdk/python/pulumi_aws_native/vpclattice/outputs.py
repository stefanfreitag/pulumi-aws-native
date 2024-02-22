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
    'ListenerDefaultAction',
    'ListenerFixedResponse',
    'ListenerForward',
    'ListenerWeightedTargetGroup',
    'RuleAction',
    'RuleFixedResponse',
    'RuleForward',
    'RuleHeaderMatch',
    'RuleHeaderMatchType',
    'RuleHttpMatch',
    'RuleMatch',
    'RulePathMatch',
    'RulePathMatchType',
    'RuleWeightedTargetGroup',
    'ServiceDnsEntry',
    'ServiceNetworkServiceAssociationDnsEntry',
    'TargetGroupConfig',
    'TargetGroupHealthCheckConfig',
    'TargetGroupMatcher',
    'TargetGroupTarget',
]

@pulumi.output_type
class ListenerDefaultAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fixedResponse":
            suggest = "fixed_response"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListenerDefaultAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListenerDefaultAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListenerDefaultAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fixed_response: Optional['outputs.ListenerFixedResponse'] = None,
                 forward: Optional['outputs.ListenerForward'] = None):
        if fixed_response is not None:
            pulumi.set(__self__, "fixed_response", fixed_response)
        if forward is not None:
            pulumi.set(__self__, "forward", forward)

    @property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional['outputs.ListenerFixedResponse']:
        return pulumi.get(self, "fixed_response")

    @property
    @pulumi.getter
    def forward(self) -> Optional['outputs.ListenerForward']:
        return pulumi.get(self, "forward")


@pulumi.output_type
class ListenerFixedResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "statusCode":
            suggest = "status_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListenerFixedResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListenerFixedResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListenerFixedResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status_code: int):
        pulumi.set(__self__, "status_code", status_code)

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> int:
        return pulumi.get(self, "status_code")


@pulumi.output_type
class ListenerForward(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetGroups":
            suggest = "target_groups"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListenerForward. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListenerForward.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListenerForward.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_groups: Sequence['outputs.ListenerWeightedTargetGroup']):
        pulumi.set(__self__, "target_groups", target_groups)

    @property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> Sequence['outputs.ListenerWeightedTargetGroup']:
        return pulumi.get(self, "target_groups")


@pulumi.output_type
class ListenerWeightedTargetGroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetGroupIdentifier":
            suggest = "target_group_identifier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ListenerWeightedTargetGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ListenerWeightedTargetGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ListenerWeightedTargetGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_group_identifier: str,
                 weight: Optional[int] = None):
        pulumi.set(__self__, "target_group_identifier", target_group_identifier)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> str:
        return pulumi.get(self, "target_group_identifier")

    @property
    @pulumi.getter
    def weight(self) -> Optional[int]:
        return pulumi.get(self, "weight")


@pulumi.output_type
class RuleAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fixedResponse":
            suggest = "fixed_response"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fixed_response: Optional['outputs.RuleFixedResponse'] = None,
                 forward: Optional['outputs.RuleForward'] = None):
        if fixed_response is not None:
            pulumi.set(__self__, "fixed_response", fixed_response)
        if forward is not None:
            pulumi.set(__self__, "forward", forward)

    @property
    @pulumi.getter(name="fixedResponse")
    def fixed_response(self) -> Optional['outputs.RuleFixedResponse']:
        return pulumi.get(self, "fixed_response")

    @property
    @pulumi.getter
    def forward(self) -> Optional['outputs.RuleForward']:
        return pulumi.get(self, "forward")


@pulumi.output_type
class RuleFixedResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "statusCode":
            suggest = "status_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleFixedResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleFixedResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleFixedResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status_code: int):
        pulumi.set(__self__, "status_code", status_code)

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> int:
        return pulumi.get(self, "status_code")


@pulumi.output_type
class RuleForward(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetGroups":
            suggest = "target_groups"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleForward. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleForward.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleForward.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_groups: Sequence['outputs.RuleWeightedTargetGroup']):
        pulumi.set(__self__, "target_groups", target_groups)

    @property
    @pulumi.getter(name="targetGroups")
    def target_groups(self) -> Sequence['outputs.RuleWeightedTargetGroup']:
        return pulumi.get(self, "target_groups")


@pulumi.output_type
class RuleHeaderMatch(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "caseSensitive":
            suggest = "case_sensitive"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleHeaderMatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleHeaderMatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleHeaderMatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 match: 'outputs.RuleHeaderMatchType',
                 name: str,
                 case_sensitive: Optional[bool] = None):
        pulumi.set(__self__, "match", match)
        pulumi.set(__self__, "name", name)
        if case_sensitive is not None:
            pulumi.set(__self__, "case_sensitive", case_sensitive)

    @property
    @pulumi.getter
    def match(self) -> 'outputs.RuleHeaderMatchType':
        return pulumi.get(self, "match")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[bool]:
        return pulumi.get(self, "case_sensitive")


@pulumi.output_type
class RuleHeaderMatchType(dict):
    def __init__(__self__, *,
                 contains: Optional[str] = None,
                 exact: Optional[str] = None,
                 prefix: Optional[str] = None):
        if contains is not None:
            pulumi.set(__self__, "contains", contains)
        if exact is not None:
            pulumi.set(__self__, "exact", exact)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def contains(self) -> Optional[str]:
        return pulumi.get(self, "contains")

    @property
    @pulumi.getter
    def exact(self) -> Optional[str]:
        return pulumi.get(self, "exact")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")


@pulumi.output_type
class RuleHttpMatch(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "headerMatches":
            suggest = "header_matches"
        elif key == "pathMatch":
            suggest = "path_match"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleHttpMatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleHttpMatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleHttpMatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 header_matches: Optional[Sequence['outputs.RuleHeaderMatch']] = None,
                 method: Optional['RuleHttpMatchMethod'] = None,
                 path_match: Optional['outputs.RulePathMatch'] = None):
        if header_matches is not None:
            pulumi.set(__self__, "header_matches", header_matches)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if path_match is not None:
            pulumi.set(__self__, "path_match", path_match)

    @property
    @pulumi.getter(name="headerMatches")
    def header_matches(self) -> Optional[Sequence['outputs.RuleHeaderMatch']]:
        return pulumi.get(self, "header_matches")

    @property
    @pulumi.getter
    def method(self) -> Optional['RuleHttpMatchMethod']:
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="pathMatch")
    def path_match(self) -> Optional['outputs.RulePathMatch']:
        return pulumi.get(self, "path_match")


@pulumi.output_type
class RuleMatch(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "httpMatch":
            suggest = "http_match"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleMatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleMatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleMatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 http_match: 'outputs.RuleHttpMatch'):
        pulumi.set(__self__, "http_match", http_match)

    @property
    @pulumi.getter(name="httpMatch")
    def http_match(self) -> 'outputs.RuleHttpMatch':
        return pulumi.get(self, "http_match")


@pulumi.output_type
class RulePathMatch(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "caseSensitive":
            suggest = "case_sensitive"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RulePathMatch. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RulePathMatch.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RulePathMatch.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 match: 'outputs.RulePathMatchType',
                 case_sensitive: Optional[bool] = None):
        pulumi.set(__self__, "match", match)
        if case_sensitive is not None:
            pulumi.set(__self__, "case_sensitive", case_sensitive)

    @property
    @pulumi.getter
    def match(self) -> 'outputs.RulePathMatchType':
        return pulumi.get(self, "match")

    @property
    @pulumi.getter(name="caseSensitive")
    def case_sensitive(self) -> Optional[bool]:
        return pulumi.get(self, "case_sensitive")


@pulumi.output_type
class RulePathMatchType(dict):
    def __init__(__self__, *,
                 exact: Optional[str] = None,
                 prefix: Optional[str] = None):
        if exact is not None:
            pulumi.set(__self__, "exact", exact)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def exact(self) -> Optional[str]:
        return pulumi.get(self, "exact")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")


@pulumi.output_type
class RuleWeightedTargetGroup(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetGroupIdentifier":
            suggest = "target_group_identifier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RuleWeightedTargetGroup. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RuleWeightedTargetGroup.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RuleWeightedTargetGroup.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_group_identifier: str,
                 weight: Optional[int] = None):
        pulumi.set(__self__, "target_group_identifier", target_group_identifier)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="targetGroupIdentifier")
    def target_group_identifier(self) -> str:
        return pulumi.get(self, "target_group_identifier")

    @property
    @pulumi.getter
    def weight(self) -> Optional[int]:
        return pulumi.get(self, "weight")


@pulumi.output_type
class ServiceDnsEntry(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "domainName":
            suggest = "domain_name"
        elif key == "hostedZoneId":
            suggest = "hosted_zone_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceDnsEntry. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceDnsEntry.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceDnsEntry.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 domain_name: Optional[str] = None,
                 hosted_zone_id: Optional[str] = None):
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if hosted_zone_id is not None:
            pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[str]:
        return pulumi.get(self, "hosted_zone_id")


@pulumi.output_type
class ServiceNetworkServiceAssociationDnsEntry(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "domainName":
            suggest = "domain_name"
        elif key == "hostedZoneId":
            suggest = "hosted_zone_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceNetworkServiceAssociationDnsEntry. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceNetworkServiceAssociationDnsEntry.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceNetworkServiceAssociationDnsEntry.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 domain_name: Optional[str] = None,
                 hosted_zone_id: Optional[str] = None):
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if hosted_zone_id is not None:
            pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[str]:
        return pulumi.get(self, "hosted_zone_id")


@pulumi.output_type
class TargetGroupConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "healthCheck":
            suggest = "health_check"
        elif key == "ipAddressType":
            suggest = "ip_address_type"
        elif key == "lambdaEventStructureVersion":
            suggest = "lambda_event_structure_version"
        elif key == "protocolVersion":
            suggest = "protocol_version"
        elif key == "vpcIdentifier":
            suggest = "vpc_identifier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TargetGroupConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TargetGroupConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TargetGroupConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 health_check: Optional['outputs.TargetGroupHealthCheckConfig'] = None,
                 ip_address_type: Optional['TargetGroupConfigIpAddressType'] = None,
                 lambda_event_structure_version: Optional['TargetGroupConfigLambdaEventStructureVersion'] = None,
                 port: Optional[int] = None,
                 protocol: Optional['TargetGroupConfigProtocol'] = None,
                 protocol_version: Optional['TargetGroupConfigProtocolVersion'] = None,
                 vpc_identifier: Optional[str] = None):
        if health_check is not None:
            pulumi.set(__self__, "health_check", health_check)
        if ip_address_type is not None:
            pulumi.set(__self__, "ip_address_type", ip_address_type)
        if lambda_event_structure_version is not None:
            pulumi.set(__self__, "lambda_event_structure_version", lambda_event_structure_version)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if protocol_version is not None:
            pulumi.set(__self__, "protocol_version", protocol_version)
        if vpc_identifier is not None:
            pulumi.set(__self__, "vpc_identifier", vpc_identifier)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional['outputs.TargetGroupHealthCheckConfig']:
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional['TargetGroupConfigIpAddressType']:
        return pulumi.get(self, "ip_address_type")

    @property
    @pulumi.getter(name="lambdaEventStructureVersion")
    def lambda_event_structure_version(self) -> Optional['TargetGroupConfigLambdaEventStructureVersion']:
        return pulumi.get(self, "lambda_event_structure_version")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> Optional['TargetGroupConfigProtocol']:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional['TargetGroupConfigProtocolVersion']:
        return pulumi.get(self, "protocol_version")

    @property
    @pulumi.getter(name="vpcIdentifier")
    def vpc_identifier(self) -> Optional[str]:
        return pulumi.get(self, "vpc_identifier")


@pulumi.output_type
class TargetGroupHealthCheckConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "healthCheckIntervalSeconds":
            suggest = "health_check_interval_seconds"
        elif key == "healthCheckTimeoutSeconds":
            suggest = "health_check_timeout_seconds"
        elif key == "healthyThresholdCount":
            suggest = "healthy_threshold_count"
        elif key == "protocolVersion":
            suggest = "protocol_version"
        elif key == "unhealthyThresholdCount":
            suggest = "unhealthy_threshold_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TargetGroupHealthCheckConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TargetGroupHealthCheckConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TargetGroupHealthCheckConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 health_check_interval_seconds: Optional[int] = None,
                 health_check_timeout_seconds: Optional[int] = None,
                 healthy_threshold_count: Optional[int] = None,
                 matcher: Optional['outputs.TargetGroupMatcher'] = None,
                 path: Optional[str] = None,
                 port: Optional[int] = None,
                 protocol: Optional['TargetGroupHealthCheckConfigProtocol'] = None,
                 protocol_version: Optional['TargetGroupHealthCheckConfigProtocolVersion'] = None,
                 unhealthy_threshold_count: Optional[int] = None):
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if health_check_interval_seconds is not None:
            pulumi.set(__self__, "health_check_interval_seconds", health_check_interval_seconds)
        if health_check_timeout_seconds is not None:
            pulumi.set(__self__, "health_check_timeout_seconds", health_check_timeout_seconds)
        if healthy_threshold_count is not None:
            pulumi.set(__self__, "healthy_threshold_count", healthy_threshold_count)
        if matcher is not None:
            pulumi.set(__self__, "matcher", matcher)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if protocol_version is not None:
            pulumi.set(__self__, "protocol_version", protocol_version)
        if unhealthy_threshold_count is not None:
            pulumi.set(__self__, "unhealthy_threshold_count", unhealthy_threshold_count)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="healthCheckIntervalSeconds")
    def health_check_interval_seconds(self) -> Optional[int]:
        return pulumi.get(self, "health_check_interval_seconds")

    @property
    @pulumi.getter(name="healthCheckTimeoutSeconds")
    def health_check_timeout_seconds(self) -> Optional[int]:
        return pulumi.get(self, "health_check_timeout_seconds")

    @property
    @pulumi.getter(name="healthyThresholdCount")
    def healthy_threshold_count(self) -> Optional[int]:
        return pulumi.get(self, "healthy_threshold_count")

    @property
    @pulumi.getter
    def matcher(self) -> Optional['outputs.TargetGroupMatcher']:
        return pulumi.get(self, "matcher")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> Optional['TargetGroupHealthCheckConfigProtocol']:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional['TargetGroupHealthCheckConfigProtocolVersion']:
        return pulumi.get(self, "protocol_version")

    @property
    @pulumi.getter(name="unhealthyThresholdCount")
    def unhealthy_threshold_count(self) -> Optional[int]:
        return pulumi.get(self, "unhealthy_threshold_count")


@pulumi.output_type
class TargetGroupMatcher(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "httpCode":
            suggest = "http_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TargetGroupMatcher. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TargetGroupMatcher.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TargetGroupMatcher.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 http_code: str):
        pulumi.set(__self__, "http_code", http_code)

    @property
    @pulumi.getter(name="httpCode")
    def http_code(self) -> str:
        return pulumi.get(self, "http_code")


@pulumi.output_type
class TargetGroupTarget(dict):
    def __init__(__self__, *,
                 id: str,
                 port: Optional[int] = None):
        pulumi.set(__self__, "id", id)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")


