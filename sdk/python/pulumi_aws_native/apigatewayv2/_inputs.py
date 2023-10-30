# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ApiBodyS3LocationArgs',
    'ApiCorsArgs',
    'ApiGatewayManagedOverridesAccessLogSettingsArgs',
    'ApiGatewayManagedOverridesIntegrationOverridesArgs',
    'ApiGatewayManagedOverridesRouteOverridesArgs',
    'ApiGatewayManagedOverridesRouteSettingsArgs',
    'ApiGatewayManagedOverridesStageOverridesArgs',
    'AuthorizerJwtConfigurationArgs',
    'DomainNameConfigurationArgs',
    'DomainNameMutualTlsAuthenticationArgs',
    'IntegrationTlsConfigArgs',
    'RouteResponseRouteParametersArgs',
    'StageAccessLogSettingsArgs',
    'StageRouteSettingsArgs',
]

@pulumi.input_type
class ApiBodyS3LocationArgs:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The ``BodyS3Location`` property specifies an S3 location from which to import an OpenAPI definition. Supported only for HTTP APIs.
        :param pulumi.Input[str] bucket: The S3 bucket that contains the OpenAPI definition to import. Required if you specify a ``BodyS3Location`` for an API.
        :param pulumi.Input[str] etag: The Etag of the S3 object.
        :param pulumi.Input[str] key: The key of the S3 object. Required if you specify a ``BodyS3Location`` for an API.
        :param pulumi.Input[str] version: The version of the S3 object.
        """
        if bucket is not None:
            pulumi.set(__self__, "bucket", bucket)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        The S3 bucket that contains the OpenAPI definition to import. Required if you specify a ``BodyS3Location`` for an API.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        The Etag of the S3 object.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key of the S3 object. Required if you specify a ``BodyS3Location`` for an API.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the S3 object.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class ApiCorsArgs:
    def __init__(__self__, *,
                 allow_credentials: Optional[pulumi.Input[bool]] = None,
                 allow_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allow_methods: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allow_origins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 max_age: Optional[pulumi.Input[int]] = None):
        """
        The ``Cors`` property specifies a CORS configuration for an API. Supported only for HTTP APIs. See [Configuring CORS](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html) for more information.
        :param pulumi.Input[bool] allow_credentials: Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allow_headers: Represents a collection of allowed headers. Supported only for HTTP APIs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allow_methods: Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allow_origins: Represents a collection of allowed origins. Supported only for HTTP APIs.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] expose_headers: Represents a collection of exposed headers. Supported only for HTTP APIs.
        :param pulumi.Input[int] max_age: The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.
        """
        if allow_credentials is not None:
            pulumi.set(__self__, "allow_credentials", allow_credentials)
        if allow_headers is not None:
            pulumi.set(__self__, "allow_headers", allow_headers)
        if allow_methods is not None:
            pulumi.set(__self__, "allow_methods", allow_methods)
        if allow_origins is not None:
            pulumi.set(__self__, "allow_origins", allow_origins)
        if expose_headers is not None:
            pulumi.set(__self__, "expose_headers", expose_headers)
        if max_age is not None:
            pulumi.set(__self__, "max_age", max_age)

    @property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "allow_credentials")

    @allow_credentials.setter
    def allow_credentials(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_credentials", value)

    @property
    @pulumi.getter(name="allowHeaders")
    def allow_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Represents a collection of allowed headers. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "allow_headers")

    @allow_headers.setter
    def allow_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allow_headers", value)

    @property
    @pulumi.getter(name="allowMethods")
    def allow_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "allow_methods")

    @allow_methods.setter
    def allow_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allow_methods", value)

    @property
    @pulumi.getter(name="allowOrigins")
    def allow_origins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Represents a collection of allowed origins. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "allow_origins")

    @allow_origins.setter
    def allow_origins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allow_origins", value)

    @property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Represents a collection of exposed headers. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "expose_headers")

    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "expose_headers", value)

    @property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[pulumi.Input[int]]:
        """
        The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.
        """
        return pulumi.get(self, "max_age")

    @max_age.setter
    def max_age(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_age", value)


@pulumi.input_type
class ApiGatewayManagedOverridesAccessLogSettingsArgs:
    def __init__(__self__, *,
                 destination_arn: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None):
        if destination_arn is not None:
            pulumi.set(__self__, "destination_arn", destination_arn)
        if format is not None:
            pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination_arn")

    @destination_arn.setter
    def destination_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_arn", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class ApiGatewayManagedOverridesIntegrationOverridesArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 integration_method: Optional[pulumi.Input[str]] = None,
                 payload_format_version: Optional[pulumi.Input[str]] = None,
                 timeout_in_millis: Optional[pulumi.Input[int]] = None):
        if description is not None:
            pulumi.set(__self__, "description", description)
        if integration_method is not None:
            pulumi.set(__self__, "integration_method", integration_method)
        if payload_format_version is not None:
            pulumi.set(__self__, "payload_format_version", payload_format_version)
        if timeout_in_millis is not None:
            pulumi.set(__self__, "timeout_in_millis", timeout_in_millis)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="integrationMethod")
    def integration_method(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "integration_method")

    @integration_method.setter
    def integration_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "integration_method", value)

    @property
    @pulumi.getter(name="payloadFormatVersion")
    def payload_format_version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "payload_format_version")

    @payload_format_version.setter
    def payload_format_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payload_format_version", value)

    @property
    @pulumi.getter(name="timeoutInMillis")
    def timeout_in_millis(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "timeout_in_millis")

    @timeout_in_millis.setter
    def timeout_in_millis(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout_in_millis", value)


@pulumi.input_type
class ApiGatewayManagedOverridesRouteOverridesArgs:
    def __init__(__self__, *,
                 authorization_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authorization_type: Optional[pulumi.Input[str]] = None,
                 authorizer_id: Optional[pulumi.Input[str]] = None,
                 operation_name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        if authorization_scopes is not None:
            pulumi.set(__self__, "authorization_scopes", authorization_scopes)
        if authorization_type is not None:
            pulumi.set(__self__, "authorization_type", authorization_type)
        if authorizer_id is not None:
            pulumi.set(__self__, "authorizer_id", authorizer_id)
        if operation_name is not None:
            pulumi.set(__self__, "operation_name", operation_name)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "authorization_scopes")

    @authorization_scopes.setter
    def authorization_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "authorization_scopes", value)

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorization_type")

    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_type", value)

    @property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authorizer_id")

    @authorizer_id.setter
    def authorizer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorizer_id", value)

    @property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "operation_name")

    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_name", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


@pulumi.input_type
class ApiGatewayManagedOverridesRouteSettingsArgs:
    def __init__(__self__, *,
                 data_trace_enabled: Optional[pulumi.Input[bool]] = None,
                 detailed_metrics_enabled: Optional[pulumi.Input[bool]] = None,
                 logging_level: Optional[pulumi.Input[str]] = None,
                 throttling_burst_limit: Optional[pulumi.Input[int]] = None,
                 throttling_rate_limit: Optional[pulumi.Input[float]] = None):
        if data_trace_enabled is not None:
            pulumi.set(__self__, "data_trace_enabled", data_trace_enabled)
        if detailed_metrics_enabled is not None:
            pulumi.set(__self__, "detailed_metrics_enabled", detailed_metrics_enabled)
        if logging_level is not None:
            pulumi.set(__self__, "logging_level", logging_level)
        if throttling_burst_limit is not None:
            pulumi.set(__self__, "throttling_burst_limit", throttling_burst_limit)
        if throttling_rate_limit is not None:
            pulumi.set(__self__, "throttling_rate_limit", throttling_rate_limit)

    @property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "data_trace_enabled")

    @data_trace_enabled.setter
    def data_trace_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "data_trace_enabled", value)

    @property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "detailed_metrics_enabled")

    @detailed_metrics_enabled.setter
    def detailed_metrics_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detailed_metrics_enabled", value)

    @property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "logging_level")

    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_level", value)

    @property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "throttling_burst_limit")

    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "throttling_burst_limit", value)

    @property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "throttling_rate_limit")

    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "throttling_rate_limit", value)


@pulumi.input_type
class ApiGatewayManagedOverridesStageOverridesArgs:
    def __init__(__self__, *,
                 access_log_settings: Optional[pulumi.Input['ApiGatewayManagedOverridesAccessLogSettingsArgs']] = None,
                 auto_deploy: Optional[pulumi.Input[bool]] = None,
                 default_route_settings: Optional[pulumi.Input['ApiGatewayManagedOverridesRouteSettingsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 route_settings: Optional[Any] = None,
                 stage_variables: Optional[Any] = None):
        if access_log_settings is not None:
            pulumi.set(__self__, "access_log_settings", access_log_settings)
        if auto_deploy is not None:
            pulumi.set(__self__, "auto_deploy", auto_deploy)
        if default_route_settings is not None:
            pulumi.set(__self__, "default_route_settings", default_route_settings)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if route_settings is not None:
            pulumi.set(__self__, "route_settings", route_settings)
        if stage_variables is not None:
            pulumi.set(__self__, "stage_variables", stage_variables)

    @property
    @pulumi.getter(name="accessLogSettings")
    def access_log_settings(self) -> Optional[pulumi.Input['ApiGatewayManagedOverridesAccessLogSettingsArgs']]:
        return pulumi.get(self, "access_log_settings")

    @access_log_settings.setter
    def access_log_settings(self, value: Optional[pulumi.Input['ApiGatewayManagedOverridesAccessLogSettingsArgs']]):
        pulumi.set(self, "access_log_settings", value)

    @property
    @pulumi.getter(name="autoDeploy")
    def auto_deploy(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "auto_deploy")

    @auto_deploy.setter
    def auto_deploy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_deploy", value)

    @property
    @pulumi.getter(name="defaultRouteSettings")
    def default_route_settings(self) -> Optional[pulumi.Input['ApiGatewayManagedOverridesRouteSettingsArgs']]:
        return pulumi.get(self, "default_route_settings")

    @default_route_settings.setter
    def default_route_settings(self, value: Optional[pulumi.Input['ApiGatewayManagedOverridesRouteSettingsArgs']]):
        pulumi.set(self, "default_route_settings", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="routeSettings")
    def route_settings(self) -> Optional[Any]:
        return pulumi.get(self, "route_settings")

    @route_settings.setter
    def route_settings(self, value: Optional[Any]):
        pulumi.set(self, "route_settings", value)

    @property
    @pulumi.getter(name="stageVariables")
    def stage_variables(self) -> Optional[Any]:
        return pulumi.get(self, "stage_variables")

    @stage_variables.setter
    def stage_variables(self, value: Optional[Any]):
        pulumi.set(self, "stage_variables", value)


@pulumi.input_type
class AuthorizerJwtConfigurationArgs:
    def __init__(__self__, *,
                 audience: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 issuer: Optional[pulumi.Input[str]] = None):
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)

    @property
    @pulumi.getter
    def audience(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "audience")

    @audience.setter
    def audience(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "audience", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)


@pulumi.input_type
class DomainNameConfigurationArgs:
    def __init__(__self__, *,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 ownership_verification_certificate_arn: Optional[pulumi.Input[str]] = None,
                 security_policy: Optional[pulumi.Input[str]] = None):
        """
        The ``DomainNameConfiguration`` property type specifies the configuration for an API's domain name.
         ``DomainNameConfiguration`` is a property of the [AWS::ApiGatewayV2::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html) resource.
        :param pulumi.Input[str] certificate_arn: An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
        :param pulumi.Input[str] certificate_name: The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
        :param pulumi.Input[str] endpoint_type: The endpoint type.
        :param pulumi.Input[str] ownership_verification_certificate_arn: The Amazon resource name (ARN) for the public certificate issued by ACMlong. This ARN is used to validate custom domain ownership. It's required only if you configure mutual TLS and use either an ACM-imported or a private CA certificate ARN as the regionalCertificateArn.
        :param pulumi.Input[str] security_policy: The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are ``TLS_1_0`` and ``TLS_1_2``.
        """
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if certificate_name is not None:
            pulumi.set(__self__, "certificate_name", certificate_name)
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if ownership_verification_certificate_arn is not None:
            pulumi.set(__self__, "ownership_verification_certificate_arn", ownership_verification_certificate_arn)
        if security_policy is not None:
            pulumi.set(__self__, "security_policy", security_policy)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_name", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[str]]:
        """
        The endpoint type.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon resource name (ARN) for the public certificate issued by ACMlong. This ARN is used to validate custom domain ownership. It's required only if you configure mutual TLS and use either an ACM-imported or a private CA certificate ARN as the regionalCertificateArn.
        """
        return pulumi.get(self, "ownership_verification_certificate_arn")

    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ownership_verification_certificate_arn", value)

    @property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are ``TLS_1_0`` and ``TLS_1_2``.
        """
        return pulumi.get(self, "security_policy")

    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_policy", value)


@pulumi.input_type
class DomainNameMutualTlsAuthenticationArgs:
    def __init__(__self__, *,
                 truststore_uri: Optional[pulumi.Input[str]] = None,
                 truststore_version: Optional[pulumi.Input[str]] = None):
        """
        If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
        :param pulumi.Input[str] truststore_uri: An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, ``s3://bucket-name/key-name``. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.
        :param pulumi.Input[str] truststore_version: The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.
        """
        if truststore_uri is not None:
            pulumi.set(__self__, "truststore_uri", truststore_uri)
        if truststore_version is not None:
            pulumi.set(__self__, "truststore_version", truststore_version)

    @property
    @pulumi.getter(name="truststoreUri")
    def truststore_uri(self) -> Optional[pulumi.Input[str]]:
        """
        An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, ``s3://bucket-name/key-name``. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.
        """
        return pulumi.get(self, "truststore_uri")

    @truststore_uri.setter
    def truststore_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "truststore_uri", value)

    @property
    @pulumi.getter(name="truststoreVersion")
    def truststore_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.
        """
        return pulumi.get(self, "truststore_version")

    @truststore_version.setter
    def truststore_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "truststore_version", value)


@pulumi.input_type
class IntegrationTlsConfigArgs:
    def __init__(__self__, *,
                 server_name_to_verify: Optional[pulumi.Input[str]] = None):
        if server_name_to_verify is not None:
            pulumi.set(__self__, "server_name_to_verify", server_name_to_verify)

    @property
    @pulumi.getter(name="serverNameToVerify")
    def server_name_to_verify(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server_name_to_verify")

    @server_name_to_verify.setter
    def server_name_to_verify(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name_to_verify", value)


@pulumi.input_type
class RouteResponseRouteParametersArgs:
    def __init__(__self__):
        pass


@pulumi.input_type
class StageAccessLogSettingsArgs:
    def __init__(__self__, *,
                 destination_arn: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None):
        if destination_arn is not None:
            pulumi.set(__self__, "destination_arn", destination_arn)
        if format is not None:
            pulumi.set(__self__, "format", format)

    @property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "destination_arn")

    @destination_arn.setter
    def destination_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_arn", value)

    @property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "format", value)


@pulumi.input_type
class StageRouteSettingsArgs:
    def __init__(__self__, *,
                 data_trace_enabled: Optional[pulumi.Input[bool]] = None,
                 detailed_metrics_enabled: Optional[pulumi.Input[bool]] = None,
                 logging_level: Optional[pulumi.Input[str]] = None,
                 throttling_burst_limit: Optional[pulumi.Input[int]] = None,
                 throttling_rate_limit: Optional[pulumi.Input[float]] = None):
        if data_trace_enabled is not None:
            pulumi.set(__self__, "data_trace_enabled", data_trace_enabled)
        if detailed_metrics_enabled is not None:
            pulumi.set(__self__, "detailed_metrics_enabled", detailed_metrics_enabled)
        if logging_level is not None:
            pulumi.set(__self__, "logging_level", logging_level)
        if throttling_burst_limit is not None:
            pulumi.set(__self__, "throttling_burst_limit", throttling_burst_limit)
        if throttling_rate_limit is not None:
            pulumi.set(__self__, "throttling_rate_limit", throttling_rate_limit)

    @property
    @pulumi.getter(name="dataTraceEnabled")
    def data_trace_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "data_trace_enabled")

    @data_trace_enabled.setter
    def data_trace_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "data_trace_enabled", value)

    @property
    @pulumi.getter(name="detailedMetricsEnabled")
    def detailed_metrics_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "detailed_metrics_enabled")

    @detailed_metrics_enabled.setter
    def detailed_metrics_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detailed_metrics_enabled", value)

    @property
    @pulumi.getter(name="loggingLevel")
    def logging_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "logging_level")

    @logging_level.setter
    def logging_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_level", value)

    @property
    @pulumi.getter(name="throttlingBurstLimit")
    def throttling_burst_limit(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "throttling_burst_limit")

    @throttling_burst_limit.setter
    def throttling_burst_limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "throttling_burst_limit", value)

    @property
    @pulumi.getter(name="throttlingRateLimit")
    def throttling_rate_limit(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "throttling_rate_limit")

    @throttling_rate_limit.setter
    def throttling_rate_limit(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "throttling_rate_limit", value)


