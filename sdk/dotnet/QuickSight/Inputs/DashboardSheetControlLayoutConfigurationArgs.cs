// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardSheetControlLayoutConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("gridLayout")]
        public Input<Inputs.DashboardGridLayoutConfigurationArgs>? GridLayout { get; set; }

        public DashboardSheetControlLayoutConfigurationArgs()
        {
        }
        public static new DashboardSheetControlLayoutConfigurationArgs Empty => new DashboardSheetControlLayoutConfigurationArgs();
    }
}
