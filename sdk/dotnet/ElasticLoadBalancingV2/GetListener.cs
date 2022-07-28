// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2
{
    public static class GetListener
    {
        /// <summary>
        /// Resource Type definition for AWS::ElasticLoadBalancingV2::Listener
        /// </summary>
        public static Task<GetListenerResult> InvokeAsync(GetListenerArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetListenerResult>("aws-native:elasticloadbalancingv2:getListener", args ?? new GetListenerArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ElasticLoadBalancingV2::Listener
        /// </summary>
        public static Output<GetListenerResult> Invoke(GetListenerInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetListenerResult>("aws-native:elasticloadbalancingv2:getListener", args ?? new GetListenerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetListenerArgs : global::Pulumi.InvokeArgs
    {
        [Input("listenerArn", required: true)]
        public string ListenerArn { get; set; } = null!;

        public GetListenerArgs()
        {
        }
        public static new GetListenerArgs Empty => new GetListenerArgs();
    }

    public sealed class GetListenerInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("listenerArn", required: true)]
        public Input<string> ListenerArn { get; set; } = null!;

        public GetListenerInvokeArgs()
        {
        }
        public static new GetListenerInvokeArgs Empty => new GetListenerInvokeArgs();
    }


    [OutputType]
    public sealed class GetListenerResult
    {
        public readonly ImmutableArray<string> AlpnPolicy;
        public readonly ImmutableArray<Outputs.ListenerCertificate> Certificates;
        public readonly ImmutableArray<Outputs.ListenerAction> DefaultActions;
        public readonly string? ListenerArn;
        public readonly int? Port;
        public readonly string? Protocol;
        public readonly string? SslPolicy;

        [OutputConstructor]
        private GetListenerResult(
            ImmutableArray<string> alpnPolicy,

            ImmutableArray<Outputs.ListenerCertificate> certificates,

            ImmutableArray<Outputs.ListenerAction> defaultActions,

            string? listenerArn,

            int? port,

            string? protocol,

            string? sslPolicy)
        {
            AlpnPolicy = alpnPolicy;
            Certificates = certificates;
            DefaultActions = defaultActions;
            ListenerArn = listenerArn;
            Port = port;
            Protocol = protocol;
            SslPolicy = sslPolicy;
        }
    }
}
