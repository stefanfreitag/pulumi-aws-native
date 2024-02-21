// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3ObjectLambda
{
    public static class GetAccessPointPolicy
    {
        /// <summary>
        /// AWS::S3ObjectLambda::AccessPointPolicy resource is an Amazon S3ObjectLambda policy type that you can use to control permissions for your S3ObjectLambda
        /// </summary>
        public static Task<GetAccessPointPolicyResult> InvokeAsync(GetAccessPointPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAccessPointPolicyResult>("aws-native:s3objectlambda:getAccessPointPolicy", args ?? new GetAccessPointPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// AWS::S3ObjectLambda::AccessPointPolicy resource is an Amazon S3ObjectLambda policy type that you can use to control permissions for your S3ObjectLambda
        /// </summary>
        public static Output<GetAccessPointPolicyResult> Invoke(GetAccessPointPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAccessPointPolicyResult>("aws-native:s3objectlambda:getAccessPointPolicy", args ?? new GetAccessPointPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAccessPointPolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Amazon S3 ObjectLambdaAccessPoint to which the policy applies.
        /// </summary>
        [Input("objectLambdaAccessPoint", required: true)]
        public string ObjectLambdaAccessPoint { get; set; } = null!;

        public GetAccessPointPolicyArgs()
        {
        }
        public static new GetAccessPointPolicyArgs Empty => new GetAccessPointPolicyArgs();
    }

    public sealed class GetAccessPointPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Amazon S3 ObjectLambdaAccessPoint to which the policy applies.
        /// </summary>
        [Input("objectLambdaAccessPoint", required: true)]
        public Input<string> ObjectLambdaAccessPoint { get; set; } = null!;

        public GetAccessPointPolicyInvokeArgs()
        {
        }
        public static new GetAccessPointPolicyInvokeArgs Empty => new GetAccessPointPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetAccessPointPolicyResult
    {
        /// <summary>
        /// A policy document containing permissions to add to the specified ObjectLambdaAccessPoint. For more information, see Access Policy Language Overview (https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the Amazon Simple Storage Service Developer Guide. 
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3ObjectLambda::AccessPointPolicy` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? PolicyDocument;

        [OutputConstructor]
        private GetAccessPointPolicyResult(object? policyDocument)
        {
            PolicyDocument = policyDocument;
        }
    }
}
