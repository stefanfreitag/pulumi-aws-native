// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFRegional.Inputs
{

    public sealed class RateBasedRulePredicateArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataId", required: true)]
        public Input<string> DataId { get; set; } = null!;

        [Input("negated", required: true)]
        public Input<bool> Negated { get; set; } = null!;

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public RateBasedRulePredicateArgs()
        {
        }
        public static new RateBasedRulePredicateArgs Empty => new RateBasedRulePredicateArgs();
    }
}
