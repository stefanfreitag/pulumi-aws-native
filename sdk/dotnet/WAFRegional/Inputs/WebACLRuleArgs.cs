// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFRegional.Inputs
{

    public sealed class WebACLRuleArgs : global::Pulumi.ResourceArgs
    {
        [Input("action", required: true)]
        public Input<Inputs.WebACLActionArgs> Action { get; set; } = null!;

        [Input("priority", required: true)]
        public Input<int> Priority { get; set; } = null!;

        [Input("ruleId", required: true)]
        public Input<string> RuleId { get; set; } = null!;

        public WebACLRuleArgs()
        {
        }
        public static new WebACLRuleArgs Empty => new WebACLRuleArgs();
    }
}
