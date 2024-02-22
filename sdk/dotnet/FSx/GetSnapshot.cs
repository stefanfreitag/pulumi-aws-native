// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx
{
    public static class GetSnapshot
    {
        /// <summary>
        /// Resource Type definition for AWS::FSx::Snapshot
        /// </summary>
        public static Task<GetSnapshotResult> InvokeAsync(GetSnapshotArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSnapshotResult>("aws-native:fsx:getSnapshot", args ?? new GetSnapshotArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::FSx::Snapshot
        /// </summary>
        public static Output<GetSnapshotResult> Invoke(GetSnapshotInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSnapshotResult>("aws-native:fsx:getSnapshot", args ?? new GetSnapshotInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSnapshotArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetSnapshotArgs()
        {
        }
        public static new GetSnapshotArgs Empty => new GetSnapshotArgs();
    }

    public sealed class GetSnapshotInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetSnapshotInvokeArgs()
        {
        }
        public static new GetSnapshotInvokeArgs Empty => new GetSnapshotInvokeArgs();
    }


    [OutputType]
    public sealed class GetSnapshotResult
    {
        public readonly string? Id;
        public readonly string? Name;
        public readonly string? ResourceArn;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetSnapshotResult(
            string? id,

            string? name,

            string? resourceArn,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Id = id;
            Name = name;
            ResourceArn = resourceArn;
            Tags = tags;
        }
    }
}
