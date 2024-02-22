// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Sso
{
    public static class GetPermissionSet
    {
        /// <summary>
        /// Resource Type definition for SSO PermissionSet
        /// </summary>
        public static Task<GetPermissionSetResult> InvokeAsync(GetPermissionSetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPermissionSetResult>("aws-native:sso:getPermissionSet", args ?? new GetPermissionSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for SSO PermissionSet
        /// </summary>
        public static Output<GetPermissionSetResult> Invoke(GetPermissionSetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPermissionSetResult>("aws-native:sso:getPermissionSet", args ?? new GetPermissionSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPermissionSetArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The sso instance arn that the permission set is owned.
        /// </summary>
        [Input("instanceArn", required: true)]
        public string InstanceArn { get; set; } = null!;

        /// <summary>
        /// The permission set that the policy will be attached to
        /// </summary>
        [Input("permissionSetArn", required: true)]
        public string PermissionSetArn { get; set; } = null!;

        public GetPermissionSetArgs()
        {
        }
        public static new GetPermissionSetArgs Empty => new GetPermissionSetArgs();
    }

    public sealed class GetPermissionSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The sso instance arn that the permission set is owned.
        /// </summary>
        [Input("instanceArn", required: true)]
        public Input<string> InstanceArn { get; set; } = null!;

        /// <summary>
        /// The permission set that the policy will be attached to
        /// </summary>
        [Input("permissionSetArn", required: true)]
        public Input<string> PermissionSetArn { get; set; } = null!;

        public GetPermissionSetInvokeArgs()
        {
        }
        public static new GetPermissionSetInvokeArgs Empty => new GetPermissionSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetPermissionSetResult
    {
        public readonly ImmutableArray<Outputs.PermissionSetCustomerManagedPolicyReference> CustomerManagedPolicyReferences;
        /// <summary>
        /// The permission set description.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The inline policy to put in permission set.
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::SSO::PermissionSet` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? InlinePolicy;
        public readonly ImmutableArray<string> ManagedPolicies;
        /// <summary>
        /// The permission set that the policy will be attached to
        /// </summary>
        public readonly string? PermissionSetArn;
        public readonly Outputs.PermissionSetPermissionsBoundary? PermissionsBoundary;
        /// <summary>
        /// The relay state URL that redirect links to any service in the AWS Management Console.
        /// </summary>
        public readonly string? RelayStateType;
        /// <summary>
        /// The length of time that a user can be signed in to an AWS account.
        /// </summary>
        public readonly string? SessionDuration;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetPermissionSetResult(
            ImmutableArray<Outputs.PermissionSetCustomerManagedPolicyReference> customerManagedPolicyReferences,

            string? description,

            object? inlinePolicy,

            ImmutableArray<string> managedPolicies,

            string? permissionSetArn,

            Outputs.PermissionSetPermissionsBoundary? permissionsBoundary,

            string? relayStateType,

            string? sessionDuration,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            CustomerManagedPolicyReferences = customerManagedPolicyReferences;
            Description = description;
            InlinePolicy = inlinePolicy;
            ManagedPolicies = managedPolicies;
            PermissionSetArn = permissionSetArn;
            PermissionsBoundary = permissionsBoundary;
            RelayStateType = relayStateType;
            SessionDuration = sessionDuration;
            Tags = tags;
        }
    }
}
