// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CertificateManager
{
    public static class GetCertificate
    {
        /// <summary>
        /// Resource Type definition for AWS::CertificateManager::Certificate
        /// </summary>
        public static Task<GetCertificateResult> InvokeAsync(GetCertificateArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCertificateResult>("aws-native:certificatemanager:getCertificate", args ?? new GetCertificateArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CertificateManager::Certificate
        /// </summary>
        public static Output<GetCertificateResult> Invoke(GetCertificateInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetCertificateResult>("aws-native:certificatemanager:getCertificate", args ?? new GetCertificateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCertificateArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetCertificateArgs()
        {
        }
        public static new GetCertificateArgs Empty => new GetCertificateArgs();
    }

    public sealed class GetCertificateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetCertificateInvokeArgs()
        {
        }
        public static new GetCertificateInvokeArgs Empty => new GetCertificateInvokeArgs();
    }


    [OutputType]
    public sealed class GetCertificateResult
    {
        public readonly string? CertificateTransparencyLoggingPreference;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.CertificateTag> Tags;

        [OutputConstructor]
        private GetCertificateResult(
            string? certificateTransparencyLoggingPreference,

            string? id,

            ImmutableArray<Outputs.CertificateTag> tags)
        {
            CertificateTransparencyLoggingPreference = certificateTransparencyLoggingPreference;
            Id = id;
            Tags = tags;
        }
    }
}
