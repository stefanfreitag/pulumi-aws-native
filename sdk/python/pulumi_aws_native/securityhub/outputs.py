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
    'AutomationRuleDateFilter',
    'AutomationRuleDateRange',
    'AutomationRuleMapFilter',
    'AutomationRuleNoteUpdate',
    'AutomationRuleNumberFilter',
    'AutomationRuleRelatedFinding',
    'AutomationRuleSeverityUpdate',
    'AutomationRuleStringFilter',
    'AutomationRuleTags',
    'AutomationRuleWorkflowUpdate',
    'AutomationRulearnOrId',
    'AutomationRulemap',
    'AutomationRulesAction',
    'AutomationRulesFindingFieldsUpdate',
    'AutomationRulesFindingFilters',
    'StandardsControl',
]

@pulumi.output_type
class AutomationRuleDateFilter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dateRange":
            suggest = "date_range"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationRuleDateFilter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationRuleDateFilter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationRuleDateFilter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 date_range: Optional['outputs.AutomationRuleDateRange'] = None,
                 end: Optional[str] = None,
                 start: Optional[str] = None):
        if date_range is not None:
            pulumi.set(__self__, "date_range", date_range)
        if end is not None:
            pulumi.set(__self__, "end", end)
        if start is not None:
            pulumi.set(__self__, "start", start)

    @property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional['outputs.AutomationRuleDateRange']:
        return pulumi.get(self, "date_range")

    @property
    @pulumi.getter
    def end(self) -> Optional[str]:
        return pulumi.get(self, "end")

    @property
    @pulumi.getter
    def start(self) -> Optional[str]:
        return pulumi.get(self, "start")


@pulumi.output_type
class AutomationRuleDateRange(dict):
    def __init__(__self__, *,
                 unit: 'AutomationRuleDateRangeUnit',
                 value: float):
        pulumi.set(__self__, "unit", unit)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def unit(self) -> 'AutomationRuleDateRangeUnit':
        return pulumi.get(self, "unit")

    @property
    @pulumi.getter
    def value(self) -> float:
        return pulumi.get(self, "value")


@pulumi.output_type
class AutomationRuleMapFilter(dict):
    def __init__(__self__, *,
                 comparison: 'AutomationRuleMapFilterComparison',
                 key: str,
                 value: str):
        pulumi.set(__self__, "comparison", comparison)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def comparison(self) -> 'AutomationRuleMapFilterComparison':
        return pulumi.get(self, "comparison")

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class AutomationRuleNoteUpdate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "updatedBy":
            suggest = "updated_by"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationRuleNoteUpdate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationRuleNoteUpdate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationRuleNoteUpdate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 text: str,
                 updated_by: 'outputs.AutomationRulearnOrId'):
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter
    def text(self) -> str:
        return pulumi.get(self, "text")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> 'outputs.AutomationRulearnOrId':
        return pulumi.get(self, "updated_by")


@pulumi.output_type
class AutomationRuleNumberFilter(dict):
    def __init__(__self__, *,
                 eq: Optional[float] = None,
                 gte: Optional[float] = None,
                 lte: Optional[float] = None):
        if eq is not None:
            pulumi.set(__self__, "eq", eq)
        if gte is not None:
            pulumi.set(__self__, "gte", gte)
        if lte is not None:
            pulumi.set(__self__, "lte", lte)

    @property
    @pulumi.getter
    def eq(self) -> Optional[float]:
        return pulumi.get(self, "eq")

    @property
    @pulumi.getter
    def gte(self) -> Optional[float]:
        return pulumi.get(self, "gte")

    @property
    @pulumi.getter
    def lte(self) -> Optional[float]:
        return pulumi.get(self, "lte")


@pulumi.output_type
class AutomationRuleRelatedFinding(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "productArn":
            suggest = "product_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationRuleRelatedFinding. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationRuleRelatedFinding.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationRuleRelatedFinding.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: 'outputs.AutomationRulearnOrId',
                 product_arn: str):
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "product_arn", product_arn)

    @property
    @pulumi.getter
    def id(self) -> 'outputs.AutomationRulearnOrId':
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="productArn")
    def product_arn(self) -> str:
        return pulumi.get(self, "product_arn")


@pulumi.output_type
class AutomationRuleSeverityUpdate(dict):
    def __init__(__self__, *,
                 label: Optional['AutomationRuleSeverityUpdateLabel'] = None,
                 normalized: Optional[int] = None,
                 product: Optional[float] = None):
        if label is not None:
            pulumi.set(__self__, "label", label)
        if normalized is not None:
            pulumi.set(__self__, "normalized", normalized)
        if product is not None:
            pulumi.set(__self__, "product", product)

    @property
    @pulumi.getter
    def label(self) -> Optional['AutomationRuleSeverityUpdateLabel']:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def normalized(self) -> Optional[int]:
        return pulumi.get(self, "normalized")

    @property
    @pulumi.getter
    def product(self) -> Optional[float]:
        return pulumi.get(self, "product")


@pulumi.output_type
class AutomationRuleStringFilter(dict):
    def __init__(__self__, *,
                 comparison: 'AutomationRuleStringFilterComparison',
                 value: str):
        pulumi.set(__self__, "comparison", comparison)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def comparison(self) -> 'AutomationRuleStringFilterComparison':
        return pulumi.get(self, "comparison")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class AutomationRuleTags(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__):
        """
        A key-value pair to associate with a resource.
        """
        pass


@pulumi.output_type
class AutomationRuleWorkflowUpdate(dict):
    def __init__(__self__, *,
                 status: 'AutomationRuleWorkflowUpdateStatus'):
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> 'AutomationRuleWorkflowUpdateStatus':
        return pulumi.get(self, "status")


@pulumi.output_type
class AutomationRulearnOrId(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class AutomationRulemap(dict):
    def __init__(__self__):
        pass


@pulumi.output_type
class AutomationRulesAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "findingFieldsUpdate":
            suggest = "finding_fields_update"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationRulesAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationRulesAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationRulesAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 finding_fields_update: 'outputs.AutomationRulesFindingFieldsUpdate',
                 type: 'AutomationRulesActionType'):
        pulumi.set(__self__, "finding_fields_update", finding_fields_update)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="findingFieldsUpdate")
    def finding_fields_update(self) -> 'outputs.AutomationRulesFindingFieldsUpdate':
        return pulumi.get(self, "finding_fields_update")

    @property
    @pulumi.getter
    def type(self) -> 'AutomationRulesActionType':
        return pulumi.get(self, "type")


@pulumi.output_type
class AutomationRulesFindingFieldsUpdate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "relatedFindings":
            suggest = "related_findings"
        elif key == "userDefinedFields":
            suggest = "user_defined_fields"
        elif key == "verificationState":
            suggest = "verification_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationRulesFindingFieldsUpdate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationRulesFindingFieldsUpdate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationRulesFindingFieldsUpdate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 confidence: Optional[int] = None,
                 criticality: Optional[int] = None,
                 note: Optional['outputs.AutomationRuleNoteUpdate'] = None,
                 related_findings: Optional[Sequence['outputs.AutomationRuleRelatedFinding']] = None,
                 severity: Optional['outputs.AutomationRuleSeverityUpdate'] = None,
                 types: Optional[Sequence[str]] = None,
                 user_defined_fields: Optional['outputs.AutomationRulemap'] = None,
                 verification_state: Optional['AutomationRulesFindingFieldsUpdateVerificationState'] = None,
                 workflow: Optional['outputs.AutomationRuleWorkflowUpdate'] = None):
        """
        :param 'AutomationRuleNoteUpdate' note: Note added to the finding
        :param 'AutomationRuleSeverityUpdate' severity: Severity of the finding
        :param 'AutomationRuleWorkflowUpdate' workflow: Workflow status set for the finding
        """
        if confidence is not None:
            pulumi.set(__self__, "confidence", confidence)
        if criticality is not None:
            pulumi.set(__self__, "criticality", criticality)
        if note is not None:
            pulumi.set(__self__, "note", note)
        if related_findings is not None:
            pulumi.set(__self__, "related_findings", related_findings)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if types is not None:
            pulumi.set(__self__, "types", types)
        if user_defined_fields is not None:
            pulumi.set(__self__, "user_defined_fields", user_defined_fields)
        if verification_state is not None:
            pulumi.set(__self__, "verification_state", verification_state)
        if workflow is not None:
            pulumi.set(__self__, "workflow", workflow)

    @property
    @pulumi.getter
    def confidence(self) -> Optional[int]:
        return pulumi.get(self, "confidence")

    @property
    @pulumi.getter
    def criticality(self) -> Optional[int]:
        return pulumi.get(self, "criticality")

    @property
    @pulumi.getter
    def note(self) -> Optional['outputs.AutomationRuleNoteUpdate']:
        """
        Note added to the finding
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter(name="relatedFindings")
    def related_findings(self) -> Optional[Sequence['outputs.AutomationRuleRelatedFinding']]:
        return pulumi.get(self, "related_findings")

    @property
    @pulumi.getter
    def severity(self) -> Optional['outputs.AutomationRuleSeverityUpdate']:
        """
        Severity of the finding
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def types(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "types")

    @property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional['outputs.AutomationRulemap']:
        return pulumi.get(self, "user_defined_fields")

    @property
    @pulumi.getter(name="verificationState")
    def verification_state(self) -> Optional['AutomationRulesFindingFieldsUpdateVerificationState']:
        return pulumi.get(self, "verification_state")

    @property
    @pulumi.getter
    def workflow(self) -> Optional['outputs.AutomationRuleWorkflowUpdate']:
        """
        Workflow status set for the finding
        """
        return pulumi.get(self, "workflow")


@pulumi.output_type
class AutomationRulesFindingFilters(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "awsAccountId":
            suggest = "aws_account_id"
        elif key == "companyName":
            suggest = "company_name"
        elif key == "complianceAssociatedStandardsId":
            suggest = "compliance_associated_standards_id"
        elif key == "complianceSecurityControlId":
            suggest = "compliance_security_control_id"
        elif key == "complianceStatus":
            suggest = "compliance_status"
        elif key == "createdAt":
            suggest = "created_at"
        elif key == "firstObservedAt":
            suggest = "first_observed_at"
        elif key == "generatorId":
            suggest = "generator_id"
        elif key == "lastObservedAt":
            suggest = "last_observed_at"
        elif key == "noteText":
            suggest = "note_text"
        elif key == "noteUpdatedAt":
            suggest = "note_updated_at"
        elif key == "noteUpdatedBy":
            suggest = "note_updated_by"
        elif key == "productArn":
            suggest = "product_arn"
        elif key == "productName":
            suggest = "product_name"
        elif key == "recordState":
            suggest = "record_state"
        elif key == "relatedFindingsId":
            suggest = "related_findings_id"
        elif key == "relatedFindingsProductArn":
            suggest = "related_findings_product_arn"
        elif key == "resourceDetailsOther":
            suggest = "resource_details_other"
        elif key == "resourceId":
            suggest = "resource_id"
        elif key == "resourcePartition":
            suggest = "resource_partition"
        elif key == "resourceRegion":
            suggest = "resource_region"
        elif key == "resourceTags":
            suggest = "resource_tags"
        elif key == "resourceType":
            suggest = "resource_type"
        elif key == "severityLabel":
            suggest = "severity_label"
        elif key == "sourceUrl":
            suggest = "source_url"
        elif key == "updatedAt":
            suggest = "updated_at"
        elif key == "userDefinedFields":
            suggest = "user_defined_fields"
        elif key == "verificationState":
            suggest = "verification_state"
        elif key == "workflowStatus":
            suggest = "workflow_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AutomationRulesFindingFilters. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AutomationRulesFindingFilters.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AutomationRulesFindingFilters.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 aws_account_id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 company_name: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 compliance_associated_standards_id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 compliance_security_control_id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 compliance_status: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 confidence: Optional[Sequence['outputs.AutomationRuleNumberFilter']] = None,
                 created_at: Optional[Sequence['outputs.AutomationRuleDateFilter']] = None,
                 criticality: Optional[Sequence['outputs.AutomationRuleNumberFilter']] = None,
                 description: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 first_observed_at: Optional[Sequence['outputs.AutomationRuleDateFilter']] = None,
                 generator_id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 last_observed_at: Optional[Sequence['outputs.AutomationRuleDateFilter']] = None,
                 note_text: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 note_updated_at: Optional[Sequence['outputs.AutomationRuleDateFilter']] = None,
                 note_updated_by: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 product_arn: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 product_name: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 record_state: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 related_findings_id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 related_findings_product_arn: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 resource_details_other: Optional[Sequence['outputs.AutomationRuleMapFilter']] = None,
                 resource_id: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 resource_partition: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 resource_region: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 resource_tags: Optional[Sequence['outputs.AutomationRuleMapFilter']] = None,
                 resource_type: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 severity_label: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 source_url: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 title: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 type: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 updated_at: Optional[Sequence['outputs.AutomationRuleDateFilter']] = None,
                 user_defined_fields: Optional[Sequence['outputs.AutomationRuleMapFilter']] = None,
                 verification_state: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None,
                 workflow_status: Optional[Sequence['outputs.AutomationRuleStringFilter']] = None):
        if aws_account_id is not None:
            pulumi.set(__self__, "aws_account_id", aws_account_id)
        if company_name is not None:
            pulumi.set(__self__, "company_name", company_name)
        if compliance_associated_standards_id is not None:
            pulumi.set(__self__, "compliance_associated_standards_id", compliance_associated_standards_id)
        if compliance_security_control_id is not None:
            pulumi.set(__self__, "compliance_security_control_id", compliance_security_control_id)
        if compliance_status is not None:
            pulumi.set(__self__, "compliance_status", compliance_status)
        if confidence is not None:
            pulumi.set(__self__, "confidence", confidence)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if criticality is not None:
            pulumi.set(__self__, "criticality", criticality)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if first_observed_at is not None:
            pulumi.set(__self__, "first_observed_at", first_observed_at)
        if generator_id is not None:
            pulumi.set(__self__, "generator_id", generator_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if last_observed_at is not None:
            pulumi.set(__self__, "last_observed_at", last_observed_at)
        if note_text is not None:
            pulumi.set(__self__, "note_text", note_text)
        if note_updated_at is not None:
            pulumi.set(__self__, "note_updated_at", note_updated_at)
        if note_updated_by is not None:
            pulumi.set(__self__, "note_updated_by", note_updated_by)
        if product_arn is not None:
            pulumi.set(__self__, "product_arn", product_arn)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)
        if record_state is not None:
            pulumi.set(__self__, "record_state", record_state)
        if related_findings_id is not None:
            pulumi.set(__self__, "related_findings_id", related_findings_id)
        if related_findings_product_arn is not None:
            pulumi.set(__self__, "related_findings_product_arn", related_findings_product_arn)
        if resource_details_other is not None:
            pulumi.set(__self__, "resource_details_other", resource_details_other)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if resource_partition is not None:
            pulumi.set(__self__, "resource_partition", resource_partition)
        if resource_region is not None:
            pulumi.set(__self__, "resource_region", resource_region)
        if resource_tags is not None:
            pulumi.set(__self__, "resource_tags", resource_tags)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if severity_label is not None:
            pulumi.set(__self__, "severity_label", severity_label)
        if source_url is not None:
            pulumi.set(__self__, "source_url", source_url)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)
        if user_defined_fields is not None:
            pulumi.set(__self__, "user_defined_fields", user_defined_fields)
        if verification_state is not None:
            pulumi.set(__self__, "verification_state", verification_state)
        if workflow_status is not None:
            pulumi.set(__self__, "workflow_status", workflow_status)

    @property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "aws_account_id")

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "company_name")

    @property
    @pulumi.getter(name="complianceAssociatedStandardsId")
    def compliance_associated_standards_id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "compliance_associated_standards_id")

    @property
    @pulumi.getter(name="complianceSecurityControlId")
    def compliance_security_control_id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "compliance_security_control_id")

    @property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "compliance_status")

    @property
    @pulumi.getter
    def confidence(self) -> Optional[Sequence['outputs.AutomationRuleNumberFilter']]:
        return pulumi.get(self, "confidence")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[Sequence['outputs.AutomationRuleDateFilter']]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def criticality(self) -> Optional[Sequence['outputs.AutomationRuleNumberFilter']]:
        return pulumi.get(self, "criticality")

    @property
    @pulumi.getter
    def description(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="firstObservedAt")
    def first_observed_at(self) -> Optional[Sequence['outputs.AutomationRuleDateFilter']]:
        return pulumi.get(self, "first_observed_at")

    @property
    @pulumi.getter(name="generatorId")
    def generator_id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "generator_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastObservedAt")
    def last_observed_at(self) -> Optional[Sequence['outputs.AutomationRuleDateFilter']]:
        return pulumi.get(self, "last_observed_at")

    @property
    @pulumi.getter(name="noteText")
    def note_text(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "note_text")

    @property
    @pulumi.getter(name="noteUpdatedAt")
    def note_updated_at(self) -> Optional[Sequence['outputs.AutomationRuleDateFilter']]:
        return pulumi.get(self, "note_updated_at")

    @property
    @pulumi.getter(name="noteUpdatedBy")
    def note_updated_by(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "note_updated_by")

    @property
    @pulumi.getter(name="productArn")
    def product_arn(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "product_arn")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="recordState")
    def record_state(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "record_state")

    @property
    @pulumi.getter(name="relatedFindingsId")
    def related_findings_id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "related_findings_id")

    @property
    @pulumi.getter(name="relatedFindingsProductArn")
    def related_findings_product_arn(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "related_findings_product_arn")

    @property
    @pulumi.getter(name="resourceDetailsOther")
    def resource_details_other(self) -> Optional[Sequence['outputs.AutomationRuleMapFilter']]:
        return pulumi.get(self, "resource_details_other")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourcePartition")
    def resource_partition(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "resource_partition")

    @property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "resource_region")

    @property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Sequence['outputs.AutomationRuleMapFilter']]:
        return pulumi.get(self, "resource_tags")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="severityLabel")
    def severity_label(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "severity_label")

    @property
    @pulumi.getter(name="sourceUrl")
    def source_url(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "source_url")

    @property
    @pulumi.getter
    def title(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[Sequence['outputs.AutomationRuleDateFilter']]:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional[Sequence['outputs.AutomationRuleMapFilter']]:
        return pulumi.get(self, "user_defined_fields")

    @property
    @pulumi.getter(name="verificationState")
    def verification_state(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "verification_state")

    @property
    @pulumi.getter(name="workflowStatus")
    def workflow_status(self) -> Optional[Sequence['outputs.AutomationRuleStringFilter']]:
        return pulumi.get(self, "workflow_status")


@pulumi.output_type
class StandardsControl(dict):
    """
    An individual StandardsControl within the Standard.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "standardsControlArn":
            suggest = "standards_control_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StandardsControl. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StandardsControl.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StandardsControl.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 standards_control_arn: str,
                 reason: Optional[str] = None):
        """
        An individual StandardsControl within the Standard.
        :param str standards_control_arn: the Arn for the standard control.
        :param str reason: the reason the standard control is disabled
        """
        pulumi.set(__self__, "standards_control_arn", standards_control_arn)
        if reason is not None:
            pulumi.set(__self__, "reason", reason)

    @property
    @pulumi.getter(name="standardsControlArn")
    def standards_control_arn(self) -> str:
        """
        the Arn for the standard control.
        """
        return pulumi.get(self, "standards_control_arn")

    @property
    @pulumi.getter
    def reason(self) -> Optional[str]:
        """
        the reason the standard control is disabled
        """
        return pulumi.get(self, "reason")


