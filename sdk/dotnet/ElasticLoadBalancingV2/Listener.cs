// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2
{
    /// <summary>
    /// Resource Type definition for AWS::ElasticLoadBalancingV2::Listener
    /// </summary>
    [AwsNativeResourceType("aws-native:elasticloadbalancingv2:Listener")]
    public partial class Listener : global::Pulumi.CustomResource
    {
        [Output("alpnPolicy")]
        public Output<ImmutableArray<string>> AlpnPolicy { get; private set; } = null!;

        [Output("certificates")]
        public Output<ImmutableArray<Outputs.ListenerCertificate>> Certificates { get; private set; } = null!;

        [Output("defaultActions")]
        public Output<ImmutableArray<Outputs.ListenerAction>> DefaultActions { get; private set; } = null!;

        [Output("listenerArn")]
        public Output<string> ListenerArn { get; private set; } = null!;

        [Output("loadBalancerArn")]
        public Output<string> LoadBalancerArn { get; private set; } = null!;

        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        [Output("protocol")]
        public Output<string?> Protocol { get; private set; } = null!;

        [Output("sslPolicy")]
        public Output<string?> SslPolicy { get; private set; } = null!;


        /// <summary>
        /// Create a Listener resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Listener(string name, ListenerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:elasticloadbalancingv2:Listener", name, args ?? new ListenerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Listener(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:elasticloadbalancingv2:Listener", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Listener resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Listener Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Listener(name, id, options);
        }
    }

    public sealed class ListenerArgs : global::Pulumi.ResourceArgs
    {
        [Input("alpnPolicy")]
        private InputList<string>? _alpnPolicy;
        public InputList<string> AlpnPolicy
        {
            get => _alpnPolicy ?? (_alpnPolicy = new InputList<string>());
            set => _alpnPolicy = value;
        }

        [Input("certificates")]
        private InputList<Inputs.ListenerCertificateArgs>? _certificates;
        public InputList<Inputs.ListenerCertificateArgs> Certificates
        {
            get => _certificates ?? (_certificates = new InputList<Inputs.ListenerCertificateArgs>());
            set => _certificates = value;
        }

        [Input("defaultActions", required: true)]
        private InputList<Inputs.ListenerActionArgs>? _defaultActions;
        public InputList<Inputs.ListenerActionArgs> DefaultActions
        {
            get => _defaultActions ?? (_defaultActions = new InputList<Inputs.ListenerActionArgs>());
            set => _defaultActions = value;
        }

        [Input("loadBalancerArn", required: true)]
        public Input<string> LoadBalancerArn { get; set; } = null!;

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        [Input("sslPolicy")]
        public Input<string>? SslPolicy { get; set; }

        public ListenerArgs()
        {
        }
        public static new ListenerArgs Empty => new ListenerArgs();
    }
}
