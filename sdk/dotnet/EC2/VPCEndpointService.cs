// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::VPCEndpointService
    /// </summary>
    [Obsolete(@"VPCEndpointService is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:VPCEndpointService")]
    public partial class VPCEndpointService : global::Pulumi.CustomResource
    {
        [Output("acceptanceRequired")]
        public Output<bool?> AcceptanceRequired { get; private set; } = null!;

        [Output("gatewayLoadBalancerArns")]
        public Output<ImmutableArray<string>> GatewayLoadBalancerArns { get; private set; } = null!;

        [Output("networkLoadBalancerArns")]
        public Output<ImmutableArray<string>> NetworkLoadBalancerArns { get; private set; } = null!;

        [Output("payerResponsibility")]
        public Output<string?> PayerResponsibility { get; private set; } = null!;


        /// <summary>
        /// Create a VPCEndpointService resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VPCEndpointService(string name, VPCEndpointServiceArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCEndpointService", name, args ?? new VPCEndpointServiceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VPCEndpointService(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:VPCEndpointService", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing VPCEndpointService resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VPCEndpointService Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new VPCEndpointService(name, id, options);
        }
    }

    public sealed class VPCEndpointServiceArgs : global::Pulumi.ResourceArgs
    {
        [Input("acceptanceRequired")]
        public Input<bool>? AcceptanceRequired { get; set; }

        [Input("gatewayLoadBalancerArns")]
        private InputList<string>? _gatewayLoadBalancerArns;
        public InputList<string> GatewayLoadBalancerArns
        {
            get => _gatewayLoadBalancerArns ?? (_gatewayLoadBalancerArns = new InputList<string>());
            set => _gatewayLoadBalancerArns = value;
        }

        [Input("networkLoadBalancerArns")]
        private InputList<string>? _networkLoadBalancerArns;
        public InputList<string> NetworkLoadBalancerArns
        {
            get => _networkLoadBalancerArns ?? (_networkLoadBalancerArns = new InputList<string>());
            set => _networkLoadBalancerArns = value;
        }

        [Input("payerResponsibility")]
        public Input<string>? PayerResponsibility { get; set; }

        public VPCEndpointServiceArgs()
        {
        }
        public static new VPCEndpointServiceArgs Empty => new VPCEndpointServiceArgs();
    }
}
