// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisCustomValuesConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("customValues", required: true)]
        public Input<Inputs.AnalysisCustomParameterValuesArgs> CustomValues { get; set; } = null!;

        [Input("includeNullValue")]
        public Input<bool>? IncludeNullValue { get; set; }

        public AnalysisCustomValuesConfigurationArgs()
        {
        }
        public static new AnalysisCustomValuesConfigurationArgs Empty => new AnalysisCustomValuesConfigurationArgs();
    }
}
