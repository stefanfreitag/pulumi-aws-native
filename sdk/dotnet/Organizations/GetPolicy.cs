// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Organizations
{
    public static class GetPolicy
    {
        /// <summary>
        /// Policies in AWS Organizations enable you to manage different features of the AWS accounts in your organization.  You can use policies when all features are enabled in your organization.
        /// </summary>
        public static Task<GetPolicyResult> InvokeAsync(GetPolicyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPolicyResult>("aws-native:organizations:getPolicy", args ?? new GetPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Policies in AWS Organizations enable you to manage different features of the AWS accounts in your organization.  You can use policies when all features are enabled in your organization.
        /// </summary>
        public static Output<GetPolicyResult> Invoke(GetPolicyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPolicyResult>("aws-native:organizations:getPolicy", args ?? new GetPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of the Policy
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetPolicyArgs()
        {
        }
        public static new GetPolicyArgs Empty => new GetPolicyArgs();
    }

    public sealed class GetPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of the Policy
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetPolicyInvokeArgs()
        {
        }
        public static new GetPolicyInvokeArgs Empty => new GetPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetPolicyResult
    {
        /// <summary>
        /// ARN of the Policy
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
        /// </summary>
        public readonly bool? AwsManaged;
        /// <summary>
        /// The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Organizations::Policy` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? Content;
        /// <summary>
        /// Human readable description of the policy
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Id of the Policy
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Name of the Policy
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
        /// </summary>
        public readonly ImmutableArray<Outputs.PolicyTag> Tags;
        /// <summary>
        /// List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to
        /// </summary>
        public readonly ImmutableArray<string> TargetIds;

        [OutputConstructor]
        private GetPolicyResult(
            string? arn,

            bool? awsManaged,

            object? content,

            string? description,

            string? id,

            string? name,

            ImmutableArray<Outputs.PolicyTag> tags,

            ImmutableArray<string> targetIds)
        {
            Arn = arn;
            AwsManaged = awsManaged;
            Content = content;
            Description = description;
            Id = id;
            Name = name;
            Tags = tags;
            TargetIds = targetIds;
        }
    }
}
