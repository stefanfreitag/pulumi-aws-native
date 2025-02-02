// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancing.Inputs
{

    public sealed class LoadBalancerPoliciesArgs : global::Pulumi.ResourceArgs
    {
        [Input("attributes", required: true)]
        private InputList<object>? _attributes;
        public InputList<object> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<object>());
            set => _attributes = value;
        }

        [Input("instancePorts")]
        private InputList<string>? _instancePorts;
        public InputList<string> InstancePorts
        {
            get => _instancePorts ?? (_instancePorts = new InputList<string>());
            set => _instancePorts = value;
        }

        [Input("loadBalancerPorts")]
        private InputList<string>? _loadBalancerPorts;
        public InputList<string> LoadBalancerPorts
        {
            get => _loadBalancerPorts ?? (_loadBalancerPorts = new InputList<string>());
            set => _loadBalancerPorts = value;
        }

        [Input("policyName", required: true)]
        public Input<string> PolicyName { get; set; } = null!;

        [Input("policyType", required: true)]
        public Input<string> PolicyType { get; set; } = null!;

        public LoadBalancerPoliciesArgs()
        {
        }
        public static new LoadBalancerPoliciesArgs Empty => new LoadBalancerPoliciesArgs();
    }
}
