// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkFirewall.Inputs
{

    public sealed class FirewallPolicyStatefulEngineOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("ruleOrder")]
        public Input<Pulumi.AwsNative.NetworkFirewall.FirewallPolicyRuleOrder>? RuleOrder { get; set; }

        [Input("streamExceptionPolicy")]
        public Input<Pulumi.AwsNative.NetworkFirewall.FirewallPolicyStreamExceptionPolicy>? StreamExceptionPolicy { get; set; }

        public FirewallPolicyStatefulEngineOptionsArgs()
        {
        }
        public static new FirewallPolicyStatefulEngineOptionsArgs Empty => new FirewallPolicyStatefulEngineOptionsArgs();
    }
}
