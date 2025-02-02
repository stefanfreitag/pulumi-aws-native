// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisLegendOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("height")]
        public Input<string>? Height { get; set; }

        [Input("position")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisLegendPosition>? Position { get; set; }

        [Input("title")]
        public Input<Inputs.AnalysisLabelOptionsArgs>? Title { get; set; }

        [Input("visibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? Visibility { get; set; }

        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("width")]
        public Input<string>? Width { get; set; }

        public AnalysisLegendOptionsArgs()
        {
        }
        public static new AnalysisLegendOptionsArgs Empty => new AnalysisLegendOptionsArgs();
    }
}
