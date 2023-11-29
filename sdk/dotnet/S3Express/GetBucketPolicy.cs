// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3Express
{
    public static class GetBucketPolicy
    {
        /// <summary>
        /// Resource Type definition for AWS::S3Express::BucketPolicy.
        /// </summary>
        public static Task<GetBucketPolicyResult> InvokeAsync(GetBucketPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetBucketPolicyResult>("aws-native:s3express:getBucketPolicy", args ?? new GetBucketPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::S3Express::BucketPolicy.
        /// </summary>
        public static Output<GetBucketPolicyResult> Invoke(GetBucketPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetBucketPolicyResult>("aws-native:s3express:getBucketPolicy", args ?? new GetBucketPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBucketPolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the S3 directory bucket to which the policy applies.
        /// </summary>
        [Input("bucket", required: true)]
        public string Bucket { get; set; } = null!;

        public GetBucketPolicyArgs()
        {
        }
        public static new GetBucketPolicyArgs Empty => new GetBucketPolicyArgs();
    }

    public sealed class GetBucketPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the S3 directory bucket to which the policy applies.
        /// </summary>
        [Input("bucket", required: true)]
        public Input<string> Bucket { get; set; } = null!;

        public GetBucketPolicyInvokeArgs()
        {
        }
        public static new GetBucketPolicyInvokeArgs Empty => new GetBucketPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetBucketPolicyResult
    {
        /// <summary>
        /// A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.
        /// </summary>
        public readonly object? PolicyDocument;

        [OutputConstructor]
        private GetBucketPolicyResult(object? policyDocument)
        {
            PolicyDocument = policyDocument;
        }
    }
}
