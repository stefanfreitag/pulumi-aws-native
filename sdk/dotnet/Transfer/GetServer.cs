// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Transfer
{
    public static class GetServer
    {
        /// <summary>
        /// Resource Type definition for AWS::Transfer::Server
        /// </summary>
        public static Task<GetServerResult> InvokeAsync(GetServerArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServerResult>("aws-native:transfer:getServer", args ?? new GetServerArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Transfer::Server
        /// </summary>
        public static Output<GetServerResult> Invoke(GetServerInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetServerResult>("aws-native:transfer:getServer", args ?? new GetServerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServerArgs : global::Pulumi.InvokeArgs
    {
        [Input("serverId", required: true)]
        public string ServerId { get; set; } = null!;

        public GetServerArgs()
        {
        }
        public static new GetServerArgs Empty => new GetServerArgs();
    }

    public sealed class GetServerInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("serverId", required: true)]
        public Input<string> ServerId { get; set; } = null!;

        public GetServerInvokeArgs()
        {
        }
        public static new GetServerInvokeArgs Empty => new GetServerInvokeArgs();
    }


    [OutputType]
    public sealed class GetServerResult
    {
        public readonly string? Arn;
        public readonly string? Certificate;
        public readonly Outputs.ServerEndpointDetails? EndpointDetails;
        public readonly string? EndpointType;
        public readonly Outputs.ServerIdentityProviderDetails? IdentityProviderDetails;
        public readonly string? LoggingRole;
        public readonly string? PostAuthenticationLoginBanner;
        public readonly string? PreAuthenticationLoginBanner;
        public readonly Outputs.ServerProtocolDetails? ProtocolDetails;
        public readonly ImmutableArray<Outputs.ServerProtocol> Protocols;
        public readonly string? SecurityPolicyName;
        public readonly string? ServerId;
        public readonly ImmutableArray<Outputs.ServerTag> Tags;
        public readonly Outputs.ServerWorkflowDetails? WorkflowDetails;

        [OutputConstructor]
        private GetServerResult(
            string? arn,

            string? certificate,

            Outputs.ServerEndpointDetails? endpointDetails,

            string? endpointType,

            Outputs.ServerIdentityProviderDetails? identityProviderDetails,

            string? loggingRole,

            string? postAuthenticationLoginBanner,

            string? preAuthenticationLoginBanner,

            Outputs.ServerProtocolDetails? protocolDetails,

            ImmutableArray<Outputs.ServerProtocol> protocols,

            string? securityPolicyName,

            string? serverId,

            ImmutableArray<Outputs.ServerTag> tags,

            Outputs.ServerWorkflowDetails? workflowDetails)
        {
            Arn = arn;
            Certificate = certificate;
            EndpointDetails = endpointDetails;
            EndpointType = endpointType;
            IdentityProviderDetails = identityProviderDetails;
            LoggingRole = loggingRole;
            PostAuthenticationLoginBanner = postAuthenticationLoginBanner;
            PreAuthenticationLoginBanner = preAuthenticationLoginBanner;
            ProtocolDetails = protocolDetails;
            Protocols = protocols;
            SecurityPolicyName = securityPolicyName;
            ServerId = serverId;
            Tags = tags;
            WorkflowDetails = workflowDetails;
        }
    }
}
