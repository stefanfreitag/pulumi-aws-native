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
    'IdMappingWorkflowIdMappingTechniques',
    'IdMappingWorkflowInputSource',
    'IdMappingWorkflowIntermediateSourceConfiguration',
    'IdMappingWorkflowOutputSource',
    'IdMappingWorkflowProviderProperties',
    'MatchingWorkflowInputSource',
    'MatchingWorkflowIntermediateSourceConfiguration',
    'MatchingWorkflowOutputAttribute',
    'MatchingWorkflowOutputSource',
    'MatchingWorkflowProviderProperties',
    'MatchingWorkflowResolutionTechniques',
    'MatchingWorkflowRule',
    'MatchingWorkflowRuleBasedProperties',
    'SchemaMappingSchemaInputAttribute',
]

@pulumi.output_type
class IdMappingWorkflowIdMappingTechniques(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "idMappingType":
            suggest = "id_mapping_type"
        elif key == "providerProperties":
            suggest = "provider_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdMappingWorkflowIdMappingTechniques. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdMappingWorkflowIdMappingTechniques.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdMappingWorkflowIdMappingTechniques.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id_mapping_type: Optional['IdMappingWorkflowIdMappingTechniquesIdMappingType'] = None,
                 provider_properties: Optional['outputs.IdMappingWorkflowProviderProperties'] = None):
        if id_mapping_type is not None:
            pulumi.set(__self__, "id_mapping_type", id_mapping_type)
        if provider_properties is not None:
            pulumi.set(__self__, "provider_properties", provider_properties)

    @property
    @pulumi.getter(name="idMappingType")
    def id_mapping_type(self) -> Optional['IdMappingWorkflowIdMappingTechniquesIdMappingType']:
        return pulumi.get(self, "id_mapping_type")

    @property
    @pulumi.getter(name="providerProperties")
    def provider_properties(self) -> Optional['outputs.IdMappingWorkflowProviderProperties']:
        return pulumi.get(self, "provider_properties")


@pulumi.output_type
class IdMappingWorkflowInputSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inputSourceArn":
            suggest = "input_source_arn"
        elif key == "schemaArn":
            suggest = "schema_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdMappingWorkflowInputSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdMappingWorkflowInputSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdMappingWorkflowInputSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 input_source_arn: str,
                 schema_arn: str):
        """
        :param str input_source_arn: An Glue table ARN for the input source table
        """
        pulumi.set(__self__, "input_source_arn", input_source_arn)
        pulumi.set(__self__, "schema_arn", schema_arn)

    @property
    @pulumi.getter(name="inputSourceArn")
    def input_source_arn(self) -> str:
        """
        An Glue table ARN for the input source table
        """
        return pulumi.get(self, "input_source_arn")

    @property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> str:
        return pulumi.get(self, "schema_arn")


@pulumi.output_type
class IdMappingWorkflowIntermediateSourceConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "intermediateS3Path":
            suggest = "intermediate_s3_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdMappingWorkflowIntermediateSourceConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdMappingWorkflowIntermediateSourceConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdMappingWorkflowIntermediateSourceConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 intermediate_s3_path: str):
        """
        :param str intermediate_s3_path: The s3 path that would be used to stage the intermediate data being generated during workflow execution.
        """
        pulumi.set(__self__, "intermediate_s3_path", intermediate_s3_path)

    @property
    @pulumi.getter(name="intermediateS3Path")
    def intermediate_s3_path(self) -> str:
        """
        The s3 path that would be used to stage the intermediate data being generated during workflow execution.
        """
        return pulumi.get(self, "intermediate_s3_path")


@pulumi.output_type
class IdMappingWorkflowOutputSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "outputS3Path":
            suggest = "output_s3_path"
        elif key == "kmsArn":
            suggest = "kms_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdMappingWorkflowOutputSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdMappingWorkflowOutputSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdMappingWorkflowOutputSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 output_s3_path: str,
                 kms_arn: Optional[str] = None):
        """
        :param str output_s3_path: The S3 path to which Entity Resolution will write the output table
        """
        pulumi.set(__self__, "output_s3_path", output_s3_path)
        if kms_arn is not None:
            pulumi.set(__self__, "kms_arn", kms_arn)

    @property
    @pulumi.getter(name="outputS3Path")
    def output_s3_path(self) -> str:
        """
        The S3 path to which Entity Resolution will write the output table
        """
        return pulumi.get(self, "output_s3_path")

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[str]:
        return pulumi.get(self, "kms_arn")


@pulumi.output_type
class IdMappingWorkflowProviderProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "providerServiceArn":
            suggest = "provider_service_arn"
        elif key == "intermediateSourceConfiguration":
            suggest = "intermediate_source_configuration"
        elif key == "providerConfiguration":
            suggest = "provider_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdMappingWorkflowProviderProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdMappingWorkflowProviderProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdMappingWorkflowProviderProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provider_service_arn: str,
                 intermediate_source_configuration: Optional['outputs.IdMappingWorkflowIntermediateSourceConfiguration'] = None,
                 provider_configuration: Optional[Mapping[str, str]] = None):
        """
        :param str provider_service_arn: Arn of the Provider Service being used.
        :param Mapping[str, str] provider_configuration: Additional Provider configuration that would be required for the provider service. The Configuration must be in JSON string format
        """
        pulumi.set(__self__, "provider_service_arn", provider_service_arn)
        if intermediate_source_configuration is not None:
            pulumi.set(__self__, "intermediate_source_configuration", intermediate_source_configuration)
        if provider_configuration is not None:
            pulumi.set(__self__, "provider_configuration", provider_configuration)

    @property
    @pulumi.getter(name="providerServiceArn")
    def provider_service_arn(self) -> str:
        """
        Arn of the Provider Service being used.
        """
        return pulumi.get(self, "provider_service_arn")

    @property
    @pulumi.getter(name="intermediateSourceConfiguration")
    def intermediate_source_configuration(self) -> Optional['outputs.IdMappingWorkflowIntermediateSourceConfiguration']:
        return pulumi.get(self, "intermediate_source_configuration")

    @property
    @pulumi.getter(name="providerConfiguration")
    def provider_configuration(self) -> Optional[Mapping[str, str]]:
        """
        Additional Provider configuration that would be required for the provider service. The Configuration must be in JSON string format
        """
        return pulumi.get(self, "provider_configuration")


@pulumi.output_type
class MatchingWorkflowInputSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inputSourceArn":
            suggest = "input_source_arn"
        elif key == "schemaArn":
            suggest = "schema_arn"
        elif key == "applyNormalization":
            suggest = "apply_normalization"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowInputSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowInputSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowInputSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 input_source_arn: str,
                 schema_arn: str,
                 apply_normalization: Optional[bool] = None):
        """
        :param str input_source_arn: An Glue table ARN for the input source table
        """
        pulumi.set(__self__, "input_source_arn", input_source_arn)
        pulumi.set(__self__, "schema_arn", schema_arn)
        if apply_normalization is not None:
            pulumi.set(__self__, "apply_normalization", apply_normalization)

    @property
    @pulumi.getter(name="inputSourceArn")
    def input_source_arn(self) -> str:
        """
        An Glue table ARN for the input source table
        """
        return pulumi.get(self, "input_source_arn")

    @property
    @pulumi.getter(name="schemaArn")
    def schema_arn(self) -> str:
        return pulumi.get(self, "schema_arn")

    @property
    @pulumi.getter(name="applyNormalization")
    def apply_normalization(self) -> Optional[bool]:
        return pulumi.get(self, "apply_normalization")


@pulumi.output_type
class MatchingWorkflowIntermediateSourceConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "intermediateS3Path":
            suggest = "intermediate_s3_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowIntermediateSourceConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowIntermediateSourceConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowIntermediateSourceConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 intermediate_s3_path: str):
        """
        :param str intermediate_s3_path: The s3 path that would be used to stage the intermediate data being generated during workflow execution.
        """
        pulumi.set(__self__, "intermediate_s3_path", intermediate_s3_path)

    @property
    @pulumi.getter(name="intermediateS3Path")
    def intermediate_s3_path(self) -> str:
        """
        The s3 path that would be used to stage the intermediate data being generated during workflow execution.
        """
        return pulumi.get(self, "intermediate_s3_path")


@pulumi.output_type
class MatchingWorkflowOutputAttribute(dict):
    def __init__(__self__, *,
                 name: str,
                 hashed: Optional[bool] = None):
        pulumi.set(__self__, "name", name)
        if hashed is not None:
            pulumi.set(__self__, "hashed", hashed)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def hashed(self) -> Optional[bool]:
        return pulumi.get(self, "hashed")


@pulumi.output_type
class MatchingWorkflowOutputSource(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "outputS3Path":
            suggest = "output_s3_path"
        elif key == "applyNormalization":
            suggest = "apply_normalization"
        elif key == "kmsArn":
            suggest = "kms_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowOutputSource. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowOutputSource.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowOutputSource.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 output: Sequence['outputs.MatchingWorkflowOutputAttribute'],
                 output_s3_path: str,
                 apply_normalization: Optional[bool] = None,
                 kms_arn: Optional[str] = None):
        """
        :param str output_s3_path: The S3 path to which Entity Resolution will write the output table
        """
        pulumi.set(__self__, "output", output)
        pulumi.set(__self__, "output_s3_path", output_s3_path)
        if apply_normalization is not None:
            pulumi.set(__self__, "apply_normalization", apply_normalization)
        if kms_arn is not None:
            pulumi.set(__self__, "kms_arn", kms_arn)

    @property
    @pulumi.getter
    def output(self) -> Sequence['outputs.MatchingWorkflowOutputAttribute']:
        return pulumi.get(self, "output")

    @property
    @pulumi.getter(name="outputS3Path")
    def output_s3_path(self) -> str:
        """
        The S3 path to which Entity Resolution will write the output table
        """
        return pulumi.get(self, "output_s3_path")

    @property
    @pulumi.getter(name="applyNormalization")
    def apply_normalization(self) -> Optional[bool]:
        return pulumi.get(self, "apply_normalization")

    @property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[str]:
        return pulumi.get(self, "kms_arn")


@pulumi.output_type
class MatchingWorkflowProviderProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "providerServiceArn":
            suggest = "provider_service_arn"
        elif key == "intermediateSourceConfiguration":
            suggest = "intermediate_source_configuration"
        elif key == "providerConfiguration":
            suggest = "provider_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowProviderProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowProviderProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowProviderProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provider_service_arn: str,
                 intermediate_source_configuration: Optional['outputs.MatchingWorkflowIntermediateSourceConfiguration'] = None,
                 provider_configuration: Optional[Mapping[str, str]] = None):
        """
        :param str provider_service_arn: Arn of the Provider service being used.
        :param Mapping[str, str] provider_configuration: Additional Provider configuration that would be required for the provider service. The Configuration must be in JSON string format
        """
        pulumi.set(__self__, "provider_service_arn", provider_service_arn)
        if intermediate_source_configuration is not None:
            pulumi.set(__self__, "intermediate_source_configuration", intermediate_source_configuration)
        if provider_configuration is not None:
            pulumi.set(__self__, "provider_configuration", provider_configuration)

    @property
    @pulumi.getter(name="providerServiceArn")
    def provider_service_arn(self) -> str:
        """
        Arn of the Provider service being used.
        """
        return pulumi.get(self, "provider_service_arn")

    @property
    @pulumi.getter(name="intermediateSourceConfiguration")
    def intermediate_source_configuration(self) -> Optional['outputs.MatchingWorkflowIntermediateSourceConfiguration']:
        return pulumi.get(self, "intermediate_source_configuration")

    @property
    @pulumi.getter(name="providerConfiguration")
    def provider_configuration(self) -> Optional[Mapping[str, str]]:
        """
        Additional Provider configuration that would be required for the provider service. The Configuration must be in JSON string format
        """
        return pulumi.get(self, "provider_configuration")


@pulumi.output_type
class MatchingWorkflowResolutionTechniques(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "providerProperties":
            suggest = "provider_properties"
        elif key == "resolutionType":
            suggest = "resolution_type"
        elif key == "ruleBasedProperties":
            suggest = "rule_based_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowResolutionTechniques. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowResolutionTechniques.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowResolutionTechniques.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provider_properties: Optional['outputs.MatchingWorkflowProviderProperties'] = None,
                 resolution_type: Optional['MatchingWorkflowResolutionTechniquesResolutionType'] = None,
                 rule_based_properties: Optional['outputs.MatchingWorkflowRuleBasedProperties'] = None):
        if provider_properties is not None:
            pulumi.set(__self__, "provider_properties", provider_properties)
        if resolution_type is not None:
            pulumi.set(__self__, "resolution_type", resolution_type)
        if rule_based_properties is not None:
            pulumi.set(__self__, "rule_based_properties", rule_based_properties)

    @property
    @pulumi.getter(name="providerProperties")
    def provider_properties(self) -> Optional['outputs.MatchingWorkflowProviderProperties']:
        return pulumi.get(self, "provider_properties")

    @property
    @pulumi.getter(name="resolutionType")
    def resolution_type(self) -> Optional['MatchingWorkflowResolutionTechniquesResolutionType']:
        return pulumi.get(self, "resolution_type")

    @property
    @pulumi.getter(name="ruleBasedProperties")
    def rule_based_properties(self) -> Optional['outputs.MatchingWorkflowRuleBasedProperties']:
        return pulumi.get(self, "rule_based_properties")


@pulumi.output_type
class MatchingWorkflowRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "matchingKeys":
            suggest = "matching_keys"
        elif key == "ruleName":
            suggest = "rule_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 matching_keys: Sequence[str],
                 rule_name: str):
        pulumi.set(__self__, "matching_keys", matching_keys)
        pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter(name="matchingKeys")
    def matching_keys(self) -> Sequence[str]:
        return pulumi.get(self, "matching_keys")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> str:
        return pulumi.get(self, "rule_name")


@pulumi.output_type
class MatchingWorkflowRuleBasedProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "attributeMatchingModel":
            suggest = "attribute_matching_model"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MatchingWorkflowRuleBasedProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MatchingWorkflowRuleBasedProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MatchingWorkflowRuleBasedProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 attribute_matching_model: 'MatchingWorkflowRuleBasedPropertiesAttributeMatchingModel',
                 rules: Sequence['outputs.MatchingWorkflowRule']):
        pulumi.set(__self__, "attribute_matching_model", attribute_matching_model)
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="attributeMatchingModel")
    def attribute_matching_model(self) -> 'MatchingWorkflowRuleBasedPropertiesAttributeMatchingModel':
        return pulumi.get(self, "attribute_matching_model")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.MatchingWorkflowRule']:
        return pulumi.get(self, "rules")


@pulumi.output_type
class SchemaMappingSchemaInputAttribute(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fieldName":
            suggest = "field_name"
        elif key == "groupName":
            suggest = "group_name"
        elif key == "matchKey":
            suggest = "match_key"
        elif key == "subType":
            suggest = "sub_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SchemaMappingSchemaInputAttribute. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SchemaMappingSchemaInputAttribute.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SchemaMappingSchemaInputAttribute.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 field_name: str,
                 type: 'SchemaMappingSchemaAttributeType',
                 group_name: Optional[str] = None,
                 match_key: Optional[str] = None,
                 sub_type: Optional[str] = None):
        """
        :param str sub_type: The subtype of the Attribute. Would be required only when type is PROVIDER_ID
        """
        pulumi.set(__self__, "field_name", field_name)
        pulumi.set(__self__, "type", type)
        if group_name is not None:
            pulumi.set(__self__, "group_name", group_name)
        if match_key is not None:
            pulumi.set(__self__, "match_key", match_key)
        if sub_type is not None:
            pulumi.set(__self__, "sub_type", sub_type)

    @property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> str:
        return pulumi.get(self, "field_name")

    @property
    @pulumi.getter
    def type(self) -> 'SchemaMappingSchemaAttributeType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[str]:
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter(name="matchKey")
    def match_key(self) -> Optional[str]:
        return pulumi.get(self, "match_key")

    @property
    @pulumi.getter(name="subType")
    def sub_type(self) -> Optional[str]:
        """
        The subtype of the Attribute. Would be required only when type is PROVIDER_ID
        """
        return pulumi.get(self, "sub_type")


