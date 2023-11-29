// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3Express
{
    public static class GetDirectoryBucket
    {
        /// <summary>
        /// Resource Type definition for AWS::S3Express::DirectoryBucket.
        /// </summary>
        public static Task<GetDirectoryBucketResult> InvokeAsync(GetDirectoryBucketArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDirectoryBucketResult>("aws-native:s3express:getDirectoryBucket", args ?? new GetDirectoryBucketArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::S3Express::DirectoryBucket.
        /// </summary>
        public static Output<GetDirectoryBucketResult> Invoke(GetDirectoryBucketInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDirectoryBucketResult>("aws-native:s3express:getDirectoryBucket", args ?? new GetDirectoryBucketInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDirectoryBucketArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, dots (.), and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az2--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.
        /// </summary>
        [Input("bucketName", required: true)]
        public string BucketName { get; set; } = null!;

        public GetDirectoryBucketArgs()
        {
        }
        public static new GetDirectoryBucketArgs Empty => new GetDirectoryBucketArgs();
    }

    public sealed class GetDirectoryBucketInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, dots (.), and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az2--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.
        /// </summary>
        [Input("bucketName", required: true)]
        public Input<string> BucketName { get; set; } = null!;

        public GetDirectoryBucketInvokeArgs()
        {
        }
        public static new GetDirectoryBucketInvokeArgs Empty => new GetDirectoryBucketInvokeArgs();
    }


    [OutputType]
    public sealed class GetDirectoryBucketResult
    {
        /// <summary>
        /// Returns the Amazon Resource Name (ARN) of the specified bucket.
        /// </summary>
        public readonly string? Arn;

        [OutputConstructor]
        private GetDirectoryBucketResult(string? arn)
        {
            Arn = arn;
        }
    }
}
