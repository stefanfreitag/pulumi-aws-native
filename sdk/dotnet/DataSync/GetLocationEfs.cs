// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync
{
    public static class GetLocationEfs
    {
        /// <summary>
        /// Resource schema for AWS::DataSync::LocationEFS.
        /// </summary>
        public static Task<GetLocationEfsResult> InvokeAsync(GetLocationEfsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLocationEfsResult>("aws-native:datasync:getLocationEfs", args ?? new GetLocationEfsArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DataSync::LocationEFS.
        /// </summary>
        public static Output<GetLocationEfsResult> Invoke(GetLocationEfsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLocationEfsResult>("aws-native:datasync:getLocationEfs", args ?? new GetLocationEfsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLocationEfsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public string LocationArn { get; set; } = null!;

        public GetLocationEfsArgs()
        {
        }
        public static new GetLocationEfsArgs Empty => new GetLocationEfsArgs();
    }

    public sealed class GetLocationEfsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public Input<string> LocationArn { get; set; } = null!;

        public GetLocationEfsInvokeArgs()
        {
        }
        public static new GetLocationEfsInvokeArgs Empty => new GetLocationEfsInvokeArgs();
    }


    [OutputType]
    public sealed class GetLocationEfsResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
        /// </summary>
        public readonly string? LocationArn;
        /// <summary>
        /// The URL of the EFS location that was described.
        /// </summary>
        public readonly string? LocationUri;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetLocationEfsResult(
            string? locationArn,

            string? locationUri,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            LocationArn = locationArn;
            LocationUri = locationUri;
            Tags = tags;
        }
    }
}
