// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardTooltipOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldBasedTooltip")]
        public Input<Inputs.DashboardFieldBasedTooltipArgs>? FieldBasedTooltip { get; set; }

        [Input("selectedTooltipType")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardSelectedTooltipType>? SelectedTooltipType { get; set; }

        [Input("tooltipVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? TooltipVisibility { get; set; }

        public DashboardTooltipOptionsArgs()
        {
        }
        public static new DashboardTooltipOptionsArgs Empty => new DashboardTooltipOptionsArgs();
    }
}
