// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetSoftwarePackage
    {
        /// <summary>
        /// resource definition
        /// </summary>
        public static Task<GetSoftwarePackageResult> InvokeAsync(GetSoftwarePackageArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSoftwarePackageResult>("aws-native:iot:getSoftwarePackage", args ?? new GetSoftwarePackageArgs(), options.WithDefaults());

        /// <summary>
        /// resource definition
        /// </summary>
        public static Output<GetSoftwarePackageResult> Invoke(GetSoftwarePackageInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSoftwarePackageResult>("aws-native:iot:getSoftwarePackage", args ?? new GetSoftwarePackageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSoftwarePackageArgs : global::Pulumi.InvokeArgs
    {
        [Input("packageName", required: true)]
        public string PackageName { get; set; } = null!;

        public GetSoftwarePackageArgs()
        {
        }
        public static new GetSoftwarePackageArgs Empty => new GetSoftwarePackageArgs();
    }

    public sealed class GetSoftwarePackageInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("packageName", required: true)]
        public Input<string> PackageName { get; set; } = null!;

        public GetSoftwarePackageInvokeArgs()
        {
        }
        public static new GetSoftwarePackageInvokeArgs Empty => new GetSoftwarePackageInvokeArgs();
    }


    [OutputType]
    public sealed class GetSoftwarePackageResult
    {
        public readonly string? Description;
        public readonly string? PackageArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.SoftwarePackageTag> Tags;

        [OutputConstructor]
        private GetSoftwarePackageResult(
            string? description,

            string? packageArn,

            ImmutableArray<Outputs.SoftwarePackageTag> tags)
        {
            Description = description;
            PackageArn = packageArn;
            Tags = tags;
        }
    }
}
