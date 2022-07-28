// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway
{
    public static class GetDomainName
    {
        /// <summary>
        /// Resource Type definition for AWS::ApiGateway::DomainName.
        /// </summary>
        public static Task<GetDomainNameResult> InvokeAsync(GetDomainNameArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDomainNameResult>("aws-native:apigateway:getDomainName", args ?? new GetDomainNameArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ApiGateway::DomainName.
        /// </summary>
        public static Output<GetDomainNameResult> Invoke(GetDomainNameInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetDomainNameResult>("aws-native:apigateway:getDomainName", args ?? new GetDomainNameInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDomainNameArgs : global::Pulumi.InvokeArgs
    {
        [Input("domainName", required: true)]
        public string DomainNameValue { get; set; } = null!;

        public GetDomainNameArgs()
        {
        }
        public static new GetDomainNameArgs Empty => new GetDomainNameArgs();
    }

    public sealed class GetDomainNameInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        public GetDomainNameInvokeArgs()
        {
        }
        public static new GetDomainNameInvokeArgs Empty => new GetDomainNameInvokeArgs();
    }


    [OutputType]
    public sealed class GetDomainNameResult
    {
        public readonly string? CertificateArn;
        public readonly string? DistributionDomainName;
        public readonly string? DistributionHostedZoneId;
        public readonly Outputs.DomainNameEndpointConfiguration? EndpointConfiguration;
        public readonly Outputs.DomainNameMutualTlsAuthentication? MutualTlsAuthentication;
        public readonly string? OwnershipVerificationCertificateArn;
        public readonly string? RegionalCertificateArn;
        public readonly string? RegionalDomainName;
        public readonly string? RegionalHostedZoneId;
        public readonly string? SecurityPolicy;
        public readonly ImmutableArray<Outputs.DomainNameTag> Tags;

        [OutputConstructor]
        private GetDomainNameResult(
            string? certificateArn,

            string? distributionDomainName,

            string? distributionHostedZoneId,

            Outputs.DomainNameEndpointConfiguration? endpointConfiguration,

            Outputs.DomainNameMutualTlsAuthentication? mutualTlsAuthentication,

            string? ownershipVerificationCertificateArn,

            string? regionalCertificateArn,

            string? regionalDomainName,

            string? regionalHostedZoneId,

            string? securityPolicy,

            ImmutableArray<Outputs.DomainNameTag> tags)
        {
            CertificateArn = certificateArn;
            DistributionDomainName = distributionDomainName;
            DistributionHostedZoneId = distributionHostedZoneId;
            EndpointConfiguration = endpointConfiguration;
            MutualTlsAuthentication = mutualTlsAuthentication;
            OwnershipVerificationCertificateArn = ownershipVerificationCertificateArn;
            RegionalCertificateArn = regionalCertificateArn;
            RegionalDomainName = regionalDomainName;
            RegionalHostedZoneId = regionalHostedZoneId;
            SecurityPolicy = securityPolicy;
            Tags = tags;
        }
    }
}
