// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3
{
    public static class GetStorageLensGroup
    {
        /// <summary>
        /// The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.
        /// </summary>
        public static Task<GetStorageLensGroupResult> InvokeAsync(GetStorageLensGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetStorageLensGroupResult>("aws-native:s3:getStorageLensGroup", args ?? new GetStorageLensGroupArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::S3::StorageLensGroup resource is an Amazon S3 resource type that you can use to create Storage Lens Group.
        /// </summary>
        public static Output<GetStorageLensGroupResult> Invoke(GetStorageLensGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetStorageLensGroupResult>("aws-native:s3:getStorageLensGroup", args ?? new GetStorageLensGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStorageLensGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetStorageLensGroupArgs()
        {
        }
        public static new GetStorageLensGroupArgs Empty => new GetStorageLensGroupArgs();
    }

    public sealed class GetStorageLensGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetStorageLensGroupInvokeArgs()
        {
        }
        public static new GetStorageLensGroupInvokeArgs Empty => new GetStorageLensGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetStorageLensGroupResult
    {
        public readonly Outputs.StorageLensGroupFilter? Filter;
        /// <summary>
        /// The ARN for the Amazon S3 Storage Lens Group.
        /// </summary>
        public readonly string? StorageLensGroupArn;
        /// <summary>
        /// A set of tags (key-value pairs) for this Amazon S3 Storage Lens Group.
        /// </summary>
        public readonly ImmutableArray<Outputs.StorageLensGroupTag> Tags;

        [OutputConstructor]
        private GetStorageLensGroupResult(
            Outputs.StorageLensGroupFilter? filter,

            string? storageLensGroupArn,

            ImmutableArray<Outputs.StorageLensGroupTag> tags)
        {
            Filter = filter;
            StorageLensGroupArn = storageLensGroupArn;
            Tags = tags;
        }
    }
}
