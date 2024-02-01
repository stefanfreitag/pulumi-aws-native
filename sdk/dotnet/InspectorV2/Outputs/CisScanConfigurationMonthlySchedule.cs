// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.InspectorV2.Outputs
{

    [OutputType]
    public sealed class CisScanConfigurationMonthlySchedule
    {
        public readonly Pulumi.AwsNative.InspectorV2.CisScanConfigurationDay Day;
        public readonly Outputs.CisScanConfigurationTime StartTime;

        [OutputConstructor]
        private CisScanConfigurationMonthlySchedule(
            Pulumi.AwsNative.InspectorV2.CisScanConfigurationDay day,

            Outputs.CisScanConfigurationTime startTime)
        {
            Day = day;
            StartTime = startTime;
        }
    }
}
