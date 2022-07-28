// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GlobalAccelerator
{
    public static class GetListener
    {
        /// <summary>
        /// Resource Type definition for AWS::GlobalAccelerator::Listener
        /// </summary>
        public static Task<GetListenerResult> InvokeAsync(GetListenerArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetListenerResult>("aws-native:globalaccelerator:getListener", args ?? new GetListenerArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::GlobalAccelerator::Listener
        /// </summary>
        public static Output<GetListenerResult> Invoke(GetListenerInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetListenerResult>("aws-native:globalaccelerator:getListener", args ?? new GetListenerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetListenerArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the listener.
        /// </summary>
        [Input("listenerArn", required: true)]
        public string ListenerArn { get; set; } = null!;

        public GetListenerArgs()
        {
        }
        public static new GetListenerArgs Empty => new GetListenerArgs();
    }

    public sealed class GetListenerInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the listener.
        /// </summary>
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
        /// <summary>
        /// Client affinity lets you direct all requests from a user to the same endpoint.
        /// </summary>
        public readonly Pulumi.AwsNative.GlobalAccelerator.ListenerClientAffinity? ClientAffinity;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the listener.
        /// </summary>
        public readonly string? ListenerArn;
        public readonly ImmutableArray<Outputs.ListenerPortRange> PortRanges;
        /// <summary>
        /// The protocol for the listener.
        /// </summary>
        public readonly Pulumi.AwsNative.GlobalAccelerator.ListenerProtocol? Protocol;

        [OutputConstructor]
        private GetListenerResult(
            Pulumi.AwsNative.GlobalAccelerator.ListenerClientAffinity? clientAffinity,

            string? listenerArn,

            ImmutableArray<Outputs.ListenerPortRange> portRanges,

            Pulumi.AwsNative.GlobalAccelerator.ListenerProtocol? protocol)
        {
            ClientAffinity = clientAffinity;
            ListenerArn = listenerArn;
            PortRanges = portRanges;
            Protocol = protocol;
        }
    }
}
