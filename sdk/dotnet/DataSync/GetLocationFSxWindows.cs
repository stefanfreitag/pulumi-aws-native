// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync
{
    public static class GetLocationFSxWindows
    {
        /// <summary>
        /// Resource schema for AWS::DataSync::LocationFSxWindows.
        /// </summary>
        public static Task<GetLocationFSxWindowsResult> InvokeAsync(GetLocationFSxWindowsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLocationFSxWindowsResult>("aws-native:datasync:getLocationFSxWindows", args ?? new GetLocationFSxWindowsArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DataSync::LocationFSxWindows.
        /// </summary>
        public static Output<GetLocationFSxWindowsResult> Invoke(GetLocationFSxWindowsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLocationFSxWindowsResult>("aws-native:datasync:getLocationFSxWindows", args ?? new GetLocationFSxWindowsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLocationFSxWindowsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public string LocationArn { get; set; } = null!;

        public GetLocationFSxWindowsArgs()
        {
        }
        public static new GetLocationFSxWindowsArgs Empty => new GetLocationFSxWindowsArgs();
    }

    public sealed class GetLocationFSxWindowsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public Input<string> LocationArn { get; set; } = null!;

        public GetLocationFSxWindowsInvokeArgs()
        {
        }
        public static new GetLocationFSxWindowsInvokeArgs Empty => new GetLocationFSxWindowsInvokeArgs();
    }


    [OutputType]
    public sealed class GetLocationFSxWindowsResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.
        /// </summary>
        public readonly string? LocationArn;
        /// <summary>
        /// The URL of the FSx for Windows location that was described.
        /// </summary>
        public readonly string? LocationUri;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetLocationFSxWindowsResult(
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
