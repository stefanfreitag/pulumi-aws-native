// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisDataBarsOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldId", required: true)]
        public Input<string> FieldId { get; set; } = null!;

        [Input("negativeColor")]
        public Input<string>? NegativeColor { get; set; }

        [Input("positiveColor")]
        public Input<string>? PositiveColor { get; set; }

        public AnalysisDataBarsOptionsArgs()
        {
        }
        public static new AnalysisDataBarsOptionsArgs Empty => new AnalysisDataBarsOptionsArgs();
    }
}
