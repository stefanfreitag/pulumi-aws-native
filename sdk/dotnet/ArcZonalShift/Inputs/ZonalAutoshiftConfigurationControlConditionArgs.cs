// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ArcZonalShift.Inputs
{

    public sealed class ZonalAutoshiftConfigurationControlConditionArgs : global::Pulumi.ResourceArgs
    {
        [Input("alarmIdentifier", required: true)]
        public Input<string> AlarmIdentifier { get; set; } = null!;

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.ArcZonalShift.ZonalAutoshiftConfigurationControlConditionType> Type { get; set; } = null!;

        public ZonalAutoshiftConfigurationControlConditionArgs()
        {
        }
        public static new ZonalAutoshiftConfigurationControlConditionArgs Empty => new ZonalAutoshiftConfigurationControlConditionArgs();
    }
}
