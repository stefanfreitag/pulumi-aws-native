// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;Export to .csv option.&lt;/p&gt;
    /// </summary>
    public sealed class DashboardExportToCSVOptionArgs : Pulumi.ResourceArgs
    {
        [Input("availabilityStatus")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardDashboardBehavior>? AvailabilityStatus { get; set; }

        public DashboardExportToCSVOptionArgs()
        {
        }
    }
}
