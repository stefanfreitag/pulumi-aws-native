// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync
{
    public static class GetLocationFSxOntap
    {
        /// <summary>
        /// Resource schema for AWS::DataSync::LocationFSxONTAP.
        /// </summary>
        public static Task<GetLocationFSxOntapResult> InvokeAsync(GetLocationFSxOntapArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLocationFSxOntapResult>("aws-native:datasync:getLocationFSxOntap", args ?? new GetLocationFSxOntapArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DataSync::LocationFSxONTAP.
        /// </summary>
        public static Output<GetLocationFSxOntapResult> Invoke(GetLocationFSxOntapInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLocationFSxOntapResult>("aws-native:datasync:getLocationFSxOntap", args ?? new GetLocationFSxOntapInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLocationFSxOntapArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public string LocationArn { get; set; } = null!;

        public GetLocationFSxOntapArgs()
        {
        }
        public static new GetLocationFSxOntapArgs Empty => new GetLocationFSxOntapArgs();
    }

    public sealed class GetLocationFSxOntapInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public Input<string> LocationArn { get; set; } = null!;

        public GetLocationFSxOntapInvokeArgs()
        {
        }
        public static new GetLocationFSxOntapInvokeArgs Empty => new GetLocationFSxOntapInvokeArgs();
    }


    [OutputType]
    public sealed class GetLocationFSxOntapResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) for the FSx ONAP file system.
        /// </summary>
        public readonly string? FsxFilesystemArn;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
        /// </summary>
        public readonly string? LocationArn;
        /// <summary>
        /// The URL of the FSx ONTAP file system that was described.
        /// </summary>
        public readonly string? LocationUri;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetLocationFSxOntapResult(
            string? fsxFilesystemArn,

            string? locationArn,

            string? locationUri,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            FsxFilesystemArn = fsxFilesystemArn;
            LocationArn = locationArn;
            LocationUri = locationUri;
            Tags = tags;
        }
    }
}
