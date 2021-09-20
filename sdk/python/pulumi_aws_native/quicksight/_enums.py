# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AnalysisAnalysisErrorType',
    'AnalysisResourceStatus',
    'DashboardDashboardBehavior',
    'DashboardDashboardErrorType',
    'DashboardDashboardUIState',
    'DashboardResourceStatus',
    'DataSetColumnDataType',
    'DataSetDataSetImportMode',
    'DataSetGeoSpatialCountryCode',
    'DataSetRowLevelPermissionFormatVersion',
    'DataSetRowLevelPermissionPolicy',
    'DataSourceDataSourceErrorInfoType',
    'DataSourceDataSourceType',
    'DataSourceResourceStatus',
    'TemplateResourceStatus',
    'TemplateTemplateErrorType',
    'ThemeResourceStatus',
    'ThemeThemeErrorType',
    'ThemeThemeType',
]


class AnalysisAnalysisErrorType(str, Enum):
    ACCESS_DENIED = "ACCESS_DENIED"
    SOURCE_NOT_FOUND = "SOURCE_NOT_FOUND"
    DATA_SET_NOT_FOUND = "DATA_SET_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    PARAMETER_VALUE_INCOMPATIBLE = "PARAMETER_VALUE_INCOMPATIBLE"
    PARAMETER_TYPE_INVALID = "PARAMETER_TYPE_INVALID"
    PARAMETER_NOT_FOUND = "PARAMETER_NOT_FOUND"
    COLUMN_TYPE_MISMATCH = "COLUMN_TYPE_MISMATCH"
    COLUMN_GEOGRAPHIC_ROLE_MISMATCH = "COLUMN_GEOGRAPHIC_ROLE_MISMATCH"
    COLUMN_REPLACEMENT_MISSING = "COLUMN_REPLACEMENT_MISSING"


class AnalysisResourceStatus(str, Enum):
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class DashboardDashboardBehavior(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DashboardDashboardErrorType(str, Enum):
    ACCESS_DENIED = "ACCESS_DENIED"
    SOURCE_NOT_FOUND = "SOURCE_NOT_FOUND"
    DATA_SET_NOT_FOUND = "DATA_SET_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    PARAMETER_VALUE_INCOMPATIBLE = "PARAMETER_VALUE_INCOMPATIBLE"
    PARAMETER_TYPE_INVALID = "PARAMETER_TYPE_INVALID"
    PARAMETER_NOT_FOUND = "PARAMETER_NOT_FOUND"
    COLUMN_TYPE_MISMATCH = "COLUMN_TYPE_MISMATCH"
    COLUMN_GEOGRAPHIC_ROLE_MISMATCH = "COLUMN_GEOGRAPHIC_ROLE_MISMATCH"
    COLUMN_REPLACEMENT_MISSING = "COLUMN_REPLACEMENT_MISSING"


class DashboardDashboardUIState(str, Enum):
    EXPANDED = "EXPANDED"
    COLLAPSED = "COLLAPSED"


class DashboardResourceStatus(str, Enum):
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class DataSetColumnDataType(str, Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    DECIMAL = "DECIMAL"
    DATETIME = "DATETIME"


class DataSetDataSetImportMode(str, Enum):
    SPICE = "SPICE"
    DIRECT_QUERY = "DIRECT_QUERY"


class DataSetGeoSpatialCountryCode(str, Enum):
    US = "US"


class DataSetRowLevelPermissionFormatVersion(str, Enum):
    VERSION1 = "VERSION_1"
    VERSION2 = "VERSION_2"


class DataSetRowLevelPermissionPolicy(str, Enum):
    GRANT_ACCESS = "GRANT_ACCESS"
    DENY_ACCESS = "DENY_ACCESS"


class DataSourceDataSourceErrorInfoType(str, Enum):
    ACCESS_DENIED = "ACCESS_DENIED"
    COPY_SOURCE_NOT_FOUND = "COPY_SOURCE_NOT_FOUND"
    TIMEOUT = "TIMEOUT"
    ENGINE_VERSION_NOT_SUPPORTED = "ENGINE_VERSION_NOT_SUPPORTED"
    UNKNOWN_HOST = "UNKNOWN_HOST"
    GENERIC_SQL_FAILURE = "GENERIC_SQL_FAILURE"
    CONFLICT = "CONFLICT"
    UNKNOWN = "UNKNOWN"


class DataSourceDataSourceType(str, Enum):
    ADOBE_ANALYTICS = "ADOBE_ANALYTICS"
    AMAZON_ELASTICSEARCH = "AMAZON_ELASTICSEARCH"
    ATHENA = "ATHENA"
    AURORA = "AURORA"
    AURORA_POSTGRESQL = "AURORA_POSTGRESQL"
    AWS_IOT_ANALYTICS = "AWS_IOT_ANALYTICS"
    GITHUB = "GITHUB"
    JIRA = "JIRA"
    MARIADB = "MARIADB"
    MYSQL = "MYSQL"
    ORACLE = "ORACLE"
    POSTGRESQL = "POSTGRESQL"
    PRESTO = "PRESTO"
    REDSHIFT = "REDSHIFT"
    S3 = "S3"
    SALESFORCE = "SALESFORCE"
    SERVICENOW = "SERVICENOW"
    SNOWFLAKE = "SNOWFLAKE"
    SPARK = "SPARK"
    SQLSERVER = "SQLSERVER"
    TERADATA = "TERADATA"
    TWITTER = "TWITTER"
    TIMESTREAM = "TIMESTREAM"


class DataSourceResourceStatus(str, Enum):
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class TemplateResourceStatus(str, Enum):
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class TemplateTemplateErrorType(str, Enum):
    SOURCE_NOT_FOUND = "SOURCE_NOT_FOUND"
    DATA_SET_NOT_FOUND = "DATA_SET_NOT_FOUND"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    ACCESS_DENIED = "ACCESS_DENIED"


class ThemeResourceStatus(str, Enum):
    CREATION_IN_PROGRESS = "CREATION_IN_PROGRESS"
    CREATION_SUCCESSFUL = "CREATION_SUCCESSFUL"
    CREATION_FAILED = "CREATION_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_SUCCESSFUL = "UPDATE_SUCCESSFUL"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETED = "DELETED"


class ThemeThemeErrorType(str, Enum):
    INTERNAL_FAILURE = "INTERNAL_FAILURE"


class ThemeThemeType(str, Enum):
    QUICKSIGHT = "QUICKSIGHT"
    CUSTOM = "CUSTOM"
    ALL = "ALL"
