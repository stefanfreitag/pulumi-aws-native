// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES.Inputs
{

    /// <summary>
    /// An object that contains Virtual Deliverability Manager (VDM) settings for this configuration set.
    /// </summary>
    public sealed class ConfigurationSetVdmOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("dashboardOptions")]
        public Input<Inputs.ConfigurationSetDashboardOptionsArgs>? DashboardOptions { get; set; }

        [Input("guardianOptions")]
        public Input<Inputs.ConfigurationSetGuardianOptionsArgs>? GuardianOptions { get; set; }

        public ConfigurationSetVdmOptionsArgs()
        {
        }
        public static new ConfigurationSetVdmOptionsArgs Empty => new ConfigurationSetVdmOptionsArgs();
    }
}
