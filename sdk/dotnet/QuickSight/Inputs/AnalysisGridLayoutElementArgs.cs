// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisGridLayoutElementArgs : global::Pulumi.ResourceArgs
    {
        [Input("columnIndex")]
        public Input<double>? ColumnIndex { get; set; }

        [Input("columnSpan", required: true)]
        public Input<double> ColumnSpan { get; set; } = null!;

        [Input("elementId", required: true)]
        public Input<string> ElementId { get; set; } = null!;

        [Input("elementType", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisLayoutElementType> ElementType { get; set; } = null!;

        [Input("rowIndex")]
        public Input<double>? RowIndex { get; set; }

        [Input("rowSpan", required: true)]
        public Input<double> RowSpan { get; set; } = null!;

        public AnalysisGridLayoutElementArgs()
        {
        }
        public static new AnalysisGridLayoutElementArgs Empty => new AnalysisGridLayoutElementArgs();
    }
}
