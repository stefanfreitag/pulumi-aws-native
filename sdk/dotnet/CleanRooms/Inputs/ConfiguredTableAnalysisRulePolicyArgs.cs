// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms.Inputs
{

    public sealed class ConfiguredTableAnalysisRulePolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("v1", required: true)]
        public Input<Inputs.ConfiguredTableAnalysisRulePolicyV1Args> V1 { get; set; } = null!;

        public ConfiguredTableAnalysisRulePolicyArgs()
        {
        }
        public static new ConfiguredTableAnalysisRulePolicyArgs Empty => new ConfiguredTableAnalysisRulePolicyArgs();
    }
}
