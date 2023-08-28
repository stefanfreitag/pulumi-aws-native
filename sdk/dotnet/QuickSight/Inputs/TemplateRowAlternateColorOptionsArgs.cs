// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateRowAlternateColorOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("rowAlternateColors")]
        private InputList<string>? _rowAlternateColors;
        public InputList<string> RowAlternateColors
        {
            get => _rowAlternateColors ?? (_rowAlternateColors = new InputList<string>());
            set => _rowAlternateColors = value;
        }

        [Input("status")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateWidgetStatus>? Status { get; set; }

        [Input("usePrimaryBackgroundColor")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateWidgetStatus>? UsePrimaryBackgroundColor { get; set; }

        public TemplateRowAlternateColorOptionsArgs()
        {
        }
        public static new TemplateRowAlternateColorOptionsArgs Empty => new TemplateRowAlternateColorOptionsArgs();
    }
}
