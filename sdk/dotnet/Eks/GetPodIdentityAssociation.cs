// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Eks
{
    public static class GetPodIdentityAssociation
    {
        /// <summary>
        /// An object representing an Amazon EKS PodIdentityAssociation.
        /// </summary>
        public static Task<GetPodIdentityAssociationResult> InvokeAsync(GetPodIdentityAssociationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPodIdentityAssociationResult>("aws-native:eks:getPodIdentityAssociation", args ?? new GetPodIdentityAssociationArgs(), options.WithDefaults());

        /// <summary>
        /// An object representing an Amazon EKS PodIdentityAssociation.
        /// </summary>
        public static Output<GetPodIdentityAssociationResult> Invoke(GetPodIdentityAssociationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPodIdentityAssociationResult>("aws-native:eks:getPodIdentityAssociation", args ?? new GetPodIdentityAssociationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPodIdentityAssociationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the pod identity association.
        /// </summary>
        [Input("associationArn", required: true)]
        public string AssociationArn { get; set; } = null!;

        public GetPodIdentityAssociationArgs()
        {
        }
        public static new GetPodIdentityAssociationArgs Empty => new GetPodIdentityAssociationArgs();
    }

    public sealed class GetPodIdentityAssociationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the pod identity association.
        /// </summary>
        [Input("associationArn", required: true)]
        public Input<string> AssociationArn { get; set; } = null!;

        public GetPodIdentityAssociationInvokeArgs()
        {
        }
        public static new GetPodIdentityAssociationInvokeArgs Empty => new GetPodIdentityAssociationInvokeArgs();
    }


    [OutputType]
    public sealed class GetPodIdentityAssociationResult
    {
        /// <summary>
        /// The ARN of the pod identity association.
        /// </summary>
        public readonly string? AssociationArn;
        /// <summary>
        /// The ID of the pod identity association.
        /// </summary>
        public readonly string? AssociationId;
        /// <summary>
        /// The IAM role ARN that the pod identity association is created for.
        /// </summary>
        public readonly string? RoleArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetPodIdentityAssociationResult(
            string? associationArn,

            string? associationId,

            string? roleArn,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            AssociationArn = associationArn;
            AssociationId = associationId;
            RoleArn = roleArn;
            Tags = tags;
        }
    }
}
