// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTEvents.Outputs
{

    /// <summary>
    /// Information needed to clear the timer.
    /// </summary>
    [OutputType]
    public sealed class DetectorModelClearTimer
    {
        public readonly string TimerName;

        [OutputConstructor]
        private DetectorModelClearTimer(string timerName)
        {
            TimerName = timerName;
        }
    }
}
