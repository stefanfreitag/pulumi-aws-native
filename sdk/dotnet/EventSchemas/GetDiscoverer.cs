// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EventSchemas
{
    public static class GetDiscoverer
    {
        /// <summary>
        /// Resource Type definition for AWS::EventSchemas::Discoverer
        /// </summary>
        public static Task<GetDiscovererResult> InvokeAsync(GetDiscovererArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDiscovererResult>("aws-native:eventschemas:getDiscoverer", args ?? new GetDiscovererArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EventSchemas::Discoverer
        /// </summary>
        public static Output<GetDiscovererResult> Invoke(GetDiscovererInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDiscovererResult>("aws-native:eventschemas:getDiscoverer", args ?? new GetDiscovererInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDiscovererArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the discoverer.
        /// </summary>
        [Input("discovererArn", required: true)]
        public string DiscovererArn { get; set; } = null!;

        public GetDiscovererArgs()
        {
        }
        public static new GetDiscovererArgs Empty => new GetDiscovererArgs();
    }

    public sealed class GetDiscovererInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the discoverer.
        /// </summary>
        [Input("discovererArn", required: true)]
        public Input<string> DiscovererArn { get; set; } = null!;

        public GetDiscovererInvokeArgs()
        {
        }
        public static new GetDiscovererInvokeArgs Empty => new GetDiscovererInvokeArgs();
    }


    [OutputType]
    public sealed class GetDiscovererResult
    {
        /// <summary>
        /// Defines whether event schemas from other accounts are discovered. Default is True.
        /// </summary>
        public readonly bool? CrossAccount;
        /// <summary>
        /// A description for the discoverer.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The ARN of the discoverer.
        /// </summary>
        public readonly string? DiscovererArn;
        /// <summary>
        /// The Id of the discoverer.
        /// </summary>
        public readonly string? DiscovererId;
        /// <summary>
        /// Defines the current state of the discoverer.
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// Tags associated with the resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetDiscovererResult(
            bool? crossAccount,

            string? description,

            string? discovererArn,

            string? discovererId,

            string? state,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            CrossAccount = crossAccount;
            Description = description;
            DiscovererArn = discovererArn;
            DiscovererId = discovererId;
            State = state;
            Tags = tags;
        }
    }
}
