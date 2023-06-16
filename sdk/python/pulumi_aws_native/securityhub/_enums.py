# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AutomationRuleDateRangeUnit',
    'AutomationRuleMapFilterComparison',
    'AutomationRuleRuleStatus',
    'AutomationRuleSeverityUpdateLabel',
    'AutomationRuleStringFilterComparison',
    'AutomationRuleWorkflowUpdateStatus',
    'AutomationRulesActionType',
    'AutomationRulesFindingFieldsUpdateVerificationState',
]


class AutomationRuleDateRangeUnit(str, Enum):
    DAYS = "DAYS"


class AutomationRuleMapFilterComparison(str, Enum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"


class AutomationRuleRuleStatus(str, Enum):
    """
    Status of the Rule upon creation
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class AutomationRuleSeverityUpdateLabel(str, Enum):
    INFORMATIONAL = "INFORMATIONAL"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class AutomationRuleStringFilterComparison(str, Enum):
    EQUALS = "EQUALS"
    PREFIX = "PREFIX"
    NOT_EQUALS = "NOT_EQUALS"
    PREFIX_NOT_EQUALS = "PREFIX_NOT_EQUALS"


class AutomationRuleWorkflowUpdateStatus(str, Enum):
    NEW = "NEW"
    NOTIFIED = "NOTIFIED"
    RESOLVED = "RESOLVED"
    SUPPRESSED = "SUPPRESSED"


class AutomationRulesActionType(str, Enum):
    FINDING_FIELDS_UPDATE = "FINDING_FIELDS_UPDATE"


class AutomationRulesFindingFieldsUpdateVerificationState(str, Enum):
    UNKNOWN = "UNKNOWN"
    TRUE_POSITIVE = "TRUE_POSITIVE"
    FALSE_POSITIVE = "FALSE_POSITIVE"
    BENIGN_POSITIVE = "BENIGN_POSITIVE"
