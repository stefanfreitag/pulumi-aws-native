// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardMissingDataConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("treatmentOption")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardMissingDataTreatmentOption>? TreatmentOption { get; set; }

        public DashboardMissingDataConfigurationArgs()
        {
        }
        public static new DashboardMissingDataConfigurationArgs Empty => new DashboardMissingDataConfigurationArgs();
    }
}
