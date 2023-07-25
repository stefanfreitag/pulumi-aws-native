// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Shield.Outputs
{

    /// <summary>
    /// Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.
    /// </summary>
    [OutputType]
    public sealed class ProtectionApplicationLayerAutomaticResponseConfigurationAction0Properties
    {
        /// <summary>
        /// Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF `Count` action.
        /// You must specify exactly one action, either `Block` or `Count`.
        /// </summary>
        public readonly object? Count;

        [OutputConstructor]
        private ProtectionApplicationLayerAutomaticResponseConfigurationAction0Properties(object? count)
        {
            Count = count;
        }
    }
}
