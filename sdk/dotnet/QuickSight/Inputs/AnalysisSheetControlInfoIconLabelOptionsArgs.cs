// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisSheetControlInfoIconLabelOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("infoIconText")]
        public Input<string>? InfoIconText { get; set; }

        [Input("visibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? Visibility { get; set; }

        public AnalysisSheetControlInfoIconLabelOptionsArgs()
        {
        }
        public static new AnalysisSheetControlInfoIconLabelOptionsArgs Empty => new AnalysisSheetControlInfoIconLabelOptionsArgs();
    }
}
