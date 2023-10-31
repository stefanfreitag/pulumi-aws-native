// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTotalOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("customLabel")]
        public Input<string>? CustomLabel { get; set; }

        [Input("placement")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateTableTotalsPlacement>? Placement { get; set; }

        [Input("scrollStatus")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateTableTotalsScrollStatus>? ScrollStatus { get; set; }

        [Input("totalAggregationOptions")]
        private InputList<Inputs.TemplateTotalAggregationOptionArgs>? _totalAggregationOptions;
        public InputList<Inputs.TemplateTotalAggregationOptionArgs> TotalAggregationOptions
        {
            get => _totalAggregationOptions ?? (_totalAggregationOptions = new InputList<Inputs.TemplateTotalAggregationOptionArgs>());
            set => _totalAggregationOptions = value;
        }

        [Input("totalCellStyle")]
        public Input<Inputs.TemplateTableCellStyleArgs>? TotalCellStyle { get; set; }

        [Input("totalsVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateVisibility>? TotalsVisibility { get; set; }

        public TemplateTotalOptionsArgs()
        {
        }
        public static new TemplateTotalOptionsArgs Empty => new TemplateTotalOptionsArgs();
    }
}
