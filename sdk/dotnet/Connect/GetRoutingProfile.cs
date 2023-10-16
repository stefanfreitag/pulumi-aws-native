// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    public static class GetRoutingProfile
    {
        /// <summary>
        /// Resource Type definition for AWS::Connect::RoutingProfile
        /// </summary>
        public static Task<GetRoutingProfileResult> InvokeAsync(GetRoutingProfileArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetRoutingProfileResult>("aws-native:connect:getRoutingProfile", args ?? new GetRoutingProfileArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Connect::RoutingProfile
        /// </summary>
        public static Output<GetRoutingProfileResult> Invoke(GetRoutingProfileInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetRoutingProfileResult>("aws-native:connect:getRoutingProfile", args ?? new GetRoutingProfileInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRoutingProfileArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the routing profile.
        /// </summary>
        [Input("routingProfileArn", required: true)]
        public string RoutingProfileArn { get; set; } = null!;

        public GetRoutingProfileArgs()
        {
        }
        public static new GetRoutingProfileArgs Empty => new GetRoutingProfileArgs();
    }

    public sealed class GetRoutingProfileInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the routing profile.
        /// </summary>
        [Input("routingProfileArn", required: true)]
        public Input<string> RoutingProfileArn { get; set; } = null!;

        public GetRoutingProfileInvokeArgs()
        {
        }
        public static new GetRoutingProfileInvokeArgs Empty => new GetRoutingProfileInvokeArgs();
    }


    [OutputType]
    public sealed class GetRoutingProfileResult
    {
        /// <summary>
        /// Whether agents with this routing profile will have their routing order calculated based on longest idle time or time since their last inbound contact.
        /// </summary>
        public readonly Pulumi.AwsNative.Connect.RoutingProfileAgentAvailabilityTimer? AgentAvailabilityTimer;
        /// <summary>
        /// The identifier of the default outbound queue for this routing profile.
        /// </summary>
        public readonly string? DefaultOutboundQueueArn;
        /// <summary>
        /// The description of the routing profile.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The identifier of the Amazon Connect instance.
        /// </summary>
        public readonly string? InstanceArn;
        /// <summary>
        /// The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
        /// </summary>
        public readonly ImmutableArray<Outputs.RoutingProfileMediaConcurrency> MediaConcurrencies;
        /// <summary>
        /// The name of the routing profile.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The queues to associate with this routing profile.
        /// </summary>
        public readonly ImmutableArray<Outputs.RoutingProfileQueueConfig> QueueConfigs;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the routing profile.
        /// </summary>
        public readonly string? RoutingProfileArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.RoutingProfileTag> Tags;

        [OutputConstructor]
        private GetRoutingProfileResult(
            Pulumi.AwsNative.Connect.RoutingProfileAgentAvailabilityTimer? agentAvailabilityTimer,

            string? defaultOutboundQueueArn,

            string? description,

            string? instanceArn,

            ImmutableArray<Outputs.RoutingProfileMediaConcurrency> mediaConcurrencies,

            string? name,

            ImmutableArray<Outputs.RoutingProfileQueueConfig> queueConfigs,

            string? routingProfileArn,

            ImmutableArray<Outputs.RoutingProfileTag> tags)
        {
            AgentAvailabilityTimer = agentAvailabilityTimer;
            DefaultOutboundQueueArn = defaultOutboundQueueArn;
            Description = description;
            InstanceArn = instanceArn;
            MediaConcurrencies = mediaConcurrencies;
            Name = name;
            QueueConfigs = queueConfigs;
            RoutingProfileArn = routingProfileArn;
            Tags = tags;
        }
    }
}
