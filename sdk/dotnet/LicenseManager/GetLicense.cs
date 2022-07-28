// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LicenseManager
{
    public static class GetLicense
    {
        /// <summary>
        /// Resource Type definition for AWS::LicenseManager::License
        /// </summary>
        public static Task<GetLicenseResult> InvokeAsync(GetLicenseArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetLicenseResult>("aws-native:licensemanager:getLicense", args ?? new GetLicenseArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::LicenseManager::License
        /// </summary>
        public static Output<GetLicenseResult> Invoke(GetLicenseInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetLicenseResult>("aws-native:licensemanager:getLicense", args ?? new GetLicenseInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLicenseArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Amazon Resource Name is a unique name for each resource.
        /// </summary>
        [Input("licenseArn", required: true)]
        public string LicenseArn { get; set; } = null!;

        public GetLicenseArgs()
        {
        }
        public static new GetLicenseArgs Empty => new GetLicenseArgs();
    }

    public sealed class GetLicenseInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Amazon Resource Name is a unique name for each resource.
        /// </summary>
        [Input("licenseArn", required: true)]
        public Input<string> LicenseArn { get; set; } = null!;

        public GetLicenseInvokeArgs()
        {
        }
        public static new GetLicenseInvokeArgs Empty => new GetLicenseInvokeArgs();
    }


    [OutputType]
    public sealed class GetLicenseResult
    {
        /// <summary>
        /// Beneficiary of the license.
        /// </summary>
        public readonly string? Beneficiary;
        public readonly Outputs.LicenseConsumptionConfiguration? ConsumptionConfiguration;
        public readonly ImmutableArray<Outputs.LicenseEntitlement> Entitlements;
        /// <summary>
        /// Home region for the created license.
        /// </summary>
        public readonly string? HomeRegion;
        public readonly Outputs.LicenseIssuerData? Issuer;
        /// <summary>
        /// Amazon Resource Name is a unique name for each resource.
        /// </summary>
        public readonly string? LicenseArn;
        public readonly ImmutableArray<Outputs.LicenseMetadata> LicenseMetadata;
        /// <summary>
        /// Name for the created license.
        /// </summary>
        public readonly string? LicenseName;
        /// <summary>
        /// Product name for the created license.
        /// </summary>
        public readonly string? ProductName;
        /// <summary>
        /// ProductSKU of the license.
        /// </summary>
        public readonly string? ProductSKU;
        public readonly Outputs.LicenseValidityDateFormat? Validity;
        /// <summary>
        /// The version of the license.
        /// </summary>
        public readonly string? Version;

        [OutputConstructor]
        private GetLicenseResult(
            string? beneficiary,

            Outputs.LicenseConsumptionConfiguration? consumptionConfiguration,

            ImmutableArray<Outputs.LicenseEntitlement> entitlements,

            string? homeRegion,

            Outputs.LicenseIssuerData? issuer,

            string? licenseArn,

            ImmutableArray<Outputs.LicenseMetadata> licenseMetadata,

            string? licenseName,

            string? productName,

            string? productSKU,

            Outputs.LicenseValidityDateFormat? validity,

            string? version)
        {
            Beneficiary = beneficiary;
            ConsumptionConfiguration = consumptionConfiguration;
            Entitlements = entitlements;
            HomeRegion = homeRegion;
            Issuer = issuer;
            LicenseArn = licenseArn;
            LicenseMetadata = licenseMetadata;
            LicenseName = licenseName;
            ProductName = productName;
            ProductSKU = productSKU;
            Validity = validity;
            Version = version;
        }
    }
}
