// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager
{
    public static class GetSiteToSiteVpnAttachment
    {
        /// <summary>
        /// AWS::NetworkManager::SiteToSiteVpnAttachment Resource Type definition.
        /// </summary>
        public static Task<GetSiteToSiteVpnAttachmentResult> InvokeAsync(GetSiteToSiteVpnAttachmentArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSiteToSiteVpnAttachmentResult>("aws-native:networkmanager:getSiteToSiteVpnAttachment", args ?? new GetSiteToSiteVpnAttachmentArgs(), options.WithDefaults());

        /// <summary>
        /// AWS::NetworkManager::SiteToSiteVpnAttachment Resource Type definition.
        /// </summary>
        public static Output<GetSiteToSiteVpnAttachmentResult> Invoke(GetSiteToSiteVpnAttachmentInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSiteToSiteVpnAttachmentResult>("aws-native:networkmanager:getSiteToSiteVpnAttachment", args ?? new GetSiteToSiteVpnAttachmentInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSiteToSiteVpnAttachmentArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the attachment.
        /// </summary>
        [Input("attachmentId", required: true)]
        public string AttachmentId { get; set; } = null!;

        public GetSiteToSiteVpnAttachmentArgs()
        {
        }
        public static new GetSiteToSiteVpnAttachmentArgs Empty => new GetSiteToSiteVpnAttachmentArgs();
    }

    public sealed class GetSiteToSiteVpnAttachmentInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the attachment.
        /// </summary>
        [Input("attachmentId", required: true)]
        public Input<string> AttachmentId { get; set; } = null!;

        public GetSiteToSiteVpnAttachmentInvokeArgs()
        {
        }
        public static new GetSiteToSiteVpnAttachmentInvokeArgs Empty => new GetSiteToSiteVpnAttachmentInvokeArgs();
    }


    [OutputType]
    public sealed class GetSiteToSiteVpnAttachmentResult
    {
        /// <summary>
        /// The ID of the attachment.
        /// </summary>
        public readonly string? AttachmentId;
        /// <summary>
        /// The policy rule number associated with the attachment.
        /// </summary>
        public readonly int? AttachmentPolicyRuleNumber;
        /// <summary>
        /// The type of attachment.
        /// </summary>
        public readonly string? AttachmentType;
        /// <summary>
        /// The ARN of a core network for the VPC attachment.
        /// </summary>
        public readonly string? CoreNetworkArn;
        /// <summary>
        /// Creation time of the attachment.
        /// </summary>
        public readonly string? CreatedAt;
        /// <summary>
        /// The Region where the edge is located.
        /// </summary>
        public readonly string? EdgeLocation;
        /// <summary>
        /// Owner account of the attachment.
        /// </summary>
        public readonly string? OwnerAccountId;
        /// <summary>
        /// The attachment to move from one segment to another.
        /// </summary>
        public readonly Outputs.SiteToSiteVpnAttachmentProposedSegmentChange? ProposedSegmentChange;
        /// <summary>
        /// The ARN of the Resource.
        /// </summary>
        public readonly string? ResourceArn;
        /// <summary>
        /// The name of the segment that attachment is in.
        /// </summary>
        public readonly string? SegmentName;
        /// <summary>
        /// The state of the attachment.
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// Tags for the attachment.
        /// </summary>
        public readonly ImmutableArray<Outputs.SiteToSiteVpnAttachmentTag> Tags;
        /// <summary>
        /// Last update time of the attachment.
        /// </summary>
        public readonly string? UpdatedAt;

        [OutputConstructor]
        private GetSiteToSiteVpnAttachmentResult(
            string? attachmentId,

            int? attachmentPolicyRuleNumber,

            string? attachmentType,

            string? coreNetworkArn,

            string? createdAt,

            string? edgeLocation,

            string? ownerAccountId,

            Outputs.SiteToSiteVpnAttachmentProposedSegmentChange? proposedSegmentChange,

            string? resourceArn,

            string? segmentName,

            string? state,

            ImmutableArray<Outputs.SiteToSiteVpnAttachmentTag> tags,

            string? updatedAt)
        {
            AttachmentId = attachmentId;
            AttachmentPolicyRuleNumber = attachmentPolicyRuleNumber;
            AttachmentType = attachmentType;
            CoreNetworkArn = coreNetworkArn;
            CreatedAt = createdAt;
            EdgeLocation = edgeLocation;
            OwnerAccountId = ownerAccountId;
            ProposedSegmentChange = proposedSegmentChange;
            ResourceArn = resourceArn;
            SegmentName = segmentName;
            State = state;
            Tags = tags;
            UpdatedAt = updatedAt;
        }
    }
}
