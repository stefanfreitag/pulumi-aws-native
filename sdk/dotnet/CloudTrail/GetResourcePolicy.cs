// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudTrail
{
    public static class GetResourcePolicy
    {
        /// <summary>
        /// Resource Type definition for AWS::CloudTrail::ResourcePolicy
        /// </summary>
        public static Task<GetResourcePolicyResult> InvokeAsync(GetResourcePolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetResourcePolicyResult>("aws-native:cloudtrail:getResourcePolicy", args ?? new GetResourcePolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CloudTrail::ResourcePolicy
        /// </summary>
        public static Output<GetResourcePolicyResult> Invoke(GetResourcePolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetResourcePolicyResult>("aws-native:cloudtrail:getResourcePolicy", args ?? new GetResourcePolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetResourcePolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the AWS CloudTrail resource to which the policy applies.
        /// </summary>
        [Input("resourceArn", required: true)]
        public string ResourceArn { get; set; } = null!;

        public GetResourcePolicyArgs()
        {
        }
        public static new GetResourcePolicyArgs Empty => new GetResourcePolicyArgs();
    }

    public sealed class GetResourcePolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the AWS CloudTrail resource to which the policy applies.
        /// </summary>
        [Input("resourceArn", required: true)]
        public Input<string> ResourceArn { get; set; } = null!;

        public GetResourcePolicyInvokeArgs()
        {
        }
        public static new GetResourcePolicyInvokeArgs Empty => new GetResourcePolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetResourcePolicyResult
    {
        /// <summary>
        /// A policy document containing permissions to add to the specified resource. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.
        /// </summary>
        public readonly object? ResourcePolicyValue;

        [OutputConstructor]
        private GetResourcePolicyResult(object? resourcePolicy)
        {
            ResourcePolicyValue = resourcePolicy;
        }
    }
}
