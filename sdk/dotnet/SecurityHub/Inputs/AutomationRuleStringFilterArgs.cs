// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecurityHub.Inputs
{

    public sealed class AutomationRuleStringFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("comparison", required: true)]
        public Input<Pulumi.AwsNative.SecurityHub.AutomationRuleStringFilterComparison> Comparison { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public AutomationRuleStringFilterArgs()
        {
        }
        public static new AutomationRuleStringFilterArgs Empty => new AutomationRuleStringFilterArgs();
    }
}
