// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardRelativeDateTimeControlDisplayOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("dateTimeFormat")]
        public Input<string>? DateTimeFormat { get; set; }

        [Input("infoIconLabelOptions")]
        public Input<Inputs.DashboardSheetControlInfoIconLabelOptionsArgs>? InfoIconLabelOptions { get; set; }

        [Input("titleOptions")]
        public Input<Inputs.DashboardLabelOptionsArgs>? TitleOptions { get; set; }

        public DashboardRelativeDateTimeControlDisplayOptionsArgs()
        {
        }
        public static new DashboardRelativeDateTimeControlDisplayOptionsArgs Empty => new DashboardRelativeDateTimeControlDisplayOptionsArgs();
    }
}
