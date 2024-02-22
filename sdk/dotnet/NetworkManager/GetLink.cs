// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager
{
    public static class GetLink
    {
        /// <summary>
        /// The AWS::NetworkManager::Link type describes a link.
        /// </summary>
        public static Task<GetLinkResult> InvokeAsync(GetLinkArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLinkResult>("aws-native:networkmanager:getLink", args ?? new GetLinkArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::NetworkManager::Link type describes a link.
        /// </summary>
        public static Output<GetLinkResult> Invoke(GetLinkInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLinkResult>("aws-native:networkmanager:getLink", args ?? new GetLinkInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLinkArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the global network.
        /// </summary>
        [Input("globalNetworkId", required: true)]
        public string GlobalNetworkId { get; set; } = null!;

        /// <summary>
        /// The ID of the link.
        /// </summary>
        [Input("linkId", required: true)]
        public string LinkId { get; set; } = null!;

        public GetLinkArgs()
        {
        }
        public static new GetLinkArgs Empty => new GetLinkArgs();
    }

    public sealed class GetLinkInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the global network.
        /// </summary>
        [Input("globalNetworkId", required: true)]
        public Input<string> GlobalNetworkId { get; set; } = null!;

        /// <summary>
        /// The ID of the link.
        /// </summary>
        [Input("linkId", required: true)]
        public Input<string> LinkId { get; set; } = null!;

        public GetLinkInvokeArgs()
        {
        }
        public static new GetLinkInvokeArgs Empty => new GetLinkInvokeArgs();
    }


    [OutputType]
    public sealed class GetLinkResult
    {
        /// <summary>
        /// The Bandwidth for the link.
        /// </summary>
        public readonly Outputs.LinkBandwidth? Bandwidth;
        /// <summary>
        /// The date and time that the device was created.
        /// </summary>
        public readonly string? CreatedAt;
        /// <summary>
        /// The description of the link.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the link.
        /// </summary>
        public readonly string? LinkArn;
        /// <summary>
        /// The ID of the link.
        /// </summary>
        public readonly string? LinkId;
        /// <summary>
        /// The provider of the link.
        /// </summary>
        public readonly string? Provider;
        /// <summary>
        /// The state of the link.
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// The tags for the link.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        /// <summary>
        /// The type of the link.
        /// </summary>
        public readonly string? Type;

        [OutputConstructor]
        private GetLinkResult(
            Outputs.LinkBandwidth? bandwidth,

            string? createdAt,

            string? description,

            string? linkArn,

            string? linkId,

            string? provider,

            string? state,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            string? type)
        {
            Bandwidth = bandwidth;
            CreatedAt = createdAt;
            Description = description;
            LinkArn = linkArn;
            LinkId = linkId;
            Provider = provider;
            State = state;
            Tags = tags;
            Type = type;
        }
    }
}
