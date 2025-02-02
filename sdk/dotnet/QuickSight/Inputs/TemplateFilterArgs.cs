// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("categoryFilter")]
        public Input<Inputs.TemplateCategoryFilterArgs>? CategoryFilter { get; set; }

        [Input("numericEqualityFilter")]
        public Input<Inputs.TemplateNumericEqualityFilterArgs>? NumericEqualityFilter { get; set; }

        [Input("numericRangeFilter")]
        public Input<Inputs.TemplateNumericRangeFilterArgs>? NumericRangeFilter { get; set; }

        [Input("relativeDatesFilter")]
        public Input<Inputs.TemplateRelativeDatesFilterArgs>? RelativeDatesFilter { get; set; }

        [Input("timeEqualityFilter")]
        public Input<Inputs.TemplateTimeEqualityFilterArgs>? TimeEqualityFilter { get; set; }

        [Input("timeRangeFilter")]
        public Input<Inputs.TemplateTimeRangeFilterArgs>? TimeRangeFilter { get; set; }

        [Input("topBottomFilter")]
        public Input<Inputs.TemplateTopBottomFilterArgs>? TopBottomFilter { get; set; }

        public TemplateFilterArgs()
        {
        }
        public static new TemplateFilterArgs Empty => new TemplateFilterArgs();
    }
}
