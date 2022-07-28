// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Events
{
    public static class GetEndpoint
    {
        /// <summary>
        /// Resource Type definition for AWS::Events::Endpoint.
        /// </summary>
        public static Task<GetEndpointResult> InvokeAsync(GetEndpointArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEndpointResult>("aws-native:events:getEndpoint", args ?? new GetEndpointArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Events::Endpoint.
        /// </summary>
        public static Output<GetEndpointResult> Invoke(GetEndpointInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetEndpointResult>("aws-native:events:getEndpoint", args ?? new GetEndpointInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEndpointArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetEndpointArgs()
        {
        }
        public static new GetEndpointArgs Empty => new GetEndpointArgs();
    }

    public sealed class GetEndpointInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetEndpointInvokeArgs()
        {
        }
        public static new GetEndpointInvokeArgs Empty => new GetEndpointInvokeArgs();
    }


    [OutputType]
    public sealed class GetEndpointResult
    {
        public readonly string? Arn;
        public readonly string? Description;
        public readonly string? EndpointId;
        public readonly string? EndpointUrl;
        public readonly ImmutableArray<Outputs.EndpointEventBus> EventBuses;
        public readonly Outputs.EndpointReplicationConfig? ReplicationConfig;
        public readonly string? RoleArn;
        public readonly Outputs.EndpointRoutingConfig? RoutingConfig;
        public readonly Pulumi.AwsNative.Events.EndpointState? State;
        public readonly string? StateReason;

        [OutputConstructor]
        private GetEndpointResult(
            string? arn,

            string? description,

            string? endpointId,

            string? endpointUrl,

            ImmutableArray<Outputs.EndpointEventBus> eventBuses,

            Outputs.EndpointReplicationConfig? replicationConfig,

            string? roleArn,

            Outputs.EndpointRoutingConfig? routingConfig,

            Pulumi.AwsNative.Events.EndpointState? state,

            string? stateReason)
        {
            Arn = arn;
            Description = description;
            EndpointId = endpointId;
            EndpointUrl = endpointUrl;
            EventBuses = eventBuses;
            ReplicationConfig = replicationConfig;
            RoleArn = roleArn;
            RoutingConfig = routingConfig;
            State = state;
            StateReason = stateReason;
        }
    }
}
